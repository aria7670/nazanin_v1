"""
Context Analyzer - تحلیلگر متن
تحلیل و درک متن مکالمه
"""

import logging
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


class ContextAnalyzer:
    """
    تحلیلگر متن
    
    این کلاس متن مکالمه را تحلیل و درک می‌کند
    """
    
    def __init__(self):
        self.conversation_context: Dict[str, Any] = {}
        self.topics: List[str] = []
        self.current_topic: Optional[str] = None
        self.topic_start_time: Optional[datetime] = None
        
        logger.info("🔍 Context Analyzer initialized")
    
    def analyze(self, processed_inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        تحلیل متن
        
        Args:
            processed_inputs: ورودی‌های پردازش شده
            
        Returns:
            تحلیل متن
        """
        if not processed_inputs:
            return self._empty_context()
        
        # تحلیل موضوع
        topic = self._extract_topic(processed_inputs)
        
        # تحلیل روند مکالمه
        conversation_flow = self._analyze_conversation_flow(processed_inputs)
        
        # تحلیل تعامل
        engagement = self._analyze_engagement(processed_inputs)
        
        # به‌روزرسانی متن فعلی
        self.conversation_context = {
            'current_topic': topic,
            'conversation_flow': conversation_flow,
            'engagement_level': engagement,
            'inputs_analyzed': len(processed_inputs),
            'time_span': self._calculate_time_span(processed_inputs),
            'dominant_intent': self._get_dominant_intent(processed_inputs),
            'overall_sentiment': self._get_overall_sentiment(processed_inputs)
        }
        
        return self.conversation_context
    
    def _empty_context(self) -> Dict[str, Any]:
        """متن خالی"""
        return {
            'current_topic': None,
            'conversation_flow': 'new',
            'engagement_level': 0.0,
            'inputs_analyzed': 0
        }
    
    def _extract_topic(self, inputs: List[Dict[str, Any]]) -> Optional[str]:
        """استخراج موضوع مکالمه"""
        # الگوریتم ساده: یافتن کلمات پرتکرار
        all_words = []
        for inp in inputs:
            words = inp.get('cleaned', '').lower().split()
            all_words.extend(words)
        
        # حذف کلمات رایج
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 
                     'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were',
                     'i', 'you', 'he', 'she', 'it', 'we', 'they', 'what', 'how', 'why'}
        
        filtered_words = [w for w in all_words if w not in stop_words and len(w) > 3]
        
        if not filtered_words:
            return None
        
        # یافتن پرتکرارترین
        word_freq = {}
        for word in filtered_words:
            word_freq[word] = word_freq.get(word, 0) + 1
        
        if word_freq:
            topic = max(word_freq.items(), key=lambda x: x[1])[0]
            
            # به‌روزرسانی موضوع فعلی
            if topic != self.current_topic:
                self.current_topic = topic
                self.topic_start_time = datetime.now()
                if topic not in self.topics:
                    self.topics.append(topic)
                    logger.info(f"📌 New topic detected: {topic}")
            
            return topic
        
        return None
    
    def _analyze_conversation_flow(self, inputs: List[Dict[str, Any]]) -> str:
        """تحلیل روند مکالمه"""
        if len(inputs) == 1:
            return 'initiating'
        elif len(inputs) < 5:
            return 'developing'
        elif len(inputs) < 15:
            return 'engaged'
        else:
            return 'extended'
    
    def _analyze_engagement(self, inputs: List[Dict[str, Any]]) -> float:
        """تحلیل سطح تعامل"""
        if not inputs:
            return 0.0
        
        # معیارهای تعامل
        avg_length = sum(inp.get('word_count', 0) for inp in inputs) / len(inputs)
        has_questions = sum(1 for inp in inputs if inp.get('has_question', False))
        
        # نرمال‌سازی
        length_score = min(1.0, avg_length / 20.0)  # 20 کلمه = تعامل کامل
        question_score = min(1.0, has_questions / 3.0)  # 3 سؤال = تعامل بالا
        
        # میانگین وزن‌دار
        engagement = length_score * 0.6 + question_score * 0.4
        
        return engagement
    
    def _calculate_time_span(self, inputs: List[Dict[str, Any]]) -> float:
        """محاسبه طول زمان مکالمه (دقیقه)"""
        if len(inputs) < 2:
            return 0.0
        
        first_time = inputs[0].get('timestamp')
        last_time = inputs[-1].get('timestamp')
        
        if first_time and last_time:
            delta = last_time - first_time
            return delta.total_seconds() / 60.0
        
        return 0.0
    
    def _get_dominant_intent(self, inputs: List[Dict[str, Any]]) -> str:
        """دریافت نیت غالب"""
        intents = [inp.get('intent', 'unknown') for inp in inputs]
        
        if not intents:
            return 'unknown'
        
        # یافتن پرتکرارترین
        intent_counts = {}
        for intent in intents:
            intent_counts[intent] = intent_counts.get(intent, 0) + 1
        
        return max(intent_counts.items(), key=lambda x: x[1])[0]
    
    def _get_overall_sentiment(self, inputs: List[Dict[str, Any]]) -> str:
        """دریافت احساس کلی"""
        sentiments = [inp.get('sentiment', 'neutral') for inp in inputs]
        
        positive = sentiments.count('positive')
        negative = sentiments.count('negative')
        neutral = sentiments.count('neutral')
        
        if positive > negative and positive > neutral:
            return 'positive'
        elif negative > positive and negative > neutral:
            return 'negative'
        else:
            return 'neutral'
    
    def should_change_topic(self) -> bool:
        """بررسی اینکه آیا باید موضوع عوض شود"""
        if not self.topic_start_time:
            return False
        
        # اگر موضوع بیش از 10 دقیقه ادامه دارد
        time_on_topic = (datetime.now() - self.topic_start_time).total_seconds() / 60.0
        
        return time_on_topic > 10.0
    
    def get_context_summary(self) -> str:
        """دریافت خلاصه متن"""
        if not self.conversation_context:
            return "No active conversation context"
        
        topic = self.conversation_context.get('current_topic', 'unknown')
        flow = self.conversation_context.get('conversation_flow', 'new')
        engagement = self.conversation_context.get('engagement_level', 0.0)
        
        return f"Topic: {topic}, Flow: {flow}, Engagement: {engagement:.1%}"
