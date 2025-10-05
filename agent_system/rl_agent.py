"""
Reinforcement Learning Agent
"""

import numpy as np
from typing import Dict, Any, List, Optional, Tuple
from collections import deque
import random


class ReinforcementLearningAgent:
    """RL Agent with Q-learning and experience replay"""
    
    def __init__(self, state_size: int, action_size: int, 
                 learning_rate: float = 0.001, gamma: float = 0.95,
                 epsilon: float = 1.0, epsilon_decay: float = 0.995,
                 epsilon_min: float = 0.01):
        
        self.state_size = state_size
        self.action_size = action_size
        self.learning_rate = learning_rate
        self.gamma = gamma  # Discount factor
        
        # Exploration vs exploitation
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        
        # Q-table for tabular methods
        self.q_table: Dict[Tuple, np.ndarray] = {}
        
        # Experience replay buffer
        self.memory = deque(maxlen=10000)
        self.batch_size = 64
        
        # Q-network (simple linear approximation)
        self.weights = np.random.randn(state_size, action_size) * 0.01
        self.bias = np.zeros(action_size)
        
        # Training statistics
        self.episode_rewards: List[float] = []
        self.episode_lengths: List[int] = []
    
    def get_action(self, state: np.ndarray, training: bool = True) -> int:
        """Select action using epsilon-greedy policy"""
        if training and random.random() < self.epsilon:
            # Explore: random action
            return random.randint(0, self.action_size - 1)
        else:
            # Exploit: best action according to Q-values
            q_values = self.predict_q_values(state)
            return int(np.argmax(q_values))
    
    def predict_q_values(self, state: np.ndarray) -> np.ndarray:
        """Predict Q-values for all actions"""
        state = state.reshape(-1)
        if len(state) != self.state_size:
            # Pad or truncate state to match state_size
            if len(state) < self.state_size:
                state = np.pad(state, (0, self.state_size - len(state)))
            else:
                state = state[:self.state_size]
        
        q_values = np.dot(state, self.weights) + self.bias
        return q_values
    
    def remember(self, state: np.ndarray, action: int, reward: float, 
                 next_state: np.ndarray, done: bool):
        """Store experience in replay buffer"""
        self.memory.append((state, action, reward, next_state, done))
    
    def replay(self) -> float:
        """Train on batch of experiences"""
        if len(self.memory) < self.batch_size:
            return 0.0
        
        # Sample random batch
        batch = random.sample(self.memory, self.batch_size)
        
        total_loss = 0.0
        
        for state, action, reward, next_state, done in batch:
            # Prepare states
            state = state.reshape(-1)
            next_state = next_state.reshape(-1)
            
            if len(state) < self.state_size:
                state = np.pad(state, (0, self.state_size - len(state)))
            else:
                state = state[:self.state_size]
            
            if len(next_state) < self.state_size:
                next_state = np.pad(next_state, (0, self.state_size - len(next_state)))
            else:
                next_state = next_state[:self.state_size]
            
            # Current Q-values
            current_q = self.predict_q_values(state)
            
            # Target Q-value
            if done:
                target_q = reward
            else:
                next_q = self.predict_q_values(next_state)
                target_q = reward + self.gamma * np.max(next_q)
            
            # Update Q-value for taken action
            td_error = target_q - current_q[action]
            
            # Gradient descent update
            gradient_weights = np.outer(state, np.eye(self.action_size)[action] * td_error)
            gradient_bias = np.eye(self.action_size)[action] * td_error
            
            self.weights += self.learning_rate * gradient_weights
            self.bias += self.learning_rate * gradient_bias
            
            total_loss += abs(td_error)
        
        # Decay epsilon
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay
        
        return total_loss / self.batch_size
    
    def train_episode(self, environment, max_steps: int = 1000) -> Dict[str, Any]:
        """Train for one episode"""
        state = environment.reset()
        episode_reward = 0
        steps = 0
        
        for step in range(max_steps):
            # Select and perform action
            action = self.get_action(state, training=True)
            next_state, reward, done, info = environment.step(action)
            
            # Store experience
            self.remember(state, action, reward, next_state, done)
            
            # Learn from experience
            loss = self.replay()
            
            episode_reward += reward
            steps += 1
            state = next_state
            
            if done:
                break
        
        self.episode_rewards.append(episode_reward)
        self.episode_lengths.append(steps)
        
        return {
            'episode_reward': episode_reward,
            'steps': steps,
            'epsilon': self.epsilon,
            'avg_reward_last_100': np.mean(self.episode_rewards[-100:]) if self.episode_rewards else 0
        }
    
    def train(self, environment, episodes: int = 100, verbose: bool = True) -> Dict[str, List]:
        """Train agent for multiple episodes"""
        training_history = {
            'rewards': [],
            'steps': [],
            'epsilons': []
        }
        
        for episode in range(episodes):
            result = self.train_episode(environment)
            
            training_history['rewards'].append(result['episode_reward'])
            training_history['steps'].append(result['steps'])
            training_history['epsilons'].append(result['epsilon'])
            
            if verbose and (episode + 1) % 10 == 0:
                print(f"Episode {episode + 1}/{episodes}")
                print(f"  Reward: {result['episode_reward']:.2f}")
                print(f"  Steps: {result['steps']}")
                print(f"  Epsilon: {result['epsilon']:.3f}")
                print(f"  Avg Reward (last 100): {result['avg_reward_last_100']:.2f}")
        
        return training_history
    
    def save_policy(self, filepath: str):
        """Save learned policy"""
        np.savez(filepath, weights=self.weights, bias=self.bias, 
                epsilon=self.epsilon, episode_rewards=self.episode_rewards)
    
    def load_policy(self, filepath: str):
        """Load learned policy"""
        data = np.load(filepath)
        self.weights = data['weights']
        self.bias = data['bias']
        self.epsilon = float(data['epsilon'])
        self.episode_rewards = data['episode_rewards'].tolist()
