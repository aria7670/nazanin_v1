"""
Brain System - سیستم مغز مصنوعی
این ماژول شبیه‌سازی مغز انسان با لایه‌های مختلف شناختی را پیاده‌سازی می‌کند
"""

from .cognitive_core import CognitiveCore
from .neural_processor import NeuralProcessor
from .consciousness import ConsciousnessLayer

__all__ = ['CognitiveCore', 'NeuralProcessor', 'ConsciousnessLayer']
