"""
System Coordinator
Manages communication between different AI subsystems
"""

import numpy as np
from typing import Any, Dict, List, Optional
from enum import Enum


class ProcessingMode(Enum):
    """Processing modes for different types of tasks"""
    CLASSICAL = "classical"
    QUANTUM = "quantum"
    NEURAL = "neural"
    BRAIN = "brain"
    HYBRID = "hybrid"
    AGENT = "agent"


class SystemCoordinator:
    """Coordinates between different AI systems"""
    
    def __init__(self):
        self.processing_mode = ProcessingMode.HYBRID
        self.system_states = {
            'brain': 'ready',
            'quantum': 'ready',
            'neural': 'ready',
            'agent': 'ready'
        }
        
        # Task routing table
        self.task_routing = {
            'pattern_recognition': ['neural', 'brain'],
            'optimization': ['quantum', 'agent'],
            'decision_making': ['agent', 'brain'],
            'learning': ['neural', 'brain', 'agent'],
            'prediction': ['neural', 'brain'],
            'search': ['quantum', 'agent'],
            'memory': ['brain'],
            'reasoning': ['agent', 'brain']
        }
        
        # Performance tracking
        self.performance_log: List[Dict[str, Any]] = []
    
    def route_task(self, task: Dict[str, Any]) -> List[str]:
        """Route task to appropriate systems"""
        task_type = task.get('type', 'general')
        
        # Check routing table
        if task_type in self.task_routing:
            systems = self.task_routing[task_type]
        else:
            # Default: use all systems
            systems = ['brain', 'neural', 'agent']
        
        # Filter by available systems
        available_systems = [s for s in systems if self.system_states.get(s) == 'ready']
        
        return available_systems if available_systems else ['brain']
    
    def coordinate_processing(self, task: Dict[str, Any], 
                            system_results: Dict[str, Any]) -> Dict[str, Any]:
        """Coordinate and merge results from multiple systems"""
        
        # Weight different systems based on task type
        weights = self._compute_system_weights(task, system_results)
        
        # Merge results
        merged_result = self._merge_results(system_results, weights)
        
        # Log performance
        self.performance_log.append({
            'task': task,
            'systems_used': list(system_results.keys()),
            'weights': weights,
            'result': merged_result
        })
        
        return merged_result
    
    def _compute_system_weights(self, task: Dict[str, Any], 
                                system_results: Dict[str, Any]) -> Dict[str, float]:
        """Compute weights for different system contributions"""
        weights = {}
        task_type = task.get('type', 'general')
        
        for system_name in system_results.keys():
            # Base weight from routing priority
            if task_type in self.task_routing:
                priority_list = self.task_routing[task_type]
                if system_name in priority_list:
                    base_weight = 1.0 / (priority_list.index(system_name) + 1)
                else:
                    base_weight = 0.5
            else:
                base_weight = 0.5
            
            # Adjust based on confidence if available
            result = system_results[system_name]
            if isinstance(result, dict) and 'confidence' in result:
                confidence = result['confidence']
                weight = base_weight * confidence
            else:
                weight = base_weight
            
            weights[system_name] = weight
        
        # Normalize weights
        total_weight = sum(weights.values())
        if total_weight > 0:
            weights = {k: v / total_weight for k, v in weights.items()}
        
        return weights
    
    def _merge_results(self, system_results: Dict[str, Any], 
                      weights: Dict[str, float]) -> Dict[str, Any]:
        """Merge results from different systems"""
        merged = {
            'systems': list(system_results.keys()),
            'weights': weights,
            'combined_confidence': sum(
                weights.get(k, 0) * v.get('confidence', 0.5)
                for k, v in system_results.items()
                if isinstance(v, dict)
            )
        }
        
        # If all systems agree, high confidence
        if len(set(str(v) for v in system_results.values())) == 1:
            merged['consensus'] = True
            merged['combined_confidence'] = min(1.0, merged['combined_confidence'] * 1.5)
        else:
            merged['consensus'] = False
        
        # Extract primary result (highest weighted)
        if weights:
            primary_system = max(weights, key=weights.get)
            merged['primary_result'] = system_results[primary_system]
            merged['primary_system'] = primary_system
        
        # Include all system results
        merged['all_results'] = system_results
        
        return merged
    
    def optimize_routing(self, task_history: List[Dict[str, Any]]):
        """Optimize task routing based on historical performance"""
        # Analyze which systems performed best for which tasks
        system_performance = {}
        
        for entry in self.performance_log[-100:]:  # Last 100 tasks
            task_type = entry['task'].get('type', 'general')
            
            if task_type not in system_performance:
                system_performance[task_type] = {}
            
            for system, weight in entry['weights'].items():
                if system not in system_performance[task_type]:
                    system_performance[task_type][system] = []
                system_performance[task_type][system].append(weight)
        
        # Update routing table based on average performance
        for task_type, systems in system_performance.items():
            # Sort systems by average weight
            sorted_systems = sorted(
                systems.items(),
                key=lambda x: np.mean(x[1]),
                reverse=True
            )
            
            # Update routing
            self.task_routing[task_type] = [s[0] for s in sorted_systems]
    
    def set_processing_mode(self, mode: ProcessingMode):
        """Set processing mode"""
        self.processing_mode = mode
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get status of all systems"""
        return {
            'processing_mode': self.processing_mode.value,
            'system_states': self.system_states,
            'tasks_processed': len(self.performance_log),
            'routing_table': self.task_routing
        }
    
    def quantum_advantage_analysis(self, task: Dict[str, Any]) -> bool:
        """Determine if quantum processing would provide advantage"""
        task_type = task.get('type', 'general')
        complexity = len(str(task))
        
        # Quantum advantage for certain task types and complexity
        quantum_friendly_tasks = ['optimization', 'search', 'simulation']
        
        if task_type in quantum_friendly_tasks and complexity > 50:
            return True
        
        return False
    
    def neural_vs_brain_decision(self, task: Dict[str, Any]) -> str:
        """Decide whether to use neural network or brain simulation"""
        task_type = task.get('type', 'general')
        
        # Neural network: good for pattern recognition, prediction
        neural_tasks = ['pattern_recognition', 'prediction', 'classification']
        
        # Brain simulation: good for memory, reasoning, complex cognition
        brain_tasks = ['memory', 'reasoning', 'decision_making']
        
        if task_type in neural_tasks:
            return 'neural'
        elif task_type in brain_tasks:
            return 'brain'
        else:
            return 'both'
