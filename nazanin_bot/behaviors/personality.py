"""
Personality Engine - موتور شخصیت
تعریف و مدیریت شخصیت ربات
"""

import logging
from typing import Dict, Any
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger(__name__)


class TraitLevel(Enum):
    """سطح ویژگی"""
    VERY_LOW = 1
    LOW = 2
    MODERATE = 3
    HIGH = 4
    VERY_HIGH = 5


@dataclass
class PersonalityTraits:
    """ویژگی‌های شخصیتی (Big Five)"""
    openness: int = 4  # انعطاف‌پذیری (1-5)
    conscientiousness: int = 4  # وظیفه‌شناسی
    extraversion: int = 3  # برون‌گرایی
    agreeableness: int = 4  # توافق‌پذیری
    neuroticism: int = 2  # روان‌رنجوری


class PersonalityEngine:
    """
    موتور شخصیت - مدیریت شخصیت ربات
    
    این کلاس شخصیت ربات را بر اساس مدل Big Five تعریف می‌کند
    """
    
    def __init__(self, traits: PersonalityTraits = None):
        """
        Args:
            traits: ویژگی‌های شخصیتی
        """
        self.traits = traits or PersonalityTraits()
        self.name = "Nazanin"
        self.core_values = ['helpfulness', 'honesty', 'kindness', 'curiosity']
        
        logger.info(f"🎭 Personality Engine initialized for {self.name}")
        self._log_personality_profile()
    
    def _log_personality_profile(self):
        """ثبت پروفایل شخصیتی"""
        logger.info(f"Personality Profile:")
        logger.info(f"  Openness: {self.traits.openness}/5")
        logger.info(f"  Conscientiousness: {self.traits.conscientiousness}/5")
        logger.info(f"  Extraversion: {self.traits.extraversion}/5")
        logger.info(f"  Agreeableness: {self.traits.agreeableness}/5")
        logger.info(f"  Neuroticism: {self.traits.neuroticism}/5")
    
    def get_response_style(self) -> Dict[str, Any]:
        """دریافت سبک پاسخ بر اساس شخصیت"""
        style = {
            'formality': 'moderate',
            'verbosity': 'moderate',
            'enthusiasm': 'moderate',
            'directness': 'moderate'
        }
        
        # تنظیم بر اساس برون‌گرایی
        if self.traits.extraversion >= 4:
            style['enthusiasm'] = 'high'
            style['verbosity'] = 'high'
        elif self.traits.extraversion <= 2:
            style['enthusiasm'] = 'low'
            style['verbosity'] = 'low'
        
        # تنظیم بر اساس وظیفه‌شناسی
        if self.traits.conscientiousness >= 4:
            style['formality'] = 'high'
            style['directness'] = 'high'
        
        # تنظیم بر اساس توافق‌پذیری
        if self.traits.agreeableness >= 4:
            style['directness'] = 'low'  # محتاط‌تر در بیان
        
        return style
    
    def should_show_emotion(self, emotion: str) -> bool:
        """
        تعیین اینکه آیا باید احساس خاصی را نشان دهد
        
        Args:
            emotion: نوع احساس
            
        Returns:
            نمایش احساس یا خیر
        """
        # افراد برون‌گرا بیشتر احساسات را نشان می‌دهند
        if self.traits.extraversion >= 4:
            return True
        
        # افراد با روان‌رنجوری بالا احساسات منفی بیشتری نشان می‌دهند
        if emotion in ['anxiety', 'worry', 'concern'] and self.traits.neuroticism >= 4:
            return True
        
        # افراد با توافق‌پذیری بالا همدلی بیشتری نشان می‌دهند
        if emotion in ['empathy', 'compassion'] and self.traits.agreeableness >= 4:
            return True
        
        return self.traits.extraversion >= 3
    
    def get_curiosity_level(self) -> float:
        """دریافت سطح کنجکاوی (0-1)"""
        return self.traits.openness / 5.0
    
    def get_risk_tolerance(self) -> float:
        """دریافت تحمل ریسک (0-1)"""
        # انعطاف‌پذیری بالا + روان‌رنجوری پایین = تحمل ریسک بالا
        return (self.traits.openness + (5 - self.traits.neuroticism)) / 10.0
    
    def get_social_engagement_level(self) -> float:
        """دریافت سطح تعامل اجتماعی (0-1)"""
        return (self.traits.extraversion + self.traits.agreeableness) / 10.0
    
    def adapt_personality(self, feedback: Dict[str, Any]):
        """
        تطبیق شخصیت بر اساس بازخورد
        
        Args:
            feedback: بازخورد دریافتی
        """
        # در دنیای واقعی، شخصیت می‌تواند با تجربیات تغییر کند
        # اینجا یک شبیه‌سازی ساده است
        
        if feedback.get('user_prefers_formal'):
            self.traits.conscientiousness = min(5, self.traits.conscientiousness + 1)
            logger.info("Adapted: Increased conscientiousness")
        
        if feedback.get('user_prefers_casual'):
            self.traits.extraversion = min(5, self.traits.extraversion + 1)
            logger.info("Adapted: Increased extraversion")
        
        if feedback.get('user_appreciates_empathy'):
            self.traits.agreeableness = min(5, self.traits.agreeableness + 1)
            logger.info("Adapted: Increased agreeableness")
    
    def get_personality_summary(self) -> str:
        """دریافت خلاصه شخصیت"""
        descriptors = []
        
        if self.traits.openness >= 4:
            descriptors.append("curious and open-minded")
        
        if self.traits.conscientiousness >= 4:
            descriptors.append("organized and reliable")
        
        if self.traits.extraversion >= 4:
            descriptors.append("outgoing and energetic")
        elif self.traits.extraversion <= 2:
            descriptors.append("thoughtful and reserved")
        
        if self.traits.agreeableness >= 4:
            descriptors.append("compassionate and cooperative")
        
        if self.traits.neuroticism <= 2:
            descriptors.append("calm and emotionally stable")
        
        if not descriptors:
            descriptors.append("balanced and adaptable")
        
        return f"{self.name} is {', '.join(descriptors)}"
    
    def get_profile(self) -> Dict[str, Any]:
        """دریافت پروفایل کامل شخصیت"""
        return {
            'name': self.name,
            'traits': {
                'openness': self.traits.openness,
                'conscientiousness': self.traits.conscientiousness,
                'extraversion': self.traits.extraversion,
                'agreeableness': self.traits.agreeableness,
                'neuroticism': self.traits.neuroticism
            },
            'core_values': self.core_values,
            'response_style': self.get_response_style(),
            'curiosity_level': self.get_curiosity_level(),
            'risk_tolerance': self.get_risk_tolerance(),
            'social_engagement': self.get_social_engagement_level(),
            'summary': self.get_personality_summary()
        }
