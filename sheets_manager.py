"""
Google Sheets Manager
Handles all interactions with Google Sheets for configuration and data storage
"""

import asyncio
import gspread
from google.oauth2.service_account import Credentials
from typing import Dict, List, Any, Optional
import json
import time
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)


class SheetsManager:
    """Manages all Google Sheets operations with caching"""
    
    def __init__(self, credentials_file: str, spreadsheet_id: str):
        self.credentials_file = credentials_file
        self.spreadsheet_id = spreadsheet_id
        self.client = None
        self.spreadsheet = None
        self._cache = {}
        self._cache_timestamps = {}
        self.cache_duration = 300  # 5 minutes in seconds
        
    async def initialize(self):
        """Initialize Google Sheets connection"""
        try:
            scope = [
                'https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive'
            ]
            creds = Credentials.from_service_account_file(
                self.credentials_file, 
                scopes=scope
            )
            self.client = gspread.authorize(creds)
            self.spreadsheet = self.client.open_by_key(self.spreadsheet_id)
            logger.info("✅ Google Sheets initialized successfully")
        except Exception as e:
            logger.error(f"❌ Failed to initialize Google Sheets: {e}")
            raise
    
    def _is_cache_valid(self, sheet_name: str) -> bool:
        """Check if cached data is still valid"""
        if sheet_name not in self._cache_timestamps:
            return False
        elapsed = time.time() - self._cache_timestamps[sheet_name]
        return elapsed < self.cache_duration
    
    async def get_sheet_data(self, sheet_name: str, use_cache: bool = True) -> List[Dict[str, Any]]:
        """Get all data from a sheet as list of dictionaries"""
        if use_cache and self._is_cache_valid(sheet_name):
            logger.debug(f"📦 Using cached data for {sheet_name}")
            return self._cache[sheet_name]
        
        try:
            worksheet = self.spreadsheet.worksheet(sheet_name)
            data = worksheet.get_all_records()
            self._cache[sheet_name] = data
            self._cache_timestamps[sheet_name] = time.time()
            logger.debug(f"✅ Loaded {len(data)} rows from {sheet_name}")
            return data
        except Exception as e:
            logger.error(f"❌ Failed to get sheet data from {sheet_name}: {e}")
            return []
    
    async def append_row(self, sheet_name: str, data: List[Any]):
        """Append a row to a sheet"""
        try:
            worksheet = self.spreadsheet.worksheet(sheet_name)
            worksheet.append_row(data)
            # Invalidate cache
            if sheet_name in self._cache:
                del self._cache[sheet_name]
                del self._cache_timestamps[sheet_name]
            logger.debug(f"✅ Appended row to {sheet_name}")
        except Exception as e:
            logger.error(f"❌ Failed to append row to {sheet_name}: {e}")
    
    async def update_cell(self, sheet_name: str, row: int, col: int, value: Any):
        """Update a specific cell"""
        try:
            worksheet = self.spreadsheet.worksheet(sheet_name)
            worksheet.update_cell(row, col, value)
            # Invalidate cache
            if sheet_name in self._cache:
                del self._cache[sheet_name]
                del self._cache_timestamps[sheet_name]
            logger.debug(f"✅ Updated cell {row},{col} in {sheet_name}")
        except Exception as e:
            logger.error(f"❌ Failed to update cell in {sheet_name}: {e}")
    
    async def get_personality(self) -> Dict[str, str]:
        """Get personality configuration"""
        data = await self.get_sheet_data('شخصیت')
        personality = {}
        for row in data:
            if 'ویژگی' in row and 'توضیحات' in row:
                personality[row['ویژگی']] = row['توضیحات']
        return personality
    
    async def get_channel_info(self) -> Dict[str, str]:
        """Get channel information"""
        data = await self.get_sheet_data('کانال_اطلاعات')
        info = {}
        for row in data:
            if 'کلید' in row and 'مقدار' in row:
                info[row['کلید']] = row['مقدار']
        return info
    
    async def get_learning_rules(self, category: Optional[str] = None) -> List[Dict[str, str]]:
        """Get learning rules, optionally filtered by category"""
        data = await self.get_sheet_data('یادگیری_قوانین')
        if category:
            return [r for r in data if r.get('دسته') == category]
        return data
    
    async def get_api_keys(self) -> Dict[str, List[Dict[str, Any]]]:
        """Get all API keys grouped by provider"""
        data = await self.get_sheet_data('API_Keys')
        keys = {}
        for row in data:
            if row.get('وضعیت') == 'فعال':
                provider = row.get('نام', '')
                if provider not in keys:
                    keys[provider] = []
                keys[provider].append(row)
        return keys
    
    async def log_tweet(self, content: str, tweet_id: str, category: str, metrics: Dict):
        """Log a tweet to appropriate sheet"""
        timestamp = datetime.now().isoformat()
        await self.append_row('پست_دسته_بندی', [
            timestamp,
            'twitter',
            content[:100],  # Summary
            category,
            tweet_id,
            json.dumps(metrics)
        ])
    
    async def log_telegram_post(self, content: str, post_id: str, category: str, metrics: Dict):
        """Log a Telegram post"""
        timestamp = datetime.now().isoformat()
        await self.append_row('پست_دسته_بندی', [
            timestamp,
            'telegram',
            content[:100],
            category,
            post_id,
            json.dumps(metrics)
        ])
    
    async def update_emotions(self, emotions: Dict[str, float]):
        """Update emotion scores"""
        try:
            worksheet = self.spreadsheet.worksheet('احساسات')
            records = worksheet.get_all_records()
            for emotion, score in emotions.items():
                # Find row with this emotion
                for idx, row in enumerate(records, start=2):  # Start from 2 (header is row 1)
                    if row.get('احساس') == emotion:
                        worksheet.update_cell(idx, 2, score)  # Column 2 is امتیاز
                        worksheet.update_cell(idx, 3, datetime.now().isoformat())
            logger.debug("✅ Updated emotions in sheet")
        except Exception as e:
            logger.error(f"❌ Failed to update emotions: {e}")
    
    async def clear_cache(self):
        """Clear all cached data"""
        self._cache.clear()
        self._cache_timestamps.clear()
        logger.info("🧹 Cache cleared")
    
    async def reload_keys(self):
        """Force reload API keys"""
        if 'API_Keys' in self._cache:
            del self._cache['API_Keys']
            del self._cache_timestamps['API_Keys']
        return await self.get_api_keys()
