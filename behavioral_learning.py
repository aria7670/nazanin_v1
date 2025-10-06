"""
Behavioral Learning Agents
ایجنت‌های یادگیری از رفتار کاربران برای انسانی‌تر شدن
"""

import asyncio
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from collections import defaultdict, deque
import json
import numpy as np

logger = logging.getLogger(__name__)


class UserBehaviorTracker:
    """ردیابی رفتار کاربران"""
    
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.interactions = deque(maxlen=1000)  # 1000 تعامل اخیر
        self.preferences = {}
        self.patterns = {}
        self.personality_profile = {}
        
    def record_interaction(self, interaction: Dict):
        """ثبت یک تعامل"""
        interaction['timestamp'] = datetime.now().isoformat()
        self.interactions.append(interaction)
        
        # بروزرسانی الگوها
        self._update_patterns(interaction)
    
    def _update_patterns(self, interaction: Dict):
        """بروزرسانی الگوهای رفتاری"""
        
        # الگوی زمانی
        hour = datetime.now().hour
        if 'time_patterns' not in self.patterns:
            self.patterns['time_patterns'] = defaultdict(int)
        self.patterns['time_patterns'][hour] += 1
        
        # الگوی موضوعی
        if 'topic' in interaction:
            if 'topic_interests' not in self.patterns:
                self.patterns['topic_interests'] = defaultdict(int)
            self.patterns['topic_interests'][interaction['topic']] += 1
        
        # الگوی طول پیام
        if 'message_length' in interaction:
            if 'message_lengths' not in self.patterns:
                self.patterns['message_lengths'] = []
            self.patterns['message_lengths'].append(interaction['message_length'])
            
            # نگه داشتن آخرین 100 تا
            if len(self.patterns['message_lengths']) > 100:
                self.patterns['message_lengths'] = self.patterns['message_lengths'][-100:]
    
    def get_active_hours(self) -> List[int]:
        """ساعات فعالیت کاربر"""
        if 'time_patterns' not in self.patterns:
            return []
        
        time_data = self.patterns['time_patterns']
        sorted_hours = sorted(time_data.items(), key=lambda x: x[1], reverse=True)
        
        return [hour for hour, count in sorted_hours[:5]]
    
    def get_favorite_topics(self) -> List[str]:
        """موضوعات مورد علاقه"""
        if 'topic_interests' not in self.patterns:
            return []
        
        topic_data = self.patterns['topic_interests']
        sorted_topics = sorted(topic_data.items(), key=lambda x: x[1], reverse=True)
        
        return [topic for topic, count in sorted_topics[:10]]
    
    def get_preferred_message_length(self) -> str:
        """طول پیام ترجیحی کاربر"""
        if 'message_lengths' not in self.patterns or not self.patterns['message_lengths']:
            return 'medium'
        
        avg_length = np.mean(self.patterns['message_lengths'])
        
        if avg_length < 50:
            return 'short'
        elif avg_length < 200:
            return 'medium'
        else:
            return 'long'
    
    def build_profile(self) -> Dict[str, Any]:
        """ساخت پروفایل کامل کاربر"""
        return {
            'user_id': self.user_id,
            'total_interactions': len(self.interactions),
            'active_hours': self.get_active_hours(),
            'favorite_topics': self.get_favorite_topics(),
            'preferred_length': self.get_preferred_message_length(),
            'patterns': self.patterns,
            'last_interaction': self.interactions[-1] if self.interactions else None
        }


class ConversationStyleLearner:
    """یادگیری سبک مکالمه"""
    
    def __init__(self):
        self.conversation_history = deque(maxlen=500)
        self.successful_patterns = []
        self.failed_patterns = []
        
    async def learn_from_conversation(self, messages: List[Dict], 
                                      outcome: str, feedback: Optional[Dict] = None):
        """یادگیری از یک مکالمه"""
        
        conversation = {
            'messages': messages,
            'outcome': outcome,  # 'success', 'neutral', 'failure'
            'feedback': feedback,
            'timestamp': datetime.now().isoformat(),
            'features': self._extract_features(messages)
        }
        
        self.conversation_history.append(conversation)
        
        # دسته‌بندی
        if outcome == 'success':
            self.successful_patterns.append(conversation['features'])
        elif outcome == 'failure':
            self.failed_patterns.append(conversation['features'])
        
        logger.info(f"📚 یادگیری از مکالمه: {outcome}")
    
    def _extract_features(self, messages: List[Dict]) -> Dict[str, Any]:
        """استخراج ویژگی‌های مکالمه"""
        features = {
            'message_count': len(messages),
            'avg_length': np.mean([len(m.get('content', '')) for m in messages]),
            'has_emoji': any('😀' in m.get('content', '') or '😊' in m.get('content', '') for m in messages),
            'topics': list(set([m.get('topic') for m in messages if m.get('topic')])),
            'formality': self._detect_formality(messages),
            'response_time_avg': self._calc_avg_response_time(messages)
        }
        
        return features
    
    def _detect_formality(self, messages: List[Dict]) -> str:
        """تشخیص سطح رسمی بودن"""
        formal_words = ['please', 'thank you', 'kindly', 'لطفا', 'متشکرم', 'ممنون']
        casual_words = ['hey', 'cool', 'awesome', 'lol', 'سلام', 'خوبی', 'عالیه']
        
        formal_count = 0
        casual_count = 0
        
        for msg in messages:
            content = msg.get('content', '').lower()
            formal_count += sum(1 for w in formal_words if w in content)
            casual_count += sum(1 for w in casual_words if w in content)
        
        if formal_count > casual_count:
            return 'formal'
        elif casual_count > formal_count:
            return 'casual'
        return 'neutral'
    
    def _calc_avg_response_time(self, messages: List[Dict]) -> float:
        """محاسبه میانگین زمان پاسخ"""
        times = []
        
        for i in range(1, len(messages)):
            if 'timestamp' in messages[i] and 'timestamp' in messages[i-1]:
                try:
                    t1 = datetime.fromisoformat(messages[i-1]['timestamp'])
                    t2 = datetime.fromisoformat(messages[i]['timestamp'])
                    diff = (t2 - t1).total_seconds()
                    times.append(diff)
                except:
                    pass
        
        return np.mean(times) if times else 0.0
    
    def get_best_practices(self) -> Dict[str, Any]:
        """بهترین شیوه‌ها بر اساس یادگیری"""
        
        if not self.successful_patterns:
            return {}
        
        # تحلیل الگوهای موفق
        avg_message_count = np.mean([p['message_count'] for p in self.successful_patterns])
        avg_length = np.mean([p['avg_length'] for p in self.successful_patterns])
        emoji_usage = np.mean([1 if p['has_emoji'] else 0 for p in self.successful_patterns])
        
        formality_dist = defaultdict(int)
        for p in self.successful_patterns:
            formality_dist[p['formality']] += 1
        
        best_formality = max(formality_dist.items(), key=lambda x: x[1])[0] if formality_dist else 'neutral'
        
        return {
            'optimal_message_count': int(avg_message_count),
            'optimal_message_length': int(avg_length),
            'should_use_emoji': emoji_usage > 0.5,
            'preferred_formality': best_formality,
            'success_rate': len(self.successful_patterns) / len(self.conversation_history) if self.conversation_history else 0
        }


class PersonalityAdapter:
    """تطبیق شخصیت با مخاطب"""
    
    def __init__(self):
        self.user_profiles = {}  # user_id -> UserBehaviorTracker
        self.style_learner = ConversationStyleLearner()
        
    def get_or_create_profile(self, user_id: str) -> UserBehaviorTracker:
        """دریافت یا ساخت پروفایل کاربر"""
        if user_id not in self.user_profiles:
            self.user_profiles[user_id] = UserBehaviorTracker(user_id)
        return self.user_profiles[user_id]
    
    async def adapt_response(self, user_id: str, message: str, 
                            base_response: str) -> str:
        """تطبیق پاسخ با شخصیت کاربر"""
        
        profile = self.get_or_create_profile(user_id)
        
        # تحلیل ترجیحات کاربر
        preferred_length = profile.get_preferred_message_length()
        favorite_topics = profile.get_favorite_topics()
        
        # تطبیق طول
        if preferred_length == 'short' and len(base_response) > 200:
            # خلاصه کردن
            adapted_response = await self._summarize(base_response, max_length=150)
        elif preferred_length == 'long' and len(base_response) < 100:
            # توسعه
            adapted_response = await self._expand(base_response)
        else:
            adapted_response = base_response
        
        # افزودن ارجاع به موضوعات مورد علاقه (در صورت امکان)
        if favorite_topics and any(topic in message.lower() for topic in favorite_topics):
            adapted_response = self._add_personal_touch(adapted_response, favorite_topics)
        
        return adapted_response
    
    async def _summarize(self, text: str, max_length: int = 150) -> str:
        """خلاصه کردن متن"""
        if len(text) <= max_length:
            return text
        
        # خلاصه ساده: اولین جمله + آخرین جمله
        sentences = text.split('. ')
        if len(sentences) > 2:
            return f"{sentences[0]}. ... {sentences[-1]}"
        
        return text[:max_length] + "..."
    
    async def _expand(self, text: str) -> str:
        """توسعه متن"""
        # افزودن جزئیات بیشتر (ساده)
        expansions = [
            "\n\nاین موضوع بسیار جالب است.",
            "\n\nامیدوارم این پاسخ مفید باشد.",
            "\n\nاگر سوال دیگری داشتید، بپرسید."
        ]
        
        return text + expansions[0]
    
    def _add_personal_touch(self, response: str, topics: List[str]) -> str:
        """افزودن لمس شخصی"""
        topic = topics[0]
        personal_notes = [
            f"\n\n(می‌دانم که علاقه‌مند به {topic} هستید)",
            f"\n\nبا توجه به علاقه شما به {topic}...",
        ]
        
        return response + personal_notes[0]
    
    async def record_interaction(self, user_id: str, interaction: Dict):
        """ثبت تعامل"""
        profile = self.get_or_create_profile(user_id)
        profile.record_interaction(interaction)
    
    def get_statistics(self) -> Dict[str, Any]:
        """آمار کلی"""
        return {
            'total_users': len(self.user_profiles),
            'total_interactions': sum(len(p.interactions) for p in self.user_profiles.values()),
            'best_practices': self.style_learner.get_best_practices()
        }


class EmotionalIntelligence:
    """هوش احساسی"""
    
    def __init__(self):
        self.emotional_memory = deque(maxlen=200)
        self.empathy_model = self._initialize_empathy_model()
        
    def _initialize_empathy_model(self) -> Dict[str, Dict]:
        """مدل همدلی"""
        return {
            'sad': {
                'keywords': ['sad', 'depressed', 'down', 'غمگین', 'ناراحت', '😢', '😭'],
                'response_style': 'supportive',
                'phrases': [
                    "متاسفم که این حس رو داری",
                    "درک می‌کنم چقدر سخته",
                    "I'm sorry you're going through this"
                ]
            },
            'happy': {
                'keywords': ['happy', 'excited', 'great', 'خوشحال', 'عالی', '😊', '🎉'],
                'response_style': 'enthusiastic',
                'phrases': [
                    "چه خوب!",
                    "خیلی خوشحالم برات!",
                    "That's wonderful!"
                ]
            },
            'angry': {
                'keywords': ['angry', 'mad', 'frustrated', 'عصبانی', 'عصبی', '😡'],
                'response_style': 'calming',
                'phrases': [
                    "درک می‌کنم چرا ناراحتی",
                    "حق داری که احساس کنی",
                    "I understand your frustration"
                ]
            },
            'confused': {
                'keywords': ['confused', 'unclear', 'گیج', 'نمی‌فهمم', '🤔'],
                'response_style': 'clarifying',
                'phrases': [
                    "بذار واضح‌تر توضیح بدم",
                    "ببین، این طوری راحت‌تره",
                    "Let me clarify that"
                ]
            }
        }
    
    async def detect_emotion(self, message: str) -> Dict[str, Any]:
        """تشخیص احساسات"""
        detected_emotions = {}
        
        message_lower = message.lower()
        
        for emotion, model in self.empathy_model.items():
            score = sum(1 for keyword in model['keywords'] if keyword in message_lower)
            if score > 0:
                detected_emotions[emotion] = score
        
        if not detected_emotions:
            return {'emotion': 'neutral', 'confidence': 0.5}
        
        primary_emotion = max(detected_emotions.items(), key=lambda x: x[1])
        
        return {
            'emotion': primary_emotion[0],
            'confidence': min(primary_emotion[1] / 3, 1.0),
            'all_emotions': detected_emotions
        }
    
    async def generate_empathetic_response(self, message: str, 
                                          base_response: str) -> str:
        """تولید پاسخ همدلانه"""
        
        emotion_data = await self.detect_emotion(message)
        emotion = emotion_data['emotion']
        
        if emotion == 'neutral':
            return base_response
        
        # افزودن عبارت همدلانه
        empathy_phrase = np.random.choice(self.empathy_model[emotion]['phrases'])
        
        empathetic_response = f"{empathy_phrase}\n\n{base_response}"
        
        # ذخیره در حافظه احساسی
        self.emotional_memory.append({
            'message': message[:100],
            'emotion': emotion,
            'response': empathetic_response[:100],
            'timestamp': datetime.now().isoformat()
        })
        
        return empathetic_response
    
    def get_emotional_history(self) -> List[Dict]:
        """تاریخچه احساسی"""
        return list(self.emotional_memory)


class HumanizationEngine:
    """موتور انسانی‌سازی"""
    
    def __init__(self):
        self.personality_adapter = PersonalityAdapter()
        self.emotional_intelligence = EmotionalIntelligence()
        self.response_variations = self._load_variations()
        
    def _load_variations(self) -> Dict[str, List[str]]:
        """بارگذاری تنوع پاسخ‌ها"""
        return {
            'greeting': [
                "سلام!",
                "درود!",
                "هی!",
                "Hello!",
                "Hi there!",
                "سلام دوست من!"
            ],
            'acknowledgment': [
                "فهمیدم",
                "باشه",
                "متوجه شدم",
                "Got it",
                "I see",
                "درسته"
            ],
            'thinking': [
                "بذار فکر کنم...",
                "خب...",
                "جالبه...",
                "Hmm...",
                "Let me think...",
                "یه لحظه..."
            ],
            'transition': [
                "راستی،",
                "یه چیز دیگه،",
                "ضمناً،",
                "By the way,",
                "Also,",
                "در ضمن،"
            ]
        }
    
    async def humanize_response(self, user_id: str, message: str,
                               base_response: str) -> str:
        """انسانی کردن پاسخ"""
        
        # 1. تطبیق با شخصیت کاربر
        adapted = await self.personality_adapter.adapt_response(
            user_id, message, base_response
        )
        
        # 2. افزودن هوش احساسی
        empathetic = await self.emotional_intelligence.generate_empathetic_response(
            message, adapted
        )
        
        # 3. افزودن تنوع
        humanized = self._add_natural_variations(empathetic)
        
        # 4. افزودن تاخیر تایپ (برای واقعی‌تر بودن)
        typing_delay = self._calculate_typing_delay(humanized)
        
        return {
            'response': humanized,
            'typing_delay': typing_delay,
            'metadata': {
                'user_profile': self.personality_adapter.get_or_create_profile(user_id).build_profile(),
                'emotion_detected': await self.emotional_intelligence.detect_emotion(message)
            }
        }
    
    def _add_natural_variations(self, response: str) -> str:
        """افزودن تنوع طبیعی"""
        
        # گاهی افزودن "thinking" در ابتدا
        if np.random.random() < 0.2:
            thinking = np.random.choice(self.response_variations['thinking'])
            response = f"{thinking} {response}"
        
        # گاهی افزودن acknowledgment
        if np.random.random() < 0.15:
            ack = np.random.choice(self.response_variations['acknowledgment'])
            response = f"{ack}. {response}"
        
        return response
    
    def _calculate_typing_delay(self, text: str) -> float:
        """محاسبه تاخیر تایپ واقعی"""
        # شبیه‌سازی سرعت تایپ انسان (50-80 کلمه در دقیقه)
        words = len(text.split())
        wpm = np.random.uniform(50, 80)
        delay = (words / wpm) * 60
        
        # افزودن تاخیر فکر کردن
        thinking_delay = np.random.uniform(1, 3)
        
        return delay + thinking_delay
