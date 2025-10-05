"""
Qubit simulation and quantum operations
"""

import numpy as np
from typing import Tuple, List


class Qubit:
    """Simulates a quantum bit with superposition and entanglement"""
    
    def __init__(self, qubit_id: int):
        self.qubit_id = qubit_id
        # State vector [|0>, |1>]
        self.state = np.array([1.0, 0.0], dtype=complex)
        self.entangled_with: List[int] = []
    
    def initialize(self, alpha: complex, beta: complex):
        """Initialize qubit state |ψ> = α|0> + β|1>"""
        # Normalize
        norm = np.sqrt(abs(alpha)**2 + abs(beta)**2)
        self.state = np.array([alpha/norm, beta/norm], dtype=complex)
    
    def apply_hadamard(self):
        """Apply Hadamard gate - creates superposition"""
        H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
        self.state = H @ self.state
    
    def apply_pauli_x(self):
        """Apply Pauli-X gate (quantum NOT)"""
        X = np.array([[0, 1], [1, 0]], dtype=complex)
        self.state = X @ self.state
    
    def apply_pauli_y(self):
        """Apply Pauli-Y gate"""
        Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
        self.state = Y @ self.state
    
    def apply_pauli_z(self):
        """Apply Pauli-Z gate"""
        Z = np.array([[1, 0], [0, -1]], dtype=complex)
        self.state = Z @ self.state
    
    def apply_phase(self, theta: float):
        """Apply phase rotation gate"""
        P = np.array([[1, 0], [0, np.exp(1j * theta)]], dtype=complex)
        self.state = P @ self.state
    
    def apply_rotation_x(self, theta: float):
        """Apply rotation around X axis"""
        RX = np.array([
            [np.cos(theta/2), -1j*np.sin(theta/2)],
            [-1j*np.sin(theta/2), np.cos(theta/2)]
        ], dtype=complex)
        self.state = RX @ self.state
    
    def apply_rotation_y(self, theta: float):
        """Apply rotation around Y axis"""
        RY = np.array([
            [np.cos(theta/2), -np.sin(theta/2)],
            [np.sin(theta/2), np.cos(theta/2)]
        ], dtype=complex)
        self.state = RY @ self.state
    
    def apply_rotation_z(self, theta: float):
        """Apply rotation around Z axis"""
        RZ = np.array([
            [np.exp(-1j*theta/2), 0],
            [0, np.exp(1j*theta/2)]
        ], dtype=complex)
        self.state = RZ @ self.state
    
    def measure(self) -> int:
        """Measure qubit in computational basis"""
        # Probability of measuring |0> or |1>
        prob_0 = abs(self.state[0])**2
        prob_1 = abs(self.state[1])**2
        
        # Measurement collapses state
        result = np.random.choice([0, 1], p=[prob_0, prob_1])
        
        if result == 0:
            self.state = np.array([1.0, 0.0], dtype=complex)
        else:
            self.state = np.array([0.0, 1.0], dtype=complex)
        
        return result
    
    def get_state_vector(self) -> np.ndarray:
        """Get current state vector"""
        return self.state.copy()
    
    def get_probabilities(self) -> Tuple[float, float]:
        """Get measurement probabilities"""
        return (abs(self.state[0])**2, abs(self.state[1])**2)
    
    def bloch_coordinates(self) -> Tuple[float, float, float]:
        """Get Bloch sphere coordinates"""
        alpha, beta = self.state
        
        # Bloch sphere coordinates
        x = 2 * np.real(alpha * np.conj(beta))
        y = 2 * np.imag(alpha * np.conj(beta))
        z = abs(alpha)**2 - abs(beta)**2
        
        return (float(x), float(y), float(z))
    
    def reset(self):
        """Reset qubit to |0> state"""
        self.state = np.array([1.0, 0.0], dtype=complex)
        self.entangled_with.clear()
