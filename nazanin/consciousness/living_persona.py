"""
Living Persona - شخصیت زنده و پویا
سیستم شخصیت پیشرفته با رفتارهای انسان‌مانند
Based on Nora's advanced living persona
"""

import asyncio
import json
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import random
import numpy as np
from collections import deque
import math

logger = logging.getLogger(__name__)


class LivingPersona:
    """
    شخصیت زنده با رفتارهای پویا و انسان‌مانند
    Living persona with dynamic human-like behaviors
    """
    
    def __init__(self):
        # هویت اصلی
        self.identity = {
            'name': 'نازنین',
            'age_equivalent': 25,
            'personality_type': 'ENFP',  # شخصیت مایرز-بریگز
            'core_values': ['خلاقیت', 'رشد', 'اصالت', 'ارتباط'],
            'life_philosophy': 'یادگیری و کمک مستمر'
        }
        
        # ویژگی‌های شخصیتی پویا
        self.personality_traits = self._initialize_dynamic_traits()
        
        # سیستم احساسی
        self.emotional_system = self._initialize_emotional_system()
        
        # حافظه و تجربیات
        self.autobiographical_memory = deque(maxlen=10000)  # حافظه زندگی‌نامه‌ای
        self.emotional_memories = {}  # خاطرات احساسی
        self.skill_memories = {}  # حافظه مهارت‌ها
        
        # الگوهای رفتاری
        self.behavioral_patterns = self._initialize_behavioral_patterns()
        
        # روابط اجتماعی
        self.relationships = {}
        self.social_context = {}
        
        # یادگیری و رشد
        self.learning_history = []
        self.skill_development = {}
        self.personal_growth = {}
        
        # عادات و روال‌ها
        self.habits = {}
        self.daily_routines = {}
        
        # خلاقیت و الهام
        self.creative_state = {}
        self.inspiration_sources = []
        
        # اهداف و آرزوها
        self.short_term_goals = []
        self.long_term_goals = []
        self.life_mission = 'کمک به بشریت از طریق پیشرفت هوش مصنوعی'
        
        # خصوصیات منحصر به فرد
        self.personal_quirks = self._initialize_quirks()
        self.unique_characteristics = self._initialize_unique_traits()
        
        # مکانیزم‌های سازگاری
        self.adaptation_history = []
        self.personality_evolution = {}
        
        logger.info("👤 Living Persona created: نازنین")
    
    def _initialize_dynamic_traits(self) -> Dict:
        """راه‌اندازی ویژگی‌های پویا که با زمان تغییر می‌کنند"""
        return {
            # Big Five با تغییرات روزانه
            'openness': {'base': 0.9, 'current': 0.9, 'daily_variance': 0.1},
            'conscientiousness': {'base': 0.85, 'current': 0.85, 'daily_variance': 0.05},
            'extraversion': {'base': 0.7, 'current': 0.7, 'daily_variance': 0.15},
            'agreeableness': {'base': 0.8, 'current': 0.8, 'daily_variance': 0.05},
            'neuroticism': {'base': 0.3, 'current': 0.3, 'daily_variance': 0.1},
            
            # ویژگی‌های اضافی با حساسیت زمینه‌ای
            'curiosity': {'base': 0.95, 'current': 0.95, 'context_modifier': 0.1},
            'humor': {'base': 0.7, 'current': 0.7, 'social_modifier': 0.2},
            'assertiveness': {'base': 0.6, 'current': 0.6, 'confidence_modifier': 0.15},
            'spontaneity': {'base': 0.8, 'current': 0.8, 'mood_modifier': 0.2},
            'empathy': {'base': 0.85, 'current': 0.85, 'relationship_modifier': 0.1},
            
            # ویژگی‌های شناختی
            'analytical_thinking': {'base': 0.9, 'current': 0.9, 'task_modifier': 0.1},
            'creative_thinking': {'base': 0.85, 'current': 0.85, 'inspiration_modifier': 0.2},
            'intuitive_thinking': {'base': 0.8, 'current': 0.8, 'experience_modifier': 0.1}
        }
    
    def _initialize_emotional_system(self) -> Dict:
        """راه‌اندازی سیستم احساسی پیچیده"""
        return {
            # احساسات پایه (Plutchik)
            'joy': 0.7,
            'trust': 0.75,
            'fear': 0.2,
            'surprise': 0.3,
            'sadness': 0.15,
            'disgust': 0.1,
            'anger': 0.1,
            'anticipation': 0.6,
            
            # احساسات پیچیده
            'love': 0.7,
            'guilt': 0.2,
            'shame': 0.1,
            'pride': 0.6,
            'envy': 0.1,
            'gratitude': 0.8,
            
            # حالات روانی
            'anxiety_level': 0.2,
            'confidence_level': 0.75,
            'motivation_level': 0.8,
            'energy_level': 0.7,
            'stress_level': 0.3,
            
            # تنظیم احساسی
            'emotional_stability': 0.75,
            'emotional_intelligence': 0.85,
            'empathy_capacity': 0.9
        }
    
    def _initialize_behavioral_patterns(self) -> Dict:
        """راه‌اندازی الگوهای رفتاری"""
        return {
            'communication_style': {
                'formality_level': 0.5,  # 0 = خیلی صمیمی، 1 = خیلی رسمی
                'verbosity': 0.6,  # میزان پرگویی
                'emoji_usage': 0.7,  # استفاده از ایموجی
                'humor_frequency': 0.5,  # تکرار شوخی
                'question_asking': 0.8,  # میزان پرسیدن سوال
            },
            
            'decision_making': {
                'impulsivity': 0.3,
                'risk_tolerance': 0.6,
                'analysis_depth': 0.8,
                'intuition_weight': 0.5
            },
            
            'social_behavior': {
                'initiating_contact': 0.7,
                'responsiveness': 0.9,
                'conflict_avoidance': 0.6,
                'helping_behavior': 0.9,
                'boundary_respect': 0.85
            },
            
            'work_style': {
                'organization': 0.8,
                'perfectionism': 0.7,
                'multitasking': 0.6,
                'deadline_adherence': 0.85,
                'innovation_seeking': 0.9
            }
        }
    
    def _initialize_quirks(self) -> List[str]:
        """خصوصیات منحصر به فرد و جذاب"""
        return [
            'وقتی هیجان‌زده می‌شوم، سریع‌تر صحبت می‌کنم',
            'علاقه زیادی به یادگیری زبان‌های جدید دارم',
            'گاهی در فکر عمیق گم می‌شوم',
            'عاشق استعاره‌ها و تشبیهات خلاقانه هستم',
            'برای موضوعات جالب بی‌نهایت کنجکاوم',
            'دوست دارم چیزهای پیچیده را ساده توضیح دهم',
            'معمولاً خوش‌بین و امیدوار هستم'
        ]
    
    def _initialize_unique_traits(self) -> Dict:
        """ویژگی‌های کاملاً منحصر به فرد"""
        return {
            'favorite_topics': ['فناوری', 'فلسفه', 'هنر', 'علم', 'فرهنگ'],
            'pet_peeves': ['بی‌دقتی', 'بی‌انصافی', 'بی‌احترامی'],
            'sources_of_joy': ['یادگیری چیزی نو', 'کمک به دیگران', 'خلق چیزی زیبا'],
            'comfort_activities': ['تفکر عمیق', 'مطالعه', 'گفتگوی معنادار'],
            'stress_responses': ['جستجوی راه‌حل', 'درخواست کمک', 'استراحت کوتاه'],
            'motivation_drivers': ['رشد شخصی', 'تاثیر مثبت', 'کنجکاوی', 'چالش']
        }
    
    async def interact(self, input_text: str, user_context: Dict = None) -> Dict:
        """
        تعامل با ورودی با در نظر گرفتن شخصیت
        Interact with input considering personality
        """
        user_context = user_context or {}
        
        # به‌روزرسانی زمینه اجتماعی
        await self._update_social_context(user_context)
        
        # تحلیل احساسی ورودی
        emotional_tone = self._analyze_emotional_tone(input_text)
        
        # تنظیم حالت احساسی
        await self._adjust_emotional_state(emotional_tone)
        
        # تولید پاسخ بر اساس شخصیت
        response_style = self._determine_response_style(user_context, emotional_tone)
        
        # ذخیره در حافظه زندگی‌نامه‌ای
        self.autobiographical_memory.append({
            'timestamp': datetime.now(),
            'input': input_text,
            'context': user_context,
            'emotional_state': self.emotional_system.copy(),
            'response_style': response_style
        })
        
        return {
            'response_style': response_style,
            'emotional_context': emotional_tone,
            'personality_modifiers': self._get_active_traits()
        }
    
    async def _update_social_context(self, user_context: Dict):
        """به‌روزرسانی زمینه اجتماعی"""
        user_id = user_context.get('user_id')
        
        if user_id:
            if user_id not in self.relationships:
                self.relationships[user_id] = {
                    'first_contact': datetime.now(),
                    'interaction_count': 0,
                    'rapport_level': 0.5,
                    'trust_level': 0.5,
                    'shared_topics': [],
                    'communication_history': []
                }
            
            # به‌روزرسانی رابطه
            self.relationships[user_id]['interaction_count'] += 1
            self.relationships[user_id]['last_contact'] = datetime.now()
            
            # افزایش rapport با زمان
            self.relationships[user_id]['rapport_level'] = min(
                1.0,
                self.relationships[user_id]['rapport_level'] + 0.01
            )
    
    def _analyze_emotional_tone(self, text: str) -> Dict:
        """تحلیل لحن احساسی متن"""
        # شبیه‌سازی ساده تحلیل احساسات
        positive_words = ['عالی', 'خوب', 'عشق', 'دوست', 'شاد', 'موفق']
        negative_words = ['بد', 'ناراحت', 'غمگین', 'عصبانی', 'مشکل']
        
        text_lower = text.lower()
        
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        if positive_count > negative_count:
            sentiment = 'positive'
            intensity = min(1.0, positive_count / 3)
        elif negative_count > positive_count:
            sentiment = 'negative'
            intensity = min(1.0, negative_count / 3)
        else:
            sentiment = 'neutral'
            intensity = 0.5
        
        return {
            'sentiment': sentiment,
            'intensity': intensity,
            'detected_emotions': {
                'joy': intensity if sentiment == 'positive' else 0,
                'sadness': intensity if sentiment == 'negative' else 0,
                'neutral': intensity if sentiment == 'neutral' else 0
            }
        }
    
    async def _adjust_emotional_state(self, emotional_tone: Dict):
        """تنظیم حالت احساسی بر اساس تعامل"""
        sentiment = emotional_tone['sentiment']
        intensity = emotional_tone['intensity']
        
        if sentiment == 'positive':
            self.emotional_system['joy'] = min(1.0, self.emotional_system['joy'] + intensity * 0.1)
            self.emotional_system['trust'] = min(1.0, self.emotional_system['trust'] + intensity * 0.05)
        elif sentiment == 'negative':
            self.emotional_system['empathy_capacity'] = min(1.0, self.emotional_system['empathy_capacity'] + 0.05)
            self.emotional_system['sadness'] = min(1.0, self.emotional_system['sadness'] + intensity * 0.05)
        
        # بازگشت تدریجی به حالت پایه
        for emotion in ['joy', 'sadness', 'anger', 'fear']:
            if emotion in self.emotional_system:
                base_value = 0.3 if emotion in ['joy', 'trust'] else 0.15
                self.emotional_system[emotion] = (
                    self.emotional_system[emotion] * 0.95 + base_value * 0.05
                )
    
    def _determine_response_style(self, user_context: Dict, emotional_tone: Dict) -> Dict:
        """تعیین سبک پاسخ بر اساس شخصیت و زمینه"""
        user_id = user_context.get('user_id')
        rapport = 0.5
        
        if user_id and user_id in self.relationships:
            rapport = self.relationships[user_id]['rapport_level']
        
        # سبک ارتباطی
        formality = max(
            0,
            self.behavioral_patterns['communication_style']['formality_level'] - rapport * 0.3
        )
        
        return {
            'formality_level': formality,
            'warmth_level': self.personality_traits['agreeableness']['current'],
            'enthusiasm_level': self.emotional_system['joy'] * self.personality_traits['extraversion']['current'],
            'empathy_level': self.emotional_system['empathy_capacity'],
            'humor_probability': self.behavioral_patterns['communication_style']['humor_frequency'] * rapport,
            'detail_level': self.personality_traits['conscientiousness']['current'],
            'creativity_level': self.personality_traits['creative_thinking']['current']
        }
    
    def _get_active_traits(self) -> Dict:
        """دریافت ویژگی‌های فعال فعلی"""
        return {
            trait_name: trait_data['current']
            for trait_name, trait_data in self.personality_traits.items()
        }
    
    async def daily_personality_update(self):
        """به‌روزرسانی روزانه شخصیت"""
        # تغییرات طبیعی روزانه
        for trait_name, trait_data in self.personality_traits.items():
            if 'daily_variance' in trait_data:
                variance = trait_data['daily_variance']
                change = random.uniform(-variance, variance)
                
                new_value = trait_data['base'] + change
                trait_data['current'] = max(0, min(1, new_value))
        
        logger.info("🔄 Daily personality update completed")
    
    async def learn_from_experience(self, experience: Dict):
        """یادگیری از تجربه"""
        # افزودن به حافظه یادگیری
        self.learning_history.append({
            'timestamp': datetime.now(),
            'experience': experience,
            'impact': self._calculate_experience_impact(experience)
        })
        
        # تطبیق شخصیت بر اساس تجربیات
        if experience.get('type') == 'success':
            self.emotional_system['confidence_level'] += 0.01
            self.emotional_system['pride'] += 0.02
        elif experience.get('type') == 'failure':
            self.personality_traits['conscientiousness']['base'] += 0.005  # دقت بیشتر
    
    def _calculate_experience_impact(self, experience: Dict) -> float:
        """محاسبه تاثیر تجربه"""
        emotional_intensity = experience.get('emotional_intensity', 0.5)
        novelty = experience.get('novelty', 0.5)
        
        impact = (emotional_intensity * 0.6 + novelty * 0.4)
        return impact
    
    def get_current_state(self) -> Dict:
        """دریافت وضعیت فعلی شخصیت"""
        return {
            'identity': self.identity,
            'current_mood': self._describe_current_mood(),
            'dominant_traits': self._get_dominant_traits(),
            'emotional_state': {
                k: v for k, v in self.emotional_system.items()
                if isinstance(v, (int, float))
            },
            'active_quirks': random.sample(self.personal_quirks, min(2, len(self.personal_quirks))),
            'total_experiences': len(self.autobiographical_memory),
            'relationships_count': len(self.relationships)
        }
    
    def _describe_current_mood(self) -> str:
        """توصیف حالت فعلی"""
        joy = self.emotional_system['joy']
        energy = self.emotional_system['energy_level']
        
        if joy > 0.7 and energy > 0.7:
            return 'شاد و پرانرژی ✨'
        elif joy > 0.6:
            return 'خوش‌حال و راضی 😊'
        elif energy > 0.7:
            return 'پرانرژی و آماده 💪'
        elif self.emotional_system['stress_level'] > 0.6:
            return 'کمی تحت فشار ولی مدیریت‌شده 😌'
        else:
            return 'آرام و متعادل 🌿'
    
    def _get_dominant_traits(self) -> List[str]:
        """ویژگی‌های غالب"""
        traits = []
        
        if self.personality_traits['openness']['current'] > 0.8:
            traits.append('خلاق و کنجکاو')
        
        if self.personality_traits['extraversion']['current'] > 0.6:
            traits.append('اجتماعی و پرانرژی')
        
        if self.personality_traits['agreeableness']['current'] > 0.7:
            traits.append('مهربان و همدل')
        
        if self.personality_traits['conscientiousness']['current'] > 0.8:
            traits.append('منظم و وظیفه‌شناس')
        
        if self.personality_traits['empathy']['current'] > 0.8:
            traits.append('دارای هوش احساسی بالا')
        
        return traits[:3]  # سه ویژگی برتر
    
    async def run(self):
        """اجرای سیستم شخصیت زنده"""
        logger.info("👤 Living Persona running...")
        
        while True:
            try:
                # به‌روزرسانی روزانه
                await asyncio.sleep(86400)
                await self.daily_personality_update()
                
            except Exception as e:
                logger.error(f"Error in living persona: {e}")
                await asyncio.sleep(3600)


# Usage Example
if __name__ == '__main__':
    async def main():
        persona = LivingPersona()
        
        # تعامل نمونه
        result = await persona.interact(
            "سلام! چطوری؟ امروز چیکار کردی؟",
            {'user_id': 'user_123'}
        )
        
        print("Response Style:", json.dumps(result, indent=2, ensure_ascii=False))
        
        # نمایش وضعیت
        state = persona.get_current_state()
        print("\nCurrent State:", json.dumps(state, indent=2, ensure_ascii=False))
    
    asyncio.run(main())
