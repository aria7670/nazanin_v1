"""
Human Brain Simulation System
Simulates cognitive functions, emotions, and decision-making processes
"""

import asyncio
import logging
import numpy as np
from typing import Dict, List, Any, Optional
from datetime import datetime
import json

logger = logging.getLogger(__name__)


class EmotionSystem:
    """Simulates emotional states and their dynamics"""
    
    def __init__(self):
        # Core emotions with intensity (0-100)
        self.emotions = {
            'joy': 50.0,
            'trust': 60.0,
            'fear': 10.0,
            'surprise': 30.0,
            'sadness': 5.0,
            'disgust': 5.0,
            'anger': 5.0,
            'anticipation': 40.0,
            'curiosity': 70.0,
            'confidence': 65.0
        }
        
        # Emotion decay rate
        self.decay_rate = 0.95
        
        # Baseline values (emotions tend to return to these)
        self.baseline = {
            'joy': 50.0,
            'trust': 60.0,
            'fear': 10.0,
            'surprise': 30.0,
            'sadness': 5.0,
            'disgust': 5.0,
            'anger': 5.0,
            'anticipation': 40.0,
            'curiosity': 70.0,
            'confidence': 65.0
        }
    
    def update_emotion(self, emotion: str, delta: float):
        """Update an emotion value"""
        if emotion in self.emotions:
            self.emotions[emotion] = np.clip(
                self.emotions[emotion] + delta, 
                0.0, 
                100.0
            )
            logger.debug(f"🎭 {emotion}: {self.emotions[emotion]:.1f}")
    
    def decay_emotions(self):
        """Gradually return emotions to baseline"""
        for emotion in self.emotions:
            current = self.emotions[emotion]
            target = self.baseline[emotion]
            self.emotions[emotion] = current * self.decay_rate + target * (1 - self.decay_rate)
    
    def get_dominant_emotion(self) -> str:
        """Get the currently dominant emotion"""
        return max(self.emotions.items(), key=lambda x: x[1])[0]
    
    def get_emotional_state(self) -> Dict[str, float]:
        """Get current emotional state"""
        return self.emotions.copy()


class CognitionSystem:
    """Simulates cognitive processes like attention, memory, reasoning"""
    
    def __init__(self, memory_capacity: int = 10000):
        self.short_term_memory = []
        self.long_term_memory = []
        self.memory_capacity = memory_capacity
        
        # Cognitive metrics
        self.attention_level = 80.0  # 0-100
        self.processing_speed = 75.0
        self.creativity_level = 70.0
        self.analytical_depth = 85.0
        
        # Working memory
        self.working_memory = []
        self.max_working_memory = 7  # Miller's Law
    
    async def process_information(self, information: str, context: Optional[Dict] = None) -> Dict[str, Any]:
        """Process incoming information cognitively"""
        
        # Add to working memory
        self.working_memory.append({
            'data': information,
            'timestamp': datetime.now().isoformat(),
            'context': context
        })
        
        # Limit working memory size
        if len(self.working_memory) > self.max_working_memory:
            # Move oldest to short-term memory
            old_item = self.working_memory.pop(0)
            self.short_term_memory.append(old_item)
        
        # Analyze information
        analysis = {
            'complexity': len(information) / 100.0,  # Simplified
            'relevance': self._calculate_relevance(information, context),
            'importance': self._calculate_importance(information),
            'requires_action': self._requires_action(information)
        }
        
        logger.debug(f"🧠 Processed: complexity={analysis['complexity']:.2f}, relevance={analysis['relevance']:.2f}")
        
        return analysis
    
    def _calculate_relevance(self, information: str, context: Optional[Dict]) -> float:
        """Calculate how relevant this information is"""
        # Simplified relevance calculation
        if not context:
            return 0.5
        
        keywords = context.get('keywords', [])
        relevance = sum(1 for kw in keywords if kw.lower() in information.lower())
        return min(relevance / max(len(keywords), 1), 1.0)
    
    def _calculate_importance(self, information: str) -> float:
        """Calculate importance of information"""
        # Simplified importance based on length and content
        importance = 0.5
        
        # Increase importance for certain keywords
        high_priority_words = ['urgent', 'critical', 'important', 'breaking', 'alert']
        for word in high_priority_words:
            if word in information.lower():
                importance += 0.1
        
        return min(importance, 1.0)
    
    def _requires_action(self, information: str) -> bool:
        """Determine if information requires action"""
        action_words = ['respond', 'reply', 'post', 'tweet', 'send', 'create']
        return any(word in information.lower() for word in action_words)
    
    async def consolidate_memory(self):
        """Move important short-term memories to long-term"""
        if len(self.short_term_memory) > 100:
            # Sort by importance and move top items to long-term
            important_memories = sorted(
                self.short_term_memory,
                key=lambda x: self._calculate_importance(str(x)),
                reverse=True
            )[:20]
            
            self.long_term_memory.extend(important_memories)
            self.short_term_memory = self.short_term_memory[-50:]  # Keep recent 50
            
            # Limit long-term memory
            if len(self.long_term_memory) > self.memory_capacity:
                self.long_term_memory = self.long_term_memory[-self.memory_capacity:]
            
            logger.info("🧠 Memory consolidated")
    
    async def retrieve_relevant_memories(self, query: str, limit: int = 5) -> List[Dict]:
        """Retrieve relevant memories based on query"""
        # Simple retrieval based on keyword matching
        all_memories = self.long_term_memory + self.short_term_memory
        
        scored_memories = []
        for memory in all_memories:
            score = self._calculate_relevance(
                str(memory.get('data', '')),
                {'keywords': query.split()}
            )
            if score > 0.3:
                scored_memories.append((score, memory))
        
        # Sort by score and return top results
        scored_memories.sort(reverse=True)
        return [m[1] for m in scored_memories[:limit]]


class DecisionMakingSystem:
    """Simulates decision-making processes"""
    
    def __init__(self, emotion_system: EmotionSystem, cognition_system: CognitionSystem):
        self.emotion_system = emotion_system
        self.cognition_system = cognition_system
        
        # Decision parameters
        self.risk_tolerance = 0.6  # 0-1
        self.confidence_threshold = 0.7
    
    async def make_decision(
        self, 
        options: List[Dict[str, Any]], 
        context: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """Make a decision based on cognitive and emotional state"""
        
        if not options:
            return {'decision': None, 'confidence': 0.0}
        
        # Evaluate each option
        scored_options = []
        
        for option in options:
            # Cognitive evaluation
            cognitive_score = await self._evaluate_cognitively(option, context)
            
            # Emotional evaluation
            emotional_score = self._evaluate_emotionally(option)
            
            # Combined score (weighted)
            combined_score = (
                cognitive_score * 0.7 +  # Cognitive weight
                emotional_score * 0.3     # Emotional weight
            )
            
            scored_options.append({
                'option': option,
                'score': combined_score,
                'cognitive_score': cognitive_score,
                'emotional_score': emotional_score
            })
        
        # Select best option
        best = max(scored_options, key=lambda x: x['score'])
        
        confidence = best['score']
        
        decision = {
            'decision': best['option'],
            'confidence': confidence,
            'reasoning': {
                'cognitive_score': best['cognitive_score'],
                'emotional_score': best['emotional_score'],
                'risk_assessment': self._assess_risk(best['option'])
            }
        }
        
        logger.info(f"🎯 Decision made with confidence: {confidence:.2f}")
        
        return decision
    
    async def _evaluate_cognitively(self, option: Dict, context: Optional[Dict]) -> float:
        """Evaluate option cognitively"""
        # Simplified cognitive evaluation
        score = 0.5
        
        # Check alignment with goals
        if context and 'goals' in context:
            score += 0.2
        
        # Check feasibility
        if option.get('feasible', True):
            score += 0.2
        
        # Check expected outcome
        expected_value = option.get('expected_value', 0.5)
        score = (score + expected_value) / 2
        
        return min(score, 1.0)
    
    def _evaluate_emotionally(self, option: Dict) -> float:
        """Evaluate option emotionally"""
        emotional_state = self.emotion_system.get_emotional_state()
        
        # Base score
        score = 0.5
        
        # Adjust based on emotions
        if emotional_state['confidence'] > 70:
            score += 0.2
        if emotional_state['fear'] > 60:
            score -= 0.2
        if emotional_state['curiosity'] > 70:
            score += 0.1
        
        return np.clip(score, 0.0, 1.0)
    
    def _assess_risk(self, option: Dict) -> float:
        """Assess risk level of an option"""
        base_risk = option.get('risk', 0.5)
        
        # Adjust based on confidence
        confidence = self.emotion_system.emotions['confidence'] / 100.0
        adjusted_risk = base_risk * (1 - confidence * 0.3)
        
        return adjusted_risk


class BrainSimulation:
    """Main brain simulation system integrating all subsystems"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        
        # Initialize subsystems
        self.emotion_system = EmotionSystem()
        self.cognition_system = CognitionSystem(
            memory_capacity=config.get('memory_capacity', 10000)
        )
        self.decision_system = DecisionMakingSystem(
            self.emotion_system,
            self.cognition_system
        )
        
        # State
        self.is_active = True
        self.update_interval = config.get('emotion_update_interval', 300)
        
        logger.info("🧠 Brain simulation initialized")
    
    async def process(self, input_data: str, context: Optional[Dict] = None) -> Dict[str, Any]:
        """Process input through the brain simulation"""
        
        # Cognitive processing
        cognitive_analysis = await self.cognition_system.process_information(
            input_data, 
            context
        )
        
        # Emotional response
        if cognitive_analysis['importance'] > 0.7:
            self.emotion_system.update_emotion('anticipation', 5.0)
        if cognitive_analysis['requires_action']:
            self.emotion_system.update_emotion('confidence', 3.0)
        
        # Decision making if needed
        decision = None
        if context and 'options' in context:
            decision = await self.decision_system.make_decision(
                context['options'],
                context
            )
        
        return {
            'cognitive_analysis': cognitive_analysis,
            'emotional_state': self.emotion_system.get_emotional_state(),
            'dominant_emotion': self.emotion_system.get_dominant_emotion(),
            'decision': decision,
            'timestamp': datetime.now().isoformat()
        }
    
    async def update_loop(self):
        """Background loop for brain state updates"""
        while self.is_active:
            # Decay emotions toward baseline
            self.emotion_system.decay_emotions()
            
            # Consolidate memories
            await self.cognition_system.consolidate_memory()
            
            await asyncio.sleep(self.update_interval)
    
    async def get_state(self) -> Dict[str, Any]:
        """Get current brain state"""
        return {
            'emotions': self.emotion_system.get_emotional_state(),
            'cognition': {
                'attention_level': self.cognition_system.attention_level,
                'creativity_level': self.cognition_system.creativity_level,
                'analytical_depth': self.cognition_system.analytical_depth,
                'working_memory_size': len(self.cognition_system.working_memory),
                'long_term_memory_size': len(self.cognition_system.long_term_memory)
            },
            'decision_making': {
                'risk_tolerance': self.decision_system.risk_tolerance,
                'confidence_threshold': self.decision_system.confidence_threshold
            }
        }
    
    async def shutdown(self):
        """Shutdown brain simulation"""
        self.is_active = False
        logger.info("🧠 Brain simulation shutdown")
