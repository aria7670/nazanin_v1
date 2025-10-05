"""
Short-Term Memory - حافظه کوتاه‌مدت
مشابه حافظه کاری در مغز انسان
"""

import logging
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from collections import deque

logger = logging.getLogger(__name__)


@dataclass
class MemoryItem:
    """یک مورد حافظه"""
    item_id: str
    content: Any
    importance: float  # اهمیت (0-1)
    timestamp: datetime = field(default_factory=datetime.now)
    access_count: int = 0
    last_accessed: datetime = field(default_factory=datetime.now)
    emotional_weight: float = 0.0  # بار عاطفی


class ShortTermMemory:
    """
    حافظه کوتاه‌مدت - ذخیره موقت اطلاعات
    
    مانند حافظه کاری در مغز، ظرفیت محدود دارد (7±2 مورد)
    و اطلاعات به سرعت فراموش می‌شوند
    """
    
    def __init__(self, capacity: int = 7, retention_time: int = 300):
        """
        Args:
            capacity: ظرفیت حافظه (تعداد موارد)
            retention_time: زمان نگهداری (ثانیه)
        """
        self.capacity = capacity
        self.retention_time = timedelta(seconds=retention_time)
        self.memory: deque = deque(maxlen=capacity)
        self.items: Dict[str, MemoryItem] = {}
        
        logger.info(f"🧠 Short-term memory initialized (capacity: {capacity})")
    
    def store(self, item_id: str, content: Any, importance: float = 0.5, 
              emotional_weight: float = 0.0) -> bool:
        """
        ذخیره یک مورد در حافظه کوتاه‌مدت
        
        Args:
            item_id: شناسه مورد
            content: محتوا
            importance: اهمیت (0-1)
            emotional_weight: بار عاطفی (-1 تا 1)
            
        Returns:
            موفقیت ذخیره
        """
        # بررسی فضای خالی
        if len(self.memory) >= self.capacity:
            # حذف کم‌اهمیت‌ترین مورد
            self._evict_least_important()
        
        # ایجاد مورد جدید
        memory_item = MemoryItem(
            item_id=item_id,
            content=content,
            importance=importance,
            emotional_weight=emotional_weight
        )
        
        self.memory.append(item_id)
        self.items[item_id] = memory_item
        
        logger.debug(f"📝 Stored in STM: {item_id}")
        return True
    
    def recall(self, item_id: str) -> Optional[Any]:
        """
        بازیابی یک مورد از حافظه
        
        Args:
            item_id: شناسه مورد
            
        Returns:
            محتوای مورد یا None
        """
        if item_id not in self.items:
            logger.debug(f"❌ Failed to recall: {item_id}")
            return None
        
        item = self.items[item_id]
        
        # بررسی انقضا
        if datetime.now() - item.timestamp > self.retention_time:
            self._forget(item_id)
            return None
        
        # به‌روزرسانی دسترسی
        item.access_count += 1
        item.last_accessed = datetime.now()
        
        logger.debug(f"✅ Recalled from STM: {item_id}")
        return item.content
    
    def _evict_least_important(self):
        """حذف کم‌اهمیت‌ترین مورد"""
        if not self.items:
            return
        
        # یافتن کم‌اهمیت‌ترین مورد
        least_important = min(
            self.items.items(),
            key=lambda x: x[1].importance * (1 + x[1].access_count * 0.1)
        )
        
        self._forget(least_important[0])
        logger.debug(f"🗑️ Evicted from STM: {least_important[0]}")
    
    def _forget(self, item_id: str):
        """فراموش کردن یک مورد"""
        if item_id in self.items:
            del self.items[item_id]
        
        if item_id in self.memory:
            self.memory.remove(item_id)
    
    def cleanup_expired(self):
        """پاکسازی موارد منقضی شده"""
        now = datetime.now()
        expired = []
        
        for item_id, item in self.items.items():
            if now - item.timestamp > self.retention_time:
                expired.append(item_id)
        
        for item_id in expired:
            self._forget(item_id)
        
        if expired:
            logger.info(f"🧹 Cleaned up {len(expired)} expired items from STM")
    
    def get_all_items(self) -> List[MemoryItem]:
        """دریافت تمام موارد حافظه"""
        return list(self.items.values())
    
    def get_important_items(self, threshold: float = 0.7) -> List[MemoryItem]:
        """
        دریافت موارد مهم
        
        Args:
            threshold: آستانه اهمیت
            
        Returns:
            لیست موارد مهم
        """
        return [item for item in self.items.values() if item.importance >= threshold]
    
    def get_stats(self) -> Dict[str, Any]:
        """دریافت آمار حافظه"""
        if not self.items:
            return {
                'count': 0,
                'capacity': self.capacity,
                'usage_percent': 0.0
            }
        
        return {
            'count': len(self.items),
            'capacity': self.capacity,
            'usage_percent': (len(self.items) / self.capacity) * 100,
            'average_importance': sum(item.importance for item in self.items.values()) / len(self.items),
            'most_accessed': max(self.items.values(), key=lambda x: x.access_count).item_id
        }
    
    def clear(self):
        """پاکسازی کامل حافظه"""
        self.memory.clear()
        self.items.clear()
        logger.info("🧹 Short-term memory cleared")
