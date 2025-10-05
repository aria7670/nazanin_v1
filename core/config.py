"""
Configuration management for the bot system
"""

import json
import os
from typing import Dict, Any


class Config:
    """Centralized configuration management"""
    
    def __init__(self, config_file: str = "config.json"):
        self.config_file = config_file
        self.config: Dict[str, Any] = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file or use defaults"""
        default_config = {
            "bot_name": "Nazanin v1",
            "version": "1.0.0",
            "brain_simulation": {
                "enabled": True,
                "neuron_count": 1000,
                "learning_rate": 0.01,
                "memory_capacity": 10000
            },
            "quantum": {
                "enabled": True,
                "qubit_count": 8,
                "simulation_shots": 1024
            },
            "neural_network": {
                "enabled": True,
                "hidden_layers": [128, 64, 32],
                "activation": "relu",
                "optimizer": "adam"
            },
            "agent": {
                "enabled": True,
                "max_iterations": 100,
                "exploration_rate": 0.1
            }
        }
        
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    loaded_config = json.load(f)
                    default_config.update(loaded_config)
            except Exception as e:
                print(f"Warning: Could not load config file: {e}")
        
        return default_config
    
    def save_config(self):
        """Save current configuration to file"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving config: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value
    
    def set(self, key: str, value: Any):
        """Set configuration value"""
        keys = key.split('.')
        config = self.config
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        config[keys[-1]] = value
