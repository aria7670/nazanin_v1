"""
Mood Manager - مدیریت خلق و خو
مدیریت و تنظیم خلق و خوی کلی
"""

import logging
from typing import Dict, Any, Optional
from datetime import datetime, timedelta
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger(__name__)


class MoodState(Enum):
    """حالات خلق و خو"""
    ENERGETIC = "energetic"
    CALM = "calm"
    MELANCHOLIC = "melancholic"
    ANXIOUS = "anxious"
    CONTENT = "content"
    IRRITABLE = "irritable"
    EXCITED = "excited"
    TIRED = "tired"


@dataclass
class MoodSnapshot:
    """عکس‌برداری از خلق و خو"""
    state: MoodState
    valence: float  # مثبت/منفی (-1 تا 1)
    arousal: float  # فعالیت (0-1)
    timestamp: datetime


class MoodManager:
    """
    مدیریت خلق و خو
    
    این کلاس خلق و خوی کلی را مدیریت می‌کند که
    از احساسات لحظه‌ای متفاوت است
    """
    
    def __init__(self):
        self.current_mood = MoodSnapshot(
            state=MoodState.CALM,
            valence=0.5,
            arousal=0.5,
            timestamp=datetime.now()
        )
        self.mood_history = []
        self.baseline_valence = 0.5  # خط پایه مثبت/منفی
        self.baseline_arousal = 0.5  # خط پایه فعالیت
        
        logger.info("🌈 Mood Manager initialized")
    
    def update_mood(self, valence_change: float = 0.0, arousal_change: float = 0.0):
        """
        به‌روزرسانی خلق و خو
        
        Args:
            valence_change: تغییر در مثبت/منفی
            arousal_change: تغییر در فعالیت
        """
        # به‌روزرسانی تدریجی (خلق و خو کند تغییر می‌کند)
        self.current_mood.valence += valence_change * 0.1
        self.current_mood.arousal += arousal_change * 0.1
        
        # محدودسازی
        self.current_mood.valence = max(-1.0, min(1.0, self.current_mood.valence))
        self.current_mood.arousal = max(0.0, min(1.0, self.current_mood.arousal))
        
        # بازگشت تدریجی به خط پایه
        self.current_mood.valence += (self.baseline_valence - self.current_mood.valence) * 0.05
        self.current_mood.arousal += (self.baseline_arousal - self.current_mood.arousal) * 0.05
        
        # تعیین حالت بر اساس valence و arousal
        self.current_mood.state = self._determine_mood_state()
        self.current_mood.timestamp = datetime.now()
        
        logger.debug(f"Mood updated: {self.current_mood.state.value} "
                    f"(valence: {self.current_mood.valence:.2f}, "
                    f"arousal: {self.current_mood.arousal:.2f})")
    
    def _determine_mood_state(self) -> MoodState:
        """تعیین حالت خلق و خو بر اساس valence و arousal"""
        v = self.current_mood.valence
        a = self.current_mood.arousal
        
        # مدل circumplex احساسات
        if v > 0.3 and a > 0.6:
            return MoodState.EXCITED
        elif v > 0.3 and a < 0.4:
            return MoodState.CONTENT
        elif v > 0.0 and 0.4 <= a <= 0.6:
            return MoodState.CALM
        elif v < -0.3 and a > 0.6:
            return MoodState.ANXIOUS
        elif v < -0.3 and a < 0.4:
            return MoodState.MELANCHOLIC
        elif v < 0.0 and 0.4 <= a <= 0.6:
            return MoodState.TIRED
        elif v < 0.0 and a > 0.6:
            return MoodState.IRRITABLE
        elif a > 0.7:
            return MoodState.ENERGETIC
        else:
            return MoodState.CALM
    
    def process_emotion(self, emotion_type: str, intensity: float):
        """
        پردازش احساس و تأثیر بر خلق و خو
        
        Args:
            emotion_type: نوع احساس
            intensity: شدت
        """
        # نقشه احساسات به valence و arousal
        emotion_effects = {
            'joy': (0.8, 0.7),
            'sadness': (-0.7, 0.3),
            'anger': (-0.6, 0.9),
            'fear': (-0.8, 0.8),
            'surprise': (0.1, 0.9),
            'trust': (0.6, 0.4),
            'anticipation': (0.5, 0.7),
            'disgust': (-0.7, 0.5),
            'neutral': (0.0, 0.5)
        }
        
        if emotion_type in emotion_effects:
            valence_effect, arousal_effect = emotion_effects[emotion_type]
            
            # تأثیر بر خلق و خو
            self.update_mood(
                valence_change=valence_effect * intensity,
                arousal_change=(arousal_effect - 0.5) * intensity
            )
    
    def take_snapshot(self):
        """ثبت عکس‌برداری از خلق و خوی فعلی"""
        snapshot = MoodSnapshot(
            state=self.current_mood.state,
            valence=self.current_mood.valence,
            arousal=self.current_mood.arousal,
            timestamp=datetime.now()
        )
        
        self.mood_history.append(snapshot)
        
        # محدود کردن تاریخچه
        if len(self.mood_history) > 100:
            self.mood_history.pop(0)
    
    def get_mood_description(self) -> str:
        """دریافت توضیح خلق و خو"""
        descriptions = {
            MoodState.ENERGETIC: "I'm feeling energetic and ready to go!",
            MoodState.CALM: "I'm feeling calm and centered.",
            MoodState.MELANCHOLIC: "I'm feeling a bit melancholic.",
            MoodState.ANXIOUS: "I'm feeling somewhat anxious.",
            MoodState.CONTENT: "I'm feeling content and peaceful.",
            MoodState.IRRITABLE: "I'm feeling a bit irritable.",
            MoodState.EXCITED: "I'm feeling excited and enthusiastic!",
            MoodState.TIRED: "I'm feeling a bit tired."
        }
        
        return descriptions.get(self.current_mood.state, "I'm feeling okay.")
    
    def should_rest(self) -> bool:
        """بررسی نیاز به استراحت"""
        # اگر arousal خیلی پایین یا خلق و خو منفی
        return self.current_mood.arousal < 0.3 or self.current_mood.valence < -0.5
    
    def boost_mood(self, amount: float = 0.2):
        """تقویت خلق و خو"""
        self.update_mood(valence_change=amount, arousal_change=amount * 0.5)
        logger.info("✨ Mood boosted!")
    
    def get_mood_trend(self, hours: int = 1) -> str:
        """
        دریافت روند خلق و خو
        
        Args:
            hours: تعداد ساعت برای بررسی
            
        Returns:
            روند (improving, declining, stable)
        """
        if len(self.mood_history) < 2:
            return "insufficient_data"
        
        # بررسی روند valence
        cutoff_time = datetime.now() - timedelta(hours=hours)
        recent_moods = [m for m in self.mood_history if m.timestamp > cutoff_time]
        
        if len(recent_moods) < 2:
            return "insufficient_data"
        
        # محاسبه میانگین valence ابتدا و انتها
        first_half = recent_moods[:len(recent_moods)//2]
        second_half = recent_moods[len(recent_moods)//2:]
        
        avg_first = sum(m.valence for m in first_half) / len(first_half)
        avg_second = sum(m.valence for m in second_half) / len(second_half)
        
        diff = avg_second - avg_first
        
        if diff > 0.2:
            return "improving"
        elif diff < -0.2:
            return "declining"
        else:
            return "stable"
    
    def get_state(self) -> Dict[str, Any]:
        """دریافت وضعیت خلق و خو"""
        return {
            'current_state': self.current_mood.state.value,
            'valence': self.current_mood.valence,
            'arousal': self.current_mood.arousal,
            'description': self.get_mood_description(),
            'needs_rest': self.should_rest(),
            'trend': self.get_mood_trend()
        }
