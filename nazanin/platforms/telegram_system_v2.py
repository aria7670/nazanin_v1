"""
Telegram System V2 - کنترل کامل
سیستم پیشرفته تلگرام با کنترل کامل اکانت
"""

import asyncio
import logging
from telethon import TelegramClient, events
from telethon.tl.types import User, Channel, Message
from typing import Dict, List, Any, Optional
from datetime import datetime
import json

logger = logging.getLogger(__name__)


class TelegramSystemV2:
    """سیستم پیشرفته تلگرام"""
    
    def __init__(self, config: Dict, sheets_manager=None, organism=None):
        self.config = config.get('telegram', {})
        self.sheets_manager = sheets_manager
        self.organism = organism  # موجود زیستی
        
        # Client برای کنترل کامل اکانت
        self.client = None
        
        # Channels & Groups
        self.channels = self.config.get('channels', {})
        self.groups = self.config.get('groups', {})
        
        # Settings
        self.settings = self.config.get('settings', {})
        
        # Conversation memory
        self.conversations = {}  # {user_id: conversation_data}
        self.saved_messages = []
        
        logger.info("✅ Telegram System V2 initialized")
    
    async def initialize(self):
        """راه‌اندازی"""
        logger.info("🚀 Starting Telegram System V2...")
        
        # ایجاد client
        self.client = TelegramClient(
            self.config.get('session_name', 'nazanin_user'),
            int(self.config['api_id']),
            self.config['api_hash']
        )
        
        # اتصال
        await self.client.start(phone=self.config.get('phone_number'))
        
        logger.info("✅ Telegram client started")
        
        # تنظیم event handlers
        await self._setup_handlers()
        
        # به‌روزرسانی لیست کانال‌ها و گروه‌ها در sheets
        if self.sheets_manager:
            await self._sync_channels_to_sheets()
        
        logger.info("✅ Telegram System V2 ready")
    
    async def _setup_handlers(self):
        """تنظیم handler های رویدادها"""
        
        @self.client.on(events.NewMessage)
        async def handle_new_message(event):
            """پردازش پیام جدید"""
            await self._process_new_message(event)
        
        @self.client.on(events.MessageEdited)
        async def handle_edited_message(event):
            """پردازش پیام ویرایش شده"""
            logger.debug(f"✏️ Message edited in {event.chat_id}")
        
        @self.client.on(events.ChatAction)
        async def handle_chat_action(event):
            """پردازش اکشن‌های چت (عضو جدید، خروج، و...)"""
            logger.debug(f"👥 Chat action in {event.chat_id}")
    
    async def _process_new_message(self, event):
        """پردازش پیام جدید"""
        try:
            message = event.message
            sender = await event.get_sender()
            chat = await event.get_chat()
            
            # ذخیره پیام اگه تنظیم شده
            if self.settings.get('save_messages', True):
                await self._save_message(message, sender, chat)
            
            # اگه پیام خصوصیه یا mention ما باشه، پاسخ بده
            if event.is_private or (hasattr(event, 'mentioned') and event.mentioned):
                await self._respond_to_message(event, message, sender)
            
            # ثبت در sheets
            if self.sheets_manager:
                await self._log_message_to_sheets(message, sender, chat)
        
        except Exception as e:
            logger.error(f"❌ Error processing message: {e}")
    
    async def _save_message(self, message: Message, sender, chat):
        """ذخیره پیام"""
        message_data = {
            'id': message.id,
            'date': message.date,
            'text': message.text or '',
            'sender_id': sender.id if sender else None,
            'chat_id': chat.id if chat else None
        }
        
        self.saved_messages.append(message_data)
        
        # نگه‌داری فقط 10000 پیام اخیر
        if len(self.saved_messages) > 10000:
            self.saved_messages = self.saved_messages[-10000:]
        
        # Forward به Saved Messages اگه تنظیم شده
        if self.settings.get('forward_to_saved', False):
            try:
                await message.forward_to('me')
            except:
                pass
    
    async def _respond_to_message(self, event, message: Message, sender):
        """پاسخ به پیام"""
        user_id = sender.id
        user_text = message.text or ''
        
        # شروع یا ادامه conversation
        if user_id not in self.conversations:
            self.conversations[user_id] = {
                'start_time': datetime.now(),
                'messages': [],
                'context': {}
            }
        
        self.conversations[user_id]['messages'].append({
            'from': 'user',
            'text': user_text,
            'timestamp': message.date
        })
        
        # استفاده از موجود زیستی برای پردازش
        if self.organism:
            # درک پیام
            perception = await self.organism.perceive(user_text)
            
            # فکر کردن
            thought = await self.organism.think(user_text)
            
            # تولید پاسخ
            response_text = thought.get('decision', {}).get('action', 'متوجه نشدم، می‌تونی دوباره بگی؟')
        else:
            response_text = "سلام! در حال پردازش..."
        
        # ارسال پاسخ
        await event.respond(response_text)
        
        # ذخیره پاسخ
        self.conversations[user_id]['messages'].append({
            'from': 'bot',
            'text': response_text,
            'timestamp': datetime.now()
        })
    
    async def _log_message_to_sheets(self, message: Message, sender, chat):
        """ثبت پیام در sheets"""
        try:
            await self.sheets_manager.log_telegram_message({
                'message_id': message.id,
                'timestamp': message.date.isoformat(),
                'chat_id': chat.id if chat else '',
                'user_id': sender.id if sender else '',
                'username': sender.username if sender else '',
                'message_type': 'text',
                'content': message.text or '',
                'response': '',
                'response_time': ''
            })
        except Exception as e:
            logger.debug(f"Failed to log to sheets: {e}")
    
    async def _sync_channels_to_sheets(self):
        """همگام‌سازی کانال‌ها با sheets"""
        try:
            # دریافت اطلاعات کانال‌ها
            for channel_key, channel_id in self.channels.items():
                if channel_id:
                    try:
                        entity = await self.client.get_entity(int(channel_id))
                        # به‌روزرسانی در sheets
                        # در واقعیت باید append یا update کنیم
                        logger.debug(f"   ✅ Synced channel: {channel_key}")
                    except:
                        pass
        except Exception as e:
            logger.debug(f"Failed to sync channels: {e}")
    
    # متدهای عمومی
    
    async def send_to_channel(self, channel_key: str, message: str, **kwargs):
        """ارسال به کانال"""
        channel_id = self.channels.get(channel_key)
        if not channel_id:
            logger.error(f"❌ Channel not found: {channel_key}")
            return False
        
        try:
            await self.client.send_message(int(channel_id), message, **kwargs)
            logger.info(f"✅ Sent to {channel_key}")
            return True
        except Exception as e:
            logger.error(f"❌ Failed to send to {channel_key}: {e}")
            return False
    
    async def send_file(self, channel_key: str, file_path: str, caption: str = ""):
        """ارسال فایل به کانال"""
        channel_id = self.channels.get(channel_key)
        if not channel_id:
            return False
        
        try:
            await self.client.send_file(
                int(channel_id),
                file_path,
                caption=caption
            )
            logger.info(f"📤 File sent to {channel_key}")
            return True
        except Exception as e:
            logger.error(f"❌ Failed to send file: {e}")
            return False
    
    async def get_channel_messages(self, channel_key: str, limit: int = 100) -> List[Message]:
        """دریافت پیام‌های کانال"""
        channel_id = self.channels.get(channel_key)
        if not channel_id:
            return []
        
        try:
            messages = []
            async for message in self.client.iter_messages(int(channel_id), limit=limit):
                messages.append(message)
            return messages
        except Exception as e:
            logger.error(f"❌ Failed to get messages: {e}")
            return []
    
    async def monitor_channels(self, channel_keys: List[str] = None):
        """نظارت بر کانال‌ها برای پست‌های جدید"""
        if not channel_keys:
            channel_keys = list(self.channels.keys())
        
        logger.info(f"👁️ Monitoring {len(channel_keys)} channels...")
        
        # در واقعیت با event handler پیاده‌سازی میشه
        for channel_key in channel_keys:
            messages = await self.get_channel_messages(channel_key, limit=10)
            logger.debug(f"   {channel_key}: {len(messages)} recent messages")
    
    async def send_report(self, report: str):
        """ارسال گزارش به کانال Report"""
        return await self.send_to_channel('report', report)
    
    async def backup_data(self, data: Dict, filename: str):
        """بک‌آپ داده در کانال Backup"""
        import tempfile
        import os
        
        # ذخیره موقت
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            temp_path = f.name
        
        # ارسال
        success = await self.send_file(
            'backup',
            temp_path,
            caption=f"Backup: {filename} - {datetime.now().isoformat()}"
        )
        
        # حذف فایل موقت
        os.unlink(temp_path)
        
        return success
    
    def get_conversation_history(self, user_id: int) -> List[Dict]:
        """دریافت تاریخچه مکالمه با کاربر"""
        return self.conversations.get(user_id, {}).get('messages', [])
    
    def get_stats(self) -> Dict:
        """آمار سیستم تلگرام"""
        return {
            'active_conversations': len(self.conversations),
            'saved_messages': len(self.saved_messages),
            'monitored_channels': len(self.channels),
            'monitored_groups': len(self.groups)
        }


# Usage Example
if __name__ == '__main__':
    async def main():
        config = {
            'telegram': {
                'api_id': '123456',
                'api_hash': 'xxx',
                'phone_number': '+989123456789',
                'channels': {
                    'report': '-1001234567890',
                    'storage': '-1001234567891'
                },
                'groups': {
                    'admin': '-1001234567892'
                },
                'settings': {
                    'save_messages': True,
                    'auto_read': True
                }
            }
        }
        
        telegram = TelegramSystemV2(config)
        await telegram.initialize()
        
        # ارسال گزارش
        await telegram.send_report("✅ سیستم فعال شد!")
        
        # نظارت بر کانال‌ها
        await telegram.monitor_channels()
        
        print("Stats:", telegram.get_stats())
    
    asyncio.run(main())
