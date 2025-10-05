"""
Intelligent Agent with cognitive capabilities
"""

import numpy as np
from typing import Any, Dict, List, Optional, Callable
from enum import Enum


class AgentState(Enum):
    """Agent operational states"""
    IDLE = "idle"
    THINKING = "thinking"
    LEARNING = "learning"
    ACTING = "acting"
    PLANNING = "planning"


class IntelligentAgent:
    """High-level intelligent agent with cognitive architecture"""
    
    def __init__(self, agent_id: str, capabilities: Optional[List[str]] = None):
        self.agent_id = agent_id
        self.state = AgentState.IDLE
        
        # Capabilities
        self.capabilities = capabilities or [
            'reasoning', 'learning', 'planning', 'decision_making', 'adaptation'
        ]
        
        # Knowledge base
        self.knowledge_base: Dict[str, Any] = {}
        
        # Goals and intentions
        self.goals: List[Dict[str, Any]] = []
        self.current_goal: Optional[Dict[str, Any]] = None
        
        # Action history
        self.action_history: List[Dict[str, Any]] = []
        
        # Performance metrics
        self.metrics = {
            'decisions_made': 0,
            'goals_achieved': 0,
            'learning_iterations': 0,
            'success_rate': 0.0
        }
        
        # Reasoning engine
        self.belief_state: Dict[str, float] = {}
        
    def perceive(self, observation: Any) -> Dict[str, Any]:
        """Perceive and process environmental observation"""
        self.state = AgentState.THINKING
        
        perception = {
            'timestamp': np.random.random(),  # Simplified timestamp
            'raw_observation': observation,
            'processed': self._process_observation(observation),
            'importance': self._assess_importance(observation)
        }
        
        # Update beliefs
        self._update_beliefs(perception)
        
        return perception
    
    def _process_observation(self, observation: Any) -> Dict[str, Any]:
        """Process raw observation into structured information"""
        return {
            'type': type(observation).__name__,
            'content': str(observation),
            'features': self._extract_features(observation)
        }
    
    def _extract_features(self, observation: Any) -> np.ndarray:
        """Extract features from observation"""
        # Simple feature extraction
        obs_str = str(observation)
        features = np.array([
            len(obs_str),
            hash(obs_str) % 100,
            sum(ord(c) for c in obs_str[:10]) / 10
        ])
        return features
    
    def _assess_importance(self, observation: Any) -> float:
        """Assess importance of observation"""
        # Simple importance scoring
        obs_str = str(observation)
        importance = min(1.0, len(obs_str) / 100)
        return importance
    
    def _update_beliefs(self, perception: Dict[str, Any]):
        """Update belief state based on perception"""
        features = perception['processed']['features']
        
        for i, feature_val in enumerate(features):
            belief_key = f"feature_{i}"
            # Bayesian-like update (simplified)
            prior = self.belief_state.get(belief_key, 0.5)
            likelihood = 1 / (1 + np.exp(-feature_val))
            posterior = (prior * likelihood) / ((prior * likelihood) + ((1 - prior) * (1 - likelihood)))
            self.belief_state[belief_key] = posterior
    
    def reason(self, problem: Any) -> Dict[str, Any]:
        """Apply reasoning to solve problem"""
        self.state = AgentState.THINKING
        
        # Analyze problem
        analysis = {
            'problem_type': type(problem).__name__,
            'complexity': self._assess_complexity(problem),
            'relevant_knowledge': self._retrieve_knowledge(problem)
        }
        
        # Generate solution
        solution = self._generate_solution(problem, analysis)
        
        # Evaluate solution
        evaluation = self._evaluate_solution(solution)
        
        return {
            'analysis': analysis,
            'solution': solution,
            'evaluation': evaluation,
            'confidence': evaluation['confidence']
        }
    
    def _assess_complexity(self, problem: Any) -> str:
        """Assess problem complexity"""
        size = len(str(problem))
        if size < 10:
            return "simple"
        elif size < 100:
            return "moderate"
        else:
            return "complex"
    
    def _retrieve_knowledge(self, problem: Any) -> List[Any]:
        """Retrieve relevant knowledge from knowledge base"""
        relevant = []
        problem_str = str(problem).lower()
        
        for key, value in self.knowledge_base.items():
            if problem_str in str(value).lower():
                relevant.append({key: value})
        
        return relevant[:5]  # Top 5 relevant items
    
    def _generate_solution(self, problem: Any, analysis: Dict[str, Any]) -> Any:
        """Generate solution to problem"""
        # Simple solution generation based on complexity
        complexity = analysis['complexity']
        
        if complexity == "simple":
            return f"Simple solution to: {problem}"
        elif complexity == "moderate":
            return f"Analyzed solution considering: {analysis['relevant_knowledge']}"
        else:
            return f"Complex multi-step solution with strategic approach to: {problem}"
    
    def _evaluate_solution(self, solution: Any) -> Dict[str, Any]:
        """Evaluate proposed solution"""
        solution_str = str(solution)
        
        # Heuristic evaluation
        quality_score = min(1.0, len(solution_str) / 50)
        confidence = 0.5 + (quality_score * 0.5)
        
        return {
            'quality': quality_score,
            'confidence': confidence,
            'feasible': True
        }
    
    def decide(self, options: List[Any]) -> Any:
        """Make decision among options"""
        self.state = AgentState.THINKING
        self.metrics['decisions_made'] += 1
        
        if not options:
            return None
        
        # Score each option
        scores = []
        for option in options:
            score = self._score_option(option)
            scores.append(score)
        
        # Select best option
        best_idx = np.argmax(scores)
        decision = options[best_idx]
        
        # Record decision
        self.action_history.append({
            'type': 'decision',
            'options': options,
            'chosen': decision,
            'score': scores[best_idx]
        })
        
        return decision
    
    def _score_option(self, option: Any) -> float:
        """Score an option for decision making"""
        # Multi-criteria scoring
        scores = []
        
        # Alignment with current goal
        if self.current_goal:
            alignment = self._compute_alignment(option, self.current_goal)
            scores.append(alignment)
        
        # Expected utility
        utility = hash(str(option)) % 100 / 100
        scores.append(utility)
        
        # Risk assessment
        risk = self._assess_risk(option)
        scores.append(1 - risk)
        
        return np.mean(scores)
    
    def _compute_alignment(self, option: Any, goal: Dict[str, Any]) -> float:
        """Compute alignment between option and goal"""
        option_str = str(option).lower()
        goal_str = str(goal.get('description', '')).lower()
        
        # Simple string similarity
        common = sum(1 for word in goal_str.split() if word in option_str)
        alignment = common / max(len(goal_str.split()), 1)
        
        return min(1.0, alignment)
    
    def _assess_risk(self, option: Any) -> float:
        """Assess risk of an option"""
        # Simple risk heuristic
        option_str = str(option)
        risk_keywords = ['danger', 'risk', 'unsafe', 'uncertain']
        
        risk_count = sum(1 for keyword in risk_keywords if keyword in option_str.lower())
        risk = min(1.0, risk_count * 0.3)
        
        return risk
    
    def learn(self, experience: Dict[str, Any]):
        """Learn from experience"""
        self.state = AgentState.LEARNING
        self.metrics['learning_iterations'] += 1
        
        # Extract lesson
        lesson = self._extract_lesson(experience)
        
        # Update knowledge base
        lesson_key = f"lesson_{len(self.knowledge_base)}"
        self.knowledge_base[lesson_key] = lesson
        
        # Update success rate
        if experience.get('successful', False):
            self.metrics['goals_achieved'] += 1
        
        if self.metrics['decisions_made'] > 0:
            self.metrics['success_rate'] = self.metrics['goals_achieved'] / self.metrics['decisions_made']
    
    def _extract_lesson(self, experience: Dict[str, Any]) -> Dict[str, Any]:
        """Extract lesson from experience"""
        return {
            'context': experience.get('context', 'unknown'),
            'action': experience.get('action', 'unknown'),
            'outcome': experience.get('outcome', 'unknown'),
            'successful': experience.get('successful', False)
        }
    
    def plan(self, goal: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Create plan to achieve goal"""
        self.state = AgentState.PLANNING
        self.current_goal = goal
        
        # Generate plan steps
        steps = []
        goal_desc = goal.get('description', '')
        
        # Simple planning: break into sub-goals
        num_steps = min(5, max(2, len(goal_desc) // 20))
        
        for i in range(num_steps):
            step = {
                'step_number': i + 1,
                'action': f"Execute sub-goal {i + 1} for: {goal_desc[:30]}",
                'expected_outcome': f"Progress towards: {goal_desc}",
                'priority': num_steps - i
            }
            steps.append(step)
        
        return steps
    
    def execute(self, action: Dict[str, Any]) -> Dict[str, Any]:
        """Execute an action"""
        self.state = AgentState.ACTING
        
        result = {
            'action': action,
            'executed': True,
            'success': np.random.random() > 0.3,  # Simplified success model
            'timestamp': np.random.random()
        }
        
        self.action_history.append(result)
        
        return result
    
    def get_status(self) -> Dict[str, Any]:
        """Get agent status"""
        return {
            'agent_id': self.agent_id,
            'state': self.state.value,
            'capabilities': self.capabilities,
            'knowledge_items': len(self.knowledge_base),
            'goals': len(self.goals),
            'metrics': self.metrics,
            'belief_entropy': float(np.mean(list(self.belief_state.values()))) if self.belief_state else 0.0
        }
