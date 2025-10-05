"""
Neural network layers
"""

import numpy as np
from typing import Optional, Callable


class Layer:
    """Base class for neural network layers"""
    
    def __init__(self):
        self.input = None
        self.output = None
    
    def forward(self, input_data: np.ndarray) -> np.ndarray:
        """Forward pass"""
        raise NotImplementedError
    
    def backward(self, output_gradient: np.ndarray, learning_rate: float) -> np.ndarray:
        """Backward pass"""
        raise NotImplementedError


class DenseLayer(Layer):
    """Fully connected layer"""
    
    def __init__(self, input_size: int, output_size: int):
        super().__init__()
        self.weights = np.random.randn(input_size, output_size) * 0.01
        self.bias = np.zeros((1, output_size))
        
        # For momentum
        self.weights_velocity = np.zeros_like(self.weights)
        self.bias_velocity = np.zeros_like(self.bias)
    
    def forward(self, input_data: np.ndarray) -> np.ndarray:
        """Forward pass"""
        self.input = input_data
        self.output = np.dot(input_data, self.weights) + self.bias
        return self.output
    
    def backward(self, output_gradient: np.ndarray, learning_rate: float) -> np.ndarray:
        """Backward pass with gradient descent"""
        # Gradients
        weights_gradient = np.dot(self.input.T, output_gradient)
        bias_gradient = np.sum(output_gradient, axis=0, keepdims=True)
        input_gradient = np.dot(output_gradient, self.weights.T)
        
        # Update with momentum
        momentum = 0.9
        self.weights_velocity = momentum * self.weights_velocity - learning_rate * weights_gradient
        self.bias_velocity = momentum * self.bias_velocity - learning_rate * bias_gradient
        
        self.weights += self.weights_velocity
        self.bias += self.bias_velocity
        
        return input_gradient


class ActivationLayer(Layer):
    """Activation function layer"""
    
    def __init__(self, activation: str = 'relu'):
        super().__init__()
        self.activation_name = activation
        self.activation, self.activation_prime = self._get_activation(activation)
    
    def _get_activation(self, name: str):
        """Get activation function and its derivative"""
        if name == 'relu':
            return (
                lambda x: np.maximum(0, x),
                lambda x: (x > 0).astype(float)
            )
        elif name == 'sigmoid':
            return (
                lambda x: 1 / (1 + np.exp(-np.clip(x, -500, 500))),
                lambda x: x * (1 - x)
            )
        elif name == 'tanh':
            return (
                lambda x: np.tanh(x),
                lambda x: 1 - x ** 2
            )
        elif name == 'leaky_relu':
            return (
                lambda x: np.where(x > 0, x, 0.01 * x),
                lambda x: np.where(x > 0, 1, 0.01)
            )
        elif name == 'softmax':
            def softmax(x):
                exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
                return exp_x / np.sum(exp_x, axis=-1, keepdims=True)
            
            return (softmax, lambda x: np.ones_like(x))
        else:
            # Default to linear
            return (lambda x: x, lambda x: np.ones_like(x))
    
    def forward(self, input_data: np.ndarray) -> np.ndarray:
        """Forward pass"""
        self.input = input_data
        self.output = self.activation(input_data)
        return self.output
    
    def backward(self, output_gradient: np.ndarray, learning_rate: float) -> np.ndarray:
        """Backward pass"""
        return output_gradient * self.activation_prime(self.output)


class DropoutLayer(Layer):
    """Dropout layer for regularization"""
    
    def __init__(self, dropout_rate: float = 0.5):
        super().__init__()
        self.dropout_rate = dropout_rate
        self.mask = None
        self.training = True
    
    def forward(self, input_data: np.ndarray) -> np.ndarray:
        """Forward pass"""
        self.input = input_data
        
        if self.training:
            self.mask = np.random.binomial(1, 1 - self.dropout_rate, size=input_data.shape)
            self.output = input_data * self.mask / (1 - self.dropout_rate)
        else:
            self.output = input_data
        
        return self.output
    
    def backward(self, output_gradient: np.ndarray, learning_rate: float) -> np.ndarray:
        """Backward pass"""
        if self.training and self.mask is not None:
            return output_gradient * self.mask / (1 - self.dropout_rate)
        return output_gradient


class BatchNormLayer(Layer):
    """Batch normalization layer"""
    
    def __init__(self, input_size: int, epsilon: float = 1e-5):
        super().__init__()
        self.epsilon = epsilon
        self.gamma = np.ones((1, input_size))
        self.beta = np.zeros((1, input_size))
        self.running_mean = np.zeros((1, input_size))
        self.running_var = np.ones((1, input_size))
        self.training = True
    
    def forward(self, input_data: np.ndarray) -> np.ndarray:
        """Forward pass"""
        self.input = input_data
        
        if self.training:
            self.mean = np.mean(input_data, axis=0, keepdims=True)
            self.var = np.var(input_data, axis=0, keepdims=True)
            
            # Update running statistics
            self.running_mean = 0.9 * self.running_mean + 0.1 * self.mean
            self.running_var = 0.9 * self.running_var + 0.1 * self.var
        else:
            self.mean = self.running_mean
            self.var = self.running_var
        
        self.x_normalized = (input_data - self.mean) / np.sqrt(self.var + self.epsilon)
        self.output = self.gamma * self.x_normalized + self.beta
        
        return self.output
    
    def backward(self, output_gradient: np.ndarray, learning_rate: float) -> np.ndarray:
        """Backward pass"""
        N = output_gradient.shape[0]
        
        # Gradients
        dgamma = np.sum(output_gradient * self.x_normalized, axis=0, keepdims=True)
        dbeta = np.sum(output_gradient, axis=0, keepdims=True)
        
        dx_normalized = output_gradient * self.gamma
        dvar = np.sum(dx_normalized * (self.input - self.mean) * -0.5 * 
                     (self.var + self.epsilon) ** (-1.5), axis=0, keepdims=True)
        dmean = np.sum(dx_normalized * -1 / np.sqrt(self.var + self.epsilon), axis=0, keepdims=True)
        
        input_gradient = (dx_normalized / np.sqrt(self.var + self.epsilon) + 
                         dvar * 2 * (self.input - self.mean) / N + dmean / N)
        
        # Update parameters
        self.gamma -= learning_rate * dgamma
        self.beta -= learning_rate * dbeta
        
        return input_gradient
