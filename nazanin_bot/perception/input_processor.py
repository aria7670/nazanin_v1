"""
Input Processor - پردازشگر ورودی
پردازش و تحلیل ورودی‌ها
"""

import logging
from typing import Dict, Any, List, Optional
import re
from datetime import datetime

logger = logging.getLogger(__name__)


class InputProcessor:
    """
    پردازشگر ورودی
    
    این کلاس ورودی‌ها را پردازش و تحلیل می‌کند
    """
    
    def __init__(self):
        self.input_history: List[Dict[str, Any]] = []
        
        logger.info("👂 Input Processor initialized")
    
    async def process(self, raw_input: str, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        پردازش ورودی
        
        Args:
            raw_input: ورودی خام
            metadata: متاداده
            
        Returns:
            ورودی پردازش شده
        """
        # پاکسازی
        cleaned = self._clean_input(raw_input)
        
        # تحلیل
        analysis = {
            'original': raw_input,
            'cleaned': cleaned,
            'length': len(cleaned),
            'word_count': len(cleaned.split()),
            'has_question': self._has_question(cleaned),
            'has_command': self._has_command(cleaned),
            'urgency': self._detect_urgency(cleaned),
            'sentiment': self._basic_sentiment(cleaned),
            'entities': self._extract_entities(cleaned),
            'intent': self._detect_intent(cleaned),
            'timestamp': datetime.now(),
            'metadata': metadata or {}
        }
        
        # ذخیره در تاریخچه
        self.input_history.append(analysis)
        if len(self.input_history) > 100:
            self.input_history.pop(0)
        
        logger.debug(f"Processed input: {len(cleaned)} chars, intent: {analysis['intent']}")
        
        return analysis
    
    def _clean_input(self, text: str) -> str:
        """پاکسازی ورودی"""
        # حذف فضاهای اضافی
        cleaned = re.sub(r'\s+', ' ', text)
        cleaned = cleaned.strip()
        
        return cleaned
    
    def _has_question(self, text: str) -> bool:
        """تشخیص سؤال"""
        question_words = ['what', 'why', 'how', 'when', 'where', 'who', 'which', 'can', 'could', 'would', 'should']
        text_lower = text.lower()
        
        return any(text_lower.startswith(word) for word in question_words) or '?' in text
    
    def _has_command(self, text: str) -> bool:
        """تشخیص دستور"""
        command_words = ['please', 'do', 'make', 'create', 'show', 'tell', 'give', 'help']
        text_lower = text.lower()
        
        return any(word in text_lower for word in command_words)
    
    def _detect_urgency(self, text: str) -> float:
        """تشخیص فوریت (0-1)"""
        urgency_indicators = {
            'urgent': 0.9,
            'immediately': 0.9,
            'asap': 0.9,
            'now': 0.7,
            'quickly': 0.6,
            'soon': 0.4,
            '!!!': 0.8,
            '!!': 0.6
        }
        
        text_lower = text.lower()
        max_urgency = 0.0
        
        for indicator, urgency in urgency_indicators.items():
            if indicator in text_lower:
                max_urgency = max(max_urgency, urgency)
        
        # علامت تعجب متعدد
        exclamation_count = text.count('!')
        if exclamation_count > 0:
            max_urgency = max(max_urgency, min(1.0, exclamation_count * 0.2))
        
        return max_urgency
    
    def _basic_sentiment(self, text: str) -> str:
        """تحلیل احساس ساده"""
        positive_words = ['good', 'great', 'excellent', 'amazing', 'love', 'happy', 'wonderful']
        negative_words = ['bad', 'terrible', 'awful', 'hate', 'sad', 'angry', 'disappointed']
        
        text_lower = text.lower()
        
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        if positive_count > negative_count:
            return 'positive'
        elif negative_count > positive_count:
            return 'negative'
        else:
            return 'neutral'
    
    def _extract_entities(self, text: str) -> List[Dict[str, str]]:
        """استخراج موجودیت‌ها"""
        entities = []
        
        # اعداد
        numbers = re.findall(r'\b\d+\b', text)
        for num in numbers:
            entities.append({'type': 'number', 'value': num})
        
        # ایمیل
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
        for email in emails:
            entities.append({'type': 'email', 'value': email})
        
        # URL
        urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
        for url in urls:
            entities.append({'type': 'url', 'value': url})
        
        return entities
    
    def _detect_intent(self, text: str) -> str:
        """تشخیص نیت"""
        text_lower = text.lower()
        
        intents = {
            'greeting': ['hello', 'hi', 'hey', 'greetings'],
            'farewell': ['bye', 'goodbye', 'see you', 'farewell'],
            'question': ['what', 'why', 'how', 'when', 'where'],
            'request': ['please', 'can you', 'could you', 'would you'],
            'command': ['do', 'make', 'create', 'show'],
            'thank': ['thank', 'thanks', 'appreciate'],
            'help': ['help', 'assist', 'support']
        }
        
        for intent, keywords in intents.items():
            if any(keyword in text_lower for keyword in keywords):
                return intent
        
        return 'statement'
    
    def get_context_from_history(self, lookback: int = 5) -> List[Dict[str, Any]]:
        """دریافت متن از تاریخچه"""
        return self.input_history[-lookback:] if len(self.input_history) >= lookback else self.input_history
