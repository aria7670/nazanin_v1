"""
Planning Engine - موتور برنامه‌ریزی
برنامه‌ریزی و استراتژی برای دستیابی به اهداف
"""

import logging
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

logger = logging.getLogger(__name__)


class ActionStatus(Enum):
    """وضعیت اقدام"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    BLOCKED = "blocked"


@dataclass
class Action:
    """یک اقدام در برنامه"""
    action_id: str
    description: str
    prerequisites: List[str]
    estimated_duration: float  # ثانیه
    status: ActionStatus = ActionStatus.PENDING
    result: Optional[Dict[str, Any]] = None


@dataclass
class Plan:
    """یک برنامه"""
    plan_id: str
    goal_id: str
    actions: List[Action]
    created_at: datetime
    estimated_completion: float  # ثانیه


class PlanningEngine:
    """
    موتور برنامه‌ریزی - ایجاد برنامه برای اهداف
    
    این کلاس برنامه‌های عملیاتی برای دستیابی به اهداف ایجاد می‌کند
    """
    
    def __init__(self):
        self.plans: Dict[str, Plan] = {}
        self.action_templates: Dict[str, Dict[str, Any]] = self._init_action_templates()
        
        logger.info("📋 Planning Engine initialized")
    
    def _init_action_templates(self) -> Dict[str, Dict[str, Any]]:
        """ایجاد الگوهای اقدام"""
        return {
            'gather_information': {
                'duration': 5.0,
                'description': 'Gather necessary information'
            },
            'analyze': {
                'duration': 3.0,
                'description': 'Analyze the situation'
            },
            'prepare': {
                'duration': 2.0,
                'description': 'Prepare resources'
            },
            'execute': {
                'duration': 10.0,
                'description': 'Execute the main task'
            },
            'verify': {
                'duration': 2.0,
                'description': 'Verify the results'
            }
        }
    
    def create_plan(self, goal_id: str, goal_description: str) -> Plan:
        """
        ایجاد برنامه برای یک هدف
        
        Args:
            goal_id: شناسه هدف
            goal_description: توضیحات هدف
            
        Returns:
            برنامه ایجاد شده
        """
        logger.info(f"📝 Creating plan for goal: {goal_description}")
        
        # تحلیل هدف و ایجاد اقدامات
        actions = self._generate_actions(goal_description)
        
        # محاسبه زمان تخمینی
        total_duration = sum(action.estimated_duration for action in actions)
        
        plan = Plan(
            plan_id=f"plan_{datetime.now().timestamp()}",
            goal_id=goal_id,
            actions=actions,
            created_at=datetime.now(),
            estimated_completion=total_duration
        )
        
        self.plans[plan.plan_id] = plan
        
        logger.info(f"✅ Plan created with {len(actions)} actions (estimated: {total_duration:.1f}s)")
        
        return plan
    
    def _generate_actions(self, goal_description: str) -> List[Action]:
        """تولید اقدامات بر اساس توضیحات هدف"""
        actions = []
        
        # برنامه‌ریزی ساده بر اساس الگوهای از پیش تعریف شده
        action_sequence = [
            ('gather_information', []),
            ('analyze', ['gather_information']),
            ('prepare', ['analyze']),
            ('execute', ['prepare']),
            ('verify', ['execute'])
        ]
        
        for idx, (action_type, prereqs) in enumerate(action_sequence):
            template = self.action_templates[action_type]
            
            action = Action(
                action_id=f"action_{idx}",
                description=template['description'],
                prerequisites=[f"action_{action_sequence.index((p, a))}" for p, a in action_sequence if p in prereqs],
                estimated_duration=template['duration']
            )
            
            actions.append(action)
        
        return actions
    
    def get_plan(self, plan_id: str) -> Optional[Plan]:
        """دریافت یک برنامه"""
        return self.plans.get(plan_id)
    
    def get_next_action(self, plan_id: str) -> Optional[Action]:
        """
        دریافت اقدام بعدی برای اجرا
        
        Args:
            plan_id: شناسه برنامه
            
        Returns:
            اقدام بعدی یا None
        """
        plan = self.plans.get(plan_id)
        if not plan:
            return None
        
        # یافتن اولین اقدام که پیش‌نیازهایش تکمیل شده
        for action in plan.actions:
            if action.status == ActionStatus.PENDING:
                # بررسی پیش‌نیازها
                all_prerequisites_met = all(
                    self._is_action_completed(plan, prereq)
                    for prereq in action.prerequisites
                )
                
                if all_prerequisites_met:
                    return action
        
        return None
    
    def _is_action_completed(self, plan: Plan, action_id: str) -> bool:
        """بررسی تکمیل یک اقدام"""
        for action in plan.actions:
            if action.action_id == action_id:
                return action.status == ActionStatus.COMPLETED
        return False
    
    def update_action_status(self, plan_id: str, action_id: str, 
                            status: ActionStatus, result: Optional[Dict[str, Any]] = None):
        """به‌روزرسانی وضعیت یک اقدام"""
        plan = self.plans.get(plan_id)
        if not plan:
            return
        
        for action in plan.actions:
            if action.action_id == action_id:
                action.status = status
                if result:
                    action.result = result
                
                logger.debug(f"Action {action_id} status updated to {status.value}")
                break
    
    def get_plan_progress(self, plan_id: str) -> float:
        """
        دریافت پیشرفت برنامه
        
        Args:
            plan_id: شناسه برنامه
            
        Returns:
            پیشرفت (0-1)
        """
        plan = self.plans.get(plan_id)
        if not plan or not plan.actions:
            return 0.0
        
        completed = sum(1 for action in plan.actions if action.status == ActionStatus.COMPLETED)
        
        return completed / len(plan.actions)
    
    def is_plan_completed(self, plan_id: str) -> bool:
        """بررسی تکمیل برنامه"""
        return self.get_plan_progress(plan_id) >= 1.0
    
    def get_stats(self) -> Dict[str, Any]:
        """دریافت آمار برنامه‌ریزی"""
        if not self.plans:
            return {'total_plans': 0}
        
        return {
            'total_plans': len(self.plans),
            'completed_plans': sum(1 for p in self.plans.values() 
                                  if self.is_plan_completed(p.plan_id)),
            'active_plans': sum(1 for p in self.plans.values() 
                               if 0 < self.get_plan_progress(p.plan_id) < 1.0)
        }
