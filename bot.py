"""
Nazanin v1 - Advanced Modular AI Bot
Main bot interface and controller
"""

import sys
import json
from typing import Any, Dict, Optional
from pathlib import Path

from core import Config, Logger
from integration import UnifiedAISystem


class NazaninBot:
    """Main bot controller integrating all AI systems"""
    
    def __init__(self, config_file: str = "config.json"):
        """Initialize the bot"""
        # Load configuration
        self.config = Config(config_file)
        
        # Initialize logger
        self.logger = Logger("NazaninBot")
        self.logger.info("=" * 60)
        self.logger.info("Nazanin v1 - Advanced Modular AI Bot")
        self.logger.info("=" * 60)
        
        # Initialize unified AI system
        system_config = {
            'brain_neuron_count': self.config.get('brain_simulation.neuron_count', 1000),
            'brain_learning_rate': self.config.get('brain_simulation.learning_rate', 0.01),
            'quantum_qubits': self.config.get('quantum.qubit_count', 8),
            'quantum_shots': self.config.get('quantum.simulation_shots', 1024),
            'neural_architecture': self.config.get('neural_network.hidden_layers', [10, 64, 32, 10]),
            'neural_activation': self.config.get('neural_network.activation', 'relu')
        }
        
        self.ai_system = UnifiedAISystem(system_config)
        self.logger.info("AI System initialized successfully")
        
        # Bot state
        self.is_running = False
        self.interaction_count = 0
    
    def start(self):
        """Start the bot"""
        self.is_running = True
        self.logger.info("Bot started")
        print("\n🤖 Nazanin v1 is ready!")
        print("=" * 60)
        self._print_capabilities()
        print("=" * 60)
    
    def stop(self):
        """Stop the bot"""
        self.is_running = False
        self.logger.info("Bot stopped")
        print("\n👋 Goodbye!")
    
    def _print_capabilities(self):
        """Print bot capabilities"""
        print("\n🧠 Integrated Systems:")
        print("  • Brain Simulation - Neural activity and memory")
        print("  • Quantum Processor - Quantum computing capabilities")
        print("  • Neural Network - Deep learning and pattern recognition")
        print("  • Intelligent Agent - Reasoning and decision-making")
        
        print("\n✨ Capabilities:")
        print("  • Pattern recognition and classification")
        print("  • Quantum optimization and search")
        print("  • Memory and learning")
        print("  • Intelligent reasoning and planning")
        print("  • Decision making under uncertainty")
    
    def process(self, user_input: str, task_type: str = "general") -> Dict[str, Any]:
        """Process user input"""
        self.interaction_count += 1
        self.logger.info(f"Processing interaction #{self.interaction_count}")
        
        try:
            # Process through unified AI system
            result = self.ai_system.process(user_input, task_type)
            
            self.logger.info("Processing successful")
            return result
            
        except Exception as e:
            self.logger.error(f"Error processing input: {e}")
            return {
                'error': str(e),
                'status': 'failed'
            }
    
    def learn_from_interaction(self, user_input: str, feedback: Any):
        """Learn from user interaction"""
        try:
            self.ai_system.learn(user_input, feedback, task_type="learning")
            self.logger.info("Learning from interaction complete")
        except Exception as e:
            self.logger.error(f"Error during learning: {e}")
    
    def get_status(self) -> Dict[str, Any]:
        """Get bot status"""
        return {
            'bot_name': self.config.get('bot_name'),
            'version': self.config.get('version'),
            'running': self.is_running,
            'interactions': self.interaction_count,
            'ai_system_status': self.ai_system.get_system_status()
        }
    
    def optimize(self):
        """Optimize bot systems"""
        self.logger.info("Optimizing bot systems...")
        self.ai_system.optimize()
        self.logger.info("Optimization complete")
    
    def save_state(self, filepath: str = "bot_state.json"):
        """Save bot state"""
        self.logger.info(f"Saving bot state to {filepath}")
        
        state = {
            'interactions': self.interaction_count,
            'config': self.config.config
        }
        
        # Save AI system state
        ai_state_file = filepath.replace('.json', '_ai.json')
        self.ai_system.save_state(ai_state_file)
        
        # Save bot state
        with open(filepath, 'w') as f:
            json.dump(state, f, indent=2)
        
        self.logger.info("State saved successfully")
    
    def interactive_mode(self):
        """Run bot in interactive CLI mode"""
        self.start()
        
        print("\n💬 Interactive Mode")
        print("Commands:")
        print("  - Type your message to interact")
        print("  - 'status' - Show bot status")
        print("  - 'optimize' - Optimize bot systems")
        print("  - 'save' - Save bot state")
        print("  - 'help' - Show this help message")
        print("  - 'quit' or 'exit' - Exit the bot")
        print()
        
        while self.is_running:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                # Handle commands
                if user_input.lower() in ['quit', 'exit']:
                    self.stop()
                    break
                
                elif user_input.lower() == 'status':
                    status = self.get_status()
                    print("\n📊 Bot Status:")
                    print(json.dumps(status, indent=2, default=str))
                    print()
                    continue
                
                elif user_input.lower() == 'optimize':
                    print("\n⚙️  Optimizing systems...")
                    self.optimize()
                    print("✅ Optimization complete")
                    print()
                    continue
                
                elif user_input.lower() == 'save':
                    print("\n💾 Saving state...")
                    self.save_state()
                    print("✅ State saved")
                    print()
                    continue
                
                elif user_input.lower() == 'help':
                    self._print_capabilities()
                    continue
                
                # Process normal input
                print("\n🤔 Processing...")
                result = self.process(user_input)
                
                # Display result
                print("\n🤖 Nazanin:", end=" ")
                
                if 'error' in result:
                    print(f"❌ Error: {result['error']}")
                else:
                    # Extract and display primary result
                    if 'primary_result' in result:
                        primary = result['primary_result']
                        if isinstance(primary, dict):
                            print(json.dumps(primary, indent=2, default=str))
                        else:
                            print(primary)
                    else:
                        print(json.dumps(result, indent=2, default=str))
                    
                    print(f"\n✨ Confidence: {result.get('combined_confidence', 0):.2%}")
                    print(f"🔧 Systems used: {', '.join(result.get('systems', []))}")
                
                print()
                
            except KeyboardInterrupt:
                print("\n\n⚠️  Interrupted by user")
                self.stop()
                break
            
            except Exception as e:
                self.logger.error(f"Error in interactive mode: {e}")
                print(f"\n❌ Error: {e}")
                print()


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Nazanin v1 - Advanced Modular AI Bot"
    )
    parser.add_argument(
        '--config', 
        type=str, 
        default='config.json',
        help='Path to configuration file'
    )
    parser.add_argument(
        '--interactive', 
        action='store_true',
        help='Run in interactive mode'
    )
    parser.add_argument(
        '--process',
        type=str,
        help='Process a single input and exit'
    )
    parser.add_argument(
        '--task-type',
        type=str,
        default='general',
        help='Task type for processing'
    )
    
    args = parser.parse_args()
    
    # Create bot
    bot = NazaninBot(args.config)
    
    if args.interactive or (not args.process):
        # Interactive mode
        bot.interactive_mode()
    
    elif args.process:
        # Process single input
        bot.start()
        result = bot.process(args.process, args.task_type)
        print(json.dumps(result, indent=2, default=str))
        bot.stop()


if __name__ == "__main__":
    main()
