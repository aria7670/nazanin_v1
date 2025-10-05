"""
Neuron simulation with synaptic connections
"""

import numpy as np
from typing import List, Dict


class Neuron:
    """Simulates a single neuron with synaptic connections"""
    
    def __init__(self, neuron_id: int, threshold: float = 0.5):
        self.neuron_id = neuron_id
        self.threshold = threshold
        self.activation = 0.0
        self.connections: Dict[int, float] = {}  # neuron_id -> weight
        self.firing_history: List[float] = []
    
    def add_connection(self, target_neuron_id: int, weight: float):
        """Add a synaptic connection to another neuron"""
        self.connections[target_neuron_id] = weight
    
    def receive_signal(self, signal_strength: float):
        """Receive a signal from another neuron"""
        self.activation += signal_strength
    
    def fire(self) -> bool:
        """Check if neuron should fire based on threshold"""
        if self.activation >= self.threshold:
            self.firing_history.append(self.activation)
            self.activation = 0.0
            return True
        else:
            # Decay activation over time
            self.activation *= 0.9
            return False
    
    def get_output_signal(self) -> float:
        """Get the output signal strength when firing"""
        return 1.0 if len(self.firing_history) > 0 else 0.0
    
    def update_weight(self, target_neuron_id: int, delta: float):
        """Update synaptic weight (learning)"""
        if target_neuron_id in self.connections:
            self.connections[target_neuron_id] += delta
            # Clip weights to reasonable range
            self.connections[target_neuron_id] = np.clip(
                self.connections[target_neuron_id], -2.0, 2.0
            )
    
    def reset(self):
        """Reset neuron state"""
        self.activation = 0.0
        self.firing_history.clear()
