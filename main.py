"""
Nazanin - Advanced Modular AI Bot with Brain Simulation
Main orchestrator integrating all systems
"""

import asyncio
import logging
import json
import sys
from datetime import datetime, timedelta
from typing import Dict, Any

# Core systems
from src.core import SheetsManager, APIManager
from src.agents import AgentOrchestrator

# Platform systems
from src.platforms import TwitterSystem, TelegramSystem

# Advanced AI systems
from src.ai import BrainSimulation, QuantumAgent, NeuralAgent

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('nazanin.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)


class Nazanin:
    """Main orchestrator for the Nazanin AI system"""
    
    def __init__(self, config_path: str = 'config.json'):
        self.config_path = config_path
        self.config = None
        
        # Core systems
        self.sheets_manager = None
        self.api_manager = None
        self.agent_orchestrator = None
        
        # Platform systems
        self.twitter_system = None
        self.telegram_system = None
        
        # Advanced AI systems
        self.brain_simulation = None
        self.quantum_agent = None
        self.neural_agent = None
        
        # State
        self.is_running = False
        self.tasks = []
        
    async def initialize(self):
        """Initialize all systems"""
        
        logger.info("=" * 80)
        logger.info("🚀 INITIALIZING NAZANIN - ADVANCED MODULAR AI BOT")
        logger.info("=" * 80)
        
        # Load configuration
        with open(self.config_path, 'r') as f:
            self.config = json.load(f)
        
        logger.info("✅ Configuration loaded")
        
        # Initialize Google Sheets Manager
        logger.info("\n📊 Initializing Google Sheets Manager...")
        self.sheets_manager = SheetsManager(
            self.config['google_sheets']['credentials_file'],
            self.config['google_sheets']['master_spreadsheet_id']
        )
        await self.sheets_manager.initialize()
        
        # Initialize API Manager
        logger.info("\n🤖 Initializing AI API Manager...")
        self.api_manager = APIManager()
        api_keys = await self.sheets_manager.get_api_keys()
        await self.api_manager.initialize(api_keys)
        
        # Initialize Agent Orchestrator
        logger.info("\n🎯 Initializing Agent Orchestrator...")
        self.agent_orchestrator = AgentOrchestrator(
            self.api_manager,
            self.sheets_manager
        )
        await self.agent_orchestrator.initialize()
        
        # Initialize Brain Simulation
        if self.config.get('brain_simulation', {}).get('enabled', True):
            logger.info("\n🧠 Initializing Brain Simulation System...")
            self.brain_simulation = BrainSimulation(
                self.config['brain_simulation']
            )
            logger.info("✅ Brain simulation initialized with:")
            logger.info(f"   - Emotion system with {len(self.brain_simulation.emotion_system.emotions)} emotions")
            logger.info(f"   - Cognition system with memory capacity: {self.brain_simulation.cognition_system.memory_capacity}")
            logger.info(f"   - Decision-making system")
        
        # Initialize Quantum Agent
        if self.config.get('quantum_agent', {}).get('enabled', True):
            logger.info("\n⚛️ Initializing Quantum Agent System...")
            self.quantum_agent = QuantumAgent(
                self.config['quantum_agent']
            )
            logger.info("✅ Quantum agent initialized with:")
            logger.info(f"   - {self.quantum_agent.num_qubits} quantum states")
            logger.info(f"   - Entanglement: {self.quantum_agent.entanglement_enabled}")
            logger.info(f"   - Superposition layers: {self.quantum_agent.superposition_layers}")
        
        # Initialize Neural Agent
        if self.config.get('neural_agent', {}).get('enabled', True):
            logger.info("\n🧬 Initializing Neural Agent System...")
            self.neural_agent = NeuralAgent(
                self.config['neural_agent']
            )
            logger.info("✅ Neural agent initialized with:")
            logger.info(f"   - Hidden layers: {self.neural_agent.hidden_layers}")
            logger.info(f"   - Learning rate: {self.neural_agent.learning_rate}")
        
        # Initialize Twitter System
        if self.config.get('twitter', {}).get('api_key'):
            logger.info("\n🐦 Initializing Twitter System...")
            self.twitter_system = TwitterSystem(
                self.config['twitter'],
                self.sheets_manager,
                self.agent_orchestrator
            )
            await self.twitter_system.initialize()
        
        # Initialize Telegram System
        if self.config.get('telegram', {}).get('bot_token'):
            logger.info("\n📱 Initializing Telegram System...")
            self.telegram_system = TelegramSystem(
                self.config['telegram'],
                self.sheets_manager,
                self.agent_orchestrator,
                self.brain_simulation
            )
            await self.telegram_system.initialize()
        
        self.is_running = True
        
        logger.info("\n" + "=" * 80)
        logger.info("✅ ALL SYSTEMS INITIALIZED SUCCESSFULLY")
        logger.info("=" * 80)
        logger.info("\n🎉 Nazanin is ready to operate!\n")
        
    async def start_background_loops(self):
        """Start all background loops"""
        
        logger.info("🔄 Starting background loops...")
        
        # Brain simulation update loop
        if self.brain_simulation:
            self.tasks.append(
                asyncio.create_task(self.brain_simulation.update_loop())
            )
            logger.info("✅ Brain simulation loop started")
        
        # Twitter monitoring and posting loops
        if self.twitter_system:
            self.tasks.append(
                asyncio.create_task(self.twitter_loop())
            )
            logger.info("✅ Twitter loop started")
        
        # News collection loop
        self.tasks.append(
            asyncio.create_task(self.news_loop())
        )
        logger.info("✅ News collection loop started")
        
        # Maintenance loop
        self.tasks.append(
            asyncio.create_task(self.maintenance_loop())
        )
        logger.info("✅ Maintenance loop started")
        
        # Telegram bot (runs until disconnected)
        if self.telegram_system:
            self.tasks.append(
                asyncio.create_task(self.telegram_system.run())
            )
            logger.info("✅ Telegram bot loop started")
        
    async def twitter_loop(self):
        """Main Twitter loop"""
        
        logger.info("🐦 Twitter loop running...")
        
        while self.is_running:
            try:
                # Reset daily counters
                await self.twitter_system.daily_reset()
                
                # Check mentions every 10 minutes
                mentions = await self.twitter_system.monitor_mentions()
                
                for mention in mentions:
                    await self.twitter_system.respond_to_mention(mention)
                    await asyncio.sleep(30)  # Delay between responses
                
                # Report to Telegram
                if self.telegram_system:
                    stats = await self.twitter_system.get_stats()
                    await self.telegram_system.report(
                        f"🐦 Twitter: {stats['tweets_today']} توییت، {stats['replies_today']} پاسخ"
                    )
                
            except Exception as e:
                logger.error(f"❌ Error in Twitter loop: {e}")
            
            await asyncio.sleep(600)  # 10 minutes
    
    async def news_loop(self):
        """News collection and posting loop"""
        
        logger.info("📰 News loop running...")
        
        while self.is_running:
            try:
                logger.info("📰 Collecting AI news...")
                
                if self.telegram_system:
                    await self.telegram_system.report("🔍 شروع جمع‌آوری اخبار AI...")
                
                # Post news tweet
                if self.twitter_system:
                    tweet_id = await self.twitter_system.post_news_tweet()
                    
                    if tweet_id:
                        logger.info(f"✅ News tweet posted: {tweet_id}")
                        
                        if self.telegram_system:
                            await self.telegram_system.report(
                                f"✅ توییت خبری منتشر شد: {tweet_id}"
                            )
                
            except Exception as e:
                logger.error(f"❌ Error in news loop: {e}")
            
            await asyncio.sleep(10800)  # 3 hours
    
    async def maintenance_loop(self):
        """Maintenance tasks loop"""
        
        logger.info("🔧 Maintenance loop running...")
        
        while self.is_running:
            try:
                # Clear cache every 6 hours
                await asyncio.sleep(21600)
                
                logger.info("🧹 Running maintenance tasks...")
                
                await self.sheets_manager.clear_cache()
                
                # Consolidate brain memory
                if self.brain_simulation:
                    await self.brain_simulation.cognition_system.consolidate_memory()
                
                # Reload API keys every 12 hours
                await asyncio.sleep(21600)
                
                logger.info("🔄 Reloading API keys...")
                api_keys = await self.sheets_manager.reload_keys()
                await self.api_manager.reload_keys(api_keys)
                
                # Send hourly stats
                if self.telegram_system:
                    stats = await self.get_system_stats()
                    await self.telegram_system.report(
                        f"📊 آمار ساعتی:\n{json.dumps(stats, indent=2, ensure_ascii=False)}"
                    )
                
            except Exception as e:
                logger.error(f"❌ Error in maintenance loop: {e}")
    
    async def get_system_stats(self) -> Dict[str, Any]:
        """Get comprehensive system statistics"""
        
        stats = {
            'timestamp': datetime.now().isoformat(),
            'systems': {
                'brain_simulation': False,
                'quantum_agent': False,
                'neural_agent': False,
                'twitter': False,
                'telegram': False
            }
        }
        
        if self.brain_simulation:
            stats['systems']['brain_simulation'] = True
            brain_state = await self.brain_simulation.get_state()
            stats['brain'] = {
                'dominant_emotion': max(
                    brain_state['emotions'].items(),
                    key=lambda x: x[1]
                )[0],
                'memory_items': brain_state['cognition']['long_term_memory_size']
            }
        
        if self.quantum_agent:
            stats['systems']['quantum_agent'] = True
        
        if self.neural_agent:
            stats['systems']['neural_agent'] = True
            neural_stats = await self.neural_agent.get_performance_metrics()
            stats['neural'] = neural_stats
        
        if self.twitter_system:
            stats['systems']['twitter'] = True
            stats['twitter'] = await self.twitter_system.get_stats()
        
        if self.telegram_system:
            stats['systems']['telegram'] = True
        
        return stats
    
    async def process_with_all_systems(self, input_data: str, context: Dict = None) -> Dict[str, Any]:
        """Process input through all advanced AI systems"""
        
        results = {
            'input': input_data,
            'timestamp': datetime.now().isoformat()
        }
        
        # Brain simulation processing
        if self.brain_simulation:
            brain_result = await self.brain_simulation.process(input_data, context)
            results['brain'] = brain_result
        
        # Quantum processing
        if self.quantum_agent:
            # Convert input to numerical features
            features = [float(ord(c)) / 1000.0 for c in input_data[:10]]
            quantum_result = await self.quantum_agent.process_quantum(features)
            results['quantum'] = quantum_result
        
        # Neural analysis
        if self.neural_agent:
            neural_result = await self.neural_agent.analyze_content(input_data)
            results['neural'] = neural_result
        
        return results
    
    async def shutdown(self):
        """Gracefully shutdown all systems"""
        
        logger.info("\n🛑 Shutting down Nazanin...")
        
        self.is_running = False
        
        # Cancel all background tasks
        for task in self.tasks:
            task.cancel()
        
        # Wait for tasks to complete
        await asyncio.gather(*self.tasks, return_exceptions=True)
        
        # Shutdown individual systems
        if self.brain_simulation:
            await self.brain_simulation.shutdown()
        
        if self.telegram_system:
            await self.telegram_system.shutdown()
        
        logger.info("✅ Nazanin shutdown complete")
    
    async def run(self):
        """Main run method"""
        
        try:
            await self.initialize()
            await self.start_background_loops()
            
            # Keep running
            while self.is_running:
                await asyncio.sleep(60)
                
        except KeyboardInterrupt:
            logger.info("\n⚠️ Received interrupt signal")
        except Exception as e:
            logger.error(f"❌ Fatal error: {e}", exc_info=True)
        finally:
            await self.shutdown()


async def main():
    """Main entry point"""
    
    nazanin = Nazanin('config.json')
    await nazanin.run()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
