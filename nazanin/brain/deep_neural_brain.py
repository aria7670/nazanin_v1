"""
Deep Neural Brain - مغز عصبی عمیق چند لایه
Advanced multi-layered brain system simulating human brain structure

ساختار:
- 12 لایه عصبی (شبیه مغز انسان)
- 6 ناحیه تخصصی (Cortex)
- حافظه کوتاه‌مدت و بلندمدت
- یادگیری خودکار و تطبیقی
"""

import asyncio
import logging
import numpy as np
import json
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
from collections import deque
import random
import math

logger = logging.getLogger(__name__)


class NeuralLayer:
    """لایه عصبی - شبیه‌سازی یک لایه از نورون‌ها"""
    
    def __init__(self, layer_id: int, input_size: int, output_size: int, activation: str = 'relu'):
        self.layer_id = layer_id
        self.input_size = input_size
        self.output_size = output_size
        self.activation = activation
        
        # وزن‌ها و bias های لایه
        self.weights = np.random.randn(input_size, output_size) * 0.01
        self.bias = np.zeros((1, output_size))
        
        # حافظه برای یادگیری
        self.last_input = None
        self.last_output = None
        self.activation_history = deque(maxlen=1000)
        
    def activate(self, x: np.ndarray) -> np.ndarray:
        """تابع فعال‌سازی"""
        if self.activation == 'relu':
            return np.maximum(0, x)
        elif self.activation == 'sigmoid':
            return 1 / (1 + np.exp(-np.clip(x, -500, 500)))
        elif self.activation == 'tanh':
            return np.tanh(x)
        elif self.activation == 'softmax':
            exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
            return exp_x / np.sum(exp_x, axis=1, keepdims=True)
        else:
            return x
    
    def forward(self, input_data: np.ndarray) -> np.ndarray:
        """پردازش forward"""
        self.last_input = input_data
        
        # محاسبه خروجی
        z = np.dot(input_data, self.weights) + self.bias
        output = self.activate(z)
        
        self.last_output = output
        self.activation_history.append({
            'timestamp': datetime.now().isoformat(),
            'mean_activation': float(np.mean(output)),
            'max_activation': float(np.max(output))
        })
        
        return output
    
    def update_weights(self, learning_rate: float = 0.001, gradient: np.ndarray = None):
        """به‌روزرسانی وزن‌ها (یادگیری)"""
        if gradient is None:
            # Hebbian learning: neurons that fire together, wire together
            if self.last_input is not None and self.last_output is not None:
                gradient = np.dot(self.last_input.T, self.last_output)
        
        if gradient is not None:
            self.weights += learning_rate * gradient
            
    def get_stats(self) -> Dict:
        """آمار لایه"""
        return {
            'layer_id': self.layer_id,
            'input_size': self.input_size,
            'output_size': self.output_size,
            'activation': self.activation,
            'weight_mean': float(np.mean(self.weights)),
            'weight_std': float(np.std(self.weights)),
            'activations_recorded': len(self.activation_history)
        }


class BrainCortex:
    """کورتکس مغزی - ناحیه تخصصی مغز"""
    
    def __init__(self, cortex_id: str, function: str, layers: List[NeuralLayer]):
        self.cortex_id = cortex_id
        self.function = function
        self.layers = layers
        self.memory = deque(maxlen=10000)
        self.expertise_level = 0.0
        
    async def process(self, input_data: np.ndarray, context: Dict = None) -> np.ndarray:
        """پردازش اطلاعات در این کورتکس"""
        output = input_data
        
        # عبور از تمام لایه‌ها
        for layer in self.layers:
            output = layer.forward(output)
        
        # ذخیره در حافظه
        self.memory.append({
            'timestamp': datetime.now().isoformat(),
            'input_shape': input_data.shape,
            'output_shape': output.shape,
            'context': context
        })
        
        # افزایش تخصص
        self.expertise_level += 0.001
        
        return output
    
    async def learn(self, feedback: float):
        """یادگیری بر اساس بازخورد"""
        learning_rate = 0.001 * feedback
        
        for layer in self.layers:
            layer.update_weights(learning_rate)
    
    def get_stats(self) -> Dict:
        """آمار کورتکس"""
        return {
            'cortex_id': self.cortex_id,
            'function': self.function,
            'layers_count': len(self.layers),
            'memory_size': len(self.memory),
            'expertise_level': self.expertise_level,
            'layer_stats': [layer.get_stats() for layer in self.layers]
        }


class DeepNeuralBrain:
    """
    مغز عصبی عمیق - شبیه‌سازی کامل مغز انسان
    
    ساختار:
    - Prefrontal Cortex: تصمیم‌گیری و برنامه‌ریزی
    - Temporal Cortex: پردازش زبان و حافظه
    - Parietal Cortex: پردازش حسی
    - Occipital Cortex: پردازش بینایی
    - Motor Cortex: کنترل حرکت
    - Limbic System: احساسات و انگیزه
    """
    
    def __init__(self, input_size: int = 512):
        self.input_size = input_size
        self.cortexes: Dict[str, BrainCortex] = {}
        
        # حافظه کوتاه‌مدت (Working Memory)
        self.working_memory = deque(maxlen=100)
        
        # حافظه بلندمدت (Long-term Memory)
        self.long_term_memory = {}
        
        # حافظه اپیزودیک (Episodic Memory)
        self.episodic_memory = deque(maxlen=10000)
        
        # تاریخچه فکر
        self.thought_history = deque(maxlen=1000)
        
        # سطح آگاهی
        self.consciousness_level = 0.5
        self.attention_focus = None
        
        # آمار
        self.total_thoughts = 0
        self.learning_events = 0
        
        logger.info("🧠 Initializing Deep Neural Brain...")
        self._build_brain_structure()
    
    def _build_brain_structure(self):
        """ساخت ساختار مغز"""
        
        # 1. Prefrontal Cortex - تصمیم‌گیری
        prefrontal_layers = [
            NeuralLayer(1, self.input_size, 256, 'relu'),
            NeuralLayer(2, 256, 128, 'relu'),
            NeuralLayer(3, 128, 64, 'tanh')
        ]
        self.cortexes['prefrontal'] = BrainCortex(
            'prefrontal',
            'decision_making_planning',
            prefrontal_layers
        )
        
        # 2. Temporal Cortex - زبان و حافظه
        temporal_layers = [
            NeuralLayer(4, self.input_size, 256, 'relu'),
            NeuralLayer(5, 256, 128, 'relu'),
            NeuralLayer(6, 128, 64, 'sigmoid')
        ]
        self.cortexes['temporal'] = BrainCortex(
            'temporal',
            'language_memory',
            temporal_layers
        )
        
        # 3. Parietal Cortex - پردازش حسی
        parietal_layers = [
            NeuralLayer(7, self.input_size, 128, 'relu'),
            NeuralLayer(8, 128, 64, 'relu')
        ]
        self.cortexes['parietal'] = BrainCortex(
            'parietal',
            'sensory_processing',
            parietal_layers
        )
        
        # 4. Occipital Cortex - بینایی و تصویر
        occipital_layers = [
            NeuralLayer(9, self.input_size, 128, 'relu'),
            NeuralLayer(10, 128, 64, 'tanh')
        ]
        self.cortexes['occipital'] = BrainCortex(
            'occipital',
            'visual_processing',
            occipital_layers
        )
        
        # 5. Motor Cortex - کنترل عمل
        motor_layers = [
            NeuralLayer(11, self.input_size, 64, 'relu')
        ]
        self.cortexes['motor'] = BrainCortex(
            'motor',
            'action_control',
            motor_layers
        )
        
        # 6. Limbic System - احساسات
        limbic_layers = [
            NeuralLayer(12, self.input_size, 128, 'sigmoid'),
            NeuralLayer(13, 128, 64, 'tanh')
        ]
        self.cortexes['limbic'] = BrainCortex(
            'limbic',
            'emotions_motivation',
            limbic_layers
        )
        
        logger.info(f"   ✅ Built {len(self.cortexes)} cortex regions")
    
    def _encode_input(self, input_data: Any) -> np.ndarray:
        """تبدیل ورودی به بردار عصبی"""
        if isinstance(input_data, str):
            # تبدیل متن به بردار
            encoded = np.zeros(self.input_size)
            for i, char in enumerate(input_data[:self.input_size]):
                encoded[i] = ord(char) / 255.0
            return encoded.reshape(1, -1)
        elif isinstance(input_data, (list, np.ndarray)):
            arr = np.array(input_data)
            if arr.size < self.input_size:
                padded = np.zeros(self.input_size)
                padded[:arr.size] = arr.flatten()
                return padded.reshape(1, -1)
            return arr[:self.input_size].reshape(1, -1)
        else:
            # پیش‌فرض
            return np.random.randn(1, self.input_size) * 0.1
    
    async def think(self, input_data: Any, context: Dict = None) -> Dict:
        """
        فکر کردن - پردازش کامل اطلاعات در مغز
        """
        context = context or {}
        
        # کدگذاری ورودی
        encoded_input = self._encode_input(input_data)
        
        # افزایش توجه
        self.attention_focus = input_data
        
        # پردازش در تمام کورتکس‌ها (به صورت موازی)
        cortex_outputs = {}
        
        for cortex_name, cortex in self.cortexes.items():
            output = await cortex.process(encoded_input, context)
            cortex_outputs[cortex_name] = output
        
        # ترکیب خروجی‌ها (Integration)
        integrated_output = self._integrate_cortex_outputs(cortex_outputs)
        
        # تحلیل و تصمیم‌گیری
        decision = await self._make_decision(integrated_output, cortex_outputs)
        
        # ذخیره در حافظه کوتاه‌مدت
        self.working_memory.append({
            'timestamp': datetime.now().isoformat(),
            'input': str(input_data)[:200],
            'decision': decision,
            'consciousness': self.consciousness_level
        })
        
        # ذخیره در حافظه اپیزودیک
        self.episodic_memory.append({
            'timestamp': datetime.now().isoformat(),
            'type': 'thought',
            'input': str(input_data)[:200],
            'context': context,
            'decision': decision
        })
        
        # آمار
        self.total_thoughts += 1
        
        # افزایش آگاهی
        self.consciousness_level = min(1.0, self.consciousness_level + 0.001)
        
        # ذخیره فکر
        thought = {
            'timestamp': datetime.now().isoformat(),
            'input': str(input_data)[:200],
            'cortex_activations': {k: float(np.mean(v)) for k, v in cortex_outputs.items()},
            'decision': decision,
            'consciousness_level': self.consciousness_level
        }
        self.thought_history.append(thought)
        
        return {
            'thought': thought,
            'decision': decision,
            'consciousness_level': self.consciousness_level,
            'cortex_activations': cortex_outputs
        }
    
    def _integrate_cortex_outputs(self, cortex_outputs: Dict[str, np.ndarray]) -> np.ndarray:
        """ادغام خروجی کورتکس‌ها"""
        # میانگین وزن‌دار
        weights = {
            'prefrontal': 0.3,  # تصمیم مهم‌تر
            'temporal': 0.25,   # زبان مهم
            'parietal': 0.15,
            'occipital': 0.1,
            'motor': 0.1,
            'limbic': 0.1
        }
        
        integrated = None
        for cortex_name, output in cortex_outputs.items():
            weight = weights.get(cortex_name, 0.1)
            if integrated is None:
                integrated = output * weight
            else:
                # resize if needed
                if output.shape[1] != integrated.shape[1]:
                    if output.shape[1] < integrated.shape[1]:
                        padded = np.zeros_like(integrated)
                        padded[:, :output.shape[1]] = output
                        output = padded
                    else:
                        output = output[:, :integrated.shape[1]]
                integrated += output * weight
        
        return integrated
    
    async def _make_decision(self, integrated: np.ndarray, cortex_outputs: Dict) -> Dict:
        """تصمیم‌گیری بر اساس خروجی‌های مغز"""
        
        # تحلیل activation
        prefrontal_activation = float(np.mean(cortex_outputs['prefrontal']))
        limbic_activation = float(np.mean(cortex_outputs['limbic']))
        temporal_activation = float(np.mean(cortex_outputs['temporal']))
        
        # تصمیم
        decision_strength = (prefrontal_activation + temporal_activation) / 2
        emotional_influence = limbic_activation
        
        # تعیین نوع تصمیم
        if decision_strength > 0.7:
            decision_type = 'strong_confident'
        elif decision_strength > 0.4:
            decision_type = 'moderate'
        else:
            decision_type = 'weak_uncertain'
        
        # تأثیر احساسات
        if emotional_influence > 0.6:
            emotional_state = 'high_emotion'
        elif emotional_influence > 0.3:
            emotional_state = 'balanced'
        else:
            emotional_state = 'rational'
        
        return {
            'type': decision_type,
            'strength': decision_strength,
            'emotional_influence': emotional_influence,
            'emotional_state': emotional_state,
            'confidence': decision_strength * (1 - abs(0.5 - emotional_influence))
        }
    
    async def learn_from_experience(self, experience: Dict, feedback: float = 1.0):
        """
        یادگیری از تجربه
        feedback: 1.0 = خوب، -1.0 = بد
        """
        
        # یادگیری در کورتکس‌ها
        for cortex in self.cortexes.values():
            await cortex.learn(feedback)
        
        # ذخیره در حافظه بلندمدت
        experience_key = f"exp_{len(self.long_term_memory)}"
        self.long_term_memory[experience_key] = {
            'timestamp': datetime.now().isoformat(),
            'experience': experience,
            'feedback': feedback,
            'consciousness_at_time': self.consciousness_level
        }
        
        # آمار
        self.learning_events += 1
        
        logger.info(f"   🎓 Learned from experience (feedback: {feedback:.2f})")
    
    def recall_memory(self, query: str, memory_type: str = 'all') -> List[Dict]:
        """فراخوانی حافظه"""
        results = []
        
        if memory_type in ['all', 'working']:
            # جستجو در حافظه کوتاه‌مدت
            for memory in self.working_memory:
                if query.lower() in str(memory.get('input', '')).lower():
                    results.append({'type': 'working', 'data': memory})
        
        if memory_type in ['all', 'episodic']:
            # جستجو در حافظه اپیزودیک
            for memory in self.episodic_memory:
                if query.lower() in str(memory.get('input', '')).lower():
                    results.append({'type': 'episodic', 'data': memory})
        
        if memory_type in ['all', 'long_term']:
            # جستجو در حافظه بلندمدت
            for key, memory in self.long_term_memory.items():
                if query.lower() in str(memory.get('experience', '')).lower():
                    results.append({'type': 'long_term', 'key': key, 'data': memory})
        
        return results
    
    def get_brain_state(self) -> Dict:
        """وضعیت کامل مغز"""
        return {
            'consciousness_level': self.consciousness_level,
            'attention_focus': str(self.attention_focus)[:100] if self.attention_focus else None,
            'total_thoughts': self.total_thoughts,
            'learning_events': self.learning_events,
            'working_memory_size': len(self.working_memory),
            'episodic_memory_size': len(self.episodic_memory),
            'long_term_memory_size': len(self.long_term_memory),
            'cortex_stats': {name: cortex.get_stats() for name, cortex in self.cortexes.items()},
            'recent_thoughts': list(self.thought_history)[-5:] if self.thought_history else []
        }
    
    async def consolidate_memories(self):
        """
        تثبیت حافظه‌ها (شبیه خواب)
        انتقال از حافظه کوتاه‌مدت به بلندمدت
        """
        logger.info("💤 Consolidating memories (sleep-like process)...")
        
        # انتقال حافظه‌های مهم
        important_memories = [m for m in self.working_memory if m.get('consciousness', 0) > 0.7]
        
        for memory in important_memories:
            key = f"consolidated_{len(self.long_term_memory)}"
            self.long_term_memory[key] = {
                'timestamp': datetime.now().isoformat(),
                'original': memory,
                'consolidated': True
            }
        
        logger.info(f"   ✅ Consolidated {len(important_memories)} memories")
    
    def get_stats(self) -> Dict:
        """آمار کامل"""
        return {
            'brain_type': 'Deep Neural Brain',
            'input_size': self.input_size,
            'cortex_count': len(self.cortexes),
            'total_layers': sum(len(c.layers) for c in self.cortexes.values()),
            'consciousness_level': self.consciousness_level,
            'total_thoughts': self.total_thoughts,
            'learning_events': self.learning_events,
            'memory': {
                'working': len(self.working_memory),
                'episodic': len(self.episodic_memory),
                'long_term': len(self.long_term_memory)
            }
        }
