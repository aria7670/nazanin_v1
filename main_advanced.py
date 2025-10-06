"""
Nazanin Advanced - Complete Integration
نسخه پیشرفته با تمام ایجنت‌ها، الگوریتم‌ها و سیستم‌های یادگیری
"""

import asyncio
import logging
import json
import sys
from datetime import datetime
from typing import Dict, Any

# سیستم‌های اصلی
from src.core import SheetsManager, APIManager
from src.agents import AgentOrchestrator

# پلتفرم‌ها
from src.platforms import TwitterSystem, TelegramSystem

# سیستم‌های AI پیشرفته
from src.ai import BrainSimulation, QuantumAgent, NeuralAgent

# سیستم‌های جدید
from src.utils import (
    MessageClassifier, PromptBuilder,
    PersonalityAdapter, HumanizationEngine,
    AlgorithmOrchestrator,
    TemplateLibrary, PatternLibrary, ContentGenerator
)
from src.agents import SpecializedAgentOrchestrator
from src.storage import TelegramStorage, DataBackupSystem, CacheSystem

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('nazanin_advanced.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)


class NazaninAdvanced:
    """سیستم پیشرفته نازنین با تمام قابلیت‌ها"""
    
    def __init__(self, config_path: str = 'config.json'):
        self.config_path = config_path
        self.config = None
        
        # سیستم‌های اصلی
        self.sheets_manager = None
        self.api_manager = None
        self.agent_orchestrator = None
        
        # پلتفرم‌ها
        self.twitter_system = None
        self.telegram_system = None
        
        # AI پیشرفته
        self.brain_simulation = None
        self.quantum_agent = None
        self.neural_agent = None
        
        # سیستم‌های جدید
        self.message_classifier = None
        self.prompt_builder = None
        self.personality_adapter = None
        self.humanization_engine = None
        self.specialized_agents = None
        self.algorithm_orchestrator = None
        self.content_generator = None
        self.telegram_storage = None
        self.backup_system = None
        self.cache_system = None
        
        # State
        self.is_running = False
        self.tasks = []
        
    async def initialize(self):
        """مقداردهی اولیه تمام سیستم‌ها"""
        
        logger.info("=" * 100)
        logger.info("🚀 INITIALIZING NAZANIN ADVANCED - COMPLETE AI SYSTEM")
        logger.info("=" * 100)
        
        # بارگذاری تنظیمات
        with open(self.config_path, 'r') as f:
            self.config = json.load(f)
        
        logger.info("✅ Configuration loaded")
        
        # ═══════════════════════════════════════════════════════════
        # بخش 1: سیستم‌های پایه
        # ═══════════════════════════════════════════════════════════
        
        logger.info("\n📊 SECTION 1: BASE SYSTEMS")
        logger.info("─" * 100)
        
        # Google Sheets
        self.sheets_manager = SheetsManager(
            self.config['google_sheets']['credentials_file'],
            self.config['google_sheets']['master_spreadsheet_id']
        )
        await self.sheets_manager.initialize()
        
        # API Manager
        self.api_manager = APIManager()
        api_keys = await self.sheets_manager.get_api_keys()
        await self.api_manager.initialize(api_keys)
        
        # Agent Orchestrator
        self.agent_orchestrator = AgentOrchestrator(
            self.api_manager,
            self.sheets_manager
        )
        await self.agent_orchestrator.initialize()
        
        # ═══════════════════════════════════════════════════════════
        # بخش 2: سیستم‌های دسته‌بندی و پرامپت
        # ═══════════════════════════════════════════════════════════
        
        logger.info("\n📋 SECTION 2: MESSAGE CLASSIFICATION & PROMPT BUILDING")
        logger.info("─" * 100)
        
        self.message_classifier = MessageClassifier()
        self.prompt_builder = PromptBuilder(self.message_classifier)
        
        logger.info("✅ Message classification system initialized")
        logger.info("✅ Prompt building system initialized")
        
        # ═══════════════════════════════════════════════════════════
        # بخش 3: سیستم‌های یادگیری رفتاری
        # ═══════════════════════════════════════════════════════════
        
        logger.info("\n🧠 SECTION 3: BEHAVIORAL LEARNING SYSTEMS")
        logger.info("─" * 100)
        
        self.personality_adapter = PersonalityAdapter()
        self.humanization_engine = HumanizationEngine()
        
        logger.info("✅ Personality adaptation system initialized")
        logger.info("✅ Humanization engine initialized")
        
        # ═══════════════════════════════════════════════════════════
        # بخش 4: 10 ایجنت تخصصی
        # ═══════════════════════════════════════════════════════════
        
        logger.info("\n🤖 SECTION 4: 10 SPECIALIZED AGENTS")
        logger.info("─" * 100)
        
        self.specialized_agents = SpecializedAgentOrchestrator(
            self.api_manager,
            self.sheets_manager
        )
        await self.specialized_agents.initialize()
        
        # ═══════════════════════════════════════════════════════════
        # بخش 5: الگوریتم‌های پیچیده
        # ═══════════════════════════════════════════════════════════
        
        logger.info("\n🧮 SECTION 5: ADVANCED ALGORITHMS")
        logger.info("─" * 100)
        
        self.algorithm_orchestrator = AlgorithmOrchestrator()
        
        logger.info("✅ Pattern recognition algorithm initialized")
        logger.info("✅ Content optimization algorithm initialized")
        logger.info("✅ Predictive analytics algorithm initialized")
        logger.info("✅ Clustering algorithm initialized")
        logger.info("✅ Anomaly detection algorithm initialized")
        
        # ═══════════════════════════════════════════════════════════
        # بخش 6: سیستم تمپلت و الگو
        # ═══════════════════════════════════════════════════════════
        
        logger.info("\n📝 SECTION 6: TEMPLATE & PATTERN SYSTEMS")
        logger.info("─" * 100)
        
        self.content_generator = ContentGenerator()
        
        stats = self.content_generator.get_library_stats()
        logger.info(f"✅ Template library initialized: {stats['templates']['total_templates']} templates")
        logger.info(f"✅ Pattern library initialized: {stats['patterns']['total_pattern_categories']} pattern categories")
        
        # ═══════════════════════════════════════════════════════════
        # بخش 7: AI پیشرفته (مغز، کوانتوم، عصبی)
        # ═══════════════════════════════════════════════════════════
        
        logger.info("\n🧬 SECTION 7: ADVANCED AI SYSTEMS")
        logger.info("─" * 100)
        
        if self.config.get('brain_simulation', {}).get('enabled', True):
            self.brain_simulation = BrainSimulation(
                self.config['brain_simulation']
            )
            logger.info("✅ Brain simulation system initialized")
        
        if self.config.get('quantum_agent', {}).get('enabled', True):
            self.quantum_agent = QuantumAgent(
                self.config['quantum_agent']
            )
            logger.info("✅ Quantum agent system initialized")
        
        if self.config.get('neural_agent', {}).get('enabled', True):
            self.neural_agent = NeuralAgent(
                self.config['neural_agent']
            )
            logger.info("✅ Neural agent system initialized")
        
        # ═══════════════════════════════════════════════════════════
        # بخش 8: پلتفرم‌ها
        # ═══════════════════════════════════════════════════════════
        
        logger.info("\n🌐 SECTION 8: PLATFORM SYSTEMS")
        logger.info("─" * 100)
        
        if self.config.get('twitter', {}).get('api_key'):
            self.twitter_system = TwitterSystem(
                self.config['twitter'],
                self.sheets_manager,
                self.agent_orchestrator
            )
            await self.twitter_system.initialize()
        
        if self.config.get('telegram', {}).get('bot_token'):
            self.telegram_system = TelegramSystem(
                self.config['telegram'],
                self.sheets_manager,
                self.agent_orchestrator,
                self.brain_simulation
            )
            await self.telegram_system.initialize()
            
            # ═══════════════════════════════════════════════════════════
            # بخش 9: ذخیره‌سازی تلگرام
            # ═══════════════════════════════════════════════════════════
            
            logger.info("\n💾 SECTION 9: TELEGRAM STORAGE SYSTEM")
            logger.info("─" * 100)
            
            storage_channel = self.config.get('telegram', {}).get('storage_channel_id')
            
            if storage_channel:
                self.telegram_storage = TelegramStorage(
                    self.telegram_system.bot_client,
                    storage_channel
                )
                await self.telegram_storage.initialize()
                
                self.backup_system = DataBackupSystem(self.telegram_storage)
                self.cache_system = CacheSystem(self.telegram_storage)
                
                logger.info("✅ Telegram storage system initialized")
                logger.info("✅ Backup system initialized")
                logger.info("✅ Cache system initialized")
        
        self.is_running = True
        
        logger.info("\n" + "=" * 100)
        logger.info("✅ ALL SYSTEMS INITIALIZED SUCCESSFULLY!")
        logger.info("=" * 100)
        
        # نمایش خلاصه
        await self._display_summary()
        
    async def _display_summary(self):
        """نمایش خلاصه سیستم"""
        
        logger.info("\n📊 SYSTEM SUMMARY:")
        logger.info("─" * 100)
        
        logger.info("\n✅ BASE SYSTEMS:")
        logger.info("   • Google Sheets Manager")
        logger.info("   • AI API Manager (Multi-provider)")
        logger.info("   • Agent Orchestrator")
        
        logger.info("\n✅ CLASSIFICATION & LEARNING:")
        logger.info("   • Message Classifier (10 categories)")
        logger.info("   • Prompt Builder")
        logger.info("   • Personality Adapter")
        logger.info("   • Humanization Engine")
        
        logger.info("\n✅ SPECIALIZED AGENTS (10):")
        logger.info("   1. Content Optimization Agent")
        logger.info("   2. Engagement Predictor Agent")
        logger.info("   3. Trend Analysis Agent")
        logger.info("   4. Scheduling Optimizer Agent")
        logger.info("   5. Hashtag Generator Agent")
        logger.info("   6. Sentiment Analysis Agent")
        logger.info("   7. Fact Checker Agent")
        logger.info("   8. Language Detector Agent")
        logger.info("   9. Audience Segmentation Agent")
        logger.info("   10. Competitor Monitor Agent")
        
        logger.info("\n✅ ADVANCED ALGORITHMS:")
        logger.info("   • Pattern Recognition")
        logger.info("   • Content Optimization")
        logger.info("   • Predictive Analytics")
        logger.info("   • Clustering")
        logger.info("   • Anomaly Detection")
        
        logger.info("\n✅ TEMPLATE & PATTERNS:")
        stats = self.content_generator.get_library_stats()
        logger.info(f"   • {stats['templates']['total_templates']} Templates")
        logger.info(f"   • {stats['patterns']['total_pattern_categories']} Pattern Categories")
        
        logger.info("\n✅ AI SYSTEMS:")
        if self.brain_simulation:
            logger.info("   • Brain Simulation (Emotions + Cognition + Decision)")
        if self.quantum_agent:
            logger.info("   • Quantum Agent (Superposition + Entanglement)")
        if self.neural_agent:
            logger.info("   • Neural Agent (Deep Learning + Adaptation)")
        
        logger.info("\n✅ PLATFORMS:")
        if self.twitter_system:
            logger.info("   • Twitter (Auto-threading + Smart replies)")
        if self.telegram_system:
            logger.info("   • Telegram (Persian chat + Reports)")
        
        if self.telegram_storage:
            logger.info("\n✅ STORAGE:")
            logger.info("   • Telegram Storage System")
            logger.info("   • Backup System")
            logger.info("   • Cache System")
        
        logger.info("\n" + "=" * 100)
        
    async def process_message_complete(self, user_id: str, message: str) -> Dict[str, Any]:
        """پردازش کامل یک پیام با تمام سیستم‌ها"""
        
        logger.info(f"\n{'='*80}")
        logger.info(f"🔄 PROCESSING MESSAGE FROM USER: {user_id}")
        logger.info(f"{'='*80}")
        
        result = {
            'original_message': message,
            'user_id': user_id,
            'timestamp': datetime.now().isoformat(),
            'processing_steps': []
        }
        
        # ─────────────────────────────────────────────────────────
        # مرحله 1: دسته‌بندی پیام
        # ─────────────────────────────────────────────────────────
        logger.info("\n📋 Step 1: Message Classification")
        
        classification = await self.message_classifier.classify(message)
        result['classification'] = classification
        result['processing_steps'].append('classification')
        
        logger.info(f"   Category: {classification['primary_category_name']}")
        logger.info(f"   Confidence: {classification['confidence']:.2f}")
        logger.info(f"   Priority: {classification['priority']}/10")
        
        # ─────────────────────────────────────────────────────────
        # مرحله 2: ساخت پرامپت بهینه
        # ─────────────────────────────────────────────────────────
        logger.info("\n🔧 Step 2: Building Optimized Prompt")
        
        structured_prompt = await self.prompt_builder.build_structured_prompt(
            message,
            system_role="AI assistant for Byte-Line channel"
        )
        result['prompt'] = structured_prompt
        result['processing_steps'].append('prompt_building')
        
        # ─────────────────────────────────────────────────────────
        # مرحله 3: پردازش با سیستم‌های AI پیشرفته
        # ─────────────────────────────────────────────────────────
        logger.info("\n🧠 Step 3: Advanced AI Processing")
        
        ai_results = {}
        
        # Brain Simulation
        if self.brain_simulation:
            brain_result = await self.brain_simulation.process(
                message,
                context={'classification': classification}
            )
            ai_results['brain'] = brain_result
            logger.info(f"   Brain: Emotion={brain_result['dominant_emotion']}")
        
        # Quantum Agent
        if self.quantum_agent:
            features = [float(ord(c)) / 1000.0 for c in message[:10]]
            quantum_result = await self.quantum_agent.process_quantum(features)
            ai_results['quantum'] = quantum_result
            logger.info(f"   Quantum: Entropy={quantum_result['quantum_entropy']:.4f}")
        
        # Neural Agent
        if self.neural_agent:
            neural_result = await self.neural_agent.analyze_content(message)
            ai_results['neural'] = neural_result
            logger.info(f"   Neural: Sentiment={neural_result['sentiment']['sentiment']}")
        
        result['ai_analysis'] = ai_results
        result['processing_steps'].append('ai_processing')
        
        # ─────────────────────────────────────────────────────────
        # مرحله 4: تولید پاسخ اولیه
        # ─────────────────────────────────────────────────────────
        logger.info("\n✍️ Step 4: Generating Base Response")
        
        base_response = await self.api_manager.generate(
            structured_prompt['system'] + "\n\n" + structured_prompt['user'],
            task_type='content_generation'
        )
        result['base_response'] = base_response
        result['processing_steps'].append('response_generation')
        
        # ─────────────────────────────────────────────────────────
        # مرحله 5: انسانی‌سازی پاسخ
        # ─────────────────────────────────────────────────────────
        logger.info("\n👤 Step 5: Humanizing Response")
        
        humanized = await self.humanization_engine.humanize_response(
            user_id,
            message,
            base_response
        )
        result['final_response'] = humanized['response']
        result['typing_delay'] = humanized['typing_delay']
        result['processing_steps'].append('humanization')
        
        logger.info(f"   Typing delay: {humanized['typing_delay']:.1f}s")
        
        # ─────────────────────────────────────────────────────────
        # مرحله 6: ثبت تعامل برای یادگیری
        # ─────────────────────────────────────────────────────────
        logger.info("\n📚 Step 6: Recording Interaction for Learning")
        
        interaction = {
            'user_id': user_id,
            'message': message,
            'response': humanized['response'],
            'classification': classification,
            'timestamp': datetime.now().isoformat(),
            'message_length': len(message)
        }
        
        await self.personality_adapter.record_interaction(user_id, interaction)
        result['processing_steps'].append('learning_recorded')
        
        logger.info("   ✅ Interaction recorded")
        
        # ─────────────────────────────────────────────────────────
        # مرحله 7: ذخیره‌سازی (اختیاری)
        # ─────────────────────────────────────────────────────────
        if self.telegram_storage:
            logger.info("\n💾 Step 7: Storing in Telegram")
            
            storage_key = f"interaction_{user_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            await self.telegram_storage.store_data(
                storage_key,
                result,
                metadata={'user_id': user_id, 'category': classification['primary_category']}
            )
            result['storage_ref'] = storage_key
            result['processing_steps'].append('storage')
            
            logger.info(f"   ✅ Stored: {storage_key}")
        
        logger.info(f"\n{'='*80}")
        logger.info(f"✅ MESSAGE PROCESSING COMPLETE")
        logger.info(f"   Total Steps: {len(result['processing_steps'])}")
        logger.info(f"{'='*80}\n")
        
        return result
    
    async def run(self):
        """اجرای اصلی"""
        
        try:
            await self.initialize()
            
            # شروع حلقه‌های پس‌زمینه
            # (مشابه main.py اصلی)
            
            logger.info("\n🎉 Nazanin Advanced is running!")
            logger.info("Ready to process messages with all advanced systems.\n")
            
            # نگه داشتن برنامه فعال
            while self.is_running:
                await asyncio.sleep(60)
                
        except KeyboardInterrupt:
            logger.info("\n⚠️ Received interrupt signal")
        except Exception as e:
            logger.error(f"❌ Fatal error: {e}", exc_info=True)
        finally:
            await self.shutdown()
    
    async def shutdown(self):
        """خاموش کردن سیستم"""
        
        logger.info("\n🛑 Shutting down Nazanin Advanced...")
        
        self.is_running = False
        
        # ذخیره backup نهایی
        if self.backup_system:
            backup_data = {
                'message_classifier_stats': self.message_classifier.get_statistics(),
                'personality_adapter_stats': self.personality_adapter.get_statistics(),
                'specialized_agents_performance': self.specialized_agents.get_all_performance()
            }
            await self.backup_system.auto_backup(backup_data)
        
        logger.info("✅ Nazanin Advanced shutdown complete")


async def main():
    """نقطه ورود اصلی"""
    
    nazanin = NazaninAdvanced('config.json')
    await nazanin.run()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
