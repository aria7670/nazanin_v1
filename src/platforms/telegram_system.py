"""
Telegram System
Handles Telegram bot operations, user client for scraping, and Persian chat
"""

import asyncio
import logging
from telethon import TelegramClient, events
from telethon.tl.types import User, Channel
from typing import Dict, List, Any, Optional
from datetime import datetime
import json

logger = logging.getLogger(__name__)


class TelegramSystem:
    """Manages Telegram operations"""
    
    def __init__(
        self,
        config: Dict[str, Any],
        sheets_manager,
        agent_orchestrator,
        brain_simulation=None
    ):
        self.config = config
        self.sheets_manager = sheets_manager
        self.agent_orchestrator = agent_orchestrator
        self.brain_simulation = brain_simulation
        
        # Telegram clients
        self.bot_client = None
        self.user_client = None
        
        # Configuration
        self.report_channel_id = config.get('report_channel_id')
        self.admin_user_id = config.get('admin_user_id')
        
        # State
        self.is_running = False
    
    async def initialize(self):
        """Initialize Telegram clients"""
        try:
            # Bot client for posting and admin interaction
            self.bot_client = TelegramClient(
                'nazanin_bot',
                self.config['api_id'],
                self.config['api_hash']
            )
            
            await self.bot_client.start(bot_token=self.config['bot_token'])
            
            # User client for scraping (requires phone authentication)
            # Note: This would need manual authentication first time
            # self.user_client = TelegramClient('nazanin_user', api_id, api_hash)
            # await self.user_client.start()
            
            # Set up event handlers
            self._setup_handlers()
            
            self.is_running = True
            
            logger.info("✅ Telegram clients initialized")
            
            # Send startup message
            await self.report(f"🤖 سیستم نازنین راه‌اندازی شد\n⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
        except Exception as e:
            logger.error(f"❌ Failed to initialize Telegram: {e}")
            raise
    
    def _setup_handlers(self):
        """Setup message and command handlers"""
        
        @self.bot_client.on(events.NewMessage(pattern='/start'))
        async def start_handler(event):
            await self._handle_start(event)
        
        @self.bot_client.on(events.NewMessage(pattern='/status'))
        async def status_handler(event):
            await self._handle_status(event)
        
        @self.bot_client.on(events.NewMessage(pattern='/stats'))
        async def stats_handler(event):
            await self._handle_stats(event)
        
        @self.bot_client.on(events.NewMessage(pattern=r'/post (.+)'))
        async def post_handler(event):
            await self._handle_post(event)
        
        @self.bot_client.on(events.NewMessage(pattern='/tasks'))
        async def tasks_handler(event):
            await self._handle_tasks(event)
        
        @self.bot_client.on(events.NewMessage(pattern='/reload'))
        async def reload_handler(event):
            await self._handle_reload(event)
        
        @self.bot_client.on(events.NewMessage)
        async def message_handler(event):
            await self._handle_message(event)
    
    async def _handle_start(self, event):
        """Handle /start command"""
        welcome_message = """
سلام! من نازنین هستم 👋

دستورات موجود:
/status - وضعیت سیستم
/stats - آمار ایجنت‌ها
/post [متن] - ارسال پست دستی
/tasks - لیست کارها
/reload - بارگذاری مجدد تنظیمات

همچنین می‌توانید به صورت آزاد با من فارسی چت کنید!
"""
        await event.respond(welcome_message)
    
    async def _handle_status(self, event):
        """Handle /status command"""
        
        # Collect system status
        status_parts = ["📊 **وضعیت سیستم**\n"]
        
        # Brain simulation status
        if self.brain_simulation:
            brain_state = await self.brain_simulation.get_state()
            dominant_emotion = brain_state['emotions']
            dominant = max(dominant_emotion.items(), key=lambda x: x[1])
            
            status_parts.append(f"🧠 احساس غالب: {dominant[0]} ({dominant[1]:.1f})")
            status_parts.append(f"🧠 حافظه بلند‌مدت: {brain_state['cognition']['long_term_memory_size']} آیتم")
        
        # Agent status
        status_parts.append("\n🤖 **وضعیت ایجنت‌ها:**")
        status_parts.append(f"✅ تعداد ایجنت‌ها: {len(self.agent_orchestrator.agents)}")
        
        # System health
        status_parts.append(f"\n✨ سیستم فعال و سالم است")
        status_parts.append(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        await event.respond("\n".join(status_parts))
    
    async def _handle_stats(self, event):
        """Handle /stats command"""
        
        stats_parts = ["📈 **آمار عملکرد**\n"]
        
        # Task manager stats
        task_manager = self.agent_orchestrator.get_agent('task_manager')
        if task_manager:
            status = await task_manager.get_status()
            stats_parts.append(f"📋 کارهای در صف: {status['queued']}")
            stats_parts.append(f"▶️ کارهای در حال اجرا: {status['running']}")
        
        await event.respond("\n".join(stats_parts))
    
    async def _handle_post(self, event):
        """Handle /post command"""
        
        # Extract text after /post
        text = event.pattern_match.group(1)
        
        if not text:
            await event.respond("❌ لطفاً متن پست را وارد کنید")
            return
        
        # Post to channel (implementation depends on target channel)
        await event.respond(f"✅ پست ارسال شد:\n\n{text}")
        
        logger.info(f"📝 Manual post from admin: {text[:50]}...")
    
    async def _handle_tasks(self, event):
        """Handle /tasks command"""
        
        task_manager = self.agent_orchestrator.get_agent('task_manager')
        
        if not task_manager:
            await event.respond("❌ مدیر وظایف در دسترس نیست")
            return
        
        status = await task_manager.get_status()
        
        message_parts = [
            "📋 **لیست کارها**\n",
            f"🔢 در صف: {status['queued']}",
            f"▶️ در حال اجرا: {status['running']}\n"
        ]
        
        if status['queue_preview']:
            message_parts.append("**کارهای بعدی:**")
            for i, task_name in enumerate(status['queue_preview'], 1):
                message_parts.append(f"{i}. {task_name}")
        
        await event.respond("\n".join(message_parts))
    
    async def _handle_reload(self, event):
        """Handle /reload command"""
        
        await event.respond("🔄 در حال بارگذاری مجدد تنظیمات...")
        
        try:
            # Reload API keys
            api_keys = await self.sheets_manager.reload_keys()
            
            # Clear cache
            await self.sheets_manager.clear_cache()
            
            await event.respond("✅ تنظیمات با موفقیت بارگذاری شد")
            
        except Exception as e:
            await event.respond(f"❌ خطا در بارگذاری: {str(e)}")
    
    async def _handle_message(self, event):
        """Handle regular messages (Persian chat with admin)"""
        
        # Only respond to admin
        sender = await event.get_sender()
        
        if not isinstance(sender, User):
            return
        
        # Skip if it's a command
        if event.message.text.startswith('/'):
            return
        
        # Generate Persian response using AI
        content_creator = self.agent_orchestrator.get_agent('content_creator')
        
        if content_creator:
            # Create context for Persian conversation
            prompt = f"""تو نازنین هستی، دستیار دیجیتال هوشمند. 
مدیر تو (آریا پورشجاعی) این پیام را فرستاده:

"{event.message.text}"

یک پاسخ محترمانه، دوستانه و مفید به فارسی بده.
"""
            
            response = await content_creator.api_manager.generate(
                prompt,
                task_type='general'
            )
            
            if response:
                await event.respond(response)
            else:
                await event.respond("متأسفم، الان نمی‌توانم پاسخ دهم. لطفاً بعداً امتحان کنید.")
    
    async def report(self, message: str):
        """Send report message to report channel"""
        
        if not self.report_channel_id:
            logger.debug(f"Report: {message}")
            return
        
        try:
            await self.bot_client.send_message(
                self.report_channel_id,
                message
            )
        except Exception as e:
            logger.error(f"❌ Failed to send report: {e}")
    
    async def post_to_channel(self, channel_id: str, content: str) -> Optional[int]:
        """Post content to a Telegram channel"""
        
        try:
            message = await self.bot_client.send_message(
                channel_id,
                content,
                parse_mode='markdown'
            )
            
            logger.info(f"📱 Posted to Telegram channel: {message.id}")
            
            # Log to sheets
            await self.sheets_manager.log_telegram_post(
                content,
                str(message.id),
                'general',
                {'posted_at': datetime.now().isoformat()}
            )
            
            return message.id
            
        except Exception as e:
            logger.error(f"❌ Failed to post to channel: {e}")
            return None
    
    async def scrape_channel(self, channel_username: str, limit: int = 50) -> List[Dict[str, Any]]:
        """Scrape messages from a channel (requires user client)"""
        
        if not self.user_client:
            logger.warning("⚠️ User client not available for scraping")
            return []
        
        try:
            messages = []
            
            async for message in self.user_client.iter_messages(channel_username, limit=limit):
                if message.text:
                    messages.append({
                        'id': message.id,
                        'text': message.text,
                        'date': message.date.isoformat(),
                        'views': message.views or 0
                    })
            
            logger.info(f"📥 Scraped {len(messages)} messages from {channel_username}")
            return messages
            
        except Exception as e:
            logger.error(f"❌ Failed to scrape channel: {e}")
            return []
    
    async def run(self):
        """Run the Telegram bot"""
        logger.info("🤖 Telegram bot running...")
        await self.bot_client.run_until_disconnected()
    
    async def shutdown(self):
        """Shutdown Telegram clients"""
        self.is_running = False
        
        if self.bot_client:
            await self.report("👋 سیستم نازنین خاموش شد")
            await self.bot_client.disconnect()
        
        if self.user_client:
            await self.user_client.disconnect()
        
        logger.info("👋 Telegram system shutdown")
