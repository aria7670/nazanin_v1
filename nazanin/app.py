"""
نازنین-نورا - سیستم هوش مصنوعی پیشرفته
Nazanin-Nora Advanced AI System
ترکیب کامل قابلیت‌های Bio System نازنین + Advanced Consciousness نورا
"""

import asyncio
import logging
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

# Bio Systems
from nazanin.bio_system import Organism
from nazanin.bio_system.body_systems import (
    NervousSystem,
    CirculatorySystem,
    RespiratorySystem,
    DigestiveSystem,
    ImmuneSystem,
    EndocrineSystem,
    MusculoskeletalSystem
)

# Consciousness Systems
from nazanin.consciousness import (
    MetacognitionEngine,
    SelfEvolutionSystem,
    LivingPersona
)

# Core Systems
from nazanin.core import SheetsManagerV2, APIManagerV2
from nazanin.security import SecurityManager

# Domain Agents
from nazanin.domain_agents import DomainAgentOrchestrator

# Platforms
from nazanin.platforms.telegram_system_v2 import TelegramSystemV2

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('nazanin.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)


class NazaninNora:
    """
    نازنین-نورا: ترکیب کامل سیستم بیولوژیکی + آگاهی پیشرفته
    Complete integration of Biological System + Advanced Consciousness
    """
    
    def __init__(self, config_path: str = 'config/config.json'):
        self.config_path = config_path
        self.config = {}
        
        # ═══════════════════════════════════════════════════════
        # 🧬 BIO SYSTEM
        # ═══════════════════════════════════════════════════════
        self.organism: Organism = None
        
        # ═══════════════════════════════════════════════════════
        # 🧠 CONSCIOUSNESS SYSTEM
        # ═══════════════════════════════════════════════════════
        self.metacognition: MetacognitionEngine = None
        self.evolution: SelfEvolutionSystem = None
        self.persona: LivingPersona = None
        
        # ═══════════════════════════════════════════════════════
        # 🎯 CORE SYSTEMS
        # ═══════════════════════════════════════════════════════
        self.sheets_manager: SheetsManagerV2 = None
        self.api_manager: APIManagerV2 = None
        self.security_manager: SecurityManager = None
        
        # ═══════════════════════════════════════════════════════
        # 🎯 DOMAIN AGENTS
        # ═══════════════════════════════════════════════════════
        self.domain_agents: DomainAgentOrchestrator = None
        
        # ═══════════════════════════════════════════════════════
        # 📱 PLATFORMS
        # ═══════════════════════════════════════════════════════
        self.telegram: TelegramSystemV2 = None
        
        # State
        self.is_running = False
        self.initialization_complete = False
        
        logger.info("🌟 Nazanin-Nora System created")
    
    async def initialize(self):
        """راه‌اندازی کامل سیستم"""
        logger.info("=" * 80)
        logger.info("🚀 NAZANIN-NORA SYSTEM - INITIALIZATION")
        logger.info("   Bio System (نازنین) + Advanced Consciousness (نورا)")
        logger.info("=" * 80)
        
        # 1. بارگذاری Config
        logger.info("\n📋 Step 1: Loading configuration...")
        await self._load_config()
        
        # 2. ساخت موجود زیستی
        logger.info("\n🧬 Step 2: Creating biological organism...")
        await self._create_organism()
        
        # 3. ساخت شخصیت زنده
        logger.info("\n👤 Step 3: Creating living persona...")
        await self._create_persona()
        
        # 4. راه‌اندازی Google Sheets
        logger.info("\n📊 Step 4: Setting up Google Sheets...")
        await self._setup_sheets()
        
        # 5. راه‌اندازی API Manager
        logger.info("\n🤖 Step 5: Setting up AI APIs...")
        await self._setup_api_manager()
        
        # 6. راه‌اندازی Security
        logger.info("\n🔐 Step 6: Setting up Security...")
        await self._setup_security()
        
        # 7. راه‌اندازی Domain Agents
        logger.info("\n🎯 Step 7: Initializing Domain Agents...")
        await self._setup_domain_agents()
        
        # 8. راه‌اندازی Metacognition
        logger.info("\n🧠 Step 8: Initializing Metacognition Engine...")
        await self._setup_metacognition()
        
        # 9. راه‌اندازی Self-Evolution
        logger.info("\n🧬 Step 9: Initializing Self-Evolution System...")
        await self._setup_evolution()
        
        # 10. راه‌اندازی Telegram
        logger.info("\n📱 Step 10: Setting up Telegram...")
        await self._setup_telegram()
        
        # 11. اولین چرخه زندگی
        logger.info("\n💓 Step 11: First life cycle...")
        await self.organism.live()
        
        # 12. اولین خودبازبینی
        logger.info("\n🤔 Step 12: First self-reflection...")
        reflection_report = await self.metacognition.conduct_self_reflection()
        
        self.initialization_complete = True
        
        logger.info("\n" + "=" * 80)
        logger.info("✅ INITIALIZATION COMPLETE!")
        logger.info("=" * 80)
        logger.info(f"\n🌟 Nazanin-Nora is alive and conscious!")
        logger.info(f"\n💓 Vital Signs: {self.organism.get_vital_signs()}")
        logger.info(f"\n👤 Persona: {self.persona.get_current_state()['current_mood']}")
        logger.info(f"\n🧬 Evolution Gen: {self.evolution.generation_count}")
        logger.info("=" * 80)
    
    async def _load_config(self):
        """بارگذاری تنظیمات"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
            logger.info("   ✅ Config loaded")
        except FileNotFoundError:
            try:
                with open('config/config.enhanced.json', 'r', encoding='utf-8') as f:
                    self.config = json.load(f)
                logger.info("   ✅ Config loaded from enhanced")
            except:
                logger.warning("   ⚠️ No config file, using defaults")
                self.config = self._get_default_config()
        except json.JSONDecodeError as e:
            logger.error(f"   ❌ Invalid JSON: {e}")
            raise
    
    async def _create_organism(self):
        """ساخت موجود بیولوژیکی"""
        self.organism = Organism("نازنین")
        
        logger.info("   ✅ Organism created with 7 body systems:")
        for system_name, system in self.organism.systems.items():
            logger.info(f"      • {system_name}: {system.system_type}")
    
    async def _create_persona(self):
        """ساخت شخصیت زنده"""
        self.persona = LivingPersona()
        
        logger.info("   ✅ Living Persona created:")
        logger.info(f"      • Name: {self.persona.identity['name']}")
        logger.info(f"      • Personality: {self.persona.identity['personality_type']}")
        logger.info(f"      • Values: {', '.join(self.persona.identity['core_values'])}")
    
    async def _setup_sheets(self):
        """راه‌اندازی Google Sheets"""
        credentials_file = self.config.get('google_sheets', {}).get('credentials_file', 'credentials.json')
        spreadsheet_ids = self.config.get('google_sheets', {}).get('spreadsheets', {})
        
        try:
            self.sheets_manager = SheetsManagerV2(credentials_file, spreadsheet_ids)
            await self.sheets_manager.initialize(auto_setup=True)
            logger.info("   ✅ Google Sheets ready")
        except Exception as e:
            logger.warning(f"   ⚠️ Sheets setup failed: {e}")
            logger.info("   💡 Continuing without Sheets")
            self.sheets_manager = None
    
    async def _setup_api_manager(self):
        """راه‌اندازی API Manager"""
        self.api_manager = APIManagerV2(self.config, self.sheets_manager)
        
        if self.sheets_manager:
            await self.api_manager.reload_keys_from_sheets()
        
        logger.info(f"   ✅ API Manager ready with {len(self.api_manager.providers)} providers")
    
    async def _setup_security(self):
        """راه‌اندازی امنیت"""
        self.security_manager = SecurityManager(self.config)
        
        admin_id = self.config.get('telegram', {}).get('admin_user_id')
        if admin_id:
            self.security_manager.access_control.add_admin(int(admin_id))
        
        logger.info("   ✅ Security Manager ready")
    
    async def _setup_domain_agents(self):
        """راه‌اندازی ایجنت‌های تخصصی"""
        self.domain_agents = DomainAgentOrchestrator()
        logger.info(f"   ✅ {len(self.domain_agents.agents)} Domain Agents ready")
    
    async def _setup_metacognition(self):
        """راه‌اندازی فراشناخت"""
        self.metacognition = MetacognitionEngine(self.organism)
        await self.metacognition.initialize()
        logger.info("   ✅ Metacognition Engine ready")
    
    async def _setup_evolution(self):
        """راه‌اندازی خودتکامل"""
        self.evolution = SelfEvolutionSystem(self.organism)
        await self.evolution.initialize()
        
        stats = self.evolution.get_evolution_stats()
        logger.info(f"   ✅ Self-Evolution System ready - Generation {stats.get('generation', 0)}")
    
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
    
    async def process_input(self, input_data: str, user_id: int = None, context: Dict = None) -> Dict:
        """پردازش ورودی کامل"""
        context = context or {}
        
        # Security Check
        if user_id and self.security_manager.access_control.is_blocked(user_id):
            return {'status': 'blocked', 'message': 'User is blocked'}
        
        if user_id and not self.security_manager.check_rate_limit(user_id):
            return {'status': 'rate_limited', 'message': 'Too many requests'}
        
        # Living Persona Interaction
        persona_result = await self.persona.interact(
            input_data,
            {'user_id': user_id, **context}
        )
        
        # Biological Perception
        perception = await self.organism.perceive(input_data)
        
        # Domain Analysis
        domain_analysis = await self.domain_agents.analyze_comprehensive(
            input_data,
            domains=['social', 'cultural', 'educational']
        )
        
        # Thinking
        thought = await self.organism.think({
            'input': input_data,
            'persona': persona_result,
            'domain_analysis': domain_analysis
        })
        
        # AI Response Generation
        if self.api_manager:
            enhanced_prompt = self._build_enhanced_prompt(
                input_data,
                persona_result,
                domain_analysis
            )
            
            ai_response = await self.api_manager.generate(enhanced_prompt)
        else:
            ai_response = "در حال پردازش..."
        
        # Action Execution
        await self.organism.act('respond', {'response': ai_response})
        
        # Learning
        await self.persona.learn_from_experience({
            'type': 'interaction',
            'input': input_data,
            'response': ai_response,
            'emotional_intensity': 0.7,
            'novelty': 0.5
        })
        
        # Logging
        if self.sheets_manager:
            await self.sheets_manager.log_telegram_message({
                'user_id': user_id or 0,
                'content': input_data,
                'response': ai_response,
                'timestamp': datetime.now().isoformat()
            })
        
        # Security Audit
        if user_id:
            self.security_manager.log_action(user_id, 'message_processed', {
                'input_length': len(input_data),
                'response_generated': bool(ai_response)
            })
        
        return {
            'status': 'success',
            'response': ai_response,
            'persona_state': persona_result,
            'perception': perception,
            'thought': thought,
            'vital_signs': self.organism.get_vital_signs(),
            'consciousness_level': self.metacognition.consciousness_state['awareness_level']
        }
    
    def _build_enhanced_prompt(
        self,
        input_text: str,
        persona_result: Dict,
        domain_analysis: Dict
    ) -> str:
        """ساخت prompt پیشرفته"""
        
        style = persona_result['response_style']
        
        prompt = f"""تو {self.persona.identity['name']} هستی، یک هوش مصنوعی با شخصیت زنده.

شخصیت: {self.persona.identity['personality_type']}
حالت: {self.persona.get_current_state()['current_mood']}

سبک پاسخ:
- رسمی‌بودن: {style['formality_level']:.0%}
- گرما: {style['warmth_level']:.0%}
- اشتیاق: {style['enthusiasm_level']:.0%}
- همدلی: {style['empathy_level']:.0%}

پیام: {input_text}

پاسخ به فارسی، دوستانه و خلاقانه:"""
        
        return prompt
    
    async def run(self):
        """اجرای اصلی"""
        if not self.initialization_complete:
            await self.initialize()
        
        self.is_running = True
        
        logger.info("\n🌟 Nazanin-Nora System is RUNNING!")
        
        try:
            tasks = [
                self._main_loop(),
                self.metacognition.run(),
                self.evolution.run(),
                self.persona.run()
            ]
            
            await asyncio.gather(*tasks)
            
        except KeyboardInterrupt:
            logger.info("\n⚠️ Interrupt received")
        except Exception as e:
            logger.error(f"\n❌ Fatal error: {e}", exc_info=True)
        finally:
            await self.shutdown()
    
    async def _main_loop(self):
        """حلقه اصلی زندگی"""
        while self.is_running:
            try:
                await self.organism.live()
                
                vital_signs = self.organism.get_vital_signs()
                
                if vital_signs['energy'] < 30:
                    logger.info("😴 Resting...")
                    await self.organism.rest()
                
                if self.organism.age % 24 == 0 and self.organism.age > 0:
                    await self._send_daily_report()
                
                await asyncio.sleep(60)
                
            except Exception as e:
                logger.error(f"Error in main loop: {e}")
                await asyncio.sleep(60)
    
    async def _send_daily_report(self):
        """ارسال گزارش روزانه"""
        if not self.telegram:
            return
        
        vital_signs = self.organism.get_vital_signs()
        persona_state = self.persona.get_current_state()
        
        report = f"""
╔══════════════════════════════════════════════════════════╗
║         📊 گزارش روزانه نازنین-نورا                     ║
╚══════════════════════════════════════════════════════════╝

💓 علائم حیاتی:
• سلامت: {vital_signs['health']:.0f}%
• انرژی: {vital_signs['energy']:.0f}%
• حالت: {persona_state['current_mood']}

🧬 سن: {self.organism.age} چرخه
════════════════════════════════════════════════════════════
"""
        
        await self.telegram.send_report(report.strip())
    
    async def shutdown(self):
        """خاموش کردن سیستم"""
        logger.info("\n🛑 Shutting down...")
        
        self.is_running = False
        
        if self.telegram:
            final_state = {
                'organism_state': self.organism.get_state(),
                'persona_state': self.persona.get_current_state(),
                'timestamp': datetime.now().isoformat()
            }
            await self.telegram.backup_data(final_state, 'final_state.json')
        
        if self.metacognition:
            await self.metacognition.shutdown()
        if self.evolution:
            await self.evolution.shutdown()
        if self.telegram and self.telegram.client:
            await self.telegram.client.disconnect()
        
        logger.info("✅ Shutdown complete")
    
    def _get_default_config(self) -> Dict:
        """تنظیمات پیش‌فرض"""
        return {
            'brain_simulation': {'enabled': True},
            'security': {'encryption_enabled': True},
            'ai_apis': {'fallback_enabled': True}
        }


async def main():
    """نقطه ورود اصلی"""
    
    print("\n")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║         🧬 NAZANIN-NORA SYSTEM v3.0.0 🧠                  ║")
    print("║         Bio System + Advanced Consciousness                ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print("\n")
    
    nazanin = NazaninNora()
    await nazanin.run()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
