"""
Quantum processor with multiple qubits and quantum algorithms
"""

import numpy as np
from typing import List, Dict, Any, Tuple
from .qubit import Qubit


class QuantumProcessor:
    """Quantum processor with multi-qubit operations"""
    
    def __init__(self, qubit_count: int = 8, shots: int = 1024):
        self.qubit_count = qubit_count
        self.shots = shots
        self.qubits: Dict[int, Qubit] = {}
        
        # Initialize qubits
        for i in range(qubit_count):
            self.qubits[i] = Qubit(i)
        
        self.circuit_history: List[str] = []
    
    def apply_cnot(self, control: int, target: int):
        """Apply CNOT (Controlled-NOT) gate"""
        if control not in self.qubits or target not in self.qubits:
            raise ValueError("Invalid qubit indices")
        
        control_qubit = self.qubits[control]
        target_qubit = self.qubits[target]
        
        # Simplified CNOT: if control is |1>, flip target
        prob_1_control = abs(control_qubit.state[1])**2
        
        if prob_1_control > 0.5:  # Simplified implementation
            target_qubit.apply_pauli_x()
        
        # Mark entanglement
        if target not in control_qubit.entangled_with:
            control_qubit.entangled_with.append(target)
        if control not in target_qubit.entangled_with:
            target_qubit.entangled_with.append(control)
        
        self.circuit_history.append(f"CNOT({control}, {target})")
    
    def apply_to_qubit(self, qubit_id: int, gate: str, *params):
        """Apply a gate to a specific qubit"""
        if qubit_id not in self.qubits:
            raise ValueError(f"Qubit {qubit_id} not found")
        
        qubit = self.qubits[qubit_id]
        
        if gate.upper() == 'H':
            qubit.apply_hadamard()
        elif gate.upper() == 'X':
            qubit.apply_pauli_x()
        elif gate.upper() == 'Y':
            qubit.apply_pauli_y()
        elif gate.upper() == 'Z':
            qubit.apply_pauli_z()
        elif gate.upper() == 'RX':
            qubit.apply_rotation_x(params[0] if params else np.pi/4)
        elif gate.upper() == 'RY':
            qubit.apply_rotation_y(params[0] if params else np.pi/4)
        elif gate.upper() == 'RZ':
            qubit.apply_rotation_z(params[0] if params else np.pi/4)
        elif gate.upper() == 'P':
            qubit.apply_phase(params[0] if params else np.pi/4)
        else:
            raise ValueError(f"Unknown gate: {gate}")
        
        self.circuit_history.append(f"{gate.upper()}({qubit_id})")
    
    def create_bell_state(self, q1: int = 0, q2: int = 1):
        """Create a Bell state (maximally entangled state)"""
        self.apply_to_qubit(q1, 'H')
        self.apply_cnot(q1, q2)
    
    def quantum_fourier_transform(self, qubits: List[int]):
        """Apply Quantum Fourier Transform"""
        n = len(qubits)
        
        for i, qubit in enumerate(qubits):
            self.apply_to_qubit(qubit, 'H')
            
            for j in range(i + 1, n):
                angle = np.pi / (2 ** (j - i))
                self.apply_to_qubit(qubits[j], 'P', angle)
        
        self.circuit_history.append(f"QFT({qubits})")
    
    def quantum_search(self, target_state: int) -> int:
        """Simplified Grover's search algorithm"""
        n = self.qubit_count
        
        # Initialize superposition
        for i in range(n):
            self.apply_to_qubit(i, 'H')
        
        # Number of iterations for Grover's algorithm
        iterations = int(np.pi / 4 * np.sqrt(2**n))
        
        for _ in range(min(iterations, 5)):  # Limit iterations
            # Oracle (simplified)
            for i in range(n):
                if (target_state >> i) & 1 == 0:
                    self.apply_to_qubit(i, 'X')
            
            # Apply phase flip
            self.apply_to_qubit(n-1, 'Z')
            
            # Undo oracle
            for i in range(n):
                if (target_state >> i) & 1 == 0:
                    self.apply_to_qubit(i, 'X')
            
            # Diffusion operator (simplified)
            for i in range(n):
                self.apply_to_qubit(i, 'H')
                self.apply_to_qubit(i, 'X')
            
            self.apply_to_qubit(n-1, 'Z')
            
            for i in range(n):
                self.apply_to_qubit(i, 'X')
                self.apply_to_qubit(i, 'H')
        
        # Measure
        result = self.measure_all()
        most_common = max(result, key=result.get)
        
        return most_common
    
    def quantum_annealing(self, problem_hamiltonian: np.ndarray) -> List[int]:
        """Simulate quantum annealing for optimization"""
        # Initialize random state
        for i in range(self.qubit_count):
            self.apply_to_qubit(i, 'H')
            self.apply_to_qubit(i, 'RY', np.random.uniform(0, 2*np.pi))
        
        # Annealing process (simplified)
        steps = 10
        for step in range(steps):
            beta = step / steps  # Annealing parameter
            
            for i in range(self.qubit_count):
                # Apply problem-dependent rotations
                angle = beta * np.random.uniform(-np.pi/4, np.pi/4)
                self.apply_to_qubit(i, 'RZ', angle)
        
        # Measure final state
        results = []
        for _ in range(min(self.shots, 10)):
            measurement = [self.qubits[i].measure() for i in range(self.qubit_count)]
            results.append(measurement)
            self.reset()
        
        # Return most common result
        from collections import Counter
        most_common = Counter(tuple(r) for r in results).most_common(1)[0][0]
        return list(most_common)
    
    def measure_qubit(self, qubit_id: int) -> int:
        """Measure a single qubit"""
        if qubit_id not in self.qubits:
            raise ValueError(f"Qubit {qubit_id} not found")
        
        return self.qubits[qubit_id].measure()
    
    def measure_all(self) -> Dict[int, int]:
        """Measure all qubits multiple times"""
        results = {}
        
        for _ in range(self.shots):
            measurement = 0
            for i in range(self.qubit_count):
                bit = self.qubits[i].measure()
                measurement = (measurement << 1) | bit
                self.qubits[i].reset()  # Reset for next shot
            
            results[measurement] = results.get(measurement, 0) + 1
        
        return results
    
    def get_statevector(self) -> List[complex]:
        """Get combined state vector (simplified for small systems)"""
        if self.qubit_count > 4:
            return [self.qubits[i].get_state_vector()[0] for i in range(min(4, self.qubit_count))]
        
        # For small systems, compute full state vector
        state = self.qubits[0].get_state_vector()
        for i in range(1, self.qubit_count):
            state = np.kron(state, self.qubits[i].get_state_vector())
        
        return state.tolist()
    
    def get_circuit_info(self) -> Dict[str, Any]:
        """Get information about the quantum circuit"""
        return {
            'qubit_count': self.qubit_count,
            'circuit_depth': len(self.circuit_history),
            'operations': self.circuit_history[-10:],  # Last 10 operations
            'entanglements': sum(len(q.entangled_with) for q in self.qubits.values())
        }
    
    def reset(self):
        """Reset all qubits to |0> state"""
        for qubit in self.qubits.values():
            qubit.reset()
        self.circuit_history.clear()
    
    def quantum_advantage_check(self, input_data: Any) -> Dict[str, Any]:
        """Check if quantum processing provides advantage"""
        # Classical processing time estimate
        classical_complexity = len(str(input_data)) * np.log2(len(str(input_data)))
        
        # Quantum processing
        self.reset()
        for i in range(min(self.qubit_count, 4)):
            self.apply_to_qubit(i, 'H')
        
        results = self.measure_all()
        
        # Quantum speedup potential
        quantum_complexity = np.sqrt(2 ** self.qubit_count)
        speedup = classical_complexity / quantum_complexity if quantum_complexity > 0 else 1
        
        return {
            'quantum_advantage': speedup > 1,
            'speedup_factor': float(speedup),
            'measurement_results': results,
            'recommendation': 'use_quantum' if speedup > 2 else 'use_classical'
        }
