"""
Neural Network implementation
"""

import numpy as np
from typing import List, Dict, Any, Optional
from .layers import Layer, DenseLayer, ActivationLayer, DropoutLayer


class NeuralNetwork:
    """Advanced neural network with multiple layers"""
    
    def __init__(self, architecture: List[int], activation: str = 'relu'):
        """
        Initialize neural network
        
        Args:
            architecture: List of layer sizes [input, hidden1, hidden2, ..., output]
            activation: Activation function name
        """
        self.architecture = architecture
        self.activation = activation
        self.layers: List[Layer] = []
        self.training = True
        
        # Build network
        self._build_network()
        
        # Training history
        self.history = {
            'loss': [],
            'accuracy': []
        }
    
    def _build_network(self):
        """Build the neural network layers"""
        for i in range(len(self.architecture) - 1):
            # Dense layer
            self.layers.append(
                DenseLayer(self.architecture[i], self.architecture[i + 1])
            )
            
            # Activation layer (except for last layer)
            if i < len(self.architecture) - 2:
                self.layers.append(ActivationLayer(self.activation))
                
                # Add dropout for regularization
                if i > 0:  # Not for first hidden layer
                    self.layers.append(DropoutLayer(dropout_rate=0.3))
        
        # Output activation
        self.layers.append(ActivationLayer('sigmoid'))
    
    def forward(self, input_data: np.ndarray) -> np.ndarray:
        """Forward propagation"""
        output = input_data
        
        for layer in self.layers:
            if hasattr(layer, 'training'):
                layer.training = self.training
            output = layer.forward(output)
        
        return output
    
    def backward(self, output_gradient: np.ndarray, learning_rate: float):
        """Backward propagation"""
        gradient = output_gradient
        
        for layer in reversed(self.layers):
            gradient = layer.backward(gradient, learning_rate)
    
    def predict(self, input_data: np.ndarray) -> np.ndarray:
        """Make predictions"""
        self.training = False
        predictions = self.forward(input_data)
        self.training = True
        return predictions
    
    def train_step(self, X: np.ndarray, y: np.ndarray, learning_rate: float) -> float:
        """Single training step"""
        # Forward pass
        predictions = self.forward(X)
        
        # Calculate loss (MSE)
        loss = np.mean((predictions - y) ** 2)
        
        # Backward pass
        gradient = 2 * (predictions - y) / y.shape[0]
        self.backward(gradient, learning_rate)
        
        return loss
    
    def fit(self, X: np.ndarray, y: np.ndarray, 
            epochs: int = 100, learning_rate: float = 0.01, 
            batch_size: int = 32, verbose: bool = True) -> Dict[str, List[float]]:
        """Train the neural network"""
        n_samples = X.shape[0]
        
        for epoch in range(epochs):
            # Shuffle data
            indices = np.random.permutation(n_samples)
            X_shuffled = X[indices]
            y_shuffled = y[indices]
            
            epoch_loss = 0
            n_batches = 0
            
            # Mini-batch training
            for i in range(0, n_samples, batch_size):
                X_batch = X_shuffled[i:i + batch_size]
                y_batch = y_shuffled[i:i + batch_size]
                
                loss = self.train_step(X_batch, y_batch, learning_rate)
                epoch_loss += loss
                n_batches += 1
            
            # Average loss
            avg_loss = epoch_loss / n_batches
            self.history['loss'].append(avg_loss)
            
            # Calculate accuracy
            predictions = self.predict(X)
            accuracy = self.calculate_accuracy(predictions, y)
            self.history['accuracy'].append(accuracy)
            
            if verbose and (epoch + 1) % 10 == 0:
                print(f"Epoch {epoch + 1}/{epochs} - Loss: {avg_loss:.4f}, Accuracy: {accuracy:.4f}")
        
        return self.history
    
    def calculate_accuracy(self, predictions: np.ndarray, targets: np.ndarray) -> float:
        """Calculate accuracy"""
        pred_labels = (predictions > 0.5).astype(int)
        target_labels = (targets > 0.5).astype(int)
        accuracy = np.mean(pred_labels == target_labels)
        return float(accuracy)
    
    def evaluate(self, X: np.ndarray, y: np.ndarray) -> Dict[str, float]:
        """Evaluate the model"""
        predictions = self.predict(X)
        loss = np.mean((predictions - y) ** 2)
        accuracy = self.calculate_accuracy(predictions, y)
        
        return {
            'loss': float(loss),
            'accuracy': float(accuracy)
        }
    
    def get_weights(self) -> List[np.ndarray]:
        """Get all network weights"""
        weights = []
        for layer in self.layers:
            if isinstance(layer, DenseLayer):
                weights.append(layer.weights)
                weights.append(layer.bias)
        return weights
    
    def set_weights(self, weights: List[np.ndarray]):
        """Set network weights"""
        weight_idx = 0
        for layer in self.layers:
            if isinstance(layer, DenseLayer):
                layer.weights = weights[weight_idx]
                layer.bias = weights[weight_idx + 1]
                weight_idx += 2
    
    def save_model(self, filepath: str):
        """Save model weights"""
        weights = self.get_weights()
        np.savez(filepath, *weights, architecture=self.architecture)
    
    def load_model(self, filepath: str):
        """Load model weights"""
        data = np.load(filepath, allow_pickle=True)
        weights = [data[f'arr_{i}'] for i in range(len(data.files) - 1)]
        self.set_weights(weights)
    
    def summary(self) -> str:
        """Get model summary"""
        summary = "Neural Network Architecture:\n"
        summary += "=" * 50 + "\n"
        
        total_params = 0
        layer_num = 0
        
        for i, layer in enumerate(self.layers):
            if isinstance(layer, DenseLayer):
                params = layer.weights.size + layer.bias.size
                total_params += params
                summary += f"Layer {layer_num}: Dense({layer.weights.shape[0]} -> {layer.weights.shape[1]}) - {params} params\n"
                layer_num += 1
            elif isinstance(layer, ActivationLayer):
                summary += f"         Activation: {layer.activation_name}\n"
            elif isinstance(layer, DropoutLayer):
                summary += f"         Dropout: {layer.dropout_rate}\n"
        
        summary += "=" * 50 + "\n"
        summary += f"Total parameters: {total_params}\n"
        
        return summary
