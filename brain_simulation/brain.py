"""
Main brain simulation system
"""

import numpy as np
from typing import List, Dict, Any
from .neuron import Neuron
from .memory import MemorySystem


class BrainSimulator:
    """Advanced brain simulation with neural networks and memory"""
    
    def __init__(self, neuron_count: int = 1000, learning_rate: float = 0.01):
        self.neuron_count = neuron_count
        self.learning_rate = learning_rate
        
        # Create neurons
        self.neurons: Dict[int, Neuron] = {}
        for i in range(neuron_count):
            self.neurons[i] = Neuron(i, threshold=np.random.uniform(0.3, 0.7))
        
        # Create random connections (simulating synapses)
        self._initialize_connections()
        
        # Memory system
        self.memory = MemorySystem()
        
        # Brain regions (simplified)
        self.regions = {
            'prefrontal_cortex': list(range(0, neuron_count // 4)),  # Decision making
            'hippocampus': list(range(neuron_count // 4, neuron_count // 2)),  # Memory
            'amygdala': list(range(neuron_count // 2, 3 * neuron_count // 4)),  # Emotions
            'motor_cortex': list(range(3 * neuron_count // 4, neuron_count))  # Actions
        }
        
        self.state = {
            'arousal': 0.5,
            'attention': 0.5,
            'emotional_state': 0.5
        }
    
    def _initialize_connections(self):
        """Initialize neural connections"""
        for neuron_id, neuron in self.neurons.items():
            # Each neuron connects to several others
            num_connections = np.random.randint(5, 20)
            targets = np.random.choice(
                list(self.neurons.keys()), 
                size=num_connections, 
                replace=False
            )
            
            for target in targets:
                if target != neuron_id:
                    weight = np.random.uniform(-1, 1)
                    neuron.add_connection(target, weight)
    
    def process_input(self, input_data: Any) -> Dict[str, Any]:
        """Process input through the brain simulation"""
        # Store input in memory
        self.memory.store_short_term(input_data)
        self.memory.add_to_working(input_data)
        
        # Convert input to neural signals
        input_signals = self._encode_input(input_data)
        
        # Activate input neurons
        for neuron_id, signal_strength in input_signals.items():
            if neuron_id in self.neurons:
                self.neurons[neuron_id].receive_signal(signal_strength)
        
        # Simulate neural propagation
        output = self._propagate_signals()
        
        # Learn from experience
        self._hebbian_learning()
        
        return output
    
    def _encode_input(self, input_data: Any) -> Dict[int, float]:
        """Encode input data as neural signals"""
        signals = {}
        
        # Simple encoding: hash input and distribute to neurons
        input_hash = hash(str(input_data))
        np.random.seed(input_hash % (2**32))
        
        num_activated = min(50, self.neuron_count // 10)
        activated_neurons = np.random.choice(
            list(self.neurons.keys()), 
            size=num_activated, 
            replace=False
        )
        
        for neuron_id in activated_neurons:
            signals[neuron_id] = np.random.uniform(0.5, 1.5)
        
        return signals
    
    def _propagate_signals(self, iterations: int = 10) -> Dict[str, Any]:
        """Propagate signals through the neural network"""
        firing_pattern = []
        
        for iteration in range(iterations):
            fired_neurons = []
            
            # Check which neurons fire
            for neuron_id, neuron in self.neurons.items():
                if neuron.fire():
                    fired_neurons.append(neuron_id)
            
            # Propagate signals to connected neurons
            for neuron_id in fired_neurons:
                neuron = self.neurons[neuron_id]
                signal = neuron.get_output_signal()
                
                for target_id, weight in neuron.connections.items():
                    if target_id in self.neurons:
                        self.neurons[target_id].receive_signal(signal * weight)
            
            firing_pattern.append(len(fired_neurons))
        
        # Analyze firing patterns
        output = {
            'firing_pattern': firing_pattern,
            'total_activations': sum(firing_pattern),
            'region_activity': self._analyze_region_activity(),
            'decision': self._make_decision(firing_pattern)
        }
        
        return output
    
    def _analyze_region_activity(self) -> Dict[str, float]:
        """Analyze activity in different brain regions"""
        activity = {}
        
        for region_name, neuron_ids in self.regions.items():
            total_activation = sum(
                self.neurons[nid].activation for nid in neuron_ids
            )
            activity[region_name] = total_activation / len(neuron_ids)
        
        return activity
    
    def _make_decision(self, firing_pattern: List[int]) -> str:
        """Make a decision based on firing patterns"""
        avg_activity = np.mean(firing_pattern)
        
        if avg_activity > 30:
            return "high_activity"
        elif avg_activity > 15:
            return "medium_activity"
        else:
            return "low_activity"
    
    def _hebbian_learning(self):
        """Implement Hebbian learning: neurons that fire together, wire together"""
        for neuron_id, neuron in self.neurons.items():
            if len(neuron.firing_history) > 0:
                # Strengthen connections to neurons that also fired
                for target_id in neuron.connections.keys():
                    if len(self.neurons[target_id].firing_history) > 0:
                        # Both fired - strengthen connection
                        delta = self.learning_rate
                    else:
                        # Only source fired - weaken connection
                        delta = -self.learning_rate * 0.5
                    
                    neuron.update_weight(target_id, delta)
    
    def reset(self):
        """Reset brain state"""
        for neuron in self.neurons.values():
            neuron.reset()
        self.memory.clear_working()
    
    def get_state(self) -> Dict[str, Any]:
        """Get current brain state"""
        return {
            'neurons': self.neuron_count,
            'state': self.state,
            'memory_count': len(self.memory.long_term),
            'working_memory': len(self.memory.working)
        }
