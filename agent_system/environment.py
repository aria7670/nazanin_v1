"""
Environment for agent interaction
"""

import numpy as np
from typing import Tuple, Any, Dict, List, Optional


class Environment:
    """Simulated environment for agent learning"""
    
    def __init__(self, state_size: int = 10, action_size: int = 4):
        self.state_size = state_size
        self.action_size = action_size
        self.current_state = self.reset()
        self.episode_reward = 0
        self.step_count = 0
        self.max_steps = 1000
        
        # Environment dynamics
        self.transition_matrix = np.random.randn(state_size, action_size, state_size) * 0.1
        self.reward_function = np.random.randn(state_size, action_size) * 0.5
    
    def reset(self) -> np.ndarray:
        """Reset environment to initial state"""
        self.current_state = np.random.randn(self.state_size)
        self.episode_reward = 0
        self.step_count = 0
        return self.current_state.copy()
    
    def step(self, action: int) -> Tuple[np.ndarray, float, bool, Dict]:
        """Take a step in the environment"""
        if action < 0 or action >= self.action_size:
            raise ValueError(f"Invalid action: {action}")
        
        # Calculate next state
        transition = self.transition_matrix[:, action, :]
        noise = np.random.randn(self.state_size) * 0.1
        next_state = np.tanh(np.dot(transition.T, self.current_state) + noise)
        
        # Calculate reward
        reward = float(np.dot(self.current_state, self.reward_function[:, action]))
        reward += np.random.randn() * 0.01  # Small noise
        
        self.current_state = next_state
        self.episode_reward += reward
        self.step_count += 1
        
        # Check if episode is done
        done = self.step_count >= self.max_steps or abs(reward) > 10
        
        info = {
            'episode_reward': self.episode_reward,
            'step_count': self.step_count
        }
        
        return next_state.copy(), reward, done, info
    
    def get_state(self) -> np.ndarray:
        """Get current state"""
        return self.current_state.copy()
    
    def render(self) -> str:
        """Render environment state"""
        return f"State: {self.current_state[:3]}..., Reward: {self.episode_reward:.2f}, Steps: {self.step_count}"


class GridWorldEnvironment(Environment):
    """Grid world environment for navigation tasks"""
    
    def __init__(self, grid_size: int = 10):
        self.grid_size = grid_size
        super().__init__(state_size=2, action_size=4)  # x, y position; up, down, left, right
        
        # Goal position
        self.goal = np.array([grid_size - 1, grid_size - 1])
        self.agent_pos = np.array([0, 0])
    
    def reset(self) -> np.ndarray:
        """Reset to starting position"""
        self.agent_pos = np.array([0, 0])
        self.step_count = 0
        self.episode_reward = 0
        return self.agent_pos.astype(float)
    
    def step(self, action: int) -> Tuple[np.ndarray, float, bool, Dict]:
        """Move agent in grid world"""
        # Actions: 0=up, 1=down, 2=left, 3=right
        moves = [
            np.array([-1, 0]),  # up
            np.array([1, 0]),   # down
            np.array([0, -1]),  # left
            np.array([0, 1])    # right
        ]
        
        new_pos = self.agent_pos + moves[action]
        
        # Clip to grid boundaries
        new_pos = np.clip(new_pos, 0, self.grid_size - 1)
        
        # Calculate reward
        old_distance = np.linalg.norm(self.agent_pos - self.goal)
        new_distance = np.linalg.norm(new_pos - self.goal)
        
        # Reward shaping: encourage moving towards goal
        reward = old_distance - new_distance
        
        # Large reward for reaching goal
        if np.array_equal(new_pos, self.goal):
            reward += 10
            done = True
        else:
            done = False
        
        # Small penalty for each step
        reward -= 0.01
        
        self.agent_pos = new_pos
        self.step_count += 1
        self.episode_reward += reward
        
        # Max steps limit
        if self.step_count >= self.max_steps:
            done = True
        
        info = {
            'episode_reward': self.episode_reward,
            'step_count': self.step_count,
            'distance_to_goal': new_distance
        }
        
        return self.agent_pos.astype(float), reward, done, info
    
    def render(self) -> str:
        """Render grid world"""
        grid = [['.' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        grid[self.agent_pos[0]][self.agent_pos[1]] = 'A'
        grid[self.goal[0]][self.goal[1]] = 'G'
        
        return '\n'.join([''.join(row) for row in grid])
