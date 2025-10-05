"""
Adaptive Learning - یادگیری تطبیقی
یادگیری از تجربیات و تطبیق با محیط
"""

import logging
from typing import Dict, Any, List, Optional
from datetime import datetime
from dataclasses import dataclass
import json

logger = logging.getLogger(__name__)


@dataclass
class LearningExperience:
    """یک تجربه یادگیری"""
    experience_id: str
    context: Dict[str, Any]
    action: str
    outcome: Dict[str, Any]
    success: bool
    reward: float  # پاداش (-1 تا 1)
    timestamp: datetime
    lessons_learned: List[str]


class AdaptiveLearning:
    """
    یادگیری تطبیقی
    
    این کلاس از تجربیات یاد می‌گیرد و رفتار را تطبیق می‌دهد
    """
    
    def __init__(self):
        self.experiences: List[LearningExperience] = []
        self.learned_patterns: Dict[str, Dict[str, Any]] = {}
        self.learning_rate = 0.1
        self.success_count = 0
        self.failure_count = 0
        
        logger.info("📚 Adaptive Learning initialized")
    
    def learn_from_experience(self, context: Dict[str, Any], action: str,
                             outcome: Dict[str, Any], success: bool,
                             reward: float = 0.0) -> List[str]:
        """
        یادگیری از یک تجربه
        
        Args:
            context: متن تجربه
            action: اقدام انجام شده
            outcome: نتیجه
            success: موفقیت
            reward: پاداش
            
        Returns:
            درس‌های آموخته شده
        """
        # تحلیل تجربه
        lessons = self._analyze_experience(context, action, outcome, success)
        
        # ایجاد تجربه
        experience = LearningExperience(
            experience_id=f"exp_{datetime.now().timestamp()}",
            context=context,
            action=action,
            outcome=outcome,
            success=success,
            reward=reward,
            timestamp=datetime.now(),
            lessons_learned=lessons
        )
        
        # ذخیره تجربه
        self.experiences.append(experience)
        if len(self.experiences) > 1000:
            self.experiences.pop(0)
        
        # به‌روزرسانی آمار
        if success:
            self.success_count += 1
        else:
            self.failure_count += 1
        
        # به‌روزرسانی الگوهای یادگرفته شده
        self._update_learned_patterns(context, action, success, reward)
        
        logger.info(f"📖 Learned from experience: {action} -> {'success' if success else 'failure'}")
        for lesson in lessons:
            logger.debug(f"  Lesson: {lesson}")
        
        return lessons
    
    def _analyze_experience(self, context: Dict[str, Any], action: str,
                           outcome: Dict[str, Any], success: bool) -> List[str]:
        """تحلیل تجربه و استخراج درس‌ها"""
        lessons = []
        
        if success:
            lessons.append(f"Action '{action}' works well in this context")
            
            # اگر پیش‌بینی نشده بود، درس بیشتری است
            if not self._was_expected(context, action):
                lessons.append(f"Discovered new successful approach: {action}")
        else:
            lessons.append(f"Action '{action}' should be avoided in similar contexts")
            
            # پیشنهاد جایگزین
            alternative = self._suggest_alternative(context, action)
            if alternative:
                lessons.append(f"Consider '{alternative}' instead")
        
        return lessons
    
    def _was_expected(self, context: Dict[str, Any], action: str) -> bool:
        """بررسی اینکه آیا این نتیجه قابل پیش‌بینی بود"""
        context_key = self._get_context_key(context)
        
        if context_key in self.learned_patterns:
            pattern = self.learned_patterns[context_key]
            return action in pattern.get('successful_actions', [])
        
        return False
    
    def _suggest_alternative(self, context: Dict[str, Any], failed_action: str) -> Optional[str]:
        """پیشنهاد اقدام جایگزین"""
        context_key = self._get_context_key(context)
        
        if context_key in self.learned_patterns:
            pattern = self.learned_patterns[context_key]
            successful_actions = pattern.get('successful_actions', [])
            
            if successful_actions:
                return successful_actions[0]
        
        return None
    
    def _get_context_key(self, context: Dict[str, Any]) -> str:
        """تولید کلید برای متن"""
        # ساده‌سازی متن به کلید
        context_type = context.get('type', 'unknown')
        context_category = context.get('category', 'general')
        
        return f"{context_type}_{context_category}"
    
    def _update_learned_patterns(self, context: Dict[str, Any], action: str,
                                success: bool, reward: float):
        """به‌روزرسانی الگوهای یادگرفته شده"""
        context_key = self._get_context_key(context)
        
        if context_key not in self.learned_patterns:
            self.learned_patterns[context_key] = {
                'successful_actions': [],
                'failed_actions': [],
                'total_attempts': 0,
                'success_rate': 0.0,
                'average_reward': 0.0
            }
        
        pattern = self.learned_patterns[context_key]
        pattern['total_attempts'] += 1
        
        if success:
            if action not in pattern['successful_actions']:
                pattern['successful_actions'].append(action)
        else:
            if action not in pattern['failed_actions']:
                pattern['failed_actions'].append(action)
        
        # به‌روزرسانی نرخ موفقیت
        pattern['success_rate'] = (
            pattern['success_rate'] * (pattern['total_attempts'] - 1) + (1.0 if success else 0.0)
        ) / pattern['total_attempts']
        
        # به‌روزرسانی پاداش میانگین
        pattern['average_reward'] = (
            pattern['average_reward'] * (pattern['total_attempts'] - 1) + reward
        ) / pattern['total_attempts']
    
    def predict_success(self, context: Dict[str, Any], action: str) -> float:
        """
        پیش‌بینی احتمال موفقیت
        
        Args:
            context: متن
            action: اقدام
            
        Returns:
            احتمال موفقیت (0-1)
        """
        context_key = self._get_context_key(context)
        
        if context_key not in self.learned_patterns:
            return 0.5  # عدم قطعیت
        
        pattern = self.learned_patterns[context_key]
        
        if action in pattern['successful_actions']:
            return min(0.9, 0.5 + pattern['success_rate'] * 0.5)
        elif action in pattern['failed_actions']:
            return max(0.1, 0.5 - pattern['success_rate'] * 0.5)
        else:
            return pattern['success_rate']
    
    def get_best_action(self, context: Dict[str, Any],
                       available_actions: List[str]) -> Optional[str]:
        """
        دریافت بهترین اقدام بر اساس یادگیری
        
        Args:
            context: متن
            available_actions: اقدامات موجود
            
        Returns:
            بهترین اقدام
        """
        if not available_actions:
            return None
        
        # پیش‌بینی موفقیت برای هر اقدام
        predictions = {
            action: self.predict_success(context, action)
            for action in available_actions
        }
        
        # انتخاب بهترین
        best_action = max(predictions.items(), key=lambda x: x[1])
        
        logger.debug(f"Best action for context: {best_action[0]} (confidence: {best_action[1]:.2f})")
        
        return best_action[0]
    
    def adapt_behavior(self, performance_feedback: Dict[str, Any]):
        """
        تطبیق رفتار بر اساس بازخورد عملکرد
        
        Args:
            performance_feedback: بازخورد عملکرد
        """
        overall_success_rate = self.success_count / max(1, self.success_count + self.failure_count)
        
        if overall_success_rate < 0.5:
            # عملکرد ضعیف - افزایش اکتشاف
            self.learning_rate = min(0.3, self.learning_rate + 0.05)
            logger.info("📊 Low success rate, increasing exploration")
        elif overall_success_rate > 0.8:
            # عملکرد خوب - کاهش اکتشاف
            self.learning_rate = max(0.05, self.learning_rate - 0.02)
            logger.info("📊 High success rate, decreasing exploration")
    
    def get_learning_stats(self) -> Dict[str, Any]:
        """دریافت آمار یادگیری"""
        total_experiences = len(self.experiences)
        
        if total_experiences == 0:
            return {
                'total_experiences': 0,
                'success_rate': 0.0
            }
        
        overall_success_rate = self.success_count / max(1, self.success_count + self.failure_count)
        
        return {
            'total_experiences': total_experiences,
            'success_count': self.success_count,
            'failure_count': self.failure_count,
            'success_rate': overall_success_rate,
            'learning_rate': self.learning_rate,
            'patterns_learned': len(self.learned_patterns),
            'recent_lessons': [
                exp.lessons_learned
                for exp in self.experiences[-5:]
            ]
        }
