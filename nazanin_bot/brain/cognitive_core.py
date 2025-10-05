"""
Cognitive Core - هسته شناختی
مرکز اصلی پردازش شناختی که تمام لایه‌های مغز را هماهنگ می‌کند
"""

import logging
from typing import Dict, Any, List, Optional
from datetime import datetime
import asyncio
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)


@dataclass
class CognitiveState:
    """وضعیت شناختی فعلی"""
    attention_level: float = 0.5  # سطح توجه (0-1)
    focus_target: Optional[str] = None  # هدف تمرکز
    cognitive_load: float = 0.0  # بار شناختی (0-1)
    awareness_level: float = 0.7  # سطح آگاهی
    timestamp: datetime = field(default_factory=datetime.now)
    active_thoughts: List[str] = field(default_factory=list)


class CognitiveCore:
    """
    هسته شناختی - مرکز پردازش اطلاعات و تصمیم‌گیری
    
    این کلاس شبیه به کورتکس پره‌فرونتال در مغز انسان عمل می‌کند
    و مسئول هماهنگی تمام فرآیندهای شناختی است
    """
    
    def __init__(self):
        self.state = CognitiveState()
        self.working_memory = []  # حافظه کاری
        self.attention_filter = {}  # فیلتر توجه
        self.processing_queue = asyncio.Queue()
        self.is_active = False
        
        logger.info("🧠 Cognitive Core initialized")
    
    async def start(self):
        """شروع فعالیت هسته شناختی"""
        self.is_active = True
        logger.info("✨ Cognitive Core activated")
        asyncio.create_task(self._cognitive_loop())
    
    async def stop(self):
        """توقف فعالیت هسته شناختی"""
        self.is_active = False
        logger.info("💤 Cognitive Core deactivated")
    
    async def _cognitive_loop(self):
        """حلقه اصلی پردازش شناختی"""
        while self.is_active:
            try:
                # پردازش اطلاعات در صف
                if not self.processing_queue.empty():
                    task = await self.processing_queue.get()
                    await self._process_cognitive_task(task)
                
                # به‌روزرسانی وضعیت شناختی
                await self._update_cognitive_state()
                
                await asyncio.sleep(0.1)  # چرخه 100ms
                
            except Exception as e:
                logger.error(f"Error in cognitive loop: {e}")
    
    async def _process_cognitive_task(self, task: Dict[str, Any]):
        """پردازش یک وظیفه شناختی"""
        task_type = task.get('type')
        data = task.get('data')
        
        logger.debug(f"Processing cognitive task: {task_type}")
        
        # شبیه‌سازی زمان پردازش بر اساس پیچیدگی
        complexity = task.get('complexity', 0.5)
        processing_time = complexity * 0.5
        await asyncio.sleep(processing_time)
        
        # افزودن به حافظه کاری
        if len(self.working_memory) > 7:  # محدودیت حافظه کاری (Miller's Law)
            self.working_memory.pop(0)
        
        self.working_memory.append({
            'task': task_type,
            'timestamp': datetime.now(),
            'data': data
        })
    
    async def _update_cognitive_state(self):
        """به‌روزرسانی وضعیت شناختی"""
        # محاسبه بار شناختی بر اساس حافظه کاری
        self.state.cognitive_load = len(self.working_memory) / 7.0
        
        # تنظیم سطح توجه بر اساس بار شناختی
        if self.state.cognitive_load > 0.8:
            self.state.attention_level = max(0.3, self.state.attention_level - 0.1)
        else:
            self.state.attention_level = min(1.0, self.state.attention_level + 0.05)
        
        self.state.timestamp = datetime.now()
    
    async def process_input(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        پردازش ورودی جدید
        
        Args:
            input_data: داده‌های ورودی
            
        Returns:
            نتیجه پردازش
        """
        # فیلتر توجه - آیا این ورودی قابل توجه است؟
        if not self._is_worthy_of_attention(input_data):
            logger.debug("Input filtered out by attention system")
            return {'status': 'filtered', 'reason': 'low_priority'}
        
        # افزودن به صف پردازش
        await self.processing_queue.put({
            'type': 'input_processing',
            'data': input_data,
            'complexity': input_data.get('complexity', 0.5),
            'timestamp': datetime.now()
        })
        
        return {
            'status': 'queued',
            'cognitive_load': self.state.cognitive_load,
            'attention_level': self.state.attention_level
        }
    
    def _is_worthy_of_attention(self, input_data: Dict[str, Any]) -> bool:
        """
        تعیین اینکه آیا ورودی قابل توجه است
        (شبیه به سیستم فیلتر توجه در مغز)
        """
        priority = input_data.get('priority', 0.5)
        novelty = input_data.get('novelty', 0.5)
        relevance = input_data.get('relevance', 0.5)
        
        # ترکیب وزن‌دار معیارها
        attention_score = (priority * 0.4 + novelty * 0.3 + relevance * 0.3)
        
        # آستانه توجه پویا بر اساس بار شناختی
        threshold = 0.3 + (self.state.cognitive_load * 0.3)
        
        return attention_score > threshold
    
    def get_state(self) -> CognitiveState:
        """دریافت وضعیت فعلی شناختی"""
        return self.state
    
    async def set_focus(self, target: str, duration: float = 5.0):
        """
        تنظیم تمرکز روی یک هدف خاص
        
        Args:
            target: هدف تمرکز
            duration: مدت زمان تمرکز (ثانیه)
        """
        self.state.focus_target = target
        self.state.attention_level = 0.9
        logger.info(f"🎯 Focus set on: {target}")
        
        # پس از مدت مشخص، تمرکز را آزاد کن
        await asyncio.sleep(duration)
        if self.state.focus_target == target:
            self.state.focus_target = None
            logger.info(f"🔓 Focus released from: {target}")
    
    def get_working_memory(self) -> List[Dict[str, Any]]:
        """دریافت محتویات حافظه کاری"""
        return self.working_memory.copy()
    
    async def think(self, thought: str):
        """افزودن یک فکر به جریان آگاهی"""
        if len(self.state.active_thoughts) > 10:
            self.state.active_thoughts.pop(0)
        
        self.state.active_thoughts.append(thought)
        logger.debug(f"💭 Thought: {thought}")
