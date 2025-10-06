"""
Advanced Message Classification System
پیشرفته‌ترین سیستم دسته‌بندی پیام‌ها برای تولید پرامپت‌های بهینه
"""

import asyncio
import logging
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import json
import re
from collections import Counter

logger = logging.getLogger(__name__)


class MessagePattern:
    """الگوی پیام برای شناسایی"""
    
    def __init__(self, name: str, keywords: List[str], weight: float = 1.0):
        self.name = name
        self.keywords = keywords
        self.weight = weight
        self.regex_patterns = []
        
    def add_regex(self, pattern: str):
        """افزودن الگوی regex"""
        self.regex_patterns.append(re.compile(pattern, re.IGNORECASE))
    
    def match_score(self, text: str) -> float:
        """محاسبه امتیاز تطابق"""
        score = 0.0
        text_lower = text.lower()
        
        # امتیاز کلمات کلیدی
        for keyword in self.keywords:
            if keyword.lower() in text_lower:
                score += self.weight
        
        # امتیاز regex
        for pattern in self.regex_patterns:
            if pattern.search(text):
                score += self.weight * 1.5
        
        return score


class MessageClassifier:
    """سیستم دسته‌بندی پیشرفته پیام‌ها"""
    
    # دسته‌بندی‌های اصلی
    CATEGORIES = {
        'question': {
            'name': 'سوال',
            'keywords': ['?', 'چرا', 'چطور', 'کی', 'کجا', 'چی', 'why', 'how', 'when', 'where', 'what', 'who'],
            'weight': 2.0
        },
        'opinion_request': {
            'name': 'درخواست نظر',
            'keywords': ['نظرت', 'فکر میکنی', 'چی میگی', 'what do you think', 'your opinion'],
            'weight': 1.8
        },
        'technical': {
            'name': 'فنی',
            'keywords': ['API', 'code', 'bug', 'error', 'کد', 'خطا', 'technical', 'algorithm'],
            'weight': 1.5
        },
        'news': {
            'name': 'خبر',
            'keywords': ['خبر', 'اعلام', 'منتشر', 'news', 'announced', 'released', 'breaking'],
            'weight': 1.7
        },
        'analysis': {
            'name': 'تحلیل',
            'keywords': ['تحلیل', 'بررسی', 'analysis', 'review', 'breakdown', 'deep dive'],
            'weight': 1.6
        },
        'casual': {
            'name': 'غیررسمی',
            'keywords': ['سلام', 'چطوری', 'خوبی', 'hi', 'hello', 'hey', 'lol', '😂', '❤️'],
            'weight': 1.0
        },
        'complaint': {
            'name': 'شکایت',
            'keywords': ['مشکل', 'خراب', 'کار نمیکنه', 'problem', 'issue', 'broken', 'not working'],
            'weight': 1.8
        },
        'praise': {
            'name': 'تمجید',
            'keywords': ['عالی', 'خوب', 'perfect', 'great', 'amazing', 'awesome', '👏', '🔥'],
            'weight': 1.3
        },
        'request': {
            'name': 'درخواست',
            'keywords': ['میشه', 'لطفا', 'please', 'can you', 'could you', 'would you'],
            'weight': 1.7
        },
        'urgent': {
            'name': 'فوری',
            'keywords': ['فوری', 'urgent', 'asap', 'emergency', 'critical', '🚨'],
            'weight': 2.5
        }
    }
    
    def __init__(self):
        self.patterns = {}
        self.learning_data = []
        self.category_history = Counter()
        self._initialize_patterns()
        
    def _initialize_patterns(self):
        """مقداردهی اولیه الگوها"""
        for cat_id, cat_data in self.CATEGORIES.items():
            pattern = MessagePattern(
                cat_data['name'],
                cat_data['keywords'],
                cat_data['weight']
            )
            
            # افزودن regex‌های خاص
            if cat_id == 'question':
                pattern.add_regex(r'\?$')
                pattern.add_regex(r'^(why|how|what|when|where|who)\s')
            elif cat_id == 'technical':
                pattern.add_regex(r'\b[A-Z]{2,}\b')  # اختصارات
                pattern.add_regex(r'```[\s\S]*?```')  # کد
            elif cat_id == 'urgent':
                pattern.add_regex(r'!!!+')
                pattern.add_regex(r'[A-Z]{5,}')  # حروف بزرگ متوالی
            
            self.patterns[cat_id] = pattern
    
    async def classify(self, message: str, context: Optional[Dict] = None) -> Dict[str, Any]:
        """دسته‌بندی پیام"""
        
        if not message or len(message.strip()) == 0:
            return {
                'primary_category': 'unknown',
                'categories': {},
                'confidence': 0.0,
                'metadata': {}
            }
        
        # محاسبه امتیاز هر دسته
        scores = {}
        for cat_id, pattern in self.patterns.items():
            score = pattern.match_score(message)
            if score > 0:
                scores[cat_id] = score
        
        # نرمال‌سازی امتیازها
        if scores:
            max_score = max(scores.values())
            normalized_scores = {
                cat: score / max_score 
                for cat, score in scores.items()
            }
        else:
            normalized_scores = {'unknown': 1.0}
        
        # دسته اصلی
        primary = max(normalized_scores.items(), key=lambda x: x[1])
        
        # متادیتا
        metadata = {
            'length': len(message),
            'word_count': len(message.split()),
            'has_emoji': bool(re.search(r'[\U0001F600-\U0001F64F]', message)),
            'has_url': bool(re.search(r'https?://', message)),
            'has_mention': bool(re.search(r'@\w+', message)),
            'has_hashtag': bool(re.search(r'#\w+', message)),
            'language': self._detect_language(message),
            'sentiment': await self._analyze_sentiment(message),
            'timestamp': datetime.now().isoformat()
        }
        
        # ذخیره برای یادگیری
        self.category_history[primary[0]] += 1
        
        result = {
            'primary_category': primary[0],
            'primary_category_name': self.CATEGORIES.get(primary[0], {}).get('name', 'نامشخص'),
            'confidence': primary[1],
            'all_categories': normalized_scores,
            'metadata': metadata,
            'priority': self._calculate_priority(primary[0], metadata),
            'suggested_response_type': self._suggest_response_type(primary[0], metadata)
        }
        
        # یادگیری
        self.learning_data.append({
            'message': message[:100],  # خلاصه
            'classification': result,
            'context': context
        })
        
        # محدود کردن حافظه
        if len(self.learning_data) > 1000:
            self.learning_data = self.learning_data[-500:]
        
        return result
    
    def _detect_language(self, text: str) -> str:
        """تشخیص زبان"""
        # ساده: بر اساس حروف فارسی
        persian_chars = len(re.findall(r'[\u0600-\u06FF]', text))
        english_chars = len(re.findall(r'[a-zA-Z]', text))
        
        if persian_chars > english_chars:
            return 'fa'
        elif english_chars > 0:
            return 'en'
        return 'unknown'
    
    async def _analyze_sentiment(self, text: str) -> str:
        """تحلیل احساسات ساده"""
        positive_words = ['good', 'great', 'awesome', 'perfect', 'love', 'عالی', 'خوب', '😊', '❤️', '👍']
        negative_words = ['bad', 'terrible', 'awful', 'hate', 'بد', 'افتضاح', '😢', '😡', '👎']
        
        text_lower = text.lower()
        
        pos_count = sum(1 for word in positive_words if word in text_lower)
        neg_count = sum(1 for word in negative_words if word in text_lower)
        
        if pos_count > neg_count:
            return 'positive'
        elif neg_count > pos_count:
            return 'negative'
        return 'neutral'
    
    def _calculate_priority(self, category: str, metadata: Dict) -> int:
        """محاسبه اولویت (1-10)"""
        priority = 5  # پیش‌فرض
        
        # اولویت بر اساس دسته
        if category == 'urgent':
            priority = 10
        elif category == 'complaint':
            priority = 8
        elif category == 'question':
            priority = 7
        elif category == 'request':
            priority = 7
        elif category == 'technical':
            priority = 6
        elif category == 'casual':
            priority = 3
        
        # تنظیم بر اساس احساسات
        if metadata.get('sentiment') == 'negative':
            priority = min(10, priority + 1)
        
        return priority
    
    def _suggest_response_type(self, category: str, metadata: Dict) -> str:
        """پیشنهاد نوع پاسخ"""
        if category == 'question':
            return 'detailed_answer'
        elif category == 'opinion_request':
            return 'analytical_opinion'
        elif category == 'technical':
            return 'technical_explanation'
        elif category == 'complaint':
            return 'empathetic_solution'
        elif category == 'praise':
            return 'grateful_acknowledgment'
        elif category == 'casual':
            return 'friendly_chat'
        elif category == 'urgent':
            return 'immediate_action'
        elif category == 'request':
            return 'helpful_response'
        else:
            return 'general_response'
    
    async def generate_prompt_context(self, message: str, classification: Dict) -> Dict[str, Any]:
        """تولید context برای پرامپت AI"""
        
        context = {
            'message': message,
            'category': classification['primary_category_name'],
            'confidence': classification['confidence'],
            'priority': classification['priority'],
            'response_type': classification['suggested_response_type'],
            'metadata': classification['metadata'],
            'instructions': self._get_response_instructions(classification),
            'tone': self._get_tone_guidelines(classification),
            'constraints': self._get_constraints(classification),
            'examples': self._get_similar_examples(classification)
        }
        
        return context
    
    def _get_response_instructions(self, classification: Dict) -> List[str]:
        """دستورالعمل‌های پاسخ"""
        instructions = []
        
        response_type = classification['suggested_response_type']
        
        if response_type == 'detailed_answer':
            instructions = [
                "پاسخ کامل و مستدل بده",
                "از منابع معتبر استفاده کن",
                "مثال‌های کاربردی بیار",
                "ساده و قابل فهم بنویس"
            ]
        elif response_type == 'technical_explanation':
            instructions = [
                "توضیح فنی دقیق بده",
                "از اصطلاحات تخصصی استفاده کن",
                "کد نمونه بیار اگر لازم بود",
                "مراجع فنی ذکر کن"
            ]
        elif response_type == 'empathetic_solution':
            instructions = [
                "اول همدلی نشون بده",
                "مشکل رو تایید کن",
                "راه‌حل عملی ارائه بده",
                "follow up پیشنهاد بده"
            ]
        elif response_type == 'friendly_chat':
            instructions = [
                "صمیمی و دوستانه باش",
                "emoji مناسب استفاده کن",
                "کوتاه و جذاب بنویس"
            ]
        else:
            instructions = [
                "پاسخ حرفه‌ای و مفید بده",
                "محترمانه باش",
                "واضح بنویس"
            ]
        
        return instructions
    
    def _get_tone_guidelines(self, classification: Dict) -> Dict[str, str]:
        """راهنمای لحن"""
        category = classification['primary_category']
        sentiment = classification['metadata'].get('sentiment', 'neutral')
        
        tone = {
            'formality': 'professional',  # professional, casual, formal
            'emotion': 'neutral',  # warm, neutral, enthusiastic
            'style': 'informative'  # informative, conversational, technical
        }
        
        if category == 'casual':
            tone['formality'] = 'casual'
            tone['emotion'] = 'warm'
            tone['style'] = 'conversational'
        elif category == 'technical':
            tone['formality'] = 'formal'
            tone['emotion'] = 'neutral'
            tone['style'] = 'technical'
        elif category == 'praise':
            tone['emotion'] = 'warm'
        elif category == 'complaint':
            tone['emotion'] = 'empathetic'
        
        return tone
    
    def _get_constraints(self, classification: Dict) -> Dict[str, Any]:
        """محدودیت‌های پاسخ"""
        return {
            'max_length': 280 if classification['metadata'].get('platform') == 'twitter' else 2000,
            'must_include_source': classification['primary_category'] in ['technical', 'news'],
            'allow_emoji': classification['primary_category'] in ['casual', 'praise'],
            'language': classification['metadata']['language']
        }
    
    def _get_similar_examples(self, classification: Dict) -> List[Dict]:
        """مثال‌های مشابه از تاریخچه"""
        category = classification['primary_category']
        
        similar = [
            item for item in self.learning_data[-50:]  # 50 تای اخیر
            if item['classification']['primary_category'] == category
        ]
        
        return similar[:3]  # حداکثر 3 مثال
    
    async def learn_from_feedback(self, message: str, classification: Dict, 
                                  user_feedback: Dict):
        """یادگیری از بازخورد کاربر"""
        
        # اگر کاربر دسته‌بندی درست رو تایید کرد
        if user_feedback.get('correct_category'):
            correct_cat = user_feedback['correct_category']
            
            # افزایش وزن این دسته برای این نوع پیام
            if correct_cat in self.patterns:
                # استخراج کلمات کلیدی جدید از پیام
                words = message.lower().split()
                important_words = [w for w in words if len(w) > 4]
                
                # افزودن به کلمات کلیدی
                for word in important_words[:3]:  # حداکثر 3 کلمه
                    if word not in self.patterns[correct_cat].keywords:
                        self.patterns[correct_cat].keywords.append(word)
        
        # ذخیره بازخورد
        self.learning_data.append({
            'message': message[:100],
            'classification': classification,
            'feedback': user_feedback,
            'timestamp': datetime.now().isoformat()
        })
        
        logger.info(f"✅ یادگیری از بازخورد: {user_feedback.get('correct_category', 'N/A')}")
    
    def get_statistics(self) -> Dict[str, Any]:
        """آمار دسته‌بندی‌ها"""
        total = sum(self.category_history.values())
        
        return {
            'total_messages': total,
            'category_distribution': dict(self.category_history),
            'most_common': self.category_history.most_common(5),
            'learning_samples': len(self.learning_data),
            'patterns_count': len(self.patterns)
        }


class PromptBuilder:
    """سازنده پرامپت‌های بهینه برای AI"""
    
    def __init__(self, classifier: MessageClassifier):
        self.classifier = classifier
        
    async def build_prompt(self, message: str, context: Optional[Dict] = None) -> str:
        """ساخت پرامپت کامل"""
        
        # دسته‌بندی پیام
        classification = await self.classifier.classify(message, context)
        
        # تولید context
        prompt_context = await self.classifier.generate_prompt_context(
            message, 
            classification
        )
        
        # ساخت پرامپت JSON
        prompt = {
            'task': 'respond_to_message',
            'message': {
                'content': message,
                'category': classification['primary_category_name'],
                'language': classification['metadata']['language'],
                'sentiment': classification['metadata']['sentiment']
            },
            'response_requirements': {
                'type': classification['suggested_response_type'],
                'priority': classification['priority'],
                'tone': prompt_context['tone'],
                'constraints': prompt_context['constraints']
            },
            'instructions': prompt_context['instructions'],
            'context': context or {},
            'examples': prompt_context['examples']
        }
        
        # تبدیل به JSON قابل خواندن
        prompt_json = json.dumps(prompt, ensure_ascii=False, indent=2)
        
        # ساخت پرامپت نهایی
        final_prompt = f"""You are an AI assistant analyzing and responding to messages.

MESSAGE ANALYSIS:
{prompt_json}

Based on this analysis, generate an appropriate response following all instructions and constraints.
Your response should match the specified tone and type."""
        
        return final_prompt
    
    async def build_structured_prompt(self, message: str, 
                                     system_role: str = "helpful assistant",
                                     context: Optional[Dict] = None) -> Dict[str, Any]:
        """ساخت پرامپت ساختاریافته برای API‌های مختلف"""
        
        classification = await self.classifier.classify(message, context)
        prompt_context = await self.classifier.generate_prompt_context(message, classification)
        
        # System message
        system_message = f"""You are {system_role}.

Response Guidelines:
- Category: {classification['primary_category_name']}
- Type: {classification['suggested_response_type']}
- Priority: {classification['priority']}/10
- Tone: {prompt_context['tone']}

Instructions:
{chr(10).join('- ' + inst for inst in prompt_context['instructions'])}"""
        
        # User message
        user_message = f"{message}"
        
        return {
            'system': system_message,
            'user': user_message,
            'metadata': {
                'classification': classification,
                'context': prompt_context
            }
        }
