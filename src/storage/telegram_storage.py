"""
Telegram Storage System
سیستم ذخیره‌سازی فایل‌ها و داده‌ها در تلگرام
"""

import asyncio
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
import json
import pickle
import base64
from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterDocument

logger = logging.getLogger(__name__)


class TelegramStorage:
    """ذخیره‌سازی در تلگرام"""
    
    def __init__(self, client: TelegramClient, storage_channel_id: str):
        self.client = client
        self.storage_channel_id = storage_channel_id
        self.index = {}  # فهرست فایل‌های ذخیره شده
        self.initialized = False
        
    async def initialize(self):
        """مقداردهی اولیه"""
        try:
            # بارگذاری index از کانال
            await self._load_index()
            self.initialized = True
            logger.info("✅ Telegram storage initialized")
        except Exception as e:
            logger.error(f"❌ Failed to initialize Telegram storage: {e}")
            raise
    
    async def store_data(self, key: str, data: Any, 
                        metadata: Optional[Dict] = None) -> str:
        """ذخیره داده"""
        try:
            # تبدیل داده به JSON
            if isinstance(data, (dict, list)):
                content = json.dumps(data, ensure_ascii=False, indent=2)
                file_type = 'json'
            elif isinstance(data, str):
                content = data
                file_type = 'text'
            else:
                # سریالیز کردن اشیاء پیچیده
                content = base64.b64encode(pickle.dumps(data)).decode()
                file_type = 'binary'
            
            # ساخت پیام
            timestamp = datetime.now().isoformat()
            message = f"""📦 **Storage Entry**

🔑 Key: `{key}`
📅 Timestamp: {timestamp}
📝 Type: {file_type}
📊 Size: {len(content)} bytes

{metadata if metadata else ''}

{'='*50}

{content if len(content) < 3000 else content[:3000] + '...[truncated]'}
"""
            
            # ارسال به کانال
            sent_message = await self.client.send_message(
                self.storage_channel_id,
                message
            )
            
            # بروزرسانی index
            self.index[key] = {
                'message_id': sent_message.id,
                'timestamp': timestamp,
                'type': file_type,
                'size': len(content),
                'metadata': metadata
            }
            
            # ذخیره index
            await self._save_index()
            
            logger.info(f"✅ Stored data with key: {key}")
            
            return f"telegram://message/{sent_message.id}"
            
        except Exception as e:
            logger.error(f"❌ Failed to store data: {e}")
            raise
    
    async def store_file(self, key: str, file_path: str, 
                        metadata: Optional[Dict] = None) -> str:
        """ذخیره فایل"""
        try:
            # آپلود فایل
            sent_file = await self.client.send_file(
                self.storage_channel_id,
                file_path,
                caption=f"📁 File: {key}\n⏰ {datetime.now().isoformat()}\n\n{json.dumps(metadata, ensure_ascii=False) if metadata else ''}"
            )
            
            # بروزرسانی index
            self.index[key] = {
                'message_id': sent_file.id,
                'timestamp': datetime.now().isoformat(),
                'type': 'file',
                'file_path': file_path,
                'metadata': metadata
            }
            
            await self._save_index()
            
            logger.info(f"✅ Stored file: {key}")
            
            return f"telegram://file/{sent_file.id}"
            
        except Exception as e:
            logger.error(f"❌ Failed to store file: {e}")
            raise
    
    async def retrieve_data(self, key: str) -> Optional[Any]:
        """بازیابی داده"""
        try:
            if key not in self.index:
                logger.warning(f"⚠️ Key not found: {key}")
                return None
            
            entry = self.index[key]
            message_id = entry['message_id']
            file_type = entry['type']
            
            # دریافت پیام
            message = await self.client.get_messages(
                self.storage_channel_id,
                ids=message_id
            )
            
            if not message:
                return None
            
            # استخراج محتوا
            content = message.text
            
            # پردازش بر اساس نوع
            if file_type == 'json':
                # استخراج JSON از پیام
                json_start = content.find('{')
                if json_start == -1:
                    json_start = content.find('[')
                
                if json_start != -1:
                    json_content = content[json_start:]
                    return json.loads(json_content)
            
            elif file_type == 'text':
                # استخراج متن
                separator = '=' * 50
                if separator in content:
                    parts = content.split(separator)
                    return parts[-1].strip()
                return content
            
            elif file_type == 'binary':
                # دی‌سریالیز
                separator = '=' * 50
                if separator in content:
                    parts = content.split(separator)
                    encoded = parts[-1].strip()
                    return pickle.loads(base64.b64decode(encoded))
            
            return content
            
        except Exception as e:
            logger.error(f"❌ Failed to retrieve data: {e}")
            return None
    
    async def retrieve_file(self, key: str, download_path: str) -> Optional[str]:
        """بازیابی فایل"""
        try:
            if key not in self.index:
                return None
            
            entry = self.index[key]
            message_id = entry['message_id']
            
            # دریافت پیام
            message = await self.client.get_messages(
                self.storage_channel_id,
                ids=message_id
            )
            
            if not message or not message.media:
                return None
            
            # دانلود فایل
            downloaded_path = await self.client.download_media(
                message,
                file=download_path
            )
            
            logger.info(f"✅ Retrieved file: {key}")
            
            return downloaded_path
            
        except Exception as e:
            logger.error(f"❌ Failed to retrieve file: {e}")
            return None
    
    async def list_keys(self, filter_type: Optional[str] = None) -> List[str]:
        """لیست کلیدها"""
        if filter_type:
            return [
                key for key, entry in self.index.items()
                if entry.get('type') == filter_type
            ]
        return list(self.index.keys())
    
    async def delete_data(self, key: str) -> bool:
        """حذف داده"""
        try:
            if key not in self.index:
                return False
            
            entry = self.index[key]
            message_id = entry['message_id']
            
            # حذف پیام
            await self.client.delete_messages(
                self.storage_channel_id,
                [message_id]
            )
            
            # حذف از index
            del self.index[key]
            await self._save_index()
            
            logger.info(f"✅ Deleted data: {key}")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Failed to delete data: {e}")
            return False
    
    async def search(self, query: str) -> List[Dict]:
        """جستجو در داده‌ها"""
        results = []
        
        for key, entry in self.index.items():
            if query.lower() in key.lower():
                results.append({
                    'key': key,
                    'entry': entry
                })
            elif entry.get('metadata') and query.lower() in str(entry['metadata']).lower():
                results.append({
                    'key': key,
                    'entry': entry
                })
        
        return results
    
    async def _save_index(self):
        """ذخیره index"""
        try:
            index_json = json.dumps(self.index, ensure_ascii=False, indent=2)
            
            # جستجوی پیام index قبلی
            messages = await self.client.get_messages(
                self.storage_channel_id,
                search='📚 Storage Index'
            )
            
            if messages:
                # بروزرسانی
                await self.client.edit_message(
                    self.storage_channel_id,
                    messages[0].id,
                    f"📚 **Storage Index**\n\nLast Updated: {datetime.now().isoformat()}\n\nTotal Entries: {len(self.index)}\n\n```json\n{index_json}\n```"
                )
            else:
                # ایجاد جدید
                await self.client.send_message(
                    self.storage_channel_id,
                    f"📚 **Storage Index**\n\nCreated: {datetime.now().isoformat()}\n\nTotal Entries: {len(self.index)}\n\n```json\n{index_json}\n```"
                )
            
        except Exception as e:
            logger.error(f"❌ Failed to save index: {e}")
    
    async def _load_index(self):
        """بارگذاری index"""
        try:
            messages = await self.client.get_messages(
                self.storage_channel_id,
                search='📚 Storage Index'
            )
            
            if messages and messages[0].text:
                # استخراج JSON
                text = messages[0].text
                json_start = text.find('```json') + 7
                json_end = text.find('```', json_start)
                
                if json_start > 6 and json_end > json_start:
                    index_json = text[json_start:json_end].strip()
                    self.index = json.loads(index_json)
                    logger.info(f"✅ Loaded index with {len(self.index)} entries")
            else:
                logger.info("ℹ️ No existing index found, starting fresh")
                self.index = {}
                
        except Exception as e:
            logger.error(f"❌ Failed to load index: {e}")
            self.index = {}
    
    async def get_stats(self) -> Dict[str, Any]:
        """آمار ذخیره‌سازی"""
        type_distribution = {}
        total_size = 0
        
        for entry in self.index.values():
            entry_type = entry.get('type', 'unknown')
            type_distribution[entry_type] = type_distribution.get(entry_type, 0) + 1
            total_size += entry.get('size', 0)
        
        return {
            'total_entries': len(self.index),
            'type_distribution': type_distribution,
            'total_size_bytes': total_size,
            'total_size_mb': total_size / (1024 * 1024),
            'storage_channel': self.storage_channel_id
        }


class DataBackupSystem:
    """سیستم پشتیبان‌گیری"""
    
    def __init__(self, telegram_storage: TelegramStorage):
        self.storage = telegram_storage
        self.backup_history = []
        
    async def backup_data(self, data_name: str, data: Any, 
                         backup_type: str = 'incremental') -> str:
        """پشتیبان‌گیری از داده"""
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_key = f"backup_{data_name}_{timestamp}"
        
        metadata = {
            'backup_type': backup_type,
            'original_name': data_name,
            'timestamp': timestamp,
            'data_type': type(data).__name__
        }
        
        # ذخیره
        storage_ref = await self.storage.store_data(
            backup_key,
            data,
            metadata
        )
        
        # ثبت در تاریخچه
        self.backup_history.append({
            'key': backup_key,
            'ref': storage_ref,
            'metadata': metadata
        })
        
        logger.info(f"✅ Backup created: {backup_key}")
        
        return backup_key
    
    async def restore_backup(self, backup_key: str) -> Optional[Any]:
        """بازیابی از پشتیبان"""
        
        data = await self.storage.retrieve_data(backup_key)
        
        if data:
            logger.info(f"✅ Backup restored: {backup_key}")
        
        return data
    
    async def list_backups(self, data_name: Optional[str] = None) -> List[Dict]:
        """لیست پشتیبان‌ها"""
        
        if data_name:
            return [
                backup for backup in self.backup_history
                if backup['metadata']['original_name'] == data_name
            ]
        
        return self.backup_history
    
    async def auto_backup(self, data_dict: Dict[str, Any]):
        """پشتیبان‌گیری خودکار از چندین داده"""
        
        logger.info("🔄 Starting auto-backup...")
        
        backup_refs = {}
        
        for name, data in data_dict.items():
            try:
                ref = await self.backup_data(name, data, 'auto')
                backup_refs[name] = ref
            except Exception as e:
                logger.error(f"❌ Failed to backup {name}: {e}")
        
        logger.info(f"✅ Auto-backup completed: {len(backup_refs)} items backed up")
        
        return backup_refs


class CacheSystem:
    """سیستم کش با پشتیبان در تلگرام"""
    
    def __init__(self, telegram_storage: TelegramStorage, 
                 cache_duration_seconds: int = 3600):
        self.storage = telegram_storage
        self.cache_duration = cache_duration_seconds
        self.memory_cache = {}
        self.cache_metadata = {}
        
    async def get(self, key: str, fetch_function=None) -> Optional[Any]:
        """دریافت از کش"""
        
        # بررسی memory cache
        if key in self.memory_cache:
            metadata = self.cache_metadata.get(key, {})
            cached_time = metadata.get('cached_at')
            
            if cached_time:
                age = (datetime.now() - datetime.fromisoformat(cached_time)).total_seconds()
                
                if age < self.cache_duration:
                    logger.debug(f"💨 Cache hit (memory): {key}")
                    return self.memory_cache[key]
        
        # بررسی Telegram storage
        data = await self.storage.retrieve_data(f"cache_{key}")
        
        if data:
            # بررسی تاریخ انقضا
            metadata = self.cache_metadata.get(key, {})
            cached_time = metadata.get('cached_at')
            
            if cached_time:
                age = (datetime.now() - datetime.fromisoformat(cached_time)).total_seconds()
                
                if age < self.cache_duration:
                    # بازگردانی به memory
                    self.memory_cache[key] = data
                    logger.debug(f"💨 Cache hit (telegram): {key}")
                    return data
        
        # Cache miss - fetch جدید
        if fetch_function:
            logger.debug(f"🔄 Cache miss, fetching: {key}")
            data = await fetch_function()
            await self.set(key, data)
            return data
        
        return None
    
    async def set(self, key: str, value: Any):
        """ذخیره در کش"""
        
        # ذخیره در memory
        self.memory_cache[key] = value
        
        # ذخیره metadata
        self.cache_metadata[key] = {
            'cached_at': datetime.now().isoformat(),
            'size': len(str(value))
        }
        
        # ذخیره در Telegram
        await self.storage.store_data(
            f"cache_{key}",
            value,
            self.cache_metadata[key]
        )
        
        logger.debug(f"✅ Cached: {key}")
    
    async def invalidate(self, key: str):
        """باطل کردن کش"""
        
        if key in self.memory_cache:
            del self.memory_cache[key]
        
        if key in self.cache_metadata:
            del self.cache_metadata[key]
        
        await self.storage.delete_data(f"cache_{key}")
        
        logger.debug(f"🗑️ Cache invalidated: {key}")
    
    async def clear_all(self):
        """پاک کردن تمام کش"""
        
        self.memory_cache.clear()
        self.cache_metadata.clear()
        
        # حذف از Telegram
        cache_keys = await self.storage.list_keys()
        cache_keys = [k for k in cache_keys if k.startswith('cache_')]
        
        for key in cache_keys:
            await self.storage.delete_data(key)
        
        logger.info("🗑️ All cache cleared")
