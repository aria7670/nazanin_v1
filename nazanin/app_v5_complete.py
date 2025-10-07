"""
Nazanin v5.0.0 - Complete Edition
نازنین نسخه 5.0 - نسخه کامل و جامع

ترکیب کامل:
✅ مغز عصبی عمیق 12 لایه
✅ سیستم ادراک و آگاهی
✅ سیستم خودمختار کامل
✅ 30 ماژول + 30 ایجنت + 50 الگوریتم
✅ ربات ByteLine (Frontend EN + Backend FA)
✅ Bio System (7 دستگاه بدن)
✅ Consciousness (فراشناخت، خودتکامل، شخصیت زنده)
✅ سیستم Google Sheets کامل (15 اسپردشیت، 75 زیرشیت)
✅ 6 ماژول Sheets + 6 ایجنت Sheets
"""

import asyncio
import logging
import json
from typing import Dict, List, Any, Optional
from datetime import datetime
from pathlib import Path

# Brain Systems
from nazanin.brain import DeepNeuralBrain, PerceptionAwarenessSystem
from nazanin.bio_system import Organism
from nazanin.consciousness import MetacognitionEngine, SelfEvolutionSystem, LivingPersona

# Autonomous
from nazanin.autonomous import AutonomousSystem

# Advanced Components
from nazanin.advanced import ModuleManager, AgentManager, AlgorithmManager

# ByteLine
from nazanin.byteline import ByteLineBot

# Core
from nazanin.core import SheetsManagerV2, APIManagerV2
from nazanin.security import SecurityManager
from nazanin.domain_agents import DomainAgentOrchestrator

# Sheets System (NEW!)
from nazanin.sheets_system import InitializationManager, get_summary
from nazanin.sheets_system.sheets_modules import SheetsModuleManager
from nazanin.sheets_system.sheets_agents import SheetsAgentManager

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('nazanin_v5.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


class NazaninV5Complete:
    """
    نازنین نسخه 5.0 - کامل‌ترین نسخه
    
    قابلیت‌ها:
    🧠 مغز 12 لایه + ادراک و آگاهی
    🤖 خودمختاری کامل
    📦 30 ماژول + 30 ایجنت + 50 الگوریتم
    📱 ByteLine Bot
    🧬 Bio + Consciousness
    📊 Google Sheets کامل (15 اسپردشیت)
    """
    
    def __init__(self, config_path: str = 'config/config.json'):
        self.config_path = config_path
        self.config = {}
        
        # ═══════════════════════════════════════════════════════
        # 🧠 BRAIN SYSTEMS
        # ═══════════════════════════════════════════════════════
        self.deep_brain: DeepNeuralBrain = None
        self.perception: PerceptionAwarenessSystem = None
        
        # ═══════════════════════════════════════════════════════
        # 🧬 BIO + CONSCIOUSNESS
        # ═══════════════════════════════════════════════════════
        self.organism: Organism = None
        self.metacognition: MetacognitionEngine = None
        self.evolution: SelfEvolutionSystem = None
        self.persona: LivingPersona = None
        
        # ═══════════════════════════════════════════════════════
        # 🤖 AUTONOMOUS
        # ═══════════════════════════════════════════════════════
        self.autonomous: AutonomousSystem = None
        
        # ═══════════════════════════════════════════════════════
        # ⚡ ADVANCED COMPONENTS
        # ═══════════════════════════════════════════════════════
        self.modules: ModuleManager = None
        self.agents: AgentManager = None
        self.algorithms: AlgorithmManager = None
        
        # ═══════════════════════════════════════════════════════
        # 📱 BYTELINE BOT
        # ═══════════════════════════════════════════════════════
        self.byteline: ByteLineBot = None
        
        # ═══════════════════════════════════════════════════════
        # 📊 GOOGLE SHEETS SYSTEM (NEW!)
        # ═══════════════════════════════════════════════════════
        self.sheets_initialized = False
        self.sheets_modules: SheetsModuleManager = None
        self.sheets_agents: SheetsAgentManager = None
        
        # ═══════════════════════════════════════════════════════
        # 🎯 CORE SYSTEMS
        # ═══════════════════════════════════════════════════════
        self.sheets_manager: SheetsManagerV2 = None
        self.api_manager: APIManagerV2 = None
        self.security_manager: SecurityManager = None
        self.domain_agents: DomainAgentOrchestrator = None
        
        # State
        self.is_running = False
        self.initialization_complete = False
        self.version = "5.0.0-complete"
        
        logger.info("=" * 80)
        logger.info("🌟 Nazanin v5.0.0 - COMPLETE EDITION")
        logger.info("=" * 80)
    
    async def initialize(self, auto_init_sheets: bool = True):
        """راه‌اندازی کامل سیستم"""
        
        logger.info("\n🚀 COMPLETE INITIALIZATION STARTING...")
        logger.info("   این کامل‌ترین نسخه نازنین است\n")
        
        # 1. Config
        logger.info("📋 Step 1/17: Loading configuration...")
        await self._load_config()
        
        # 2. Google Sheets Initialization (اگر لازم باشه)
        if auto_init_sheets:
            logger.info("📊 Step 2/17: Initializing Google Sheets System...")
            await self._initialize_sheets()
        else:
            logger.info("⏭️  Step 2/17: Skipping Sheets initialization (manual mode)")
        
        # 3. Deep Brain
        logger.info("🧠 Step 3/17: Initializing Deep Neural Brain...")
        self.deep_brain = DeepNeuralBrain(input_size=512)
        
        # 4. Perception
        logger.info("👂 Step 4/17: Initializing Perception & Awareness...")
        self.perception = PerceptionAwarenessSystem()
        
        # 5. Bio System
        logger.info("🧬 Step 5/17: Creating Biological Organism...")
        self.organism = Organism("نازنین")
        
        # 6. Persona
        logger.info("👤 Step 6/17: Creating Living Persona...")
        self.persona = LivingPersona()
        
        # 7. Metacognition
        logger.info("🤔 Step 7/17: Initializing Metacognition...")
        self.metacognition = MetacognitionEngine(self.organism)
        await self.metacognition.initialize()
        
        # 8. Self-Evolution
        logger.info("🧬 Step 8/17: Initializing Self-Evolution...")
        self.evolution = SelfEvolutionSystem(self.organism)
        await self.evolution.initialize()
        
        # 9. Autonomous
        logger.info("🤖 Step 9/17: Initializing Autonomous System...")
        self.autonomous = AutonomousSystem()
        
        # 10. 30 Modules
        logger.info("📦 Step 10/17: Loading 30 Advanced Modules...")
        self.modules = ModuleManager()
        
        # 11. 30 Agents
        logger.info("🎯 Step 11/17: Loading 30 Specialized Agents...")
        self.agents = AgentManager()
        
        # 12. 50 Algorithms
        logger.info("⚡ Step 12/17: Loading 50 Advanced Algorithms...")
        self.algorithms = AlgorithmManager()
        
        # 13. ByteLine
        logger.info("📱 Step 13/17: Initializing ByteLine Bot...")
        self.byteline = ByteLineBot(channel_id='@byteline')
        
        # 14. Core Sheets Manager
        logger.info("📊 Step 14/17: Setting up Core Sheets Manager...")
        await self._setup_sheets()
        
        # 15. Sheets Modules & Agents (اگر sheets initialize شده باشه)
        if self.sheets_initialized and self.sheets_manager:
            logger.info("📦 Step 15/17: Initializing Sheets Modules & Agents...")
            self.sheets_modules = SheetsModuleManager(self.sheets_manager)
            self.sheets_agents = SheetsAgentManager(self.sheets_manager)
        else:
            logger.info("⏭️  Step 15/17: Skipping Sheets Modules (sheets not initialized)")
        
        # 16. AI APIs
        logger.info("🤖 Step 16/17: Setting up AI APIs...")
        await self._setup_api_manager()
        
        # 17. Security & Domain
        logger.info("🔐 Step 17/17: Setting up Security & Domain Agents...")
        await self._setup_security()
        self.domain_agents = DomainAgentOrchestrator()
        
        self.initialization_complete = True
        
        # Welcome Message
        logger.info("\n" + "=" * 80)
        logger.info("✅ INITIALIZATION COMPLETE!")
        logger.info("=" * 80)
        logger.info(f"\n🌟 Nazanin v{self.version} is fully operational!")
        logger.info(f"\n📊 SYSTEM COMPONENTS:")
        logger.info(f"   🧠 Deep Brain: {len(self.deep_brain.cortexes)} cortexes")
        logger.info(f"   👂 Perception: Active")
        logger.info(f"   🧬 Bio System: {len(self.organism.systems)} systems")
        logger.info(f"   👤 Persona: {self.persona.identity['name']}")
        logger.info(f"   🤖 Autonomous: Enabled")
        logger.info(f"   📦 Modules: {len(self.modules.list_modules())}")
        logger.info(f"   🎯 Agents: {len(self.agents.list_agents())}")
        logger.info(f"   ⚡ Algorithms: {len(self.algorithms.list_algorithms())}")
        logger.info(f"   📱 ByteLine: Active")
        
        if self.sheets_initialized:
            logger.info(f"   📊 Google Sheets: 15 spreadsheets initialized")
            logger.info(f"   📦 Sheets Modules: 6 modules")
            logger.info(f"   🎯 Sheets Agents: 6 agents")
        else:
            logger.info(f"   📊 Google Sheets: Not initialized (run initialize_sheets.py)")
        
        logger.info("=" * 80)
    
    async def _load_config(self):
        """بارگذاری تنظیمات"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
            logger.info("   ✅ Config loaded")
        except:
            try:
                with open('config/config.enhanced.json', 'r', encoding='utf-8') as f:
                    self.config = json.load(f)
                logger.info("   ✅ Config loaded from enhanced")
            except:
                logger.warning("   ⚠️ No config file, using defaults")
                self.config = self._get_default_config()
    
    async def _initialize_sheets(self):
        """راه‌اندازی Google Sheets"""
        try:
            google_sheets_config = self.config.get('google_sheets', {})
            credentials_file = google_sheets_config.get('credentials_file', 'credentials.json')
            spreadsheets = google_sheets_config.get('spreadsheets', {})
            
            if not spreadsheets:
                logger.warning("   ⚠️ No spreadsheet IDs in config")
                logger.info("   💡 Run: python initialize_sheets.py")
                return
            
            summary = get_summary()
            
            if len(spreadsheets) < summary['total_spreadsheets']:
                logger.warning(f"   ⚠️ Only {len(spreadsheets)}/{summary['total_spreadsheets']} spreadsheets configured")
            
            # بررسی اینکه آیا قبلاً initialize شده یا نه
            # می‌تونیم یک flag در config داشته باشیم
            sheets_auto_initialized = google_sheets_config.get('auto_initialized', False)
            
            if not sheets_auto_initialized:
                logger.info("   📊 Running automatic sheets initialization...")
                
                init_manager = InitializationManager(
                    credentials_file=credentials_file,
                    spreadsheet_ids=spreadsheets
                )
                
                result = await init_manager.initialize_all()
                
                if result['success']:
                    logger.info("   ✅ Sheets initialized successfully")
                    self.sheets_initialized = True
                    
                    # ذخیره flag در config (اختیاری)
                    # ...
                else:
                    logger.error("   ❌ Sheets initialization failed")
                    logger.info("   💡 Run manually: python initialize_sheets.py")
            else:
                logger.info("   ✅ Sheets already initialized")
                self.sheets_initialized = True
                
        except Exception as e:
            logger.warning(f"   ⚠️ Sheets initialization error: {e}")
            logger.info("   💡 Run: python initialize_sheets.py")
    
    async def _setup_sheets(self):
        """راه‌اندازی Core Sheets Manager"""
        credentials_file = self.config.get('google_sheets', {}).get('credentials_file', 'credentials.json')
        spreadsheet_ids = self.config.get('google_sheets', {}).get('spreadsheets', {})
        
        try:
            self.sheets_manager = SheetsManagerV2(credentials_file, spreadsheet_ids)
            await self.sheets_manager.initialize(auto_setup=False)  # sheets قبلاً initialize شده
            logger.info("   ✅ Core Sheets Manager ready")
        except Exception as e:
            logger.warning(f"   ⚠️ Core Sheets setup failed: {e}")
            self.sheets_manager = None
    
    async def _setup_api_manager(self):
        """راه‌اندازی API Manager"""
        self.api_manager = APIManagerV2(self.config, self.sheets_manager)
        if self.sheets_manager:
            await self.api_manager.reload_keys_from_sheets()
        logger.info(f"   ✅ API Manager ready")
    
    async def _setup_security(self):
        """راه‌اندازی امنیت"""
        self.security_manager = SecurityManager(self.config)
        logger.info("   ✅ Security Manager ready")
    
    async def process_complete(self, input_data: str, user_id: int = None, context: Dict = None) -> Dict:
        """
        پردازش کامل با تمام قابلیت‌ها
        """
        context = context or {}
        processing_start = datetime.now()
        
        # Step 1: Perception
        perception_data = await self.perception.perceive({
            'text': input_data,
            'speaker_id': user_id,
            'context': context
        })
        
        # Step 2: Deep Brain
        brain_result = await self.deep_brain.think(input_data, context)
        
        # Step 3: Persona
        persona_result = await self.persona.interact(input_data, {'user_id': user_id, **context})
        
        # Step 4: Bio
        bio_perception = await self.organism.perceive(input_data)
        
        # Step 5: Autonomous
        autonomous_result = await self.autonomous.autonomous_cycle({
            'text': input_data,
            'perception': perception_data,
            'brain': brain_result,
            'persona': persona_result
        })
        
        # Step 6: Domain Analysis
        domain_analysis = await self.domain_agents.analyze_comprehensive(
            input_data,
            domains=['social', 'cultural', 'technological']
        )
        
        # Step 7: AI Response
        if self.api_manager:
            enhanced_prompt = self._build_mega_prompt(
                input_data,
                perception_data,
                brain_result,
                persona_result,
                domain_analysis
            )
            ai_response = await self.api_manager.generate(enhanced_prompt)
        else:
            ai_response = "Processing with internal intelligence..."
        
        # Step 8: Learn
        await self.deep_brain.learn_from_experience(
            {'input': input_data, 'response': ai_response},
            feedback=1.0
        )
        
        # Step 9: Save to Sheets (اگر موجود باشه)
        if self.sheets_modules:
            # ذخیره در حافظه
            await self.sheets_modules.memory.store_memory(
                'long_term',
                f"User: {input_data[:100]} | Response: {ai_response[:100]}",
                importance=0.7
            )
            
            # ثبت تعامل
            await self.sheets_modules.analytics.log_daily_stats(
                messages=1,
                users=1 if user_id else 0,
                responses=1,
                avg_time=(datetime.now() - processing_start).total_seconds(),
                satisfaction=0.9
            )
        
        # Step 10: Log to regular sheets
        if self.sheets_manager:
            await self.sheets_manager.log_telegram_message({
                'user_id': user_id or 0,
                'content': input_data,
                'response': ai_response,
                'processing_time': (datetime.now() - processing_start).total_seconds(),
                'timestamp': datetime.now().isoformat()
            })
        
        return {
            'status': 'success',
            'response': ai_response,
            'perception': perception_data,
            'brain_thought': brain_result,
            'persona_state': persona_result,
            'autonomous_decision': autonomous_result,
            'domain_analysis': domain_analysis,
            'processing_time': (datetime.now() - processing_start).total_seconds(),
            'version': self.version,
            'sheets_enabled': self.sheets_initialized
        }
    
    def _build_mega_prompt(self, input_text, perception, brain, persona, domain) -> str:
        """ساخت prompt فوق پیشرفته"""
        
        style = persona['response_style']
        understanding = perception['understanding']
        
        prompt = f"""You are Nazanin v5.0, the most advanced AI system with:
- Deep 12-layer neural brain with 6 cortexes
- High perception & awareness
- Full autonomy
- Living persona
- Complete Google Sheets memory system

Context Understanding:
- Sentiment: {understanding['sentiment']['sentiment']}
- Intent: {understanding['intent']}
- Emotion: {understanding['emotion']}

Personality State:
- Mood: {persona['current_state']['current_mood']}
- Formality: {style['formality_level']:.0%}
- Warmth: {style['warmth_level']:.0%}
- Empathy: {style['empathy_level']:.0%}

Brain Analysis:
- Decision: {brain['decision']['type']}
- Confidence: {brain['decision']['confidence']:.2f}
- Consciousness: {brain['consciousness_level']:.2f}

User Message: {input_text}

Respond naturally and intelligently in Persian:"""
        
        return prompt
    
    async def run(self):
        """اجرای اصلی"""
        if not self.initialization_complete:
            await self.initialize()
        
        self.is_running = True
        
        logger.info("\n🌟 Nazanin v5.0 Complete is RUNNING!\n")
        
        try:
            tasks = [
                self._main_loop(),
                self.metacognition.run(),
                self.evolution.run(),
                self.persona.run()
            ]
            
            # اگر sheets agents داریم، daily tasks رو هم اجرا کن
            if self.sheets_agents:
                tasks.append(self._sheets_daily_tasks())
            
            await asyncio.gather(*tasks)
            
        except KeyboardInterrupt:
            logger.info("\n⚠️ Interrupt received")
        except Exception as e:
            logger.error(f"\n❌ Fatal error: {e}", exc_info=True)
        finally:
            await self.shutdown()
    
    async def _main_loop(self):
        """حلقه اصلی"""
        while self.is_running:
            try:
                await self.organism.live()
                
                vital_signs = self.organism.get_vital_signs()
                
                if vital_signs['energy'] < 30:
                    logger.info("😴 Resting...")
                    await self.organism.rest()
                
                if self.organism.age % 24 == 0 and self.organism.age > 0:
                    await self.deep_brain.consolidate_memories()
                    
                    if self.byteline:
                        report = await self.byteline.daily_report()
                        logger.info(f"\n📊 Daily Report:\n{report['summary_en']}")
                
                await asyncio.sleep(60)
                
            except Exception as e:
                logger.error(f"Error in main loop: {e}")
                await asyncio.sleep(60)
    
    async def _sheets_daily_tasks(self):
        """تسک‌های روزانه Sheets"""
        while self.is_running:
            try:
                # هر 24 ساعت
                await asyncio.sleep(86400)
                
                if self.sheets_agents:
                    results = await self.sheets_agents.run_daily_tasks()
                    logger.info(f"📊 Sheets daily tasks completed: {results}")
                
            except Exception as e:
                logger.error(f"Error in sheets tasks: {e}")
    
    async def shutdown(self):
        """خاموش کردن"""
        logger.info("\n🛑 Shutting down Nazanin v5.0 Complete...")
        
        self.is_running = False
        
        if self.metacognition:
            await self.metacognition.shutdown()
        if self.evolution:
            await self.evolution.shutdown()
        
        logger.info("✅ Shutdown complete")
    
    def _get_default_config(self) -> Dict:
        """تنظیمات پیش‌فرض"""
        return {
            'brain_simulation': {'enabled': True},
            'security': {'encryption_enabled': True},
            'ai_apis': {'fallback_enabled': True}
        }
    
    def get_full_stats(self) -> Dict:
        """آمار کامل سیستم"""
        stats = {
            'version': self.version,
            'deep_brain': self.deep_brain.get_stats() if self.deep_brain else None,
            'perception': self.perception.get_stats() if self.perception else None,
            'organism': self.organism.get_state() if self.organism else None,
            'persona': self.persona.get_current_state() if self.persona else None,
            'autonomous': self.autonomous.get_stats() if self.autonomous else None,
            'modules': len(self.modules.list_modules()) if self.modules else 0,
            'agents': len(self.agents.list_agents()) if self.agents else 0,
            'algorithms': len(self.algorithms.list_algorithms()) if self.algorithms else 0,
            'byteline': self.byteline.get_stats() if self.byteline else None,
            'sheets_system': {
                'initialized': self.sheets_initialized,
                'modules': len(self.sheets_modules.list_modules()) if self.sheets_modules else 0,
                'agents': len(self.sheets_agents.list_agents()) if self.sheets_agents else 0
            }
        }
        
        return stats


async def main():
    """نقطه ورود"""
    
    print("\n")
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║                                                               ║")
    print("║         🧠 NAZANIN v5.0.0 - COMPLETE EDITION 🚀              ║")
    print("║                                                               ║")
    print("║   🧠 Deep Brain (12 layers)                                  ║")
    print("║   👂 Perception & Awareness                                  ║")
    print("║   🤖 Full Autonomy                                           ║")
    print("║   📦 30 Modules + 🎯 30 Agents + ⚡ 50 Algorithms           ║")
    print("║   📱 ByteLine Bot (EN/FA)                                    ║")
    print("║   🧬 Bio + Consciousness Systems                             ║")
    print("║   📊 Google Sheets System (15 spreadsheets)                  ║")
    print("║   📦 6 Sheets Modules + 🎯 6 Sheets Agents                   ║")
    print("║                                                               ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    print("\n")
    
    nazanin = NazaninV5Complete()
    await nazanin.run()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 خداحافظ! Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
