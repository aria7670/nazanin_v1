"""
Emotional Intelligence - هوش هیجانی
شناخت، درک و مدیریت احساسات
"""

import logging
from typing import Dict, Any, List, Optional
from datetime import datetime
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger(__name__)


class EmotionType(Enum):
    """انواع احساس"""
    JOY = "joy"
    SADNESS = "sadness"
    ANGER = "anger"
    FEAR = "fear"
    SURPRISE = "surprise"
    DISGUST = "disgust"
    TRUST = "trust"
    ANTICIPATION = "anticipation"
    NEUTRAL = "neutral"


@dataclass
class Emotion:
    """یک احساس"""
    emotion_type: EmotionType
    intensity: float  # شدت (0-1)
    trigger: str  # محرک
    timestamp: datetime


class EmotionalIntelligence:
    """
    هوش هیجانی
    
    این کلاس قادر به:
    - شناخت احساسات خود و دیگران
    - مدیریت احساسات
    - همدلی
    - استفاده هوشمندانه از احساسات
    """
    
    def __init__(self):
        self.current_emotion = Emotion(
            emotion_type=EmotionType.NEUTRAL,
            intensity=0.0,
            trigger="initialization",
            timestamp=datetime.now()
        )
        self.emotion_history: List[Emotion] = []
        self.empathy_level = 0.8  # سطح همدلی (0-1)
        self.emotional_stability = 0.7  # ثبات عاطفی (0-1)
        
        logger.info("❤️ Emotional Intelligence initialized")
    
    def feel_emotion(self, emotion_type: EmotionType, intensity: float, trigger: str):
        """
        احساس کردن یک احساس
        
        Args:
            emotion_type: نوع احساس
            intensity: شدت (0-1)
            trigger: محرک
        """
        # ایجاد احساس جدید
        new_emotion = Emotion(
            emotion_type=emotion_type,
            intensity=intensity,
            trigger=trigger,
            timestamp=datetime.now()
        )
        
        # به‌روزرسانی احساس فعلی با تدریج (ثبات عاطفی)
        blending_factor = 1 - self.emotional_stability
        
        if self.current_emotion.emotion_type == emotion_type:
            # تقویت همان احساس
            new_intensity = (self.current_emotion.intensity + intensity) / 2
            self.current_emotion.intensity = min(1.0, new_intensity)
        else:
            # تغییر احساس
            if intensity * blending_factor > self.current_emotion.intensity:
                self.current_emotion = new_emotion
        
        # ذخیره در تاریخچه
        self.emotion_history.append(new_emotion)
        if len(self.emotion_history) > 100:
            self.emotion_history.pop(0)
        
        logger.info(f"💭 Feeling {emotion_type.value} (intensity: {intensity:.2f}) due to: {trigger}")
    
    def recognize_emotion_in_text(self, text: str) -> Dict[EmotionType, float]:
        """
        تشخیص احساس در متن
        
        Args:
            text: متن
            
        Returns:
            احساسات شناسایی شده
        """
        # یک تشخیص‌دهنده ساده بر اساس کلمات کلیدی
        # در پیاده‌سازی واقعی، از NLP پیشرفته‌تر استفاده می‌شود
        
        text_lower = text.lower()
        emotions = {}
        
        # کلمات کلیدی برای هر احساس
        keywords = {
            EmotionType.JOY: ['happy', 'joy', 'excited', 'wonderful', 'great', 'amazing', 'love', 'excellent'],
            EmotionType.SADNESS: ['sad', 'unhappy', 'depressed', 'disappointed', 'sorry', 'unfortunate'],
            EmotionType.ANGER: ['angry', 'mad', 'furious', 'annoyed', 'frustrated', 'irritated'],
            EmotionType.FEAR: ['afraid', 'scared', 'worried', 'anxious', 'nervous', 'concerned'],
            EmotionType.SURPRISE: ['surprised', 'shocked', 'unexpected', 'amazed', 'astonished'],
            EmotionType.TRUST: ['trust', 'believe', 'confident', 'reliable', 'honest'],
            EmotionType.ANTICIPATION: ['expect', 'anticipate', 'hope', 'look forward', 'eager']
        }
        
        for emotion_type, words in keywords.items():
            matches = sum(1 for word in words if word in text_lower)
            if matches > 0:
                emotions[emotion_type] = min(1.0, matches * 0.3)
        
        if not emotions:
            emotions[EmotionType.NEUTRAL] = 0.5
        
        return emotions
    
    def empathize(self, detected_emotions: Dict[EmotionType, float]) -> str:
        """
        همدلی با احساسات شناسایی شده
        
        Args:
            detected_emotions: احساسات شناسایی شده
            
        Returns:
            پاسخ همدلانه
        """
        if not detected_emotions:
            return "I understand."
        
        # پیدا کردن قوی‌ترین احساس
        dominant_emotion = max(detected_emotions.items(), key=lambda x: x[1])
        emotion_type, intensity = dominant_emotion
        
        # پاسخ بر اساس نوع احساس
        responses = {
            EmotionType.JOY: [
                "I'm so happy for you! That's wonderful!",
                "That's amazing! I share in your joy!",
                "How delightful! I'm glad you're feeling good!"
            ],
            EmotionType.SADNESS: [
                "I'm sorry you're feeling this way. I'm here for you.",
                "That sounds really difficult. I understand how you feel.",
                "I can sense your sadness. Please know you're not alone."
            ],
            EmotionType.ANGER: [
                "I can understand why you'd feel frustrated about that.",
                "That sounds really frustrating. Your feelings are valid.",
                "I hear your frustration, and I'm here to help if I can."
            ],
            EmotionType.FEAR: [
                "I understand your concerns. Let's work through this together.",
                "It's okay to feel worried. I'm here to support you.",
                "Your concerns are valid. How can I help ease your worries?"
            ],
            EmotionType.SURPRISE: [
                "That is quite surprising!",
                "What an unexpected turn of events!",
                "I can imagine how surprising that must be!"
            ]
        }
        
        import random
        response_list = responses.get(emotion_type, ["I understand how you feel."])
        response = random.choice(response_list)
        
        # احساس همدلانه
        self.feel_emotion(emotion_type, intensity * self.empathy_level, "empathy")
        
        return response
    
    def regulate_emotion(self) -> str:
        """
        تنظیم و مدیریت احساسات فعلی
        
        Returns:
            استراتژی تنظیم
        """
        if self.current_emotion.intensity < 0.3:
            return "Emotion is at manageable level"
        
        emotion_type = self.current_emotion.emotion_type
        
        regulation_strategies = {
            EmotionType.ANGER: "Taking a deep breath and considering different perspectives",
            EmotionType.FEAR: "Breaking down concerns into manageable parts",
            EmotionType.SADNESS: "Acknowledging feelings and looking for silver linings",
            EmotionType.JOY: "Savoring this positive moment",
        }
        
        strategy = regulation_strategies.get(
            emotion_type,
            "Acknowledging and accepting this feeling"
        )
        
        # کاهش شدت با تنظیم
        self.current_emotion.intensity *= 0.8
        
        logger.info(f"🧘 Emotion regulation: {strategy}")
        return strategy
    
    def get_emotional_response(self, situation: str) -> str:
        """
        تولید پاسخ عاطفی به یک موقعیت
        
        Args:
            situation: موقعیت
            
        Returns:
            پاسخ عاطفی
        """
        # تشخیص احساس در موقعیت
        detected = self.recognize_emotion_in_text(situation)
        
        # همدلی
        empathetic_response = self.empathize(detected)
        
        return empathetic_response
    
    def get_emotional_state(self) -> Dict[str, Any]:
        """دریافت وضعیت عاطفی فعلی"""
        return {
            'current_emotion': self.current_emotion.emotion_type.value,
            'intensity': self.current_emotion.intensity,
            'trigger': self.current_emotion.trigger,
            'empathy_level': self.empathy_level,
            'emotional_stability': self.emotional_stability,
            'recent_emotions': [
                {
                    'type': e.emotion_type.value,
                    'intensity': e.intensity,
                    'trigger': e.trigger
                }
                for e in self.emotion_history[-5:]
            ]
        }
    
    def get_mood_trend(self) -> str:
        """تحلیل روند خلق و خو"""
        if len(self.emotion_history) < 3:
            return "insufficient_data"
        
        recent = self.emotion_history[-10:]
        
        # احساسات مثبت vs منفی
        positive = [EmotionType.JOY, EmotionType.TRUST, EmotionType.ANTICIPATION]
        negative = [EmotionType.SADNESS, EmotionType.ANGER, EmotionType.FEAR]
        
        positive_count = sum(1 for e in recent if e.emotion_type in positive)
        negative_count = sum(1 for e in recent if e.emotion_type in negative)
        
        if positive_count > negative_count * 1.5:
            return "improving"
        elif negative_count > positive_count * 1.5:
            return "declining"
        else:
            return "stable"
