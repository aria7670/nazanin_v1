"""
Basic usage examples for Nazanin v1
"""

import sys
sys.path.insert(0, '..')

from bot import NazaninBot


def example_simple_interaction():
    """Simple interaction with the bot"""
    print("=" * 60)
    print("Example 1: Simple Interaction")
    print("=" * 60)
    
    bot = NazaninBot()
    bot.start()
    
    # Process some inputs
    inputs = [
        "Hello, how are you?",
        "What is 2 + 2?",
        "Tell me about artificial intelligence"
    ]
    
    for user_input in inputs:
        print(f"\nUser: {user_input}")
        result = bot.process(user_input, task_type="general")
        
        print(f"Bot: Systems used: {result.get('systems', [])}")
        print(f"     Confidence: {result.get('combined_confidence', 0):.2%}")
    
    bot.stop()


def example_specific_tasks():
    """Examples of specific task types"""
    print("\n" + "=" * 60)
    print("Example 2: Specific Task Types")
    print("=" * 60)
    
    bot = NazaninBot()
    bot.start()
    
    tasks = [
        ("Pattern in data: 1, 2, 4, 8, 16, ?", "pattern_recognition"),
        ("Optimize path from A to B", "optimization"),
        ("Should I invest in stocks or bonds?", "decision_making"),
        ("Predict weather tomorrow", "prediction")
    ]
    
    for task_input, task_type in tasks:
        print(f"\nTask Type: {task_type}")
        print(f"Input: {task_input}")
        
        result = bot.process(task_input, task_type=task_type)
        
        print(f"Primary System: {result.get('primary_system', 'N/A')}")
        print(f"Confidence: {result.get('combined_confidence', 0):.2%}")
        print(f"All Systems: {result.get('systems', [])}")
    
    bot.stop()


def example_learning():
    """Example of learning from interactions"""
    print("\n" + "=" * 60)
    print("Example 3: Learning")
    print("=" * 60)
    
    bot = NazaninBot()
    bot.start()
    
    # Simulate learning from feedback
    interactions = [
        ("What is AI?", "Artificial Intelligence is..."),
        ("Define machine learning", "Machine learning is..."),
        ("Explain neural networks", "Neural networks are...")
    ]
    
    for user_input, feedback in interactions:
        print(f"\nLearning from: {user_input}")
        bot.learn_from_interaction(user_input, feedback)
    
    # Check memory
    print("\nChecking learned information...")
    result = bot.process("Tell me about AI", task_type="memory")
    print(f"Response confidence: {result.get('combined_confidence', 0):.2%}")
    
    bot.stop()


def example_system_status():
    """Example of checking system status"""
    print("\n" + "=" * 60)
    print("Example 4: System Status")
    print("=" * 60)
    
    bot = NazaninBot()
    bot.start()
    
    # Do some processing
    bot.process("Test input 1")
    bot.process("Test input 2")
    bot.process("Test input 3")
    
    # Get status
    status = bot.get_status()
    
    print("\n📊 Bot Status:")
    print(f"  Name: {status['bot_name']}")
    print(f"  Version: {status['version']}")
    print(f"  Running: {status['running']}")
    print(f"  Interactions: {status['interactions']}")
    
    print("\n🧠 AI System Status:")
    ai_status = status['ai_system_status']
    print(f"  Brain neurons: {ai_status['brain']['neurons']}")
    print(f"  Brain memory: {ai_status['brain']['memory_count']}")
    print(f"  Quantum qubits: {ai_status['quantum']['qubit_count']}")
    print(f"  Neural architecture: {ai_status['neural']['architecture']}")
    print(f"  Agent knowledge: {ai_status['agent']['knowledge_items']}")
    
    bot.stop()


if __name__ == "__main__":
    print("🤖 Nazanin v1 - Example Scripts")
    print()
    
    # Run examples
    example_simple_interaction()
    example_specific_tasks()
    example_learning()
    example_system_status()
    
    print("\n" + "=" * 60)
    print("✅ All examples completed!")
    print("=" * 60)
