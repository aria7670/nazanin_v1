"""
Nazanin v4.0.0 - Advanced Edition
نازنین نسخه 4.0 - نسخه پیشرفته

ترکیب کامل:
- مغز عصبی عمیق 12 لایه
- سیستم ادراک و آگاهی
- سیستم خودمختار کامل
- 30 ماژول پیشرفته
- 30 ایجنت تخصصی
- 50 الگوریتم حرفه‌ای
- ربات ByteLine (Frontend EN + Backend FA)
- Bio System (7 دستگاه بدن)
- Consciousness (فراشناخت، خودتکامل، شخصیت زنده)
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

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('nazanin_v4.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


class NazaninV4Advanced:
    """
    نازنین نسخه 4.0 - پیشرفته‌ترین نسخه
    
    قابلیت‌ها:
    ✅ مغز 12 لایه عصبی
    ✅ ادراک و آگاهی بالا
    ✅ خودمختاری کامل
    ✅ 30 ماژول + 30 ایجنت + 50 الگوریتم
    ✅ ByteLine Bot (دوزبانه)
    ✅ Bio + Consciousness Systems
    """
    
    def __init__(self, config_path: str = 'config/config.json'):
        self.config_path = config_path
        self.config = {}
        
        # ═══════════════════════════════════════════════════════
        # 🧠 BRAIN SYSTEMS
        # ═══════════════════════════════════════════════════════
        self.deep_brain: DeepNeuralBrain = None  # مغز 12 لایه
        self.perception: PerceptionAwarenessSystem = None  # ادراک و آگاهی
        
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
        # ⚡ ADVANCED COMPONENTS (30+30+50)
        # ═══════════════════════════════════════════════════════
        self.modules: ModuleManager = None  # 30 ماژول
        self.agents: AgentManager = None  # 30 ایجنت
        self.algorithms: AlgorithmManager = None  # 50 الگوریتم
        
        # ═══════════════════════════════════════════════════════
        # 📱 BYTELINE BOT
        # ═══════════════════════════════════════════════════════
        self.byteline: ByteLineBot = None
        
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
        self.version = "4.0.0-advanced"
        
        logger.info("=" * 80)
        logger.info("🌟 Nazanin v4.0.0 - ADVANCED EDITION")
        logger.info("=" * 80)
    
    async def initialize(self):
        """راه‌اندازی کامل سیستم پیشرفته"""
        
        logger.info("\n🚀 ADVANCED INITIALIZATION STARTING...")
        logger.info("   این بزرگترین و پیشرفته‌ترین نسخه نازنین است\n")
        
        # 1. Config
        logger.info("📋 Step 1/15: Loading configuration...")
        await self._load_config()
        
        # 2. Deep Brain (12 layers)
        logger.info("🧠 Step 2/15: Initializing Deep Neural Brain (12 layers)...")
        self.deep_brain = DeepNeuralBrain(input_size=512)
        
        # 3. Perception & Awareness
        logger.info("👂 Step 3/15: Initializing Perception & Awareness...")
        self.perception = PerceptionAwarenessSystem()
        
        # 4. Bio System
        logger.info("🧬 Step 4/15: Creating Biological Organism...")
        self.organism = Organism("نازنین")
        
        # 5. Living Persona
        logger.info("👤 Step 5/15: Creating Living Persona...")
        self.persona = LivingPersona()
        
        # 6. Metacognition
        logger.info("🤔 Step 6/15: Initializing Metacognition...")
        self.metacognition = MetacognitionEngine(self.organism)
        await self.metacognition.initialize()
        
        # 7. Self-Evolution
        logger.info("🧬 Step 7/15: Initializing Self-Evolution...")
        self.evolution = SelfEvolutionSystem(self.organism)
        await self.evolution.initialize()
        
        # 8. Autonomous System
        logger.info("🤖 Step 8/15: Initializing Autonomous System...")
        self.autonomous = AutonomousSystem()
        
        # 9. 30 Modules
        logger.info("📦 Step 9/15: Loading 30 Advanced Modules...")
        self.modules = ModuleManager()
        
        # 10. 30 Agents
        logger.info("🎯 Step 10/15: Loading 30 Specialized Agents...")
        self.agents = AgentManager()
        
        # 11. 50 Algorithms
        logger.info("⚡ Step 11/15: Loading 50 Advanced Algorithms...")
        self.algorithms = AlgorithmManager()
        
        # 12. ByteLine Bot
        logger.info("📱 Step 12/15: Initializing ByteLine Bot...")
        self.byteline = ByteLineBot(channel_id='@byteline')
        
        # 13. Google Sheets
        logger.info("📊 Step 13/15: Setting up Google Sheets...")
        await self._setup_sheets()
        
        # 14. AI APIs
        logger.info("🤖 Step 14/15: Setting up AI APIs...")
        await self._setup_api_manager()
        
        # 15. Security & Domain Agents
        logger.info("🔐 Step 15/15: Setting up Security & Domain Agents...")
        await self._setup_security()
        self.domain_agents = DomainAgentOrchestrator()
        
        self.initialization_complete = True
        
        # Welcome Message
        logger.info("\n" + "=" * 80)
        logger.info("✅ INITIALIZATION COMPLETE!")
        logger.info("=" * 80)
        logger.info(f"\n🌟 Nazanin v{self.version} is fully operational!")
        logger.info(f"\n📊 SYSTEM COMPONENTS:")
        logger.info(f"   🧠 Deep Brain: {len(self.deep_brain.cortexes)} cortexes, 12+ layers")
        logger.info(f"   👂 Perception: Active listening & understanding")
        logger.info(f"   🧬 Bio System: {len(self.organism.systems)} body systems")
        logger.info(f"   👤 Persona: {self.persona.identity['name']}")
        logger.info(f"   🤖 Autonomous: Fully autonomous")
        logger.info(f"   📦 Modules: {len(self.modules.list_modules())} modules")
        logger.info(f"   🎯 Agents: {len(self.agents.list_agents())} agents")
        logger.info(f"   ⚡ Algorithms: {len(self.algorithms.list_algorithms())} algorithms")
        logger.info(f"   📱 ByteLine: Frontend EN + Backend FA")
        logger.info("=" * 80)
    
    async def _load_config(self):
        """بارگذاری تنظیمات"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
            logger.info("   ✅ Config loaded")
        except:
            logger.warning("   ⚠️ No config file, using defaults")
            self.config = self._get_default_config()
    
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
    
    async def process_advanced(self, input_data: str, user_id: int = None, context: Dict = None) -> Dict:
        """
        پردازش پیشرفته - استفاده از تمام قابلیت‌ها
        """
        context = context or {}
        processing_start = datetime.now()
        
        # Step 1: Perception (شنود و درک)
        perception_data = await self.perception.perceive({
            'text': input_data,
            'speaker_id': user_id,
            'context': context
        })
        
        # Step 2: Deep Brain Thinking (فکر عمیق)
        brain_result = await self.deep_brain.think(input_data, context)
        
        # Step 3: Persona Interaction (تعامل شخصیت)
        persona_result = await self.persona.interact(input_data, {'user_id': user_id, **context})
        
        # Step 4: Biological Processing (پردازش بیولوژیکی)
        bio_perception = await self.organism.perceive(input_data)
        
        # Step 5: Autonomous Decision (تصمیم خودمختار)
        autonomous_result = await self.autonomous.autonomous_cycle({
            'text': input_data,
            'perception': perception_data,
            'brain': brain_result,
            'persona': persona_result
        })
        
        # Step 6: Domain Analysis (تحلیل حوزه‌ای)
        domain_analysis = await self.domain_agents.analyze_comprehensive(
            input_data,
            domains=['social', 'cultural', 'technological']
        )
        
        # Step 7: AI Response Generation
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
        
        # Step 8: Learn from Experience
        await self.deep_brain.learn_from_experience(
            {'input': input_data, 'response': ai_response},
            feedback=1.0
        )
        
        # Step 9: Log Everything
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
            'version': self.version
        }
    
    def _build_mega_prompt(
        self,
        input_text: str,
        perception: Dict,
        brain: Dict,
        persona: Dict,
        domain: Dict
    ) -> str:
        """ساخت prompt فوق پیشرفته"""
        
        style = persona['response_style']
        understanding = perception['understanding']
        
        prompt = f"""You are Nazanin, an advanced AI with:
- Deep 12-layer neural brain
- High perception & awareness
- Living persona
- Full autonomy

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
- Decision Type: {brain['decision']['type']}
- Confidence: {brain['decision']['confidence']:.2f}
- Consciousness: {brain['consciousness_level']:.2f}

User Message: {input_text}

Respond in Persian, naturally and intelligently:"""
        
        return prompt
    
    async def run(self):
        """اجرای اصلی"""
        if not self.initialization_complete:
            await self.initialize()
        
        self.is_running = True
        
        logger.info("\n🌟 Nazanin v4.0 Advanced is RUNNING!\n")
        
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
        """حلقه اصلی"""
        while self.is_running:
            try:
                # Life cycle
                await self.organism.live()
                
                # Check vital signs
                vital_signs = self.organism.get_vital_signs()
                
                if vital_signs['energy'] < 30:
                    logger.info("😴 Resting...")
                    await self.organism.rest()
                
                # Daily consolidation (هر 24 چرخه)
                if self.organism.age % 24 == 0 and self.organism.age > 0:
                    await self.deep_brain.consolidate_memories()
                    
                    # ByteLine daily report
                    if self.byteline:
                        report = await self.byteline.daily_report()
                        logger.info(f"\n📊 Daily Report:\n{report['summary_en']}")
                
                await asyncio.sleep(60)
                
            except Exception as e:
                logger.error(f"Error in main loop: {e}")
                await asyncio.sleep(60)
    
    async def shutdown(self):
        """خاموش کردن"""
        logger.info("\n🛑 Shutting down Nazanin v4.0 Advanced...")
        
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
        return {
            'version': self.version,
            'deep_brain': self.deep_brain.get_stats() if self.deep_brain else None,
            'perception': self.perception.get_stats() if self.perception else None,
            'organism': self.organism.get_state() if self.organism else None,
            'persona': self.persona.get_current_state() if self.persona else None,
            'autonomous': self.autonomous.get_stats() if self.autonomous else None,
            'modules': len(self.modules.list_modules()) if self.modules else 0,
            'agents': len(self.agents.list_agents()) if self.agents else 0,
            'algorithms': len(self.algorithms.list_algorithms()) if self.algorithms else 0,
            'byteline': self.byteline.get_stats() if self.byteline else None
        }


async def main():
    """نقطه ورود"""
    
    print("\n")
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║                                                               ║")
    print("║         🧠 NAZANIN v4.0.0 - ADVANCED EDITION 🚀              ║")
    print("║                                                               ║")
    print("║   🧠 Deep Brain (12 layers)                                  ║")
    print("║   👂 Perception & Awareness                                  ║")
    print("║   🤖 Full Autonomy                                           ║")
    print("║   📦 30 Modules + 🎯 30 Agents + ⚡ 50 Algorithms           ║")
    print("║   📱 ByteLine Bot (EN/FA)                                    ║")
    print("║   🧬 Bio + Consciousness Systems                             ║")
    print("║                                                               ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    print("\n")
    
    nazanin = NazaninV4Advanced()
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
