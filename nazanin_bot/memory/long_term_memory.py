"""
Long-Term Memory - حافظه بلندمدت
ذخیره‌سازی دائمی خاطرات و دانش
"""

import logging
import json
from typing import Dict, Any, List, Optional
from datetime import datetime
from dataclasses import dataclass, field, asdict
from pathlib import Path
import sqlite3
from contextlib import contextmanager

logger = logging.getLogger(__name__)


@dataclass
class LongTermMemoryItem:
    """یک خاطره بلندمدت"""
    memory_id: str
    content: Dict[str, Any]
    category: str  # دسته‌بندی (episodic, semantic, procedural)
    importance: float
    consolidation_level: float = 0.0  # میزان تثبیت (0-1)
    created_at: datetime = field(default_factory=datetime.now)
    last_accessed: datetime = field(default_factory=datetime.now)
    access_count: int = 0
    emotional_tags: List[str] = field(default_factory=list)
    associations: List[str] = field(default_factory=list)  # ارتباط با خاطرات دیگر


class LongTermMemory:
    """
    حافظه بلندمدت - ذخیره دائمی اطلاعات
    
    شامل سه نوع حافظه:
    - Episodic: خاطرات رویدادها
    - Semantic: دانش مفهومی
    - Procedural: مهارت‌ها و روش‌ها
    """
    
    def __init__(self, storage_path: str = "./data/ltm.db"):
        """
        Args:
            storage_path: مسیر ذخیره‌سازی پایگاه داده
        """
        self.storage_path = Path(storage_path)
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        
        # ایجاد پایگاه داده
        self._init_database()
        
        logger.info(f"🗄️ Long-term memory initialized at {storage_path}")
    
    def _init_database(self):
        """ایجاد جداول پایگاه داده"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            # جدول خاطرات
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS memories (
                    memory_id TEXT PRIMARY KEY,
                    content TEXT NOT NULL,
                    category TEXT NOT NULL,
                    importance REAL NOT NULL,
                    consolidation_level REAL DEFAULT 0.0,
                    created_at TEXT NOT NULL,
                    last_accessed TEXT NOT NULL,
                    access_count INTEGER DEFAULT 0,
                    emotional_tags TEXT,
                    associations TEXT
                )
            """)
            
            # ایندکس برای جستجوی سریع‌تر
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_category ON memories(category)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_importance ON memories(importance)
            """)
            
            conn.commit()
    
    @contextmanager
    def _get_connection(self):
        """مدیریت اتصال به پایگاه داده"""
        conn = sqlite3.connect(str(self.storage_path))
        try:
            yield conn
        finally:
            conn.close()
    
    def store(self, memory_id: str, content: Dict[str, Any], category: str,
              importance: float, emotional_tags: List[str] = None) -> bool:
        """
        ذخیره یک خاطره در حافظه بلندمدت
        
        Args:
            memory_id: شناسه خاطره
            content: محتوا
            category: دسته‌بندی (episodic/semantic/procedural)
            importance: اهمیت (0-1)
            emotional_tags: برچسب‌های عاطفی
            
        Returns:
            موفقیت ذخیره
        """
        try:
            memory = LongTermMemoryItem(
                memory_id=memory_id,
                content=content,
                category=category,
                importance=importance,
                emotional_tags=emotional_tags or []
            )
            
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT OR REPLACE INTO memories 
                    (memory_id, content, category, importance, consolidation_level,
                     created_at, last_accessed, access_count, emotional_tags, associations)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    memory.memory_id,
                    json.dumps(memory.content),
                    memory.category,
                    memory.importance,
                    memory.consolidation_level,
                    memory.created_at.isoformat(),
                    memory.last_accessed.isoformat(),
                    memory.access_count,
                    json.dumps(memory.emotional_tags),
                    json.dumps(memory.associations)
                ))
                conn.commit()
            
            logger.info(f"💾 Stored in LTM: {memory_id} ({category})")
            return True
            
        except Exception as e:
            logger.error(f"Failed to store memory: {e}")
            return False
    
    def recall(self, memory_id: str) -> Optional[LongTermMemoryItem]:
        """
        بازیابی یک خاطره
        
        Args:
            memory_id: شناسه خاطره
            
        Returns:
            خاطره یا None
        """
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT * FROM memories WHERE memory_id = ?
                """, (memory_id,))
                
                row = cursor.fetchone()
                if not row:
                    return None
                
                # به‌روزرسانی آمار دسترسی
                cursor.execute("""
                    UPDATE memories 
                    SET access_count = access_count + 1,
                        last_accessed = ?
                    WHERE memory_id = ?
                """, (datetime.now().isoformat(), memory_id))
                conn.commit()
                
                # تبدیل به شیء
                memory = LongTermMemoryItem(
                    memory_id=row[0],
                    content=json.loads(row[1]),
                    category=row[2],
                    importance=row[3],
                    consolidation_level=row[4],
                    created_at=datetime.fromisoformat(row[5]),
                    last_accessed=datetime.fromisoformat(row[6]),
                    access_count=row[7] + 1,
                    emotional_tags=json.loads(row[8]) if row[8] else [],
                    associations=json.loads(row[9]) if row[9] else []
                )
                
                logger.debug(f"✅ Recalled from LTM: {memory_id}")
                return memory
                
        except Exception as e:
            logger.error(f"Failed to recall memory: {e}")
            return None
    
    def search(self, category: Optional[str] = None, 
               min_importance: float = 0.0,
               limit: int = 10) -> List[LongTermMemoryItem]:
        """
        جستجوی خاطرات
        
        Args:
            category: فیلتر دسته‌بندی
            min_importance: حداقل اهمیت
            limit: حداکثر تعداد نتایج
            
        Returns:
            لیست خاطرات
        """
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                
                query = "SELECT * FROM memories WHERE importance >= ?"
                params = [min_importance]
                
                if category:
                    query += " AND category = ?"
                    params.append(category)
                
                query += " ORDER BY importance DESC, access_count DESC LIMIT ?"
                params.append(limit)
                
                cursor.execute(query, params)
                rows = cursor.fetchall()
                
                memories = []
                for row in rows:
                    memory = LongTermMemoryItem(
                        memory_id=row[0],
                        content=json.loads(row[1]),
                        category=row[2],
                        importance=row[3],
                        consolidation_level=row[4],
                        created_at=datetime.fromisoformat(row[5]),
                        last_accessed=datetime.fromisoformat(row[6]),
                        access_count=row[7],
                        emotional_tags=json.loads(row[8]) if row[8] else [],
                        associations=json.loads(row[9]) if row[9] else []
                    )
                    memories.append(memory)
                
                return memories
                
        except Exception as e:
            logger.error(f"Failed to search memories: {e}")
            return []
    
    def consolidate(self, memory_id: str, consolidation_increase: float = 0.1) -> bool:
        """
        تثبیت یک خاطره (افزایش سطح تثبیت)
        
        Args:
            memory_id: شناسه خاطره
            consolidation_increase: میزان افزایش تثبیت
            
        Returns:
            موفقیت
        """
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE memories 
                    SET consolidation_level = MIN(1.0, consolidation_level + ?)
                    WHERE memory_id = ?
                """, (consolidation_increase, memory_id))
                conn.commit()
                
                logger.debug(f"🔒 Consolidated memory: {memory_id}")
                return True
                
        except Exception as e:
            logger.error(f"Failed to consolidate memory: {e}")
            return False
    
    def get_stats(self) -> Dict[str, Any]:
        """دریافت آمار حافظه بلندمدت"""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                
                # تعداد کل
                cursor.execute("SELECT COUNT(*) FROM memories")
                total_count = cursor.fetchone()[0]
                
                # تعداد به تفکیک دسته
                cursor.execute("""
                    SELECT category, COUNT(*) 
                    FROM memories 
                    GROUP BY category
                """)
                category_counts = dict(cursor.fetchall())
                
                # میانگین اهمیت
                cursor.execute("SELECT AVG(importance) FROM memories")
                avg_importance = cursor.fetchone()[0] or 0.0
                
                return {
                    'total_memories': total_count,
                    'by_category': category_counts,
                    'average_importance': avg_importance
                }
                
        except Exception as e:
            logger.error(f"Failed to get stats: {e}")
            return {}
    
    def forget_weak_memories(self, threshold: float = 0.2) -> int:
        """
        فراموش کردن خاطرات ضعیف
        
        Args:
            threshold: آستانه اهمیت
            
        Returns:
            تعداد خاطرات حذف شده
        """
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                
                # حذف خاطرات با اهمیت کم و تثبیت کم
                cursor.execute("""
                    DELETE FROM memories 
                    WHERE importance < ? AND consolidation_level < 0.3
                """, (threshold,))
                
                deleted_count = cursor.rowcount
                conn.commit()
                
                if deleted_count > 0:
                    logger.info(f"🧹 Forgot {deleted_count} weak memories")
                
                return deleted_count
                
        except Exception as e:
            logger.error(f"Failed to forget memories: {e}")
            return 0
