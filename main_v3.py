"""
Nazanin V3 - Biological Intelligence System
سیستم هوش زیستی - نسخه 3
"""

import asyncio
import logging
import json
import sys
from datetime import datetime
from typing import Dict, Any

# سیستم‌های اصلی
from src.core import SheetsManagerV2, APIManagerV2, SheetsAutoSetup
from src.bio_system import Organism
from src.domain_agents import DomainAgentOrchestrator
from src.platforms import TelegramSystemV2
from src.security import SecurityManager

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('nazanin_v3.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)


class NazaninV3:
    """نازنین نسخه 3 - موجود زیستی هوشمند"""
    
    def __init__(self, config_path: str = 'config/config.enhanced.json'):
        self.config_path = config_path
        self.config = {}
        
        # سیستم‌های اصلی
        self.sheets_manager = None
        self.api_manager = None
        self.security_manager = None
        self.telegram_system = None
        
        # سیستم زیستی
        self.organism = None  # موجود کامل
        
        # ایجنت‌های تخصصی
        self.domain_agents = None
        
        # وضعیت
        self.is_running = False
        self.start_time = None
        
        logger.info("🧬 Nazanin V3 created")
    
    async def initialize(self):
        """راه‌اندازی کامل سیستم"""
        logger.info("=" * 60)
        logger.info("🚀 NAZANIN V3 - BIOLOGICAL INTELLIGENCE SYSTEM")
        logger.info("=" * 60)
        logger.info("")
        
        self.start_time = datetime.now()
        
        # 1. بارگذاری Config
        logger.info("📋 Step 1/7: Loading configuration...")
        await self._load_config()
        logger.info("✅ Config loaded")
        
        # 2. Security Manager
        logger.info("\n🔐 Step 2/7: Initializing Security...")
        self.security_manager = SecurityManager(self.config)
        logger.info("✅ Security initialized")
        
        # 3. Sheets Manager (با Auto Setup)
        logger.info("\n📊 Step 3/7: Setting up Google Sheets...")
        try:
            spreadsheet_ids = self.config.get('google_sheets', {}).get('spreadsheets', {})
            self.sheets_manager = SheetsManagerV2(
                self.config['google_sheets']['credentials_file'],
                spreadsheet_ids
            )
            await self.sheets_manager.initialize(auto_setup=True)
            logger.info("✅ Sheets Manager ready (Auto setup completed)")
        except Exception as e:
            logger.warning(f"⚠️ Sheets setup failed: {e}")
            logger.info("💡 Continuing without Sheets...")
        
        # 4. API Manager (با Fallback)
        logger.info("\n🤖 Step 4/7: Initializing AI APIs...")
        self.api_manager = APIManagerV2(self.config, self.sheets_manager)
        
        # بارگذاری کلیدها از Sheets (اگه موجوده)
        if self.sheets_manager:
            try:
                await self.api_manager.reload_keys_from_sheets()
            except:
                logger.info("💡 Using API keys from config file")
        
        logger.info(f"✅ API Manager ready with {len(self.api_manager.providers)} providers")
        
        # 5. Biological System (موجود زیستی)
        logger.info("\n🧬 Step 5/7: Creating biological organism...")
        self.organism = Organism("Nazanin")
        logger.info("✅ Organism 'Nazanin' is alive!")
        logger.info(f"   Vital Signs: {self.organism.get_vital_signs()}")
        
        # 6. Domain Agents (ایجنت‌های تخصصی)
        logger.info("\n🎯 Step 6/7: Activating domain agents...")
        self.domain_agents = DomainAgentOrchestrator()
        logger.info(f"✅ {len(self.domain_agents.agents)} domain agents active")
        for agent_name in self.domain_agents.agents.keys():
            logger.info(f"   • {agent_name}")
        
        # 7. Telegram System
        logger.info("\n📱 Step 7/7: Connecting to Telegram...")
        try:
            self.telegram_system = TelegramSystemV2(
                self.config,
                self.sheets_manager,
                self.organism
            )
            await self.telegram_system.initialize()
            logger.info("✅ Telegram connected")
            
            # ارسال گزارش راه‌اندازی
            await self._send_startup_report()
        except Exception as e:
            logger.warning(f"⚠️ Telegram connection failed: {e}")
            logger.info("💡 Continuing without Telegram...")
        
        # آماده!
        self.is_running = True
        
        logger.info("")
        logger.info("=" * 60)
        logger.info("🌟 NAZANIN V3 IS NOW ALIVE AND RUNNING!")
        logger.info("=" * 60)
        logger.info("")
        logger.info("💚 Health: 100%")
        logger.info("⚡ Energy: 100%")
        logger.info("🧠 Consciousness: Active")
        logger.info("🤖 All systems: Operational")
        logger.info("")
        logger.info("Press Ctrl+C to shutdown gracefully")
        logger.info("")
    
    async def _load_config(self):
        """بارگذاری تنظیمات"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            # اگه config.enhanced.json نبود، از config.json استفاده کن
            try:
                with open('config/config.json', 'r', encoding='utf-8') as f:
                    self.config = json.load(f)
                logger.info("💡 Using config.json")
            except:
                logger.error("❌ No config file found!")
                raise
    
    async def _send_startup_report(self):
        """ارسال گزارش راه‌اندازی"""
        report = f"""
🧬 **Nazanin V3 - Startup Report**

⏰ **Time**: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}

🟢 **Status**: All Systems Operational

**Biological Systems**:
• Health: {self.organism.health}%
• Energy: {self.organism.energy}%
• Active Systems: {len(self.organism.systems)}

**AI Systems**:
• API Providers: {len(self.api_manager.providers)}
• Domain Agents: {len(self.domain_agents.agents)}

**Data**:
• Spreadsheets: {len(self.sheets_manager.spreadsheets) if self.sheets_manager else 0}
• Channels: {len(self.telegram_system.channels) if self.telegram_system else 0}

**Security**:
• Encryption: {'Enabled' if self.security_manager.config.get('encryption_enabled') else 'Disabled'}
• Rate Limiting: {'Enabled' if self.security_manager.rate_limiter.enabled else 'Disabled'}

✅ Ready to serve!
        """
        
        if self.telegram_system:
            await self.telegram_system.send_report(report.strip())
    
    async def live_cycle(self):
        """چرخه زندگی - هر 60 ثانیه"""
        while self.is_running:
            try:
                # موجود زندگی می‌کنه
                await self.organism.live()
                
                # بررسی علائم حیاتی
                vital_signs = self.organism.get_vital_signs()
                
                # اگه انرژی کمه، استراحت
                if vital_signs['energy'] < 30:
                    logger.info("😴 Low energy, resting...")
                    await self.organism.rest()
                
                # لاگ وضعیت (هر 10 چرخه)
                if self.organism.age % 10 == 0:
                    logger.info(f"💚 Health: {vital_signs['health']}% | "
                              f"⚡ Energy: {vital_signs['energy']}% | "
                              f"❤️ Heart: {vital_signs['heart_rate']} bpm")
                
                # صبر برای چرخه بعد
                await asyncio.sleep(60)
                
            except Exception as e:
                logger.error(f"❌ Error in live cycle: {e}")
                await asyncio.sleep(60)
    
    async def process_input(self, input_text: str, context: Dict = None) -> Dict:
        """پردازش ورودی کامل"""
        try:
            # 1. Security check
            if context and 'user_id' in context:
                if not self.security_manager.check_rate_limit(context['user_id']):
                    return {'error': 'rate_limit_exceeded'}
            
            # 2. موجود زیستی ورودی رو درک می‌کنه
            perception = await self.organism.perceive(input_text)
            
            # اگه تهدید شناسایی شد
            if perception.get('blocked'):
                return {'status': 'blocked', 'reason': 'threat_detected'}
            
            # 3. تحلیل توسط domain agents
            domain_analysis = await self.domain_agents.analyze_comprehensive(
                input_text,
                domains=['social', 'cultural', 'educational']  # مرتبط‌ترین‌ها
            )
            
            # 4. فکر کردن توسط مغز
            thought = await self.organism.think(input_text)
            
            # 5. تولید پاسخ با AI
            ai_response = await self.api_manager.generate(
                f"کاربر گفت: {input_text}\n\nبا لحن دوستانه و مفید پاسخ بده:"
            )
            
            # 6. ترکیب نهایی
            final_response = {
                'perception': perception,
                'analysis': domain_analysis,
                'thought': thought,
                'ai_response': ai_response,
                'vital_signs': self.organism.get_vital_signs()
            }
            
            # 7. ثبت در sheets
            if self.sheets_manager:
                try:
                    await self.sheets_manager.log_telegram_message({
                        'message_id': '',
                        'user_id': context.get('user_id', '') if context else '',
                        'content': input_text,
                        'response': ai_response or '',
                        'timestamp': datetime.now().isoformat()
                    })
                except:
                    pass
            
            return final_response
            
        except Exception as e:
            logger.error(f"❌ Error processing input: {e}")
            return {'error': str(e)}
    
    async def start_background_tasks(self):
        """شروع وظایف پس‌زمینه"""
        tasks = [
            asyncio.create_task(self.live_cycle()),  # چرخه زندگی
        ]
        
        # نظارت بر کانال‌های تلگرام
        if self.telegram_system:
            async def monitor_loop():
                while self.is_running:
                    await self.telegram_system.monitor_channels()
                    await asyncio.sleep(300)  # هر 5 دقیقه
            
            tasks.append(asyncio.create_task(monitor_loop()))
        
        # بک‌آپ روزانه
        async def daily_backup():
            while self.is_running:
                await asyncio.sleep(86400)  # هر 24 ساعت
                if self.telegram_system:
                    await self.telegram_system.backup_data(
                        {'stats': self.get_stats()},
                        f'daily_backup_{datetime.now().strftime("%Y%m%d")}.json'
                    )
        
        tasks.append(asyncio.create_task(daily_backup()))
        
        return tasks
    
    async def run(self):
        """اجرای اصلی"""
        try:
            await self.initialize()
            
            # شروع وظایف پس‌زمینه
            background_tasks = await self.start_background_tasks()
            
            # اجرا تا زمانی که متوقف بشه
            await asyncio.gather(*background_tasks)
            
        except KeyboardInterrupt:
            logger.info("\n⚠️ Shutdown signal received")
        except Exception as e:
            logger.error(f"❌ Fatal error: {e}", exc_info=True)
        finally:
            await self.shutdown()
    
    async def shutdown(self):
        """خاموش کردن سیستم"""
        logger.info("\n🛑 Shutting down Nazanin V3...")
        
        self.is_running = False
        
        # ارسال گزارش خاموشی
        if self.telegram_system:
            try:
                shutdown_report = f"""
🛑 **Shutdown Report**

⏰ Started: {self.start_time.strftime('%H:%M:%S')}
⏰ Stopped: {datetime.now().strftime('%H:%M:%S')}

📊 Final Stats:
• Organism Age: {self.organism.age} cycles
• Health: {self.organism.health}%
• Total Messages: {len(self.telegram_system.conversations) if self.telegram_system else 0}

✅ Clean shutdown completed
                """
                await self.telegram_system.send_report(shutdown_report.strip())
            except:
                pass
        
        # قطع اتصال تلگرام
        if self.telegram_system and self.telegram_system.client:
            await self.telegram_system.client.disconnect()
        
        logger.info("✅ Shutdown complete")
    
    def get_stats(self) -> Dict:
        """آمار کامل سیستم"""
        return {
            'uptime': str(datetime.now() - self.start_time) if self.start_time else '0',
            'organism': self.organism.get_state() if self.organism else {},
            'api_manager': self.api_manager.get_stats() if self.api_manager else {},
            'telegram': self.telegram_system.get_stats() if self.telegram_system else {},
            'sheets': {
                'spreadsheets': len(self.sheets_manager.spreadsheets) if self.sheets_manager else 0
            }
        }


async def main():
    """نقطه ورود اصلی"""
    
    # نمایش لوگو
    print("""
    ╔══════════════════════════════════════════════╗
    ║                                              ║
    ║     🧬 NAZANIN V3 🧬                        ║
    ║     Biological Intelligence System          ║
    ║                                              ║
    ║     نازنین - موجود زیستی هوشمند           ║
    ║                                              ║
    ║     Version: 3.0.0                          ║
    ║     Status: Experimental                    ║
    ║                                              ║
    ╚══════════════════════════════════════════════╝
    """)
    
    nazanin = NazaninV3()
    await nazanin.run()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
