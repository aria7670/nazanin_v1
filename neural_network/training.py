"""
Training utilities and optimizers
"""

import numpy as np
from typing import Dict, Any, List, Optional
from .neural_net import NeuralNetwork


class Trainer:
    """Advanced training utilities"""
    
    def __init__(self, model: NeuralNetwork):
        self.model = model
        self.best_weights = None
        self.best_loss = float('inf')
    
    def train_with_validation(self, 
                             X_train: np.ndarray, y_train: np.ndarray,
                             X_val: np.ndarray, y_val: np.ndarray,
                             epochs: int = 100, 
                             learning_rate: float = 0.01,
                             batch_size: int = 32,
                             early_stopping_patience: int = 10,
                             verbose: bool = True) -> Dict[str, List[float]]:
        """Train with validation and early stopping"""
        
        history = {
            'train_loss': [],
            'train_accuracy': [],
            'val_loss': [],
            'val_accuracy': []
        }
        
        patience_counter = 0
        
        for epoch in range(epochs):
            # Training
            train_metrics = self.model.fit(
                X_train, y_train, 
                epochs=1, 
                learning_rate=learning_rate,
                batch_size=batch_size,
                verbose=False
            )
            
            # Validation
            val_metrics = self.model.evaluate(X_val, y_val)
            
            # Record history
            history['train_loss'].append(train_metrics['loss'][-1])
            history['train_accuracy'].append(train_metrics['accuracy'][-1])
            history['val_loss'].append(val_metrics['loss'])
            history['val_accuracy'].append(val_metrics['accuracy'])
            
            # Early stopping check
            if val_metrics['loss'] < self.best_loss:
                self.best_loss = val_metrics['loss']
                self.best_weights = self.model.get_weights()
                patience_counter = 0
            else:
                patience_counter += 1
            
            if verbose and (epoch + 1) % 10 == 0:
                print(f"Epoch {epoch + 1}/{epochs}")
                print(f"  Train - Loss: {train_metrics['loss'][-1]:.4f}, Acc: {train_metrics['accuracy'][-1]:.4f}")
                print(f"  Val   - Loss: {val_metrics['loss']:.4f}, Acc: {val_metrics['accuracy']:.4f}")
            
            # Early stopping
            if patience_counter >= early_stopping_patience:
                if verbose:
                    print(f"Early stopping triggered at epoch {epoch + 1}")
                break
        
        # Restore best weights
        if self.best_weights is not None:
            self.model.set_weights(self.best_weights)
        
        return history
    
    def cross_validate(self, 
                      X: np.ndarray, y: np.ndarray,
                      k_folds: int = 5,
                      epochs: int = 50,
                      learning_rate: float = 0.01) -> Dict[str, float]:
        """K-fold cross validation"""
        
        n_samples = X.shape[0]
        fold_size = n_samples // k_folds
        
        fold_scores = []
        
        for fold in range(k_folds):
            print(f"Training fold {fold + 1}/{k_folds}")
            
            # Split data
            val_start = fold * fold_size
            val_end = val_start + fold_size
            
            X_val = X[val_start:val_end]
            y_val = y[val_start:val_end]
            
            X_train = np.concatenate([X[:val_start], X[val_end:]], axis=0)
            y_train = np.concatenate([y[:val_start], y[val_end:]], axis=0)
            
            # Reset model
            self.model._build_network()
            
            # Train
            self.model.fit(X_train, y_train, epochs=epochs, 
                          learning_rate=learning_rate, verbose=False)
            
            # Evaluate
            metrics = self.model.evaluate(X_val, y_val)
            fold_scores.append(metrics['accuracy'])
        
        return {
            'mean_accuracy': float(np.mean(fold_scores)),
            'std_accuracy': float(np.std(fold_scores)),
            'fold_scores': fold_scores
        }
    
    def learning_rate_finder(self, 
                            X: np.ndarray, y: np.ndarray,
                            start_lr: float = 1e-7,
                            end_lr: float = 1,
                            num_steps: int = 100) -> Dict[str, List[float]]:
        """Find optimal learning rate"""
        
        lrs = np.logspace(np.log10(start_lr), np.log10(end_lr), num_steps)
        losses = []
        
        original_weights = self.model.get_weights()
        
        for lr in lrs:
            # Reset to original weights
            self.model.set_weights([w.copy() for w in original_weights])
            
            # Train one step
            loss = self.model.train_step(X, y, lr)
            losses.append(loss)
        
        # Restore original weights
        self.model.set_weights(original_weights)
        
        # Find best learning rate (where loss decreases fastest)
        gradients = np.gradient(losses)
        best_idx = np.argmin(gradients)
        
        return {
            'learning_rates': lrs.tolist(),
            'losses': losses,
            'best_lr': float(lrs[best_idx])
        }
