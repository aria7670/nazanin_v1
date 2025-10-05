"""
Settings - تنظیمات پروژه
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Settings:
    """تنظیمات کلی ربات"""
    
    # تنظیمات عمومی
    bot_name: str = "Nazanin"
    version: str = "1.0.0"
    log_level: str = "INFO"
    log_file: Optional[str] = "./logs/nazanin.log"
    
    # تنظیمات مغز
    cognitive_load_threshold: float = 0.8
    attention_filter_threshold: float = 0.3
    
    # تنظیمات حافظه
    short_term_memory_capacity: int = 7
    short_term_memory_retention_time: int = 300  # ثانیه
    long_term_memory_path: str = "./data/ltm.db"
    
    # تنظیمات تصمیم‌گیری
    default_decision_style: str = "balanced"  # balanced, cautious, bold
    autonomy_level: float = 0.8
    
    # تنظیمات رفتار
    response_time_variance: float = 0.3
    typo_probability: float = 0.02
    fatigue_threshold: float = 0.8
    
    # تنظیمات شخصیت (Big Five)
    personality_openness: int = 4
    personality_conscientiousness: int = 4
    personality_extraversion: int = 3
    personality_agreeableness: int = 4
    personality_neuroticism: int = 2
    
    # تنظیمات احساسات
    empathy_level: float = 0.8
    emotional_stability: float = 0.7
    
    # تنظیمات یادگیری
    learning_rate: float = 0.1
    experience_replay_batch_size: int = 5
    
    # تنظیمات پردازش
    input_history_size: int = 100
    context_lookback: int = 5
    
    # تنظیمات عملیاتی
    enable_auto_sleep: bool = True
    sleep_hours_start: int = 2
    sleep_hours_end: int = 5
    
    def to_dict(self) -> dict:
        """تبدیل به دیکشنری"""
        return {
            'bot_name': self.bot_name,
            'version': self.version,
            'log_level': self.log_level,
            'cognitive': {
                'load_threshold': self.cognitive_load_threshold,
                'attention_threshold': self.attention_filter_threshold
            },
            'memory': {
                'stm_capacity': self.short_term_memory_capacity,
                'stm_retention': self.short_term_memory_retention_time,
                'ltm_path': self.long_term_memory_path
            },
            'decision': {
                'style': self.default_decision_style,
                'autonomy': self.autonomy_level
            },
            'personality': {
                'openness': self.personality_openness,
                'conscientiousness': self.personality_conscientiousness,
                'extraversion': self.personality_extraversion,
                'agreeableness': self.personality_agreeableness,
                'neuroticism': self.personality_neuroticism
            }
        }
