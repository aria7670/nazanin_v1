"""
Google Sheets Manager V2
مدیریت پیشرفته Google Sheets با ساختار چند Spreadsheet
"""

import asyncio
import gspread
from google.oauth2.service_account import Credentials
from typing import Dict, List, Any, Optional
import json
import time
from datetime import datetime, timedelta
import logging
from .sheets_auto_setup import SheetsAutoSetup

logger = logging.getLogger(__name__)


class SheetsManagerV2:
    """مدیریت پیشرفته Google Sheets"""
    
    def __init__(self, credentials_file: str, spreadsheet_ids: Dict[str, str] = None):
        self.credentials_file = credentials_file
        self.spreadsheet_ids = spreadsheet_ids or {}
        self.client = None
        self.spreadsheets = {}
        
        # Cache
        self._cache = {}
        self._cache_timestamps = {}
        self.cache_duration = 300  # 5 minutes
    
    async def initialize(self, auto_setup: bool = True):
        """راه‌اندازی اولیه"""
        logger.info("🚀 Initializing Sheets Manager V2...")
        
        # اتصال به Google
        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
        creds = Credentials.from_service_account_file(
            self.credentials_file,
            scopes=scope
        )
        self.client = gspread.authorize(creds)
        
        logger.info("✅ Connected to Google Sheets API")
        
        # اگه spreadsheet_ids نداریم، auto setup کن
        if not self.spreadsheet_ids and auto_setup:
            logger.info("📊 No spreadsheet IDs found. Starting auto setup...")
            setup = SheetsAutoSetup(self.credentials_file)
            await setup.initialize()
            self.spreadsheet_ids = setup.get_spreadsheet_ids()
            setup.save_config('config/spreadsheet_ids.json')
            logger.info("✅ Auto setup completed")
        
        # باز کردن تمام spreadsheets
        await self._open_all_spreadsheets()
        
        logger.info(f"✅ Sheets Manager initialized with {len(self.spreadsheets)} spreadsheets")
    
    async def _open_all_spreadsheets(self):
        """باز کردن تمام spreadsheets"""
        for name, spreadsheet_id in self.spreadsheet_ids.items():
            try:
                ss = self.client.open_by_key(spreadsheet_id)
                self.spreadsheets[name] = ss
                logger.info(f"   ✅ Opened: {name}")
            except Exception as e:
                logger.error(f"   ❌ Failed to open {name}: {e}")
    
    # متدهای اصلی
    
    async def get_sheet_data(
        self,
        spreadsheet_name: str,
        sheet_name: str,
        use_cache: bool = True
    ) -> List[Dict]:
        """دریافت داده از یک sheet"""
        cache_key = f"{spreadsheet_name}_{sheet_name}"
        
        # چک کردن cache
        if use_cache and self._is_cache_valid(cache_key):
            logger.debug(f"📦 Using cached data for {cache_key}")
            return self._cache[cache_key]
        
        try:
            # دریافت spreadsheet
            spreadsheet = self.spreadsheets.get(spreadsheet_name)
            if not spreadsheet:
                logger.error(f"❌ Spreadsheet not found: {spreadsheet_name}")
                return []
            
            # دریافت sheet
            worksheet = spreadsheet.worksheet(sheet_name)
            data = worksheet.get_all_records()
            
            # ذخیره در cache
            self._cache[cache_key] = data
            self._cache_timestamps[cache_key] = time.time()
            
            logger.debug(f"✅ Loaded {len(data)} rows from {spreadsheet_name}/{sheet_name}")
            return data
            
        except Exception as e:
            logger.error(f"❌ Error reading {spreadsheet_name}/{sheet_name}: {e}")
            return []
    
    async def append_row(
        self,
        spreadsheet_name: str,
        sheet_name: str,
        row_data: List[Any]
    ) -> bool:
        """اضافه کردن ردیف جدید"""
        try:
            spreadsheet = self.spreadsheets.get(spreadsheet_name)
            if not spreadsheet:
                return False
            
            worksheet = spreadsheet.worksheet(sheet_name)
            worksheet.append_row(row_data)
            
            # پاک کردن cache
            cache_key = f"{spreadsheet_name}_{sheet_name}"
            self._clear_cache_key(cache_key)
            
            logger.debug(f"✅ Appended row to {spreadsheet_name}/{sheet_name}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error appending to {spreadsheet_name}/{sheet_name}: {e}")
            return False
    
    async def update_cell(
        self,
        spreadsheet_name: str,
        sheet_name: str,
        row: int,
        col: int,
        value: Any
    ) -> bool:
        """به‌روزرسانی یک سلول"""
        try:
            spreadsheet = self.spreadsheets.get(spreadsheet_name)
            if not spreadsheet:
                return False
            
            worksheet = spreadsheet.worksheet(sheet_name)
            worksheet.update_cell(row, col, value)
            
            # پاک کردن cache
            cache_key = f"{spreadsheet_name}_{sheet_name}"
            self._clear_cache_key(cache_key)
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Error updating cell: {e}")
            return False
    
    # متدهای تخصصی
    
    async def log_telegram_message(self, message_data: Dict):
        """ثبت پیام تلگرام"""
        row = [
            message_data.get('message_id', ''),
            message_data.get('timestamp', datetime.now().isoformat()),
            message_data.get('chat_id', ''),
            message_data.get('user_id', ''),
            message_data.get('username', ''),
            message_data.get('message_type', ''),
            message_data.get('content', ''),
            message_data.get('response', ''),
            message_data.get('response_time', '')
        ]
        
        return await self.append_row('telegram_data', 'Messages_Log', row)
    
    async def log_tweet(self, tweet_data: Dict):
        """ثبت توییت"""
        row = [
            tweet_data.get('tweet_id', ''),
            tweet_data.get('timestamp', datetime.now().isoformat()),
            tweet_data.get('content', ''),
            tweet_data.get('type', ''),
            tweet_data.get('category', ''),
            tweet_data.get('engagement', 0),
            tweet_data.get('impressions', 0),
            tweet_data.get('ai_used', ''),
            tweet_data.get('status', 'posted')
        ]
        
        return await self.append_row('content_management', 'Tweet_Log', row)
    
    async def get_personality(self) -> Dict:
        """دریافت تنظیمات شخصیت"""
        data = await self.get_sheet_data('bot_configuration', 'Personality')
        
        personality = {}
        for row in data:
            if 'Key' in row and 'Value' in row:
                personality[row['Key']] = row['Value']
        
        return personality
    
    async def get_api_keys(self) -> Dict:
        """دریافت کلیدهای API"""
        data = await self.get_sheet_data('ai_data', 'API_Keys')
        
        api_keys = {}
        for row in data:
            provider = row.get('Provider', '').lower()
            if provider and row.get('Status') == 'active':
                if provider not in api_keys:
                    api_keys[provider] = []
                api_keys[provider].append(row.get('API_Key'))
        
        return api_keys
    
    async def get_telegram_channels(self) -> List[Dict]:
        """دریافت لیست کانال‌های تلگرام"""
        return await self.get_sheet_data('telegram_data', 'Channels')
    
    async def log_error(self, error_data: Dict):
        """ثبت خطا"""
        row = [
            error_data.get('error_id', ''),
            datetime.now().isoformat(),
            error_data.get('error_type', ''),
            error_data.get('message', ''),
            error_data.get('stack_trace', ''),
            error_data.get('severity', 'medium'),
            'False'  # Resolved
        ]
        
        return await self.append_row('security_logs', 'Error_Logs', row)
    
    async def log_security_event(self, event_data: Dict):
        """ثبت رویداد امنیتی"""
        row = [
            event_data.get('event_id', ''),
            datetime.now().isoformat(),
            event_data.get('type', ''),
            event_data.get('severity', ''),
            event_data.get('description', ''),
            event_data.get('action_taken', ''),
            event_data.get('status', 'open')
        ]
        
        return await self.append_row('security_logs', 'Security_Events', row)
    
    # Cache management
    
    def _is_cache_valid(self, cache_key: str) -> bool:
        """بررسی اعتبار cache"""
        if cache_key not in self._cache:
            return False
        
        timestamp = self._cache_timestamps.get(cache_key, 0)
        return (time.time() - timestamp) < self.cache_duration
    
    def _clear_cache_key(self, cache_key: str):
        """پاک کردن یک کلید از cache"""
        self._cache.pop(cache_key, None)
        self._cache_timestamps.pop(cache_key, None)
    
    def clear_all_cache(self):
        """پاک کردن کل cache"""
        self._cache.clear()
        self._cache_timestamps.clear()
        logger.info("🗑️ All cache cleared")


# Usage Example
if __name__ == '__main__':
    async def main():
        manager = SheetsManagerV2('credentials.json')
        await manager.initialize(auto_setup=True)
        
        # دریافت شخصیت
        personality = await manager.get_personality()
        print("Personality:", personality)
        
        # دریافت API keys
        api_keys = await manager.get_api_keys()
        print("API Keys:", {k: f"{len(v)} keys" for k, v in api_keys.items()})
        
        # ثبت پیام
        await manager.log_telegram_message({
            'message_id': '12345',
            'user_id': '67890',
            'content': 'سلام!',
            'response': 'سلام! چطور می‌تونم کمک کنم؟'
        })
        print("✅ Message logged")
    
    asyncio.run(main())
