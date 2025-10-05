"""
Experience Replay - بازپخش تجربه
بازبینی و یادگیری مجدد از تجربیات گذشته
"""

import logging
import asyncio
from typing import Dict, Any, List, Optional
import random

logger = logging.getLogger(__name__)


class ExperienceReplay:
    """
    بازپخش تجربه
    
    مشابه replay در یادگیری تقویتی و consolidation در خواب
    """
    
    def __init__(self, adaptive_learning):
        """
        Args:
            adaptive_learning: نمونه یادگیری تطبیقی
        """
        self.adaptive_learning = adaptive_learning
        self.replay_batch_size = 5
        self.prioritize_important = True
        
        logger.info("🔁 Experience Replay initialized")
    
    async def replay_experiences(self, count: Optional[int] = None) -> Dict[str, Any]:
        """
        بازپخش تجربیات
        
        Args:
            count: تعداد تجربیات برای بازپخش
            
        Returns:
            آمار بازپخش
        """
        if count is None:
            count = self.replay_batch_size
        
        experiences = self.adaptive_learning.experiences
        
        if not experiences:
            logger.info("No experiences to replay")
            return {'replayed': 0}
        
        # انتخاب تجربیات برای بازپخش
        selected = self._select_experiences(experiences, count)
        
        logger.info(f"🔁 Replaying {len(selected)} experiences...")
        
        insights_gained = []
        
        for exp in selected:
            # شبیه‌سازی بازپخش
            await asyncio.sleep(0.2)
            
            # استخراج بینش‌های جدید
            insight = self._extract_insights(exp)
            if insight:
                insights_gained.append(insight)
            
            logger.debug(f"Replayed: {exp.action} -> {'success' if exp.success else 'failure'}")
        
        return {
            'replayed': len(selected),
            'insights_gained': insights_gained
        }
    
    def _select_experiences(self, experiences: List, count: int) -> List:
        """انتخاب تجربیات برای بازپخش"""
        if len(experiences) <= count:
            return experiences
        
        if self.prioritize_important:
            # اولویت‌بندی بر اساس اهمیت
            # تجربیات با reward بالا یا شکست‌های مهم
            sorted_exp = sorted(
                experiences,
                key=lambda x: abs(x.reward) + (0.5 if not x.success else 0.0),
                reverse=True
            )
            
            # ترکیب: نیمی مهم، نیمی تصادفی
            important = sorted_exp[:count//2]
            random_sample = random.sample(experiences, count - len(important))
            
            return important + random_sample
        else:
            # انتخاب تصادفی
            return random.sample(experiences, count)
    
    def _extract_insights(self, experience) -> Optional[str]:
        """استخراج بینش از تجربه"""
        # در تجربیات موفق
        if experience.success and experience.reward > 0.5:
            return f"Successful pattern confirmed: {experience.action}"
        
        # در شکست‌های مکرر
        context_key = self.adaptive_learning._get_context_key(experience.context)
        if context_key in self.adaptive_learning.learned_patterns:
            pattern = self.adaptive_learning.learned_patterns[context_key]
            if not experience.success and pattern['success_rate'] < 0.3:
                return f"Avoid {experience.action} in context {context_key}"
        
        return None
    
    async def consolidate_learning(self):
        """تثبیت یادگیری (مانند خواب)"""
        logger.info("💤 Consolidating learning...")
        
        # بازپخش تجربیات مهم
        result = await self.replay_experiences(count=10)
        
        # تقویت الگوهای موفق
        self._reinforce_successful_patterns()
        
        logger.info(f"✨ Learning consolidated: {result['replayed']} experiences reviewed")
    
    def _reinforce_successful_patterns(self):
        """تقویت الگوهای موفق"""
        for pattern_key, pattern_data in self.adaptive_learning.learned_patterns.items():
            if pattern_data['success_rate'] > 0.7:
                # تقویت الگوی موفق
                logger.debug(f"Reinforced successful pattern: {pattern_key}")
