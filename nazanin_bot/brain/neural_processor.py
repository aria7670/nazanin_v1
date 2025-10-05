"""
Neural Processor - پردازشگر عصبی
شبیه‌سازی شبکه‌های عصبی مغز برای پردازش اطلاعات
"""

import logging
import numpy as np
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
import asyncio

logger = logging.getLogger(__name__)


@dataclass
class NeuralPattern:
    """الگوی عصبی"""
    pattern_id: str
    activation_level: float
    connections: Dict[str, float]  # ارتباطات با سایر الگوها
    strength: float = 1.0  # قدرت الگو
    usage_count: int = 0


class NeuralProcessor:
    """
    پردازشگر عصبی - شبیه‌سازی پردازش عصبی مغز
    
    این کلاس از مکانیزم‌های شبیه به شبکه‌های عصبی استفاده می‌کند
    برای پردازش و یادگیری الگوها
    """
    
    def __init__(self, learning_rate: float = 0.01):
        self.learning_rate = learning_rate
        self.patterns: Dict[str, NeuralPattern] = {}
        self.activation_history: List[Dict[str, float]] = []
        self.neural_state = np.zeros(100)  # حالت عصبی (100 نورون مجازی)
        
        logger.info("🧬 Neural Processor initialized")
    
    async def process(self, input_vector: np.ndarray) -> Dict[str, Any]:
        """
        پردازش یک ورودی از طریق شبکه عصبی
        
        Args:
            input_vector: بردار ورودی
            
        Returns:
            نتایج پردازش عصبی
        """
        # نرمال‌سازی ورودی
        normalized_input = self._normalize(input_vector)
        
        # فعال‌سازی نورون‌ها
        activation = await self._activate_neurons(normalized_input)
        
        # تشخیص الگو
        recognized_patterns = self._recognize_patterns(activation)
        
        # به‌روزرسانی تاریخچه
        self.activation_history.append({
            'activation': activation.tolist(),
            'patterns': recognized_patterns
        })
        
        if len(self.activation_history) > 1000:
            self.activation_history.pop(0)
        
        return {
            'activation': activation,
            'patterns': recognized_patterns,
            'neural_state': self.neural_state.copy()
        }
    
    async def _activate_neurons(self, input_vector: np.ndarray) -> np.ndarray:
        """فعال‌سازی نورون‌ها با استفاده از تابع فعال‌سازی"""
        # شبیه‌سازی تأخیر عصبی
        await asyncio.sleep(0.01)
        
        # ترکیب ورودی با حالت فعلی
        combined = 0.7 * input_vector + 0.3 * self.neural_state[:len(input_vector)]
        
        # تابع فعال‌سازی (sigmoid)
        activation = 1 / (1 + np.exp(-combined))
        
        # به‌روزرسانی حالت عصبی
        self.neural_state[:len(activation)] = activation
        
        return activation
    
    def _normalize(self, vector: np.ndarray) -> np.ndarray:
        """نرمال‌سازی بردار"""
        norm = np.linalg.norm(vector)
        if norm > 0:
            return vector / norm
        return vector
    
    def _recognize_patterns(self, activation: np.ndarray) -> List[str]:
        """تشخیص الگوهای فعال شده"""
        recognized = []
        
        for pattern_id, pattern in self.patterns.items():
            # محاسبه شباهت
            similarity = self._calculate_similarity(activation, pattern)
            
            if similarity > 0.7:  # آستانه تشخیص
                recognized.append(pattern_id)
                pattern.usage_count += 1
                pattern.activation_level = similarity
        
        return recognized
    
    def _calculate_similarity(self, activation: np.ndarray, pattern: NeuralPattern) -> float:
        """محاسبه شباهت بین فعال‌سازی و الگو"""
        # برای سادگی، از یک مقدار تصادفی استفاده می‌کنیم
        # در پیاده‌سازی واقعی، این باید بر اساس الگوی ذخیره شده باشد
        return np.random.random() * pattern.strength
    
    async def learn_pattern(self, pattern_id: str, data: np.ndarray):
        """
        یادگیری یک الگوی جدید
        
        Args:
            pattern_id: شناسه الگو
            data: داده‌های الگو
        """
        if pattern_id in self.patterns:
            # تقویت الگوی موجود
            existing = self.patterns[pattern_id]
            existing.strength = min(1.0, existing.strength + self.learning_rate)
            logger.debug(f"Pattern '{pattern_id}' reinforced")
        else:
            # ایجاد الگوی جدید
            new_pattern = NeuralPattern(
                pattern_id=pattern_id,
                activation_level=0.0,
                connections={},
                strength=0.5
            )
            self.patterns[pattern_id] = new_pattern
            logger.info(f"✨ New pattern learned: '{pattern_id}'")
    
    def forget_weak_patterns(self, threshold: float = 0.1):
        """فراموشی الگوهای ضعیف (شبیه فرآیند pruning در مغز)"""
        to_remove = []
        
        for pattern_id, pattern in self.patterns.items():
            if pattern.strength < threshold and pattern.usage_count < 3:
                to_remove.append(pattern_id)
        
        for pattern_id in to_remove:
            del self.patterns[pattern_id]
            logger.debug(f"Pattern '{pattern_id}' forgotten")
        
        if to_remove:
            logger.info(f"🧹 Pruned {len(to_remove)} weak patterns")
    
    def get_dominant_patterns(self, top_n: int = 5) -> List[str]:
        """دریافت الگوهای غالب"""
        sorted_patterns = sorted(
            self.patterns.items(),
            key=lambda x: x[1].strength * x[1].usage_count,
            reverse=True
        )
        
        return [p[0] for p in sorted_patterns[:top_n]]
    
    def get_neural_stats(self) -> Dict[str, Any]:
        """دریافت آمار عصبی"""
        return {
            'total_patterns': len(self.patterns),
            'average_activation': float(np.mean(self.neural_state)),
            'max_activation': float(np.max(self.neural_state)),
            'dominant_patterns': self.get_dominant_patterns(3)
        }
