"""
Integration Layer
Connects brain simulation, quantum, neural, and agent systems
"""

from .unified_system import UnifiedAISystem
from .coordinator import SystemCoordinator

__all__ = ['UnifiedAISystem', 'SystemCoordinator']
