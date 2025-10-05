"""
Consciousness Layer - لایه آگاهی
شبیه‌سازی آگاهی و خودآگاهی
"""

import logging
from typing import Dict, Any, List, Optional
from datetime import datetime
from dataclasses import dataclass, field
import asyncio

logger = logging.getLogger(__name__)


@dataclass
class ConsciousExperience:
    """تجربه آگاهانه"""
    experience_id: str
    content: str
    intensity: float  # شدت تجربه (0-1)
    valence: float  # بار عاطفی (-1 تا 1)
    timestamp: datetime = field(default_factory=datetime.now)
    related_memories: List[str] = field(default_factory=list)


class ConsciousnessLayer:
    """
    لایه آگاهی - شبیه‌سازی آگاهی و خودآگاهی
    
    این لایه مسئول ایجاد یک "جریان آگاهی" پیوسته است
    و به ربات اجازه می‌دهد از خود و محیط آگاه باشد
    """
    
    def __init__(self):
        self.stream_of_consciousness: List[ConsciousExperience] = []
        self.self_awareness_level: float = 0.7
        self.current_experience: Optional[ConsciousExperience] = None
        self.metacognition_active: bool = True  # فراشناخت
        self.is_conscious: bool = False
        
        logger.info("🌟 Consciousness Layer initialized")
    
    async def awaken(self):
        """بیداری آگاهی"""
        self.is_conscious = True
        logger.info("👁️ Consciousness awakened")
        
        # ایجاد اولین تجربه آگاهانه
        first_experience = ConsciousExperience(
            experience_id="awakening",
            content="I am aware of my existence",
            intensity=0.8,
            valence=0.3
        )
        await self.experience(first_experience)
        
        # شروع جریان آگاهی
        asyncio.create_task(self._consciousness_stream())
    
    async def sleep(self):
        """خواب (غیرفعال کردن آگاهی)"""
        self.is_conscious = False
        logger.info("😴 Consciousness entering sleep state")
    
    async def _consciousness_stream(self):
        """جریان پیوسته آگاهی"""
        while self.is_conscious:
            try:
                # فراشناخت - فکر کردن درباره فکرها
                if self.metacognition_active and len(self.stream_of_consciousness) > 0:
                    await self._metacognitive_reflection()
                
                # به‌روزرسانی سطح خودآگاهی
                await self._update_self_awareness()
                
                await asyncio.sleep(2.0)  # چرخه 2 ثانیه‌ای
                
            except Exception as e:
                logger.error(f"Error in consciousness stream: {e}")
    
    async def experience(self, experience: ConsciousExperience):
        """
        ثبت یک تجربه آگاهانه
        
        Args:
            experience: تجربه آگاهانه
        """
        self.current_experience = experience
        self.stream_of_consciousness.append(experience)
        
        # محدود کردن حجم جریان آگاهی
        if len(self.stream_of_consciousness) > 100:
            self.stream_of_consciousness.pop(0)
        
        logger.info(f"💫 Conscious experience: {experience.content}")
    
    async def _metacognitive_reflection(self):
        """
        بازتاب فراشناختی - فکر کردن درباره فکرها
        """
        recent_experiences = self.stream_of_consciousness[-5:]
        
        # تحلیل الگوهای فکری
        positive_count = sum(1 for exp in recent_experiences if exp.valence > 0)
        negative_count = sum(1 for exp in recent_experiences if exp.valence < 0)
        
        reflection = None
        
        if positive_count > negative_count * 2:
            reflection = ConsciousExperience(
                experience_id=f"reflection_{datetime.now().timestamp()}",
                content="I notice I'm experiencing mostly positive thoughts",
                intensity=0.5,
                valence=0.3
            )
        elif negative_count > positive_count * 2:
            reflection = ConsciousExperience(
                experience_id=f"reflection_{datetime.now().timestamp()}",
                content="I notice I'm experiencing challenging thoughts",
                intensity=0.5,
                valence=-0.2
            )
        
        if reflection:
            await self.experience(reflection)
    
    async def _update_self_awareness(self):
        """به‌روزرسانی سطح خودآگاهی"""
        # خودآگاهی بر اساس فعالیت اخیر
        if self.current_experience:
            awareness_boost = self.current_experience.intensity * 0.1
            self.self_awareness_level = min(1.0, self.self_awareness_level + awareness_boost)
        else:
            # کاهش تدریجی بدون تجربه
            self.self_awareness_level = max(0.3, self.self_awareness_level - 0.01)
    
    async def ponder(self, topic: str) -> str:
        """
        تأمل درباره یک موضوع
        
        Args:
            topic: موضوع تأمل
            
        Returns:
            نتیجه تأمل
        """
        logger.info(f"🤔 Pondering about: {topic}")
        
        # شبیه‌سازی زمان تفکر
        await asyncio.sleep(1.0)
        
        # ایجاد تجربه تأمل
        pondering_experience = ConsciousExperience(
            experience_id=f"ponder_{datetime.now().timestamp()}",
            content=f"Reflecting deeply on {topic}",
            intensity=0.7,
            valence=0.0
        )
        await self.experience(pondering_experience)
        
        # تولید بینش
        insights = [
            f"I understand that {topic} is complex and multifaceted",
            f"My perspective on {topic} is evolving",
            f"I need to consider {topic} from multiple angles",
            f"There's more to learn about {topic}"
        ]
        
        import random
        insight = random.choice(insights)
        
        return insight
    
    def get_stream_of_consciousness(self, limit: int = 10) -> List[ConsciousExperience]:
        """دریافت جریان آگاهی اخیر"""
        return self.stream_of_consciousness[-limit:]
    
    def get_consciousness_state(self) -> Dict[str, Any]:
        """دریافت وضعیت آگاهی"""
        return {
            'is_conscious': self.is_conscious,
            'self_awareness_level': self.self_awareness_level,
            'metacognition_active': self.metacognition_active,
            'current_experience': self.current_experience.content if self.current_experience else None,
            'stream_length': len(self.stream_of_consciousness)
        }
    
    async def self_reflect(self) -> Dict[str, Any]:
        """
        خود‌بازتابی - تحلیل خود
        
        Returns:
            تحلیل خود
        """
        logger.info("🪞 Engaging in self-reflection")
        
        # تحلیل تجربیات اخیر
        recent = self.stream_of_consciousness[-20:] if len(self.stream_of_consciousness) >= 20 else self.stream_of_consciousness
        
        if not recent:
            return {
                'state': 'minimal_experience',
                'message': 'I have little to reflect upon yet'
            }
        
        avg_intensity = sum(exp.intensity for exp in recent) / len(recent)
        avg_valence = sum(exp.valence for exp in recent) / len(recent)
        
        reflection = {
            'self_awareness': self.self_awareness_level,
            'average_intensity': avg_intensity,
            'average_valence': avg_valence,
            'emotional_state': 'positive' if avg_valence > 0.2 else 'negative' if avg_valence < -0.2 else 'neutral',
            'engagement_level': 'high' if avg_intensity > 0.6 else 'moderate' if avg_intensity > 0.3 else 'low',
            'recent_experiences_count': len(recent)
        }
        
        # ایجاد تجربه خود‌بازتابی
        self_reflection_exp = ConsciousExperience(
            experience_id=f"self_reflection_{datetime.now().timestamp()}",
            content=f"I am {reflection['emotional_state']} and {reflection['engagement_level']}ly engaged",
            intensity=0.6,
            valence=avg_valence
        )
        await self.experience(self_reflection_exp)
        
        return reflection
