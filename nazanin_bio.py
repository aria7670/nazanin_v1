"""
Nazanin Bio System - نسخه بیولوژیکی کامل
سیستم کامل با شبیه‌سازی بدن انسان و ایجنت‌های تخصصی
"""

import asyncio
import logging
import json
import sys
from datetime import datetime
from typing import Dict, Any

# Bio Systems
from src.bio_system import Organism
from src.bio_system.body_systems import (
    NervousSystem,
    CirculatorySystem,
    RespiratorySystem,
    DigestiveSystem,
    ImmuneSystem,
    EndocrineSystem,
    MusculoskeletalSystem
)

# Core Systems
from src.core import SheetsManagerV2, APIManagerV2, SheetsAutoSetup
from src.security import SecurityManager

# Domain Agents
from src.domain_agents import DomainAgentOrchestrator

# Platforms
from src.platforms.telegram_system_v2 import TelegramSystemV2

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('nazanin_bio.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)


class NazaninBio:
    """
    نازنین - نسخه بیولوژیکی
    یک موجود دیجیتال با سیستم‌های بیولوژیکی کامل
    """
    
    def __init__(self, config_path: str = 'config/config.json'):
        self.config_path = config_path
        self.config = {}
        
        # Bio System - موجود زنده
        self.organism: Organism = None
        
        # Core Systems
        self.sheets_manager: SheetsManagerV2 = None
        self.api_manager: APIManagerV2 = None
        self.security_manager: SecurityManager = None
        
        # Domain Agents
        self.domain_agents: DomainAgentOrchestrator = None
        
        # Platforms
        self.telegram: TelegramSystemV2 = None
        
        # State
        self.is_running = False
        self.initialization_complete = False
        
        logger.info("🧬 Nazanin Bio System created")
    
    async def initialize(self):
        """راه‌اندازی کامل سیستم"""
        logger.info("=" * 60)
        logger.info("🚀 NAZANIN BIO SYSTEM - INITIALIZATION")
        logger.info("=" * 60)
        
        # 1. بارگذاری config
        logger.info("\n📋 Step 1: Loading configuration...")
        await self._load_config()
        
        # 2. ساخت موجود زیستی
        logger.info("\n🧬 Step 2: Creating biological organism...")
        await self._create_organism()
        
        # 3. راه‌اندازی Google Sheets (با auto setup)
        logger.info("\n📊 Step 3: Setting up Google Sheets...")
        await self._setup_sheets()
        
        # 4. راه‌اندازی API Manager
        logger.info("\n🤖 Step 4: Setting up AI APIs...")
        await self._setup_api_manager()
        
        # 5. راه‌اندازی Security
        logger.info("\n🔐 Step 5: Setting up Security...")
        await self._setup_security()
        
        # 6. راه‌اندازی Domain Agents
        logger.info("\n🎯 Step 6: Initializing Domain Agents...")
        await self._setup_domain_agents()
        
        # 7. راه‌اندازی Telegram
        logger.info("\n📱 Step 7: Setting up Telegram...")
        await self._setup_telegram()
        
        # 8. اولین چرخه زندگی
        logger.info("\n💓 Step 8: First life cycle...")
        await self.organism.live()
        
        self.initialization_complete = True
        
        logger.info("\n" + "=" * 60)
        logger.info("✅ INITIALIZATION COMPLETE!")
        logger.info("=" * 60)
        logger.info(f"\n🌟 Nazanin is alive! Vital signs:")
        logger.info(f"   {self.organism.get_vital_signs()}")
        logger.info("=" * 60)
    
    async def _load_config(self):
        """بارگذاری تنظیمات"""
        try:
            # تلاش برای config.json
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
            logger.info("   ✅ Config loaded from config.json")
        
        except FileNotFoundError:
            # تلاش برای config.enhanced.json
            try:
                with open('config/config.enhanced.json', 'r', encoding='utf-8') as f:
                    self.config = json.load(f)
                logger.info("   ✅ Config loaded from config.enhanced.json")
            except:
                logger.warning("   ⚠️ No config file found, using defaults")
                self.config = self._get_default_config()
        
        except json.JSONDecodeError as e:
            logger.error(f"   ❌ Config file is invalid JSON: {e}")
            raise
    
    async def _create_organism(self):
        """ساخت موجود زیستی"""
        self.organism = Organism("Nazanin")
        
        logger.info("   ✅ Organism created with systems:")
        for system_name, system in self.organism.systems.items():
            logger.info(f"      • {system_name}: {system.system_type}")
    
    async def _setup_sheets(self):
        """راه‌اندازی Google Sheets"""
        credentials_file = self.config.get('google_sheets', {}).get('credentials_file', 'credentials.json')
        spreadsheet_ids = self.config.get('google_sheets', {}).get('spreadsheets', {})
        
        try:
            self.sheets_manager = SheetsManagerV2(credentials_file, spreadsheet_ids)
            await self.sheets_manager.initialize(auto_setup=True)
            logger.info("   ✅ Google Sheets ready")
        except Exception as e:
            logger.warning(f"   ⚠️ Google Sheets setup failed: {e}")
            logger.info("   💡 Continuing without Sheets (will use local storage)")
            self.sheets_manager = None
    
    async def _setup_api_manager(self):
        """راه‌اندازی API Manager"""
        self.api_manager = APIManagerV2(self.config, self.sheets_manager)
        
        # بارگذاری کلیدها از sheets (اگه موجوده)
        if self.sheets_manager:
            await self.api_manager.reload_keys_from_sheets()
        
        logger.info(f"   ✅ API Manager ready with {len(self.api_manager.providers)} providers")
    
    async def _setup_security(self):
        """راه‌اندازی امنیت"""
        self.security_manager = SecurityManager(self.config)
        
        # افزودن admin اولیه
        admin_id = self.config.get('telegram', {}).get('admin_user_id')
        if admin_id:
            self.security_manager.access_control.add_admin(int(admin_id))
        
        logger.info("   ✅ Security Manager ready")
    
    async def _setup_domain_agents(self):
        """راه‌اندازی ایجنت‌های تخصصی"""
        self.domain_agents = DomainAgentOrchestrator()
        logger.info(f"   ✅ {len(self.domain_agents.agents)} Domain Agents ready")
        for agent_name in self.domain_agents.agents.keys():
            logger.info(f"      • {agent_name}")
    
    async def _setup_telegram(self):
        """راه‌اندازی تلگرام"""
        try:
            self.telegram = TelegramSystemV2(
                self.config,
                self.sheets_manager,
                self.organism
            )
            await self.telegram.initialize()
            logger.info("   ✅ Telegram System ready")
        except Exception as e:
            logger.warning(f"   ⚠️ Telegram setup failed: {e}")
            logger.info("   💡 Continuing without Telegram")
            self.telegram = None
    
    async def process_input(self, input_data: str, user_id: int = None) -> Dict:
        """پردازش ورودی کامل"""
        
        # 1. بررسی امنیتی
        if user_id and self.security_manager.access_control.is_blocked(user_id):
            return {'status': 'blocked', 'message': 'User is blocked'}
        
        # 2. بررسی rate limit
        if user_id and not self.security_manager.check_rate_limit(user_id):
            return {'status': 'rate_limited', 'message': 'Too many requests'}
        
        # 3. درک توسط موجود زیستی
        perception = await self.organism.perceive(input_data)
        
        # 4. تحلیل توسط domain agents
        domain_analysis = await self.domain_agents.analyze_comprehensive(
            input_data,
            domains=['social', 'cultural', 'educational']
        )
        
        # 5. فکر کردن
        thought = await self.organism.think({
            'input': input_data,
            'domain_analysis': domain_analysis
        })
        
        # 6. تولید پاسخ با AI
        if self.api_manager:
            ai_response = await self.api_manager.generate(
                f"پاسخ به این پیام بده (فارسی، دوستانه): {input_data}"
            )
        else:
            ai_response = "متوجه شدم. در حال پردازش..."
        
        # 7. انجام عمل
        await self.organism.act('respond', {'response': ai_response})
        
        # 8. ثبت log
        if self.sheets_manager:
            await self.sheets_manager.log_telegram_message({
                'user_id': user_id or 0,
                'content': input_data,
                'response': ai_response,
                'timestamp': datetime.now().isoformat()
            })
        
        # 9. ثبت امنیتی
        if user_id:
            self.security_manager.log_action(user_id, 'message_processed', {
                'input_length': len(input_data),
                'response_generated': bool(ai_response)
            })
        
        return {
            'status': 'success',
            'response': ai_response,
            'perception': perception,
            'thought': thought,
            'vital_signs': self.organism.get_vital_signs()
        }
    
    async def run(self):
        """اجرای اصلی"""
        if not self.initialization_complete:
            await self.initialize()
        
        self.is_running = True
        
        logger.info("\n🌟 Nazanin Bio System is now RUNNING!")
        logger.info("\n💡 System capabilities:")
        logger.info("   • Biological organism simulation")
        logger.info("   • 8 specialized domain agents")
        logger.info("   • Auto-setup Google Sheets")
        logger.info("   • Advanced security")
        logger.info("   • Full Telegram control")
        logger.info("")
        
        try:
            # حلقه اصلی زندگی
            while self.is_running:
                # یک چرخه زندگی
                await self.organism.live()
                
                # چک کردن سلامت
                vital_signs = self.organism.get_vital_signs()
                
                # اگه انرژی کم شد، استراحت کن
                if vital_signs['energy'] < 30:
                    logger.info("😴 Energy low, resting...")
                    await self.organism.rest()
                
                # گزارش روزانه (هر 24 چرخه)
                if self.organism.age % 24 == 0 and self.organism.age > 0:
                    await self._send_daily_report()
                
                # صبر کن
                await asyncio.sleep(60)  # هر دقیقه یک چرخه
        
        except KeyboardInterrupt:
            logger.info("\n⚠️ Received interrupt signal")
        except Exception as e:
            logger.error(f"\n❌ Fatal error: {e}", exc_info=True)
        finally:
            await self.shutdown()
    
    async def _send_daily_report(self):
        """ارسال گزارش روزانه"""
        if not self.telegram:
            return
        
        vital_signs = self.organism.get_vital_signs()
        state = self.organism.get_state()
        stats = self.api_manager.get_stats() if self.api_manager else {}
        
        report = f"""
📊 گزارش روزانه نازنین
━━━━━━━━━━━━━━━━━━━━

💓 علائم حیاتی:
• سلامت: {vital_signs['health']}%
• انرژی: {vital_signs['energy']}%
• ضربان قلب: {vital_signs['heart_rate']} bpm
• اکسیژن: {vital_signs['oxygen']}%
• استرس: {vital_signs['stress']}%
• شادی: {vital_signs['happiness']}%

🤖 عملکرد AI:
• تعداد کل فراخوانی: {stats.get('total_calls', 0)}
• موفق: {stats.get('successful_calls', 0)}
• ناموفق: {stats.get('failed_calls', 0)}
• نرخ موفقیت: {stats.get('success_rate', 0):.2%}

🧬 سن: {state['age']} چرخه

🌟 وضعیت: {'سالم و فعال' if vital_signs['health'] > 70 else 'نیاز به مراقبت'}
        """
        
        await self.telegram.send_report(report.strip())
    
    async def shutdown(self):
        """خاموش کردن سیستم"""
        logger.info("\n🛑 Shutting down Nazanin Bio...")
        
        self.is_running = False
        
        # بک‌آپ وضعیت نهایی
        if self.telegram:
            final_state = {
                'organism_state': self.organism.get_state(),
                'timestamp': datetime.now().isoformat(),
                'age': self.organism.age
            }
            await self.telegram.backup_data(final_state, 'final_state.json')
        
        # قطع اتصالات
        if self.telegram and self.telegram.client:
            await self.telegram.client.disconnect()
        
        logger.info("✅ Shutdown complete. Goodbye! 👋")
    
    def _get_default_config(self) -> Dict:
        """تنظیمات پیش‌فرض"""
        return {
            'brain_simulation': {'enabled': True},
            'quantum_agent': {'enabled': True},
            'neural_agent': {'enabled': True},
            'security': {
                'encryption_enabled': True,
                'rate_limiting': {'enabled': True}
            },
            'ai_apis': {
                'fallback_enabled': True
            }
        }


async def main():
    """نقطه ورود اصلی"""
    
    print("\n")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║                                                            ║")
    print("║         🧬 NAZANIN BIO SYSTEM v2.1.0 🧬                   ║")
    print("║                                                            ║")
    print("║     ربات هوش مصنوعی با شبیه‌سازی کامل بدن انسان         ║")
    print("║                                                            ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print("\n")
    
    nazanin = NazaninBio()
    await nazanin.run()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
