"""
Memory Consolidation - تثبیت حافظه
انتقال خاطرات از حافظه کوتاه‌مدت به بلندمدت
"""

import logging
import asyncio
from typing import Dict, Any, List
from datetime import datetime

logger = logging.getLogger(__name__)


class MemoryConsolidation:
    """
    تثبیت حافظه - فرآیند انتقال از STM به LTM
    
    این کلاس شبیه به فرآیند تثبیت حافظه در خواب عمل می‌کند
    و خاطرات مهم را از حافظه کوتاه‌مدت به بلندمدت منتقل می‌کند
    """
    
    def __init__(self, short_term_memory, long_term_memory):
        """
        Args:
            short_term_memory: نمونه حافظه کوتاه‌مدت
            long_term_memory: نمونه حافظه بلندمدت
        """
        self.stm = short_term_memory
        self.ltm = long_term_memory
        self.consolidation_threshold = 0.6  # آستانه اهمیت برای تثبیت
        self.is_running = False
        
        logger.info("🔄 Memory Consolidation initialized")
    
    async def start_consolidation_loop(self):
        """شروع حلقه تثبیت حافظه (مانند خواب)"""
        self.is_running = True
        logger.info("💤 Memory consolidation process started")
        
        while self.is_running:
            try:
                await asyncio.sleep(60)  # هر 60 ثانیه
                await self.consolidate_memories()
            except Exception as e:
                logger.error(f"Error in consolidation loop: {e}")
    
    def stop_consolidation_loop(self):
        """توقف حلقه تثبیت"""
        self.is_running = False
        logger.info("⏸️ Memory consolidation process stopped")
    
    async def consolidate_memories(self) -> Dict[str, int]:
        """
        تثبیت خاطرات مهم از STM به LTM
        
        Returns:
            آمار تثبیت
        """
        logger.info("🔄 Starting memory consolidation...")
        
        # دریافت موارد مهم از حافظه کوتاه‌مدت
        important_items = self.stm.get_important_items(self.consolidation_threshold)
        
        consolidated_count = 0
        episodic_count = 0
        semantic_count = 0
        
        for item in important_items:
            # تعیین نوع خاطره
            category = self._determine_memory_category(item.content)
            
            # ذخیره در حافظه بلندمدت
            success = self.ltm.store(
                memory_id=f"consolidated_{item.item_id}",
                content={'original_content': item.content, 'context': 'consolidated'},
                category=category,
                importance=item.importance,
                emotional_tags=self._extract_emotional_tags(item)
            )
            
            if success:
                consolidated_count += 1
                if category == 'episodic':
                    episodic_count += 1
                elif category == 'semantic':
                    semantic_count += 1
                
                logger.debug(f"✅ Consolidated: {item.item_id} -> {category}")
        
        stats = {
            'total_consolidated': consolidated_count,
            'episodic': episodic_count,
            'semantic': semantic_count
        }
        
        if consolidated_count > 0:
            logger.info(f"✨ Consolidated {consolidated_count} memories "
                       f"(episodic: {episodic_count}, semantic: {semantic_count})")
        
        return stats
    
    def _determine_memory_category(self, content: Any) -> str:
        """
        تعیین دسته‌بندی خاطره
        
        Args:
            content: محتوای خاطره
            
        Returns:
            دسته‌بندی (episodic/semantic/procedural)
        """
        # منطق ساده برای تعیین نوع
        # در پیاده‌سازی واقعی، می‌تواند پیچیده‌تر باشد
        
        if isinstance(content, dict):
            if 'event' in str(content).lower() or 'happened' in str(content).lower():
                return 'episodic'  # خاطره رویداد
            elif 'how_to' in str(content).lower() or 'procedure' in str(content).lower():
                return 'procedural'  # مهارت/روش
            else:
                return 'semantic'  # دانش مفهومی
        
        return 'semantic'  # پیش‌فرض
    
    def _extract_emotional_tags(self, item) -> List[str]:
        """استخراج برچسب‌های عاطفی از مورد حافظه"""
        tags = []
        
        emotional_weight = getattr(item, 'emotional_weight', 0.0)
        
        if emotional_weight > 0.5:
            tags.append('positive')
        elif emotional_weight < -0.5:
            tags.append('negative')
        else:
            tags.append('neutral')
        
        if item.importance > 0.8:
            tags.append('significant')
        
        return tags
    
    async def replay_memories(self, count: int = 5):
        """
        بازپخش خاطرات (مانند فرآیند replay در خواب)
        
        Args:
            count: تعداد خاطرات برای بازپخش
        """
        logger.info(f"🔁 Replaying {count} memories...")
        
        # دریافت خاطرات مهم از LTM
        memories = self.ltm.search(min_importance=0.7, limit=count)
        
        for memory in memories:
            # شبیه‌سازی بازپخش
            await asyncio.sleep(0.5)
            
            # تقویت تثبیت
            self.ltm.consolidate(memory.memory_id, consolidation_increase=0.05)
            
            logger.debug(f"🔁 Replayed: {memory.memory_id}")
        
        logger.info(f"✅ Replayed {len(memories)} memories")
    
    async def sleep_consolidation(self, duration: float = 10.0):
        """
        تثبیت حافظه در حالت خواب
        
        Args:
            duration: مدت زمان خواب (ثانیه)
        """
        logger.info(f"💤 Entering sleep mode for {duration}s...")
        
        start_time = asyncio.get_event_loop().time()
        
        while asyncio.get_event_loop().time() - start_time < duration:
            # تثبیت خاطرات
            await self.consolidate_memories()
            
            # بازپخش خاطرات
            await self.replay_memories(count=3)
            
            # استراحت کوتاه
            await asyncio.sleep(2.0)
        
        logger.info("🌅 Waking up from sleep mode")
    
    def set_consolidation_threshold(self, threshold: float):
        """
        تنظیم آستانه تثبیت
        
        Args:
            threshold: آستانه اهمیت (0-1)
        """
        self.consolidation_threshold = max(0.0, min(1.0, threshold))
        logger.info(f"⚙️ Consolidation threshold set to {self.consolidation_threshold}")
