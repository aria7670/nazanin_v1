#!/usr/bin/env python3
"""
Quick test script for Nazanin v1
"""

import sys
import numpy as np

print("=" * 60)
print("🧪 Testing Nazanin v1 Systems")
print("=" * 60)

# Test 1: Core modules
print("\n1️⃣  Testing Core Modules...")
try:
    from core import Config, Logger
    logger = Logger("TestBot")
    config = Config()
    print("   ✅ Core modules: PASSED")
except Exception as e:
    print(f"   ❌ Core modules: FAILED - {e}")
    sys.exit(1)

# Test 2: Brain simulation
print("\n2️⃣  Testing Brain Simulation...")
try:
    from brain_simulation import BrainSimulator
    brain = BrainSimulator(neuron_count=100, learning_rate=0.01)
    result = brain.process_input("test input")
    assert 'firing_pattern' in result
    print(f"   ✅ Brain simulation: PASSED (neurons: {brain.neuron_count})")
except Exception as e:
    print(f"   ❌ Brain simulation: FAILED - {e}")
    sys.exit(1)

# Test 3: Quantum system
print("\n3️⃣  Testing Quantum System...")
try:
    from quantum_system import QuantumProcessor
    qp = QuantumProcessor(qubit_count=4)
    qp.apply_to_qubit(0, 'H')
    qp.create_bell_state(0, 1)
    results = qp.measure_all()
    print(f"   ✅ Quantum system: PASSED (qubits: {qp.qubit_count})")
except Exception as e:
    print(f"   ❌ Quantum system: FAILED - {e}")
    sys.exit(1)

# Test 4: Neural network
print("\n4️⃣  Testing Neural Network...")
try:
    from neural_network import NeuralNetwork
    nn = NeuralNetwork(architecture=[5, 10, 5])
    X = np.random.randn(10, 5)
    predictions = nn.predict(X)
    assert predictions.shape == (10, 5)
    print(f"   ✅ Neural network: PASSED (architecture: {nn.architecture})")
except Exception as e:
    print(f"   ❌ Neural network: FAILED - {e}")
    sys.exit(1)

# Test 5: Agent system
print("\n5️⃣  Testing Agent System...")
try:
    from agent_system import IntelligentAgent
    agent = IntelligentAgent(agent_id="test_agent")
    perception = agent.perceive("test observation")
    reasoning = agent.reason("test problem")
    decision = agent.decide(["option1", "option2"])
    print(f"   ✅ Agent system: PASSED (agent: {agent.agent_id})")
except Exception as e:
    print(f"   ❌ Agent system: FAILED - {e}")
    sys.exit(1)

# Test 6: Integration layer
print("\n6️⃣  Testing Integration Layer...")
try:
    from integration import UnifiedAISystem
    ai = UnifiedAISystem()
    result = ai.process("test input", task_type="general")
    assert 'systems' in result
    assert 'combined_confidence' in result
    print(f"   ✅ Integration layer: PASSED")
except Exception as e:
    print(f"   ❌ Integration layer: FAILED - {e}")
    sys.exit(1)

# Test 7: Main bot
print("\n7️⃣  Testing Main Bot...")
try:
    from bot import NazaninBot
    bot = NazaninBot()
    bot.start()
    result = bot.process("Hello", task_type="general")
    status = bot.get_status()
    bot.stop()
    print(f"   ✅ Main bot: PASSED (interactions: {status['interactions']})")
except Exception as e:
    print(f"   ❌ Main bot: FAILED - {e}")
    sys.exit(1)

# All tests passed
print("\n" + "=" * 60)
print("✅ All Tests PASSED!")
print("=" * 60)
print("\n🎉 Nazanin v1 is ready to use!")
print("\nTo start the bot in interactive mode:")
print("  python3 bot.py --interactive")
print("\nTo process a single input:")
print("  python3 bot.py --process 'your input here' --task-type general")
print("\nFor examples:")
print("  python3 examples/basic_usage.py")
print("  python3 examples/advanced_usage.py")
print()
