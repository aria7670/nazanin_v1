"""
Emotion Detector - تشخیص‌دهنده احساسات
تشخیص احساسات از متن و سیگنال‌های مختلف
"""

import logging
from typing import Dict, Any, List
import re

logger = logging.getLogger(__name__)


class EmotionDetector:
    """
    تشخیص‌دهنده احساسات
    
    این کلاس احساسات را از منابع مختلف تشخیص می‌دهد
    """
    
    def __init__(self):
        self.emotion_lexicon = self._build_emotion_lexicon()
        self.intensity_modifiers = self._build_intensity_modifiers()
        
        logger.info("🔍 Emotion Detector initialized")
    
    def _build_emotion_lexicon(self) -> Dict[str, List[str]]:
        """ساخت واژه‌نامه احساسات"""
        return {
            'joy': [
                'happy', 'joy', 'joyful', 'delighted', 'pleased', 'content',
                'cheerful', 'glad', 'excited', 'thrilled', 'wonderful',
                'fantastic', 'great', 'amazing', 'excellent', 'love', 'adore'
            ],
            'sadness': [
                'sad', 'unhappy', 'depressed', 'miserable', 'disappointed',
                'sorrowful', 'gloomy', 'melancholy', 'downcast', 'dejected',
                'heartbroken', 'unfortunate', 'tragic'
            ],
            'anger': [
                'angry', 'mad', 'furious', 'enraged', 'irritated', 'annoyed',
                'frustrated', 'outraged', 'infuriated', 'hostile', 'bitter'
            ],
            'fear': [
                'afraid', 'scared', 'frightened', 'terrified', 'worried',
                'anxious', 'nervous', 'concerned', 'alarmed', 'panicked',
                'fearful', 'uneasy'
            ],
            'surprise': [
                'surprised', 'shocked', 'astonished', 'amazed', 'startled',
                'stunned', 'astounded', 'unexpected', 'sudden'
            ],
            'trust': [
                'trust', 'believe', 'confident', 'reliable', 'honest',
                'sincere', 'faithful', 'loyal', 'dependable'
            ],
            'anticipation': [
                'expect', 'anticipate', 'hope', 'eager', 'looking forward',
                'await', 'ready', 'prepared'
            ]
        }
    
    def _build_intensity_modifiers(self) -> Dict[str, float]:
        """ساخت تعدیل‌کننده‌های شدت"""
        return {
            'very': 1.5,
            'extremely': 1.8,
            'really': 1.4,
            'so': 1.3,
            'quite': 1.2,
            'somewhat': 0.7,
            'slightly': 0.5,
            'a bit': 0.6,
            'not': -1.0,
            'never': -1.0,
            'no': -0.8
        }
    
    def detect_from_text(self, text: str) -> Dict[str, Any]:
        """
        تشخیص احساسات از متن
        
        Args:
            text: متن ورودی
            
        Returns:
            احساسات شناسایی شده و شدت آنها
        """
        text_lower = text.lower()
        detected_emotions = {}
        
        for emotion, keywords in self.emotion_lexicon.items():
            emotion_score = 0.0
            matches = []
            
            for keyword in keywords:
                if keyword in text_lower:
                    # یافتن موقعیت کلمه
                    matches.append(keyword)
                    
                    # بررسی تعدیل‌کننده‌های شدت
                    intensity = 1.0
                    for modifier, factor in self.intensity_modifiers.items():
                        pattern = rf'\b{modifier}\s+\w*{keyword}'
                        if re.search(pattern, text_lower):
                            intensity *= factor
                    
                    emotion_score += intensity
            
            if matches:
                # نرمال‌سازی امتیاز
                normalized_score = min(1.0, emotion_score * 0.3)
                detected_emotions[emotion] = {
                    'score': normalized_score,
                    'matches': matches
                }
        
        # تعیین احساس غالب
        dominant_emotion = None
        if detected_emotions:
            dominant_emotion = max(detected_emotions.items(), key=lambda x: x[1]['score'])[0]
        
        return {
            'emotions': detected_emotions,
            'dominant': dominant_emotion,
            'text_analyzed': text
        }
    
    def detect_from_punctuation(self, text: str) -> Dict[str, float]:
        """
        تشخیص احساسات از نشانه‌گذاری
        
        Args:
            text: متن
            
        Returns:
            احساسات بر اساس نشانه‌ها
        """
        emotions = {}
        
        # تعجب - علامت تعجب
        exclamation_count = text.count('!')
        if exclamation_count > 0:
            emotions['excitement'] = min(1.0, exclamation_count * 0.3)
        
        # سؤال - علامت سؤال
        question_count = text.count('?')
        if question_count > 0:
            emotions['curiosity'] = min(1.0, question_count * 0.3)
        
        # ... - تردید یا تأمل
        if '...' in text:
            emotions['contemplation'] = 0.6
        
        # حروف بزرگ - فریاد یا تأکید
        if text.isupper() and len(text) > 5:
            emotions['intensity'] = 0.9
        
        return emotions
    
    def detect_from_emojis(self, text: str) -> Dict[str, float]:
        """
        تشخیص احساسات از اموجی‌ها
        
        Args:
            text: متن با اموجی
            
        Returns:
            احساسات بر اساس اموجی‌ها
        """
        emoji_emotions = {
            '😊': ('joy', 0.7),
            '😃': ('joy', 0.8),
            '😄': ('joy', 0.9),
            '😁': ('joy', 0.8),
            '😍': ('love', 0.9),
            '❤️': ('love', 1.0),
            '😢': ('sadness', 0.7),
            '😭': ('sadness', 0.9),
            '😡': ('anger', 0.8),
            '😠': ('anger', 0.7),
            '😱': ('fear', 0.9),
            '😰': ('fear', 0.7),
            '😮': ('surprise', 0.7),
            '😲': ('surprise', 0.9),
            '🤔': ('contemplation', 0.6),
            '👍': ('approval', 0.7),
            '👎': ('disapproval', 0.7)
        }
        
        emotions = {}
        
        for emoji, (emotion, intensity) in emoji_emotions.items():
            if emoji in text:
                count = text.count(emoji)
                emotions[emotion] = min(1.0, intensity * count)
        
        return emotions
    
    def comprehensive_analysis(self, text: str) -> Dict[str, Any]:
        """
        تحلیل جامع احساسات
        
        Args:
            text: متن
            
        Returns:
            تحلیل کامل احساسات
        """
        # تشخیص از منابع مختلف
        text_emotions = self.detect_from_text(text)
        punctuation_emotions = self.detect_from_punctuation(text)
        emoji_emotions = self.detect_from_emojis(text)
        
        # ترکیب نتایج
        all_emotions = {}
        
        # از تشخیص متنی
        for emotion, data in text_emotions.get('emotions', {}).items():
            all_emotions[emotion] = data['score']
        
        # از نشانه‌گذاری
        for emotion, score in punctuation_emotions.items():
            all_emotions[emotion] = all_emotions.get(emotion, 0.0) + score * 0.3
        
        # از اموجی‌ها
        for emotion, score in emoji_emotions.items():
            all_emotions[emotion] = all_emotions.get(emotion, 0.0) + score * 0.4
        
        # نرمال‌سازی
        for emotion in all_emotions:
            all_emotions[emotion] = min(1.0, all_emotions[emotion])
        
        # تعیین احساس غالب
        dominant = max(all_emotions.items(), key=lambda x: x[1])[0] if all_emotions else None
        
        return {
            'emotions': all_emotions,
            'dominant': dominant,
            'analysis': {
                'text_based': text_emotions,
                'punctuation_based': punctuation_emotions,
                'emoji_based': emoji_emotions
            }
        }
