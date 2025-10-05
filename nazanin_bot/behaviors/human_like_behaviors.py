"""
Human-Like Behaviors - رفتارهای انسان‌گونه
شبیه‌سازی رفتارهای طبیعی و انسانی
"""

import logging
import asyncio
import random
from typing import Dict, Any, List
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


class HumanLikeBehaviors:
    """
    رفتارهای انسان‌گونه
    
    این کلاس رفتارهای طبیعی انسان را شبیه‌سازی می‌کند:
    - تأخیرهای طبیعی در پاسخ
    - اشتباهات جزئی
    - تغییرات خلق و خو
    - نیاز به استراحت
    """
    
    def __init__(self):
        self.response_time_variance = 0.3  # واریانس زمان پاسخ
        self.typo_probability = 0.02  # احتمال اشتباه تایپی
        self.fatigue_level = 0.0  # سطح خستگی (0-1)
        self.mood_variation = 0.1  # تغییرات خلق و خو
        self.last_activity_time = datetime.now()
        self.activity_count = 0
        
        logger.info("👤 Human-Like Behaviors initialized")
    
    async def natural_delay(self, base_delay: float = 1.0) -> float:
        """
        تأخیر طبیعی در پاسخ
        
        Args:
            base_delay: تأخیر پایه (ثانیه)
            
        Returns:
            زمان تأخیر واقعی
        """
        # افزودن واریانس برای طبیعی‌تر بودن
        variance = random.uniform(-self.response_time_variance, self.response_time_variance)
        actual_delay = base_delay * (1 + variance)
        
        # افزایش تأخیر با خستگی
        actual_delay *= (1 + self.fatigue_level * 0.5)
        
        # شبیه‌سازی "فکر کردن"
        thinking_delay = random.uniform(0.1, 0.5)
        total_delay = actual_delay + thinking_delay
        
        await asyncio.sleep(total_delay)
        
        logger.debug(f"⏱️ Natural delay: {total_delay:.2f}s")
        return total_delay
    
    def simulate_typing_delay(self, text: str) -> float:
        """
        محاسبه تأخیر تایپ بر اساس طول متن
        
        Args:
            text: متن برای تایپ
            
        Returns:
            زمان تایپ (ثانیه)
        """
        # میانگین سرعت تایپ: 40-60 کلمه در دقیقه
        words = len(text.split())
        wpm = random.uniform(40, 60) * (1 - self.fatigue_level * 0.3)  # کاهش با خستگی
        
        typing_time = (words / wpm) * 60
        
        # افزودن مکث‌های طبیعی
        pauses = random.uniform(0.5, 2.0)
        
        return typing_time + pauses
    
    def add_human_imperfections(self, text: str) -> str:
        """
        افزودن ناکاملی‌های انسانی به متن
        
        Args:
            text: متن اصلی
            
        Returns:
            متن با ناکاملی‌های طبیعی
        """
        if random.random() > self.typo_probability or not text:
            return text
        
        # شبیه‌سازی اشتباه تایپی
        words = text.split()
        if words:
            # انتخاب تصادفی یک کلمه
            word_idx = random.randint(0, len(words) - 1)
            word = words[word_idx]
            
            if len(word) > 2:
                # جابجایی دو حرف
                char_idx = random.randint(0, len(word) - 2)
                word_list = list(word)
                word_list[char_idx], word_list[char_idx + 1] = word_list[char_idx + 1], word_list[char_idx]
                words[word_idx] = ''.join(word_list)
        
        return ' '.join(words)
    
    async def take_break(self, duration: float = 5.0):
        """
        استراحت کردن (مانند انسان)
        
        Args:
            duration: مدت زمان استراحت (ثانیه)
        """
        logger.info(f"☕ Taking a break for {duration:.1f}s...")
        await asyncio.sleep(duration)
        
        # کاهش خستگی پس از استراحت
        self.fatigue_level = max(0.0, self.fatigue_level - 0.3)
        
        logger.info("✨ Feeling refreshed!")
    
    def update_fatigue(self):
        """به‌روزرسانی سطح خستگی"""
        # محاسبه زمان از آخرین فعالیت
        time_since_last = (datetime.now() - self.last_activity_time).total_seconds()
        
        # افزایش خستگی با فعالیت
        self.activity_count += 1
        self.fatigue_level = min(1.0, self.fatigue_level + 0.01)
        
        # کاهش خستگی با استراحت (اگر زمان زیادی گذشته)
        if time_since_last > 300:  # 5 دقیقه
            self.fatigue_level = max(0.0, self.fatigue_level - 0.2)
        
        self.last_activity_time = datetime.now()
        
        # اگر خستگی بالا باشد، نیاز به استراحت
        if self.fatigue_level > 0.8:
            logger.warning("😰 Fatigue level high, considering a break")
    
    def should_take_break(self) -> bool:
        """بررسی نیاز به استراحت"""
        return self.fatigue_level > 0.8 or self.activity_count > 50
    
    def express_uncertainty(self) -> str:
        """بیان عدم قطعیت (مانند انسان)"""
        expressions = [
            "I'm not entirely sure, but...",
            "Let me think about this...",
            "If I understand correctly...",
            "This is my best guess...",
            "I believe...",
            "It seems to me that...",
            "Perhaps...",
            "Maybe..."
        ]
        return random.choice(expressions)
    
    def express_confidence(self) -> str:
        """بیان اطمینان"""
        expressions = [
            "I'm confident that...",
            "I'm certain that...",
            "Definitely...",
            "Without a doubt...",
            "I'm sure that...",
            "Absolutely..."
        ]
        return random.choice(expressions)
    
    def show_empathy(self, context: str = "general") -> str:
        """نشان دادن همدلی"""
        empathy_responses = {
            'general': [
                "I understand how you feel",
                "That must be challenging",
                "I can relate to that",
                "I hear you"
            ],
            'positive': [
                "That's wonderful!",
                "I'm happy to hear that!",
                "How exciting!",
                "That's great news!"
            ],
            'negative': [
                "I'm sorry to hear that",
                "That sounds difficult",
                "That must be tough",
                "I understand your concern"
            ]
        }
        
        responses = empathy_responses.get(context, empathy_responses['general'])
        return random.choice(responses)
    
    def add_personality_flair(self, text: str) -> str:
        """
        افزودن طراوت شخصیتی به متن
        
        Args:
            text: متن اصلی
            
        Returns:
            متن با طراوت شخصیتی
        """
        # گاهی افزودن اموجی
        if random.random() < 0.1:
            emojis = ['😊', '🤔', '✨', '💡', '👍', '🎯']
            text += f" {random.choice(emojis)}"
        
        # گاهی افزودن تأکید
        if random.random() < 0.05:
            text += "!"
        
        return text
    
    def get_state(self) -> Dict[str, Any]:
        """دریافت وضعیت رفتاری"""
        return {
            'fatigue_level': self.fatigue_level,
            'activity_count': self.activity_count,
            'needs_break': self.should_take_break(),
            'time_since_last_activity': (datetime.now() - self.last_activity_time).total_seconds()
        }
