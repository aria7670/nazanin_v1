"""
Goal Manager - مدیریت اهداف
مدیریت و پیگیری اهداف کوتاه‌مدت و بلندمدت
"""

import logging
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

logger = logging.getLogger(__name__)


class GoalStatus(Enum):
    """وضعیت هدف"""
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"
    FAILED = "failed"
    ABANDONED = "abandoned"


class GoalPriority(Enum):
    """اولویت هدف"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


@dataclass
class Goal:
    """یک هدف"""
    goal_id: str
    description: str
    priority: GoalPriority
    status: GoalStatus = GoalStatus.ACTIVE
    progress: float = 0.0  # پیشرفت (0-1)
    created_at: datetime = field(default_factory=datetime.now)
    deadline: Optional[datetime] = None
    sub_goals: List[str] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)
    success_criteria: Dict[str, Any] = field(default_factory=dict)


class GoalManager:
    """
    مدیریت اهداف - مدیریت اهداف کوتاه و بلندمدت
    
    این کلاس اهداف را مدیریت و اولویت‌بندی می‌کند
    """
    
    def __init__(self):
        self.goals: Dict[str, Goal] = {}
        self.active_goal: Optional[str] = None
        
        logger.info("🎯 Goal Manager initialized")
    
    def add_goal(self, goal_id: str, description: str, 
                priority: GoalPriority = GoalPriority.MEDIUM,
                deadline: Optional[datetime] = None) -> Goal:
        """
        افزودن هدف جدید
        
        Args:
            goal_id: شناسه هدف
            description: توضیحات
            priority: اولویت
            deadline: مهلت
            
        Returns:
            هدف ایجاد شده
        """
        goal = Goal(
            goal_id=goal_id,
            description=description,
            priority=priority,
            deadline=deadline
        )
        
        self.goals[goal_id] = goal
        logger.info(f"✨ New goal added: {description} (priority: {priority.name})")
        
        # اگر هدف فعلی نداریم، این را فعال کن
        if not self.active_goal and goal.status == GoalStatus.ACTIVE:
            self.set_active_goal(goal_id)
        
        return goal
    
    def get_goal(self, goal_id: str) -> Optional[Goal]:
        """دریافت یک هدف"""
        return self.goals.get(goal_id)
    
    def update_progress(self, goal_id: str, progress: float):
        """
        به‌روزرسانی پیشرفت هدف
        
        Args:
            goal_id: شناسه هدف
            progress: پیشرفت (0-1)
        """
        if goal_id not in self.goals:
            logger.warning(f"Goal not found: {goal_id}")
            return
        
        goal = self.goals[goal_id]
        old_progress = goal.progress
        goal.progress = max(0.0, min(1.0, progress))
        
        logger.debug(f"📈 Goal progress updated: {goal_id} ({old_progress:.1%} -> {goal.progress:.1%})")
        
        # بررسی تکمیل
        if goal.progress >= 1.0:
            self.complete_goal(goal_id)
    
    def complete_goal(self, goal_id: str):
        """تکمیل یک هدف"""
        if goal_id not in self.goals:
            return
        
        goal = self.goals[goal_id]
        goal.status = GoalStatus.COMPLETED
        goal.progress = 1.0
        
        logger.info(f"🎉 Goal completed: {goal.description}")
        
        # اگر این هدف فعال بود، هدف بعدی را فعال کن
        if self.active_goal == goal_id:
            self._activate_next_goal()
    
    def _activate_next_goal(self):
        """فعال‌سازی هدف بعدی با بالاترین اولویت"""
        active_goals = [
            (gid, g) for gid, g in self.goals.items()
            if g.status == GoalStatus.ACTIVE
        ]
        
        if not active_goals:
            self.active_goal = None
            logger.info("📭 No active goals remaining")
            return
        
        # مرتب‌سازی بر اساس اولویت
        sorted_goals = sorted(active_goals, key=lambda x: x[1].priority.value, reverse=True)
        next_goal = sorted_goals[0]
        
        self.set_active_goal(next_goal[0])
    
    def set_active_goal(self, goal_id: str):
        """تنظیم هدف فعال"""
        if goal_id not in self.goals:
            logger.warning(f"Cannot set active goal: {goal_id} not found")
            return
        
        self.active_goal = goal_id
        logger.info(f"🎯 Active goal set: {self.goals[goal_id].description}")
    
    def get_active_goals(self, limit: int = 5) -> List[Goal]:
        """دریافت اهداف فعال"""
        active = [
            g for g in self.goals.values()
            if g.status == GoalStatus.ACTIVE
        ]
        
        # مرتب‌سازی بر اساس اولویت
        sorted_goals = sorted(active, key=lambda x: x.priority.value, reverse=True)
        
        return sorted_goals[:limit]
    
    def get_goal_hierarchy(self) -> Dict[str, List[str]]:
        """دریافت سلسله‌مراتب اهداف"""
        hierarchy = {}
        
        for goal_id, goal in self.goals.items():
            if not goal.sub_goals:
                hierarchy[goal_id] = []
            else:
                hierarchy[goal_id] = goal.sub_goals
        
        return hierarchy
    
    def add_sub_goal(self, parent_goal_id: str, sub_goal_id: str):
        """افزودن زیرهدف"""
        if parent_goal_id not in self.goals:
            logger.warning(f"Parent goal not found: {parent_goal_id}")
            return
        
        parent = self.goals[parent_goal_id]
        if sub_goal_id not in parent.sub_goals:
            parent.sub_goals.append(sub_goal_id)
            logger.debug(f"Added sub-goal {sub_goal_id} to {parent_goal_id}")
    
    def get_stats(self) -> Dict[str, Any]:
        """دریافت آمار اهداف"""
        if not self.goals:
            return {'total_goals': 0}
        
        status_counts = {}
        for status in GoalStatus:
            status_counts[status.value] = sum(
                1 for g in self.goals.values() if g.status == status
            )
        
        active_goals = [g for g in self.goals.values() if g.status == GoalStatus.ACTIVE]
        avg_progress = sum(g.progress for g in active_goals) / len(active_goals) if active_goals else 0.0
        
        return {
            'total_goals': len(self.goals),
            'by_status': status_counts,
            'active_goal': self.active_goal,
            'average_progress': avg_progress
        }
