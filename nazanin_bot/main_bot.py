"""
Main Bot - ربات اصلی
یکپارچه‌سازی تمام سیستم‌ها و ایجاد ربات کامل
"""

import logging
import asyncio
from typing import Dict, Any, Optional
from datetime import datetime

# Import all systems
from .brain import CognitiveCore, NeuralProcessor, ConsciousnessLayer
from .memory import ShortTermMemory, LongTermMemory, MemoryConsolidation
from .decision import AutonomousDecisionMaker, GoalManager, PlanningEngine
from .behaviors import HumanLikeBehaviors, PersonalityEngine, SocialBehaviors
from .emotions import EmotionalIntelligence, EmotionDetector, MoodManager
from .learning import AdaptiveLearning, ExperienceReplay
from .perception import InputProcessor, ContextAnalyzer
from .config import Settings
from .utils import setup_logger, TimeUtils

logger = logging.getLogger(__name__)


class NazaninBot:
    """
    Nazanin Bot - ربات پیشرفته و خودمختار
    
    این کلاس تمام سیستم‌های ربات را یکپارچه می‌کند و
    یک موجود دیجیتال با رفتارهای انسان‌گونه ایجاد می‌کند
    """
    
    def __init__(self, settings: Optional[Settings] = None):
        """
        مقداردهی اولیه ربات
        
        Args:
            settings: تنظیمات (اختیاری)
        """
        self.settings = settings or Settings()
        
        # راه‌اندازی لاگر
        self.logger = setup_logger(
            name='nazanin_bot',
            level=self.settings.log_level,
            log_file=self.settings.log_file
        )
        
        self.logger.info("=" * 60)
        self.logger.info(f"🤖 Initializing {self.settings.bot_name} Bot v{self.settings.version}")
        self.logger.info("=" * 60)
        
        # مقداردهی سیستم‌ها
        self._init_systems()
        
        # وضعیت ربات
        self.is_running = False
        self.is_sleeping = False
        self.birth_time = datetime.now()
        
        self.logger.info("✨ All systems initialized successfully")
        self.logger.info(f"🎭 Personality: {self.personality.get_personality_summary()}")
    
    def _init_systems(self):
        """مقداردهی تمام سیستم‌ها"""
        self.logger.info("🔧 Initializing subsystems...")
        
        # سیستم مغز
        self.logger.info("  🧠 Initializing Brain System...")
        self.cognitive_core = CognitiveCore()
        self.neural_processor = NeuralProcessor()
        self.consciousness = ConsciousnessLayer()
        
        # سیستم حافظه
        self.logger.info("  💾 Initializing Memory System...")
        self.short_term_memory = ShortTermMemory(
            capacity=self.settings.short_term_memory_capacity,
            retention_time=self.settings.short_term_memory_retention_time
        )
        self.long_term_memory = LongTermMemory(
            storage_path=self.settings.long_term_memory_path
        )
        self.memory_consolidation = MemoryConsolidation(
            self.short_term_memory,
            self.long_term_memory
        )
        
        # سیستم تصمیم‌گیری
        self.logger.info("  🎯 Initializing Decision System...")
        self.decision_maker = AutonomousDecisionMaker()
        self.decision_maker.set_decision_style(self.settings.default_decision_style)
        self.goal_manager = GoalManager()
        self.planning_engine = PlanningEngine()
        
        # سیستم رفتار
        self.logger.info("  👤 Initializing Behavior System...")
        self.human_behaviors = HumanLikeBehaviors()
        from .behaviors.personality import PersonalityTraits
        personality_traits = PersonalityTraits(
            openness=self.settings.personality_openness,
            conscientiousness=self.settings.personality_conscientiousness,
            extraversion=self.settings.personality_extraversion,
            agreeableness=self.settings.personality_agreeableness,
            neuroticism=self.settings.personality_neuroticism
        )
        self.personality = PersonalityEngine(traits=personality_traits)
        self.social_behaviors = SocialBehaviors()
        
        # سیستم احساسات
        self.logger.info("  ❤️ Initializing Emotion System...")
        self.emotional_intelligence = EmotionalIntelligence()
        self.emotion_detector = EmotionDetector()
        self.mood_manager = MoodManager()
        
        # سیستم یادگیری
        self.logger.info("  📚 Initializing Learning System...")
        self.adaptive_learning = AdaptiveLearning()
        self.experience_replay = ExperienceReplay(self.adaptive_learning)
        
        # سیستم ادراک
        self.logger.info("  👂 Initializing Perception System...")
        self.input_processor = InputProcessor()
        self.context_analyzer = ContextAnalyzer()
    
    async def awaken(self):
        """بیداری و شروع فعالیت ربات"""
        self.logger.info("🌅 Awakening...")
        
        # بیداری آگاهی
        await self.consciousness.awaken()
        
        # شروع هسته شناختی
        await self.cognitive_core.start()
        
        # فعال‌سازی سیستم‌ها
        self.is_running = True
        
        # پیام خوشامدگویی
        greeting = TimeUtils.get_greeting_for_time()
        self.logger.info(f"👋 {greeting}! I'm {self.settings.bot_name}, ready to assist!")
        
        # ایجاد هدف اولیه
        self.goal_manager.add_goal(
            goal_id="be_helpful",
            description="Be helpful and supportive",
            priority=self.goal_manager.GoalPriority.HIGH
        )
        
        # شروع حلقه‌های پس‌زمینه
        asyncio.create_task(self._background_processes())
    
    async def _background_processes(self):
        """فرآیندهای پس‌زمینه"""
        while self.is_running:
            try:
                # پاکسازی حافظه کوتاه‌مدت
                self.short_term_memory.cleanup_expired()
                
                # تثبیت حافظه
                if not self.is_sleeping:
                    asyncio.create_task(self.memory_consolidation.consolidate_memories())
                
                # بررسی نیاز به استراحت
                if self.human_behaviors.should_take_break():
                    await self.take_break(duration=5.0)
                
                # بررسی نیاز به خواب
                if self.settings.enable_auto_sleep and TimeUtils.should_sleep():
                    await self.sleep(duration=60.0)
                
                await asyncio.sleep(30)  # چک هر 30 ثانیه
                
            except Exception as e:
                self.logger.error(f"Error in background processes: {e}")
    
    async def process_input(self, user_input: str, user_id: str = "user") -> str:
        """
        پردازش ورودی کاربر
        
        Args:
            user_input: ورودی کاربر
            user_id: شناسه کاربر
            
        Returns:
            پاسخ ربات
        """
        self.logger.info(f"📥 Received input from {user_id}: {user_input[:50]}...")
        
        # تأخیر طبیعی
        await self.human_behaviors.natural_delay(base_delay=0.5)
        
        # پردازش ورودی
        processed = await self.input_processor.process(user_input)
        
        # پردازش شناختی
        await self.cognitive_core.process_input({
            'text': user_input,
            'processed': processed,
            'complexity': 0.5,
            'priority': processed.get('urgency', 0.5),
            'novelty': 0.5,
            'relevance': 0.7
        })
        
        # تشخیص احساس
        emotion_analysis = self.emotion_detector.comprehensive_analysis(user_input)
        detected_emotions = emotion_analysis.get('emotions', {})
        
        # همدلی
        empathetic_response = self.emotional_intelligence.empathize(detected_emotions)
        
        # تحلیل متن
        context = self.context_analyzer.analyze(
            self.input_processor.get_context_from_history()
        )
        
        # تصمیم‌گیری درباره پاسخ
        response_options = [
            {
                'action': 'answer_directly',
                'utility': 0.8,
                'feasibility': 0.9,
                'risk': 0.2,
                'goal_alignment': 0.9
            },
            {
                'action': 'ask_clarification',
                'utility': 0.6,
                'feasibility': 1.0,
                'risk': 0.1,
                'goal_alignment': 0.7
            }
        ]
        
        decision = await self.decision_maker.make_decision(
            context={'input': processed},
            options=response_options,
            urgency=processed.get('urgency', 0.5)
        )
        
        # تولید پاسخ
        response = self._generate_response(
            processed=processed,
            context=context,
            emotion_analysis=emotion_analysis,
            decision=decision,
            user_id=user_id
        )
        
        # ذخیره در حافظه
        self.short_term_memory.store(
            item_id=f"interaction_{datetime.now().timestamp()}",
            content={'input': user_input, 'response': response},
            importance=0.7
        )
        
        # به‌روزرسانی رابطه
        self.social_behaviors.update_relationship(user_id, interaction_quality=0.8)
        
        # یادگیری
        self.adaptive_learning.learn_from_experience(
            context={'type': processed.get('intent', 'unknown')},
            action=decision.action,
            outcome={'response_generated': True},
            success=True,
            reward=0.7
        )
        
        self.logger.info(f"📤 Response generated: {response[:50]}...")
        
        return response
    
    def _generate_response(self, processed: Dict[str, Any], context: Dict[str, Any],
                          emotion_analysis: Dict[str, Any], decision: Any,
                          user_id: str) -> str:
        """تولید پاسخ"""
        # دریافت سلام مناسب برای اولین تعامل
        if processed.get('intent') == 'greeting':
            return self.social_behaviors.get_greeting(user_id)
        
        # دریافت خداحافظی
        if processed.get('intent') == 'farewell':
            return self.social_behaviors.get_farewell(user_id)
        
        # پاسخ همدلانه
        empathy_response = self.emotional_intelligence.get_emotional_response(
            processed.get('cleaned', '')
        )
        
        # پاسخ اصلی
        if processed.get('has_question'):
            base_response = "I understand your question. Let me help you with that."
        else:
            base_response = "I appreciate you sharing that with me."
        
        # ترکیب پاسخ
        response = f"{empathy_response} {base_response}"
        
        # افزودن شخصیت
        response = self.human_behaviors.add_personality_flair(response)
        
        return response
    
    async def take_break(self, duration: float = 5.0):
        """استراحت کردن"""
        await self.human_behaviors.take_break(duration)
        self.mood_manager.boost_mood(amount=0.2)
    
    async def sleep(self, duration: float = 60.0):
        """خواب (تثبیت حافظه و یادگیری)"""
        self.is_sleeping = True
        self.logger.info(f"💤 Entering sleep mode for {duration}s")
        
        # تثبیت حافظه در خواب
        await self.memory_consolidation.sleep_consolidation(duration=min(duration, 30.0))
        
        # بازپخش تجربیات
        await self.experience_replay.consolidate_learning()
        
        # خواب آگاهی
        await self.consciousness.sleep()
        
        await asyncio.sleep(duration)
        
        # بیداری
        await self.consciousness.awaken()
        
        self.is_sleeping = False
        self.logger.info("🌅 Waking up refreshed!")
    
    async def shutdown(self):
        """خاموش کردن ربات"""
        self.logger.info("👋 Shutting down...")
        
        self.is_running = False
        
        # توقف سیستم‌ها
        await self.cognitive_core.stop()
        await self.consciousness.sleep()
        
        # ذخیره حافظه مهم
        await self.memory_consolidation.consolidate_memories()
        
        self.logger.info("💤 Goodbye!")
    
    def get_status(self) -> Dict[str, Any]:
        """دریافت وضعیت کامل ربات"""
        uptime = (datetime.now() - self.birth_time).total_seconds()
        
        return {
            'name': self.settings.bot_name,
            'version': self.settings.version,
            'is_running': self.is_running,
            'is_sleeping': self.is_sleeping,
            'uptime': TimeUtils.format_duration(uptime),
            'cognitive_state': self.cognitive_core.get_state().__dict__,
            'consciousness': self.consciousness.get_consciousness_state(),
            'emotional_state': self.emotional_intelligence.get_emotional_state(),
            'mood': self.mood_manager.get_state(),
            'memory': {
                'short_term': self.short_term_memory.get_stats(),
                'long_term': self.long_term_memory.get_stats()
            },
            'learning': self.adaptive_learning.get_learning_stats(),
            'decision': self.decision_maker.get_decision_stats(),
            'goals': self.goal_manager.get_stats(),
            'relationships': self.social_behaviors.get_relationship_stats(),
            'personality': self.personality.get_profile()
        }
