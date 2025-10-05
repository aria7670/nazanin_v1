"""
Unified AI System
Integrates brain simulation, quantum, neural, and agent systems
"""

import numpy as np
from typing import Any, Dict, List, Optional

from brain_simulation import BrainSimulator
from quantum_system import QuantumProcessor
from neural_network import NeuralNetwork
from agent_system import IntelligentAgent, ReinforcementLearningAgent, Environment
from .coordinator import SystemCoordinator, ProcessingMode
from core import Logger


class UnifiedAISystem:
    """Unified AI system combining all subsystems"""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.logger = Logger("UnifiedAISystem")
        
        # Initialize subsystems
        self.logger.info("Initializing subsystems...")
        
        # Brain simulation
        self.brain = BrainSimulator(
            neuron_count=self.config.get('brain_neuron_count', 1000),
            learning_rate=self.config.get('brain_learning_rate', 0.01)
        )
        self.logger.info("Brain simulation initialized")
        
        # Quantum processor
        self.quantum = QuantumProcessor(
            qubit_count=self.config.get('quantum_qubits', 8),
            shots=self.config.get('quantum_shots', 1024)
        )
        self.logger.info("Quantum processor initialized")
        
        # Neural network
        architecture = self.config.get('neural_architecture', [10, 64, 32, 10])
        self.neural = NeuralNetwork(
            architecture=architecture,
            activation=self.config.get('neural_activation', 'relu')
        )
        self.logger.info("Neural network initialized")
        
        # Intelligent agent
        self.agent = IntelligentAgent(
            agent_id="nazanin_agent",
            capabilities=['reasoning', 'learning', 'planning', 'decision_making']
        )
        self.logger.info("Intelligent agent initialized")
        
        # RL agent (for learning tasks)
        self.rl_agent = ReinforcementLearningAgent(
            state_size=10,
            action_size=4,
            learning_rate=0.001
        )
        
        # System coordinator
        self.coordinator = SystemCoordinator()
        self.logger.info("System coordinator initialized")
        
        # System state
        self.processing_history: List[Dict[str, Any]] = []
        
        self.logger.info("Unified AI System fully initialized")
    
    def process(self, input_data: Any, task_type: str = "general") -> Dict[str, Any]:
        """Process input through the unified system"""
        self.logger.info(f"Processing input with task type: {task_type}")
        
        # Create task object
        task = {
            'type': task_type,
            'input': input_data,
            'complexity': self._assess_complexity(input_data)
        }
        
        # Route task to appropriate systems
        systems_to_use = self.coordinator.route_task(task)
        self.logger.info(f"Routing to systems: {systems_to_use}")
        
        # Process with each system
        system_results = {}
        
        if 'brain' in systems_to_use:
            brain_result = self._process_with_brain(input_data)
            system_results['brain'] = brain_result
            self.logger.debug("Brain processing complete")
        
        if 'quantum' in systems_to_use:
            # Check if quantum advantage exists
            if self.coordinator.quantum_advantage_analysis(task):
                quantum_result = self._process_with_quantum(input_data)
                system_results['quantum'] = quantum_result
                self.logger.debug("Quantum processing complete")
        
        if 'neural' in systems_to_use:
            neural_result = self._process_with_neural(input_data)
            system_results['neural'] = neural_result
            self.logger.debug("Neural processing complete")
        
        if 'agent' in systems_to_use:
            agent_result = self._process_with_agent(input_data, task_type)
            system_results['agent'] = agent_result
            self.logger.debug("Agent processing complete")
        
        # Coordinate and merge results
        final_result = self.coordinator.coordinate_processing(task, system_results)
        
        # Store in processing history
        self.processing_history.append({
            'task': task,
            'systems_used': systems_to_use,
            'result': final_result
        })
        
        self.logger.info("Processing complete")
        return final_result
    
    def _assess_complexity(self, input_data: Any) -> str:
        """Assess input complexity"""
        size = len(str(input_data))
        if size < 20:
            return "simple"
        elif size < 100:
            return "moderate"
        else:
            return "complex"
    
    def _process_with_brain(self, input_data: Any) -> Dict[str, Any]:
        """Process input with brain simulation"""
        result = self.brain.process_input(input_data)
        
        # Store in memory
        self.brain.memory.store_short_term(input_data)
        
        return {
            'output': result,
            'confidence': self._calculate_brain_confidence(result),
            'brain_state': self.brain.get_state()
        }
    
    def _calculate_brain_confidence(self, brain_result: Dict[str, Any]) -> float:
        """Calculate confidence from brain processing"""
        activity = brain_result.get('total_activations', 0)
        # Normalize to 0-1 range
        confidence = min(1.0, activity / 100)
        return confidence
    
    def _process_with_quantum(self, input_data: Any) -> Dict[str, Any]:
        """Process input with quantum processor"""
        # Reset quantum processor
        self.quantum.reset()
        
        # Apply quantum operations based on input
        input_hash = hash(str(input_data))
        np.random.seed(input_hash % (2**32))
        
        # Create superposition
        for i in range(min(4, self.quantum.qubit_count)):
            self.quantum.apply_to_qubit(i, 'H')
        
        # Apply some rotations
        for i in range(min(4, self.quantum.qubit_count)):
            angle = (input_hash % 360) * np.pi / 180
            self.quantum.apply_to_qubit(i, 'RY', angle)
        
        # Measure
        results = self.quantum.measure_all()
        
        # Get quantum advantage check
        advantage = self.quantum.quantum_advantage_check(input_data)
        
        return {
            'measurements': results,
            'quantum_advantage': advantage,
            'confidence': 0.8 if advantage['quantum_advantage'] else 0.5,
            'circuit_info': self.quantum.get_circuit_info()
        }
    
    def _process_with_neural(self, input_data: Any) -> Dict[str, Any]:
        """Process input with neural network"""
        # Convert input to numerical format
        input_vector = self._encode_to_vector(input_data)
        
        # Ensure correct input size
        expected_size = self.neural.architecture[0]
        if len(input_vector) < expected_size:
            input_vector = np.pad(input_vector, (0, expected_size - len(input_vector)))
        elif len(input_vector) > expected_size:
            input_vector = input_vector[:expected_size]
        
        # Reshape for prediction
        input_vector = input_vector.reshape(1, -1)
        
        # Make prediction
        prediction = self.neural.predict(input_vector)
        
        # Calculate confidence (entropy-based)
        confidence = self._calculate_neural_confidence(prediction)
        
        return {
            'prediction': prediction.tolist(),
            'confidence': confidence,
            'network_summary': self.neural.summary()
        }
    
    def _encode_to_vector(self, input_data: Any) -> np.ndarray:
        """Encode input data to numerical vector"""
        input_str = str(input_data)
        
        # Simple encoding: character values and statistics
        char_values = [ord(c) % 256 for c in input_str[:10]]
        
        # Pad to at least 10 values
        while len(char_values) < 10:
            char_values.append(0)
        
        return np.array(char_values, dtype=float) / 255.0  # Normalize
    
    def _calculate_neural_confidence(self, prediction: np.ndarray) -> float:
        """Calculate confidence from neural network prediction"""
        # Confidence based on prediction entropy
        probs = np.abs(prediction.flatten())
        probs = probs / (np.sum(probs) + 1e-10)
        
        entropy = -np.sum(probs * np.log(probs + 1e-10))
        max_entropy = np.log(len(probs))
        
        # Lower entropy = higher confidence
        confidence = 1 - (entropy / max_entropy) if max_entropy > 0 else 0.5
        
        return float(confidence)
    
    def _process_with_agent(self, input_data: Any, task_type: str) -> Dict[str, Any]:
        """Process input with intelligent agent"""
        # Agent perceives the input
        perception = self.agent.perceive(input_data)
        
        # Agent reasons about it
        if task_type in ['reasoning', 'decision_making']:
            reasoning = self.agent.reason(input_data)
            result = reasoning
        elif task_type in ['planning']:
            goal = {'description': str(input_data)}
            plan = self.agent.plan(goal)
            result = {'plan': plan}
        else:
            # Default: perceive and analyze
            result = perception
        
        return {
            'result': result,
            'confidence': result.get('confidence', 0.7),
            'agent_status': self.agent.get_status()
        }
    
    def learn(self, input_data: Any, target: Any, task_type: str = "learning"):
        """Learn from data"""
        self.logger.info("Learning from new data...")
        
        # Brain learning
        self.brain.process_input({'input': input_data, 'target': target})
        self.brain.memory.consolidate()
        
        # Neural network learning
        if isinstance(input_data, np.ndarray) and isinstance(target, np.ndarray):
            self.neural.fit(input_data, target, epochs=10, verbose=False)
        
        # Agent learning
        experience = {
            'context': input_data,
            'action': 'process',
            'outcome': target,
            'successful': True
        }
        self.agent.learn(experience)
        
        self.logger.info("Learning complete")
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get comprehensive system status"""
        return {
            'brain': self.brain.get_state(),
            'quantum': self.quantum.get_circuit_info(),
            'neural': {
                'architecture': self.neural.architecture,
                'training_history': len(self.neural.history.get('loss', []))
            },
            'agent': self.agent.get_status(),
            'coordinator': self.coordinator.get_system_status(),
            'processing_history_size': len(self.processing_history)
        }
    
    def optimize(self):
        """Optimize the entire system"""
        self.logger.info("Optimizing system...")
        
        # Optimize routing based on history
        self.coordinator.optimize_routing(self.processing_history)
        
        # Brain memory consolidation
        self.brain.memory.consolidate()
        
        # Reset quantum processor
        self.quantum.reset()
        
        self.logger.info("Optimization complete")
    
    def reset(self):
        """Reset all subsystems"""
        self.logger.info("Resetting all subsystems...")
        
        self.brain.reset()
        self.quantum.reset()
        self.processing_history.clear()
        
        self.logger.info("Reset complete")
    
    def save_state(self, filepath: str):
        """Save system state"""
        state = {
            'config': self.config,
            'processing_history': self.processing_history[-100:],  # Last 100
            'brain_memory_count': len(self.brain.memory.long_term),
            'agent_knowledge_count': len(self.agent.knowledge_base)
        }
        
        import json
        with open(filepath, 'w') as f:
            json.dump(state, f, indent=2, default=str)
        
        self.logger.info(f"State saved to {filepath}")
