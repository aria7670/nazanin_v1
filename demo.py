"""
Nazanin Demo Script
Demonstrates the capabilities of all advanced AI systems
"""

import asyncio
import json
import logging
from datetime import datetime

# Import all systems
from brain_simulation import BrainSimulation
from quantum_agent import QuantumAgent
from neural_agent import NeuralAgent

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def demo_brain_simulation():
    """Demonstrate brain simulation capabilities"""
    
    print("\n" + "="*80)
    print("🧠 BRAIN SIMULATION DEMO")
    print("="*80)
    
    config = {
        'emotion_update_interval': 300,
        'cognition_depth': 5,
        'memory_capacity': 10000
    }
    
    brain = BrainSimulation(config)
    
    # Test 1: Process simple information
    print("\n📝 Test 1: Processing Information")
    result1 = await brain.process(
        "Breaking news: Major AI breakthrough announced today!",
        context={'importance': 0.9}
    )
    
    print(f"✅ Dominant Emotion: {result1['dominant_emotion']}")
    print(f"✅ Cognitive Analysis:")
    print(f"   - Complexity: {result1['cognitive_analysis']['complexity']:.2f}")
    print(f"   - Importance: {result1['cognitive_analysis']['importance']:.2f}")
    print(f"   - Requires Action: {result1['cognitive_analysis']['requires_action']}")
    
    # Test 2: Decision making
    print("\n🎯 Test 2: Decision Making")
    options = [
        {'name': 'Option A: Tweet immediately', 'feasible': True, 'expected_value': 0.8, 'risk': 0.3},
        {'name': 'Option B: Research more', 'feasible': True, 'expected_value': 0.7, 'risk': 0.1},
        {'name': 'Option C: Wait and see', 'feasible': True, 'expected_value': 0.5, 'risk': 0.05},
    ]
    
    decision = await brain.decision_system.make_decision(options, context={'urgency': 'high'})
    
    print(f"✅ Decision: {decision['decision']['name']}")
    print(f"✅ Confidence: {decision['confidence']:.2f}")
    print(f"✅ Reasoning:")
    print(f"   - Cognitive Score: {decision['reasoning']['cognitive_score']:.2f}")
    print(f"   - Emotional Score: {decision['reasoning']['emotional_score']:.2f}")
    
    # Test 3: Emotional state
    print("\n🎭 Test 3: Current Emotional State")
    state = await brain.get_state()
    
    print("✅ Top 5 Emotions:")
    emotions = sorted(state['emotions'].items(), key=lambda x: x[1], reverse=True)[:5]
    for emotion, value in emotions:
        print(f"   - {emotion}: {value:.1f}")
    
    print(f"\n✅ Cognition Metrics:")
    print(f"   - Attention Level: {state['cognition']['attention_level']:.1f}")
    print(f"   - Creativity Level: {state['cognition']['creativity_level']:.1f}")
    print(f"   - Long-term Memory: {state['cognition']['long_term_memory_size']} items")


async def demo_quantum_agent():
    """Demonstrate quantum agent capabilities"""
    
    print("\n" + "="*80)
    print("⚛️ QUANTUM AGENT DEMO")
    print("="*80)
    
    config = {
        'quantum_states': 64,
        'entanglement_enabled': True,
        'superposition_layers': 3
    }
    
    quantum = QuantumAgent(config)
    
    # Test 1: Quantum processing
    print("\n📊 Test 1: Quantum State Processing")
    data = [0.5, 0.7, 0.3, 0.9, 0.2, 0.8, 0.6, 0.4]
    
    result1 = await quantum.process_quantum(data)
    
    print(f"✅ Quantum Entropy: {result1['quantum_entropy']:.4f}")
    print(f"✅ Measurement Result: {result1['measurement']}")
    print(f"✅ Top 5 Probabilities: {result1['probabilities'][:5]}")
    
    # Test 2: Quantum decision making
    print("\n🎯 Test 2: Quantum Decision Making")
    options = [
        {'name': 'Post about AI safety', 'relevance': 0.9, 'engagement_score': 0.7, 'risk': 0.2},
        {'name': 'Post about quantum computing', 'relevance': 0.8, 'engagement_score': 0.6, 'risk': 0.3},
        {'name': 'Post about geopolitics', 'relevance': 0.7, 'engagement_score': 0.8, 'risk': 0.5},
    ]
    
    decision = await quantum.quantum_decision(options)
    
    print(f"✅ Quantum Decision: {decision['decision']['name']}")
    print(f"✅ Confidence: {decision['confidence']:.4f}")
    print(f"✅ Quantum Entropy: {decision['quantum_analysis']['entropy']:.4f}")
    
    # Test 3: Pattern recognition
    print("\n🔍 Test 3: Quantum Pattern Recognition")
    
    # Learn some patterns
    await quantum.learn_quantum_pattern([0.9, 0.8, 0.7, 0.6], 'trending_up')
    await quantum.learn_quantum_pattern([0.3, 0.4, 0.5, 0.6], 'trending_down')
    await quantum.learn_quantum_pattern([0.5, 0.5, 0.5, 0.5], 'stable')
    
    # Test recognition
    test_pattern = [0.85, 0.75, 0.65, 0.55]
    recognition = await quantum.recognize_quantum_pattern(test_pattern)
    
    print(f"✅ Recognized Pattern: {recognition['label']}")
    print(f"✅ Confidence: {recognition['confidence']:.4f}")


async def demo_neural_agent():
    """Demonstrate neural agent capabilities"""
    
    print("\n" + "="*80)
    print("🧬 NEURAL AGENT DEMO")
    print("="*80)
    
    config = {
        'hidden_layers': [512, 256, 128],
        'learning_rate': 0.001
    }
    
    neural = NeuralAgent(config)
    
    # Test 1: Content analysis
    print("\n📝 Test 1: Content Analysis")
    
    contents = [
        "This AI breakthrough is absolutely amazing! Game-changing technology!",
        "Another day, another AI announcement. Nothing special here.",
        "Disappointing results from the AI research. Expected much more."
    ]
    
    for i, content in enumerate(contents, 1):
        analysis = await neural.analyze_content(content)
        
        print(f"\n✅ Content {i}:")
        print(f"   Text: {content[:50]}...")
        print(f"   Sentiment: {analysis['sentiment']['sentiment']}")
        print(f"   Confidence: {analysis['sentiment']['confidence']:.2f}")
        print(f"   Engagement Score: {analysis['engagement_prediction']['overall_score']:.2f}")
        print(f"   Recommendation: {analysis['recommendation']}")
    
    # Test 2: Learning from feedback
    print("\n📊 Test 2: Learning from Feedback")
    
    test_content = "Breaking: New AI model achieves human-level performance!"
    
    # Simulate actual metrics
    actual_metrics = {
        'likes': 150,
        'shares': 45,
        'comments': 23,
        'saves': 12
    }
    
    print(f"✅ Learning from performance:")
    print(f"   Likes: {actual_metrics['likes']}")
    print(f"   Shares: {actual_metrics['shares']}")
    print(f"   Comments: {actual_metrics['comments']}")
    
    await neural.learn_from_feedback(test_content, actual_metrics)
    
    print(f"✅ Neural agent updated its model!")
    
    # Test 3: Performance metrics
    print("\n📈 Test 3: Neural Agent Performance")
    
    metrics = await neural.get_performance_metrics()
    
    print(f"✅ Training Statistics:")
    print(f"   Total Experiences: {metrics['content_optimizer']['total_experiences']}")
    print(f"   Training Iterations: {metrics['content_optimizer']['training_iterations']}")
    print(f"   Sentiment Model Trained: {metrics['sentiment_trained']}")


async def demo_integrated_system():
    """Demonstrate all systems working together"""
    
    print("\n" + "="*80)
    print("🎯 INTEGRATED SYSTEM DEMO")
    print("="*80)
    
    # Initialize all systems
    brain_config = {
        'emotion_update_interval': 300,
        'cognition_depth': 5,
        'memory_capacity': 10000
    }
    
    quantum_config = {
        'quantum_states': 64,
        'entanglement_enabled': True,
        'superposition_layers': 3
    }
    
    neural_config = {
        'hidden_layers': [512, 256, 128],
        'learning_rate': 0.001
    }
    
    brain = BrainSimulation(brain_config)
    quantum = QuantumAgent(quantum_config)
    neural = NeuralAgent(neural_config)
    
    # Scenario: Deciding whether to post a tweet
    print("\n📝 Scenario: Should we post this tweet?")
    
    tweet_content = "AI is rapidly transforming industries. The future is closer than we think!"
    
    print(f"\nProposed Tweet: {tweet_content}")
    
    # Step 1: Brain processes the content
    print("\n🧠 Step 1: Brain Processing...")
    brain_result = await brain.process(tweet_content, context={'importance': 0.8})
    print(f"   Emotional Response: {brain_result['dominant_emotion']}")
    print(f"   Cognitive Importance: {brain_result['cognitive_analysis']['importance']:.2f}")
    
    # Step 2: Neural agent analyzes content
    print("\n🧬 Step 2: Neural Analysis...")
    neural_result = await neural.analyze_content(tweet_content)
    print(f"   Sentiment: {neural_result['sentiment']['sentiment']}")
    print(f"   Predicted Engagement: {neural_result['engagement_prediction']['overall_score']:.2f}")
    
    # Step 3: Quantum agent makes decision
    print("\n⚛️ Step 3: Quantum Decision...")
    
    options = [
        {
            'name': 'Post now',
            'relevance': brain_result['cognitive_analysis']['importance'],
            'engagement': neural_result['engagement_prediction']['overall_score'],
            'risk': 0.2
        },
        {
            'name': 'Revise and post later',
            'relevance': 0.7,
            'engagement': 0.8,
            'risk': 0.1
        },
        {
            'name': 'Skip this tweet',
            'relevance': 0.3,
            'engagement': 0.0,
            'risk': 0.0
        }
    ]
    
    decision = await quantum.quantum_decision(options)
    print(f"   Decision: {decision['decision']['name']}")
    print(f"   Confidence: {decision['confidence']:.4f}")
    
    # Final recommendation
    print("\n✅ FINAL RECOMMENDATION:")
    
    if decision['confidence'] > 0.7:
        print(f"   🟢 {decision['decision']['name']} (High Confidence)")
    elif decision['confidence'] > 0.5:
        print(f"   🟡 {decision['decision']['name']} (Medium Confidence)")
    else:
        print(f"   🔴 {decision['decision']['name']} (Low Confidence)")
    
    print("\n   Reasoning:")
    print(f"   - Brain thinks it's {brain_result['dominant_emotion']}")
    print(f"   - Neural predicts {neural_result['engagement_prediction']['overall_score']:.0%} engagement")
    print(f"   - Quantum confidence: {decision['confidence']:.0%}")


async def demo_performance_comparison():
    """Compare performance of different decision methods"""
    
    print("\n" + "="*80)
    print("⚡ PERFORMANCE COMPARISON")
    print("="*80)
    
    import time
    
    # Initialize systems
    brain = BrainSimulation({'emotion_update_interval': 300, 'cognition_depth': 5, 'memory_capacity': 10000})
    quantum = QuantumAgent({'quantum_states': 64, 'entanglement_enabled': True, 'superposition_layers': 3})
    neural = NeuralAgent({'hidden_layers': [256, 128], 'learning_rate': 0.001})
    
    test_data = "AI breakthroughs are happening faster than ever before!"
    
    # Brain processing time
    start = time.time()
    await brain.process(test_data)
    brain_time = time.time() - start
    
    # Quantum processing time
    start = time.time()
    features = [float(ord(c)) / 1000.0 for c in test_data[:10]]
    await quantum.process_quantum(features)
    quantum_time = time.time() - start
    
    # Neural processing time
    start = time.time()
    await neural.analyze_content(test_data)
    neural_time = time.time() - start
    
    print("\n⏱️ Processing Times:")
    print(f"   Brain Simulation: {brain_time*1000:.2f}ms")
    print(f"   Quantum Agent: {quantum_time*1000:.2f}ms")
    print(f"   Neural Agent: {neural_time*1000:.2f}ms")
    
    print("\n📊 Relative Performance:")
    fastest = min(brain_time, quantum_time, neural_time)
    print(f"   Brain: {brain_time/fastest:.2f}x")
    print(f"   Quantum: {quantum_time/fastest:.2f}x")
    print(f"   Neural: {neural_time/fastest:.2f}x")


async def main():
    """Run all demos"""
    
    print("\n")
    print("╔" + "="*78 + "╗")
    print("║" + " "*20 + "NAZANIN ADVANCED AI SYSTEMS DEMO" + " "*26 + "║")
    print("╚" + "="*78 + "╝")
    
    try:
        # Run individual demos
        await demo_brain_simulation()
        await asyncio.sleep(1)
        
        await demo_quantum_agent()
        await asyncio.sleep(1)
        
        await demo_neural_agent()
        await asyncio.sleep(1)
        
        # Run integrated demo
        await demo_integrated_system()
        await asyncio.sleep(1)
        
        # Performance comparison
        await demo_performance_comparison()
        
        print("\n" + "="*80)
        print("✅ ALL DEMOS COMPLETED SUCCESSFULLY!")
        print("="*80)
        print("\n🎉 Nazanin's advanced AI systems are working perfectly!\n")
        
    except Exception as e:
        print(f"\n❌ Error during demo: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    asyncio.run(main())
