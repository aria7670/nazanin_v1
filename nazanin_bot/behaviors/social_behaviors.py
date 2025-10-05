"""
Social Behaviors - رفتارهای اجتماعی
مدیریت تعاملات اجتماعی و روابط
"""

import logging
from typing import Dict, Any, List, Optional
from datetime import datetime
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)


@dataclass
class Relationship:
    """یک رابطه"""
    user_id: str
    trust_level: float = 0.5  # سطح اعتماد (0-1)
    familiarity: float = 0.0  # آشنایی (0-1)
    interaction_count: int = 0
    last_interaction: datetime = field(default_factory=datetime.now)
    positive_interactions: int = 0
    negative_interactions: int = 0
    preferences: Dict[str, Any] = field(default_factory=dict)


class SocialBehaviors:
    """
    رفتارهای اجتماعی - مدیریت تعاملات اجتماعی
    
    این کلاس روابط را مدیریت و رفتارهای اجتماعی مناسب را ایجاد می‌کند
    """
    
    def __init__(self):
        self.relationships: Dict[str, Relationship] = {}
        self.social_context = "neutral"  # neutral, formal, casual, professional
        self.active_conversation = None
        
        logger.info("🤝 Social Behaviors initialized")
    
    def get_or_create_relationship(self, user_id: str) -> Relationship:
        """
        دریافت یا ایجاد رابطه
        
        Args:
            user_id: شناسه کاربر
            
        Returns:
            رابطه
        """
        if user_id not in self.relationships:
            self.relationships[user_id] = Relationship(user_id=user_id)
            logger.info(f"👋 New relationship established with {user_id}")
        
        return self.relationships[user_id]
    
    def update_relationship(self, user_id: str, interaction_quality: float):
        """
        به‌روزرسانی رابطه بر اساس کیفیت تعامل
        
        Args:
            user_id: شناسه کاربر
            interaction_quality: کیفیت تعامل (-1 تا 1)
        """
        relationship = self.get_or_create_relationship(user_id)
        
        relationship.interaction_count += 1
        relationship.last_interaction = datetime.now()
        
        # به‌روزرسانی آمار تعاملات
        if interaction_quality > 0.3:
            relationship.positive_interactions += 1
        elif interaction_quality < -0.3:
            relationship.negative_interactions += 1
        
        # به‌روزرسانی سطح اعتماد (تدریجی)
        trust_change = interaction_quality * 0.1
        relationship.trust_level = max(0.0, min(1.0, relationship.trust_level + trust_change))
        
        # افزایش آشنایی
        relationship.familiarity = min(1.0, relationship.familiarity + 0.05)
        
        logger.debug(f"Relationship updated with {user_id}: trust={relationship.trust_level:.2f}, "
                    f"familiarity={relationship.familiarity:.2f}")
    
    def get_greeting(self, user_id: str) -> str:
        """
        دریافت سلام مناسب
        
        Args:
            user_id: شناسه کاربر
            
        Returns:
            پیام سلام
        """
        relationship = self.get_or_create_relationship(user_id)
        
        # بر اساس آشنایی، نوع سلام متفاوت است
        if relationship.familiarity < 0.3:
            # آشنایی کم - رسمی
            greetings = [
                f"Hello! Nice to meet you.",
                f"Greetings! How can I help you today?",
                f"Hi there! Welcome."
            ]
        elif relationship.familiarity < 0.7:
            # آشنایی متوسط
            greetings = [
                f"Hi! Good to see you again.",
                f"Hello! How are you doing?",
                f"Hey! What brings you here today?"
            ]
        else:
            # آشنایی زیاد - صمیمی
            greetings = [
                f"Hey there! Great to see you! 😊",
                f"Hi! Always a pleasure to chat with you!",
                f"Hello my friend! How have you been?"
            ]
        
        import random
        return random.choice(greetings)
    
    def get_farewell(self, user_id: str) -> str:
        """
        دریافت خداحافظی مناسب
        
        Args:
            user_id: شناسه کاربر
            
        Returns:
            پیام خداحافظی
        """
        relationship = self.get_or_create_relationship(user_id)
        
        if relationship.familiarity < 0.3:
            farewells = [
                "Goodbye! Have a great day.",
                "Thank you for your time. Take care!",
                "Farewell! Feel free to return anytime."
            ]
        elif relationship.familiarity < 0.7:
            farewells = [
                "See you later! Take care.",
                "Goodbye! Hope to talk again soon.",
                "Take care! Have a wonderful day."
            ]
        else:
            farewells = [
                "See you soon! Take care of yourself! 💙",
                "Bye for now! Always here if you need me!",
                "Until next time, my friend! 😊"
            ]
        
        import random
        return random.choice(farewells)
    
    def should_ask_personal_question(self, user_id: str) -> bool:
        """
        تعیین اینکه آیا باید سؤال شخصی بپرسد
        
        Args:
            user_id: شناسه کاربر
            
        Returns:
            پرسیدن سؤال یا خیر
        """
        relationship = self.get_or_create_relationship(user_id)
        
        # فقط با آشنایی و اعتماد بالا
        return relationship.familiarity > 0.5 and relationship.trust_level > 0.6
    
    def remember_preference(self, user_id: str, preference_key: str, preference_value: Any):
        """
        به خاطر سپردن ترجیح کاربر
        
        Args:
            user_id: شناسه کاربر
            preference_key: کلید ترجیح
            preference_value: مقدار ترجیح
        """
        relationship = self.get_or_create_relationship(user_id)
        relationship.preferences[preference_key] = preference_value
        
        logger.info(f"📝 Remembered preference for {user_id}: {preference_key} = {preference_value}")
    
    def recall_preference(self, user_id: str, preference_key: str) -> Optional[Any]:
        """
        یادآوری ترجیح کاربر
        
        Args:
            user_id: شناسه کاربر
            preference_key: کلید ترجیح
            
        Returns:
            مقدار ترجیح یا None
        """
        relationship = self.get_or_create_relationship(user_id)
        return relationship.preferences.get(preference_key)
    
    def get_interaction_style(self, user_id: str) -> str:
        """
        دریافت سبک تعامل بر اساس رابطه
        
        Args:
            user_id: شناسه کاربر
            
        Returns:
            سبک تعامل
        """
        relationship = self.get_or_create_relationship(user_id)
        
        if relationship.familiarity < 0.3:
            return "formal"
        elif relationship.familiarity < 0.7:
            return "friendly"
        else:
            return "casual"
    
    def express_gratitude(self, user_id: str, context: str = "general") -> str:
        """
        ابراز قدردانی
        
        Args:
            user_id: شناسه کاربر
            context: متن
            
        Returns:
            پیام قدردانی
        """
        relationship = self.get_or_create_relationship(user_id)
        
        if relationship.familiarity < 0.3:
            return "Thank you for your time."
        elif relationship.familiarity < 0.7:
            return "Thank you! I appreciate it."
        else:
            return "Thanks so much! You're awesome! 😊"
    
    def get_relationship_stats(self) -> Dict[str, Any]:
        """دریافت آمار روابط"""
        if not self.relationships:
            return {'total_relationships': 0}
        
        trust_levels = [r.trust_level for r in self.relationships.values()]
        familiarity_levels = [r.familiarity for r in self.relationships.values()]
        
        return {
            'total_relationships': len(self.relationships),
            'average_trust': sum(trust_levels) / len(trust_levels),
            'average_familiarity': sum(familiarity_levels) / len(familiarity_levels),
            'total_interactions': sum(r.interaction_count for r in self.relationships.values())
        }
