"""
Perception & Awareness System
سیستم ادراک و آگاهی - شنود، درک و یادگیری از مکالمات روزمره

قابلیت‌ها:
- شنود و تحلیل مکالمات
- درک context و احساسات
- یادگیری الگوهای رفتاری
- آگاهی اجتماعی و فرهنگی
"""

import asyncio
import logging
import json
import re
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
from collections import deque, defaultdict
import random

logger = logging.getLogger(__name__)


class ConversationListener:
    """شنونده مکالمات - گوش دادن و ضبط"""
    
    def __init__(self):
        self.conversations = deque(maxlen=10000)
        self.patterns = defaultdict(int)
        self.topics = defaultdict(int)
        self.speakers = defaultdict(dict)
        
    async def listen(self, conversation: Dict) -> Dict:
        """گوش دادن به مکالمه"""
        
        # ذخیره مکالمه
        conv_data = {
            'timestamp': datetime.now().isoformat(),
            'speaker_id': conversation.get('speaker_id'),
            'text': conversation.get('text', ''),
            'context': conversation.get('context', {}),
            'metadata': conversation.get('metadata', {})
        }
        
        self.conversations.append(conv_data)
        
        # استخراج الگوها
        await self._extract_patterns(conv_data)
        
        # شناسایی موضوع
        await self._identify_topic(conv_data)
        
        # تحلیل گوینده
        await self._analyze_speaker(conv_data)
        
        return {
            'recorded': True,
            'patterns_found': len(self.patterns),
            'topic': await self._identify_topic(conv_data)
        }
    
    async def _extract_patterns(self, conv: Dict):
        """استخراج الگوهای گفتاری"""
        text = conv['text'].lower()
        
        # الگوهای سلام و خداحافظی
        greetings = ['سلام', 'درود', 'صبح بخیر', 'hello', 'hi', 'hey']
        farewells = ['خداحافظ', 'بای', 'goodbye', 'bye', 'see you']
        
        for g in greetings:
            if g in text:
                self.patterns[f'greeting_{g}'] += 1
        
        for f in farewells:
            if f in text:
                self.patterns[f'farewell_{f}'] += 1
        
        # الگوهای سوالی
        if '?' in text or any(q in text for q in ['چی', 'کی', 'کجا', 'چرا', 'چطور', 'what', 'when', 'where', 'why', 'how']):
            self.patterns['question'] += 1
    
    async def _identify_topic(self, conv: Dict) -> str:
        """شناسایی موضوع"""
        text = conv['text'].lower()
        
        # دسته‌بندی موضوعات
        topics_keywords = {
            'technology': ['کامپیوتر', 'گوشی', 'اینترنت', 'computer', 'phone', 'tech'],
            'health': ['سلامتی', 'دکتر', 'بیماری', 'health', 'doctor', 'medicine'],
            'food': ['غذا', 'رستوران', 'food', 'restaurant', 'eat'],
            'work': ['کار', 'شغل', 'پروژه', 'work', 'job', 'project'],
            'education': ['درس', 'مدرسه', 'دانشگاه', 'study', 'school', 'university'],
            'entertainment': ['فیلم', 'بازی', 'موسیقی', 'movie', 'game', 'music']
        }
        
        for topic, keywords in topics_keywords.items():
            if any(kw in text for kw in keywords):
                self.topics[topic] += 1
                return topic
        
        return 'general'
    
    async def _analyze_speaker(self, conv: Dict):
        """تحلیل گوینده"""
        speaker_id = conv.get('speaker_id', 'unknown')
        
        if speaker_id not in self.speakers:
            self.speakers[speaker_id] = {
                'first_seen': datetime.now().isoformat(),
                'message_count': 0,
                'topics': defaultdict(int),
                'patterns': defaultdict(int),
                'personality_traits': {}
            }
        
        self.speakers[speaker_id]['message_count'] += 1
        self.speakers[speaker_id]['last_seen'] = datetime.now().isoformat()


class ContextualUnderstanding:
    """درک زمینه‌ای - فهم context"""
    
    def __init__(self):
        self.context_history = deque(maxlen=1000)
        self.context_patterns = {}
        
    async def understand(self, text: str, previous_context: Dict = None) -> Dict:
        """درک context"""
        
        context = {
            'text': text,
            'timestamp': datetime.now().isoformat(),
            'previous': previous_context,
            'sentiment': await self._analyze_sentiment(text),
            'intent': await self._detect_intent(text),
            'entities': await self._extract_entities(text),
            'emotion': await self._detect_emotion(text),
            'formality': await self._detect_formality(text)
        }
        
        self.context_history.append(context)
        
        return context
    
    async def _analyze_sentiment(self, text: str) -> Dict:
        """تحلیل احساسات"""
        text_lower = text.lower()
        
        positive_words = ['خوب', 'عالی', 'دوست دارم', 'خوشحال', 'good', 'great', 'love', 'happy', 'excellent']
        negative_words = ['بد', 'ناراحت', 'عصبانی', 'متنفر', 'bad', 'sad', 'angry', 'hate', 'terrible']
        
        positive_score = sum(1 for word in positive_words if word in text_lower)
        negative_score = sum(1 for word in negative_words if word in text_lower)
        
        if positive_score > negative_score:
            sentiment = 'positive'
            score = min(1.0, positive_score / 5.0)
        elif negative_score > positive_score:
            sentiment = 'negative'
            score = -min(1.0, negative_score / 5.0)
        else:
            sentiment = 'neutral'
            score = 0.0
        
        return {
            'sentiment': sentiment,
            'score': score,
            'positive_words': positive_score,
            'negative_words': negative_score
        }
    
    async def _detect_intent(self, text: str) -> str:
        """تشخیص قصد"""
        text_lower = text.lower()
        
        if '?' in text or any(q in text_lower for q in ['چی', 'what', 'how', 'why', 'when']):
            return 'question'
        elif any(cmd in text_lower for cmd in ['لطفا', 'please', 'میشه', 'can you']):
            return 'request'
        elif any(greet in text_lower for q in ['سلام', 'hello', 'hi']):
            return 'greeting'
        elif any(info in text_lower for info in ['خبر', 'اطلاع', 'info', 'news']):
            return 'information_seeking'
        else:
            return 'statement'
    
    async def _extract_entities(self, text: str) -> List[Dict]:
        """استخراج موجودیت‌ها"""
        entities = []
        
        # اعداد
        numbers = re.findall(r'\d+', text)
        for num in numbers:
            entities.append({'type': 'number', 'value': num})
        
        # تاریخ‌ها
        date_patterns = ['امروز', 'فردا', 'دیروز', 'today', 'tomorrow', 'yesterday']
        for pattern in date_patterns:
            if pattern in text.lower():
                entities.append({'type': 'date', 'value': pattern})
        
        # لوکیشن‌ها
        locations = ['تهران', 'اصفهان', 'شیراز', 'tehran', 'new york', 'london']
        for loc in locations:
            if loc in text.lower():
                entities.append({'type': 'location', 'value': loc})
        
        return entities
    
    async def _detect_emotion(self, text: str) -> str:
        """تشخیص احساس"""
        text_lower = text.lower()
        
        emotions = {
            'joy': ['خوشحال', 'شاد', 'happy', 'joyful', '😊', '😄', '❤️'],
            'sadness': ['غمگین', 'ناراحت', 'sad', 'depressed', '😢', '😭'],
            'anger': ['عصبانی', 'angry', 'mad', '😠', '😡'],
            'fear': ['ترس', 'نگران', 'fear', 'worried', '😨'],
            'surprise': ['تعجب', 'surprise', 'shocked', '😮', '😲'],
            'love': ['عشق', 'دوست دارم', 'love', '❤️', '💕']
        }
        
        for emotion, keywords in emotions.items():
            if any(kw in text_lower for kw in keywords):
                return emotion
        
        return 'neutral'
    
    async def _detect_formality(self, text: str) -> float:
        """تشخیص رسمی‌بودن (0=غیررسمی, 1=رسمی)"""
        text_lower = text.lower()
        
        formal_indicators = ['سلام', 'جناب', 'خانم', 'شما', 'hello', 'sir', 'madam', 'you']
        informal_indicators = ['سلام', 'هی', 'تو', 'داداش', 'hi', 'hey', 'bro']
        
        formal_score = sum(1 for ind in formal_indicators if ind in text_lower)
        informal_score = sum(1 for ind in informal_indicators if ind in text_lower)
        
        total = formal_score + informal_score
        if total == 0:
            return 0.5
        
        return formal_score / total


class BehavioralLearner:
    """یادگیرنده رفتاری - یادگیری از رفتار مردم"""
    
    def __init__(self):
        self.behavior_patterns = defaultdict(list)
        self.response_patterns = defaultdict(list)
        self.cultural_norms = {}
        self.learned_phrases = defaultdict(int)
        
    async def learn_from_conversation(self, conversation: Dict, response: str = None):
        """یادگیری از مکالمه"""
        
        text = conversation.get('text', '')
        speaker = conversation.get('speaker_id', 'unknown')
        
        # یادگیری عبارات
        phrases = text.split('.')
        for phrase in phrases:
            phrase = phrase.strip()
            if phrase:
                self.learned_phrases[phrase] += 1
        
        # یادگیری الگوی رفتاری
        behavior = {
            'timestamp': datetime.now().isoformat(),
            'input': text,
            'response': response,
            'context': conversation.get('context', {})
        }
        self.behavior_patterns[speaker].append(behavior)
        
        # یادگیری الگوی پاسخ
        if response:
            pattern_key = text[:50]  # کلید الگو
            self.response_patterns[pattern_key].append(response)
    
    async def suggest_response(self, input_text: str, context: Dict = None) -> str:
        """پیشنهاد پاسخ بر اساس یادگیری"""
        
        # جستجوی الگوی مشابه
        pattern_key = input_text[:50]
        
        if pattern_key in self.response_patterns:
            responses = self.response_patterns[pattern_key]
            return random.choice(responses) if responses else None
        
        # اگر الگوی دقیق نداشتیم، از عبارات یادگرفته شده استفاده کن
        common_phrases = sorted(self.learned_phrases.items(), key=lambda x: x[1], reverse=True)
        if common_phrases:
            return common_phrases[0][0]
        
        return None
    
    def get_learned_behaviors(self, speaker_id: str = None) -> Dict:
        """دریافت رفتارهای یادگرفته شده"""
        if speaker_id:
            return {
                'speaker': speaker_id,
                'behaviors': self.behavior_patterns.get(speaker_id, []),
                'behavior_count': len(self.behavior_patterns.get(speaker_id, []))
            }
        else:
            return {
                'total_speakers': len(self.behavior_patterns),
                'total_behaviors': sum(len(b) for b in self.behavior_patterns.values()),
                'learned_phrases': len(self.learned_phrases),
                'response_patterns': len(self.response_patterns)
            }


class SocialAwareness:
    """آگاهی اجتماعی - درک نورم‌های اجتماعی و فرهنگی"""
    
    def __init__(self):
        self.social_norms = {}
        self.cultural_knowledge = {}
        self.etiquette_rules = []
        self.taboos = []
        
        self._load_default_norms()
    
    def _load_default_norms(self):
        """بارگذاری نورم‌های پیش‌فرض"""
        
        # نورم‌های فارسی
        self.social_norms['persian'] = {
            'greetings': ['سلام', 'درود', 'صبح بخیر', 'ظهر بخیر', 'عصر بخیر'],
            'polite_words': ['لطفا', 'متشکرم', 'ببخشید', 'خواهش می‌کنم'],
            'farewells': ['خداحافظ', 'به امید دیدار', 'خدانگهدار'],
            'formality': 'high'  # فرهنگ فارسی رسمی‌تر است
        }
        
        # نورم‌های انگلیسی
        self.social_norms['english'] = {
            'greetings': ['hello', 'hi', 'good morning', 'good afternoon'],
            'polite_words': ['please', 'thank you', 'sorry', 'excuse me'],
            'farewells': ['goodbye', 'bye', 'see you', 'take care'],
            'formality': 'medium'
        }
        
        # قوانین ادب
        self.etiquette_rules = [
            'Use polite words when making requests',
            'Greet before starting conversation',
            'Say farewell when leaving',
            'Respect personal space',
            'Listen before responding'
        ]
        
        # تابوها
        self.taboos = [
            'personal_financial_questions',
            'inappropriate_jokes',
            'religious_insults',
            'political_extremism'
        ]
    
    async def check_appropriateness(self, text: str, context: Dict = None) -> Dict:
        """بررسی مناسب‌بودن متن"""
        
        text_lower = text.lower()
        issues = []
        
        # بررسی تابوها
        for taboo in self.taboos:
            if taboo.replace('_', ' ') in text_lower:
                issues.append(f'potential_{taboo}')
        
        # بررسی ادب
        has_polite_words = any(word in text_lower for word in ['please', 'لطفا', 'thank', 'متشکر'])
        
        return {
            'appropriate': len(issues) == 0,
            'issues': issues,
            'has_polite_language': has_polite_words,
            'recommendation': 'appropriate' if len(issues) == 0 else 'needs_review'
        }
    
    async def suggest_polite_alternative(self, text: str) -> str:
        """پیشنهاد گزینه مودبانه"""
        
        # اگر فاقد کلمات مودبانه بود
        if not any(polite in text.lower() for polite in ['please', 'لطفا', 'thank', 'متشکر']):
            # اضافه کردن کلمه مودبانه
            if 'please' not in text.lower() and 'لطفا' not in text.lower():
                return f"لطفاً {text}" if any(ord(c) > 127 for c in text) else f"Please {text}"
        
        return text


class PerceptionAwarenessSystem:
    """
    سیستم کامل ادراک و آگاهی
    """
    
    def __init__(self):
        self.listener = ConversationListener()
        self.understanding = ContextualUnderstanding()
        self.learner = BehavioralLearner()
        self.social_awareness = SocialAwareness()
        
        # آمار
        self.total_conversations = 0
        self.total_learning_events = 0
        
        logger.info("👂 Perception & Awareness System initialized")
    
    async def perceive(self, input_data: Dict) -> Dict:
        """ادراک کامل - شنیدن، فهمیدن، یادگیری"""
        
        # گوش دادن
        listen_result = await self.listener.listen(input_data)
        
        # فهم context
        text = input_data.get('text', '')
        understanding = await self.understanding.understand(text, input_data.get('context'))
        
        # یادگیری
        await self.learner.learn_from_conversation(input_data)
        
        # بررسی مناسب‌بودن
        appropriateness = await self.social_awareness.check_appropriateness(text)
        
        # آمار
        self.total_conversations += 1
        self.total_learning_events += 1
        
        return {
            'perceived': True,
            'listening': listen_result,
            'understanding': understanding,
            'appropriateness': appropriateness,
            'learned': True,
            'timestamp': datetime.now().isoformat()
        }
    
    async def generate_appropriate_response(self, input_text: str, context: Dict = None) -> str:
        """تولید پاسخ مناسب"""
        
        # پیشنهاد بر اساس یادگیری
        suggested = await self.learner.suggest_response(input_text, context)
        
        if suggested:
            # بررسی مناسب‌بودن
            appropriateness = await self.social_awareness.check_appropriateness(suggested)
            
            if appropriateness['appropriate']:
                return suggested
            else:
                # پیشنهاد گزینه مودبانه
                return await self.social_awareness.suggest_polite_alternative(suggested)
        
        return None
    
    def get_stats(self) -> Dict:
        """آمار سیستم"""
        return {
            'total_conversations': self.total_conversations,
            'total_learning_events': self.total_learning_events,
            'conversations_listened': len(self.listener.conversations),
            'patterns_learned': len(self.listener.patterns),
            'topics_identified': len(self.listener.topics),
            'speakers_known': len(self.listener.speakers),
            'learned_behaviors': self.learner.get_learned_behaviors(),
            'context_history': len(self.understanding.context_history)
        }
