"""
Advanced usage examples for Nazanin v1
"""

import sys
sys.path.insert(0, '..')

import numpy as np
from integration import UnifiedAISystem
from quantum_system import QuantumProcessor
from brain_simulation import BrainSimulator
from neural_network import NeuralNetwork, Trainer
from agent_system import IntelligentAgent, ReinforcementLearningAgent, GridWorldEnvironment


def example_quantum_computing():
    """Quantum computing examples"""
    print("=" * 60)
    print("Example 1: Quantum Computing")
    print("=" * 60)
    
    qp = QuantumProcessor(qubit_count=4)
    
    # Bell state
    print("\n1. Creating Bell State (Entanglement)")
    qp.create_bell_state(0, 1)
    print("Bell state created!")
    
    # Quantum search
    print("\n2. Quantum Search (Grover's Algorithm)")
    target = 5
    result = qp.quantum_search(target)
    print(f"Searching for state {target}, found: {result}")
    
    # QFT
    print("\n3. Quantum Fourier Transform")
    qp.reset()
    qp.quantum_fourier_transform([0, 1, 2])
    results = qp.measure_all()
    print(f"QFT measurements: {list(results.items())[:5]}")
    
    # Circuit info
    print("\n4. Circuit Information")
    info = qp.get_circuit_info()
    print(f"Circuit depth: {info['circuit_depth']}")
    print(f"Entanglements: {info['entanglements']}")


def example_brain_simulation():
    """Brain simulation examples"""
    print("\n" + "=" * 60)
    print("Example 2: Brain Simulation")
    print("=" * 60)
    
    brain = BrainSimulator(neuron_count=500, learning_rate=0.02)
    
    # Process multiple inputs
    print("\n1. Processing Inputs")
    inputs = ["pattern A", "pattern B", "pattern A", "pattern B"]
    
    for inp in inputs:
        result = brain.process_input(inp)
        print(f"Input: {inp}")
        print(f"  Total activations: {result['total_activations']}")
        print(f"  Decision: {result['decision']}")
    
    # Memory system
    print("\n2. Memory System")
    brain.memory.store_long_term("fact1", "The sky is blue")
    brain.memory.store_long_term("fact2", "Water boils at 100°C")
    
    retrieved = brain.memory.retrieve("fact1")
    print(f"Retrieved memory: {retrieved}")
    
    recent = brain.memory.get_recent_memories(2)
    print(f"Recent memories: {recent}")
    
    # Brain state
    print("\n3. Brain State")
    state = brain.get_state()
    print(f"Neurons: {state['neurons']}")
    print(f"Memory count: {state['memory_count']}")
    print(f"Working memory: {state['working_memory']}")


def example_neural_network_training():
    """Neural network training examples"""
    print("\n" + "=" * 60)
    print("Example 3: Neural Network Training")
    print("=" * 60)
    
    # Create synthetic dataset
    print("\n1. Creating Dataset")
    X_train = np.random.randn(200, 10)
    y_train = (np.sum(X_train, axis=1, keepdims=True) > 0).astype(float)
    y_train = np.tile(y_train, (1, 10))  # Match output size
    
    X_val = np.random.randn(50, 10)
    y_val = (np.sum(X_val, axis=1, keepdims=True) > 0).astype(float)
    y_val = np.tile(y_val, (1, 10))
    
    print(f"Training samples: {X_train.shape[0]}")
    print(f"Validation samples: {X_val.shape[0]}")
    
    # Create and train model
    print("\n2. Training Neural Network")
    nn = NeuralNetwork(architecture=[10, 32, 16, 10], activation='relu')
    print(nn.summary())
    
    trainer = Trainer(nn)
    history = trainer.train_with_validation(
        X_train, y_train,
        X_val, y_val,
        epochs=30,
        learning_rate=0.01,
        early_stopping_patience=10,
        verbose=False
    )
    
    print(f"\nFinal training accuracy: {history['train_accuracy'][-1]:.4f}")
    print(f"Final validation accuracy: {history['val_accuracy'][-1]:.4f}")
    
    # Evaluate
    print("\n3. Evaluation")
    metrics = nn.evaluate(X_val, y_val)
    print(f"Test loss: {metrics['loss']:.4f}")
    print(f"Test accuracy: {metrics['accuracy']:.4f}")


def example_intelligent_agent():
    """Intelligent agent examples"""
    print("\n" + "=" * 60)
    print("Example 4: Intelligent Agent")
    print("=" * 60)
    
    agent = IntelligentAgent(agent_id="advanced_agent")
    
    # Perception
    print("\n1. Perception")
    perception = agent.perceive("Complex environmental data")
    print(f"Importance: {perception['importance']:.2f}")
    
    # Reasoning
    print("\n2. Reasoning")
    problem = "How to optimize energy consumption in a smart city?"
    reasoning = agent.reason(problem)
    print(f"Problem complexity: {reasoning['analysis']['complexity']}")
    print(f"Solution confidence: {reasoning['confidence']:.2f}")
    print(f"Solution: {reasoning['solution'][:100]}...")
    
    # Decision making
    print("\n3. Decision Making")
    options = [
        "Implement solar panels",
        "Upgrade to LED lighting",
        "Install smart thermostats",
        "Use energy monitoring system"
    ]
    decision = agent.decide(options)
    print(f"Chosen option: {decision}")
    
    # Planning
    print("\n4. Planning")
    goal = {'description': 'Reduce energy consumption by 30%'}
    plan = agent.plan(goal)
    print(f"Plan steps: {len(plan)}")
    for step in plan[:3]:
        print(f"  Step {step['step_number']}: {step['action'][:50]}...")
    
    # Status
    print("\n5. Agent Status")
    status = agent.get_status()
    print(f"Knowledge items: {status['knowledge_items']}")
    print(f"Decisions made: {status['metrics']['decisions_made']}")


def example_reinforcement_learning():
    """Reinforcement learning examples"""
    print("\n" + "=" * 60)
    print("Example 5: Reinforcement Learning")
    print("=" * 60)
    
    # Create environment
    env = GridWorldEnvironment(grid_size=5)
    
    # Create RL agent
    rl_agent = ReinforcementLearningAgent(
        state_size=2,
        action_size=4,
        learning_rate=0.01
    )
    
    print("\n1. Training RL Agent")
    print("Training in GridWorld environment...")
    
    # Train
    history = rl_agent.train(env, episodes=50, verbose=False)
    
    print(f"Episodes trained: {len(history['rewards'])}")
    print(f"Average reward (last 10): {np.mean(history['rewards'][-10:]):.2f}")
    print(f"Final epsilon: {history['epsilons'][-1]:.3f}")
    
    # Test trained agent
    print("\n2. Testing Trained Agent")
    state = env.reset()
    total_reward = 0
    steps = 0
    
    for _ in range(50):
        action = rl_agent.get_action(state, training=False)
        state, reward, done, info = env.step(action)
        total_reward += reward
        steps += 1
        
        if done:
            break
    
    print(f"Test episode reward: {total_reward:.2f}")
    print(f"Steps taken: {steps}")


def example_unified_system():
    """Unified system examples"""
    print("\n" + "=" * 60)
    print("Example 6: Unified AI System")
    print("=" * 60)
    
    ai = UnifiedAISystem()
    
    # Different task types
    tasks = [
        ("Recognize pattern: 1, 1, 2, 3, 5, 8, ?", "pattern_recognition"),
        ("Find optimal route from A to E", "optimization"),
        ("Should we launch product now or wait?", "decision_making"),
        ("What will happen next?", "prediction")
    ]
    
    print("\n1. Processing Different Task Types")
    for task_input, task_type in tasks:
        print(f"\nTask: {task_type}")
        result = ai.process(task_input, task_type)
        print(f"  Systems used: {result.get('systems', [])}")
        print(f"  Primary: {result.get('primary_system', 'N/A')}")
        print(f"  Confidence: {result.get('combined_confidence', 0):.2%}")
    
    # System optimization
    print("\n2. System Optimization")
    ai.optimize()
    print("System optimized!")
    
    # System status
    print("\n3. System Status")
    status = ai.get_system_status()
    print(f"Processing history: {status['processing_history_size']} items")
    print(f"Coordinator tasks: {status['coordinator']['tasks_processed']}")


if __name__ == "__main__":
    print("🤖 Nazanin v1 - Advanced Examples")
    print()
    
    # Run advanced examples
    example_quantum_computing()
    example_brain_simulation()
    example_neural_network_training()
    example_intelligent_agent()
    example_reinforcement_learning()
    example_unified_system()
    
    print("\n" + "=" * 60)
    print("✅ All advanced examples completed!")
    print("=" * 60)
