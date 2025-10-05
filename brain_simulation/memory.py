"""
Memory system simulating different types of human memory
"""

from typing import Any, Dict, List, Optional
from collections import deque
import time


class MemorySystem:
    """Simulates short-term, long-term, and working memory"""
    
    def __init__(self, capacity: int = 10000):
        self.capacity = capacity
        
        # Short-term memory (recent events)
        self.short_term: deque = deque(maxlen=100)
        
        # Long-term memory (persistent storage)
        self.long_term: Dict[str, Any] = {}
        
        # Working memory (active processing)
        self.working: List[Any] = []
        
        # Memory consolidation queue
        self.consolidation_queue: deque = deque(maxlen=50)
    
    def store_short_term(self, memory: Any):
        """Store in short-term memory"""
        self.short_term.append({
            'content': memory,
            'timestamp': time.time(),
            'access_count': 0
        })
        self.consolidation_queue.append(memory)
    
    def store_long_term(self, key: str, memory: Any):
        """Store in long-term memory"""
        if len(self.long_term) >= self.capacity:
            # Remove least accessed memory
            if self.long_term:
                min_key = min(self.long_term, 
                            key=lambda k: self.long_term[k].get('access_count', 0))
                del self.long_term[min_key]
        
        self.long_term[key] = {
            'content': memory,
            'timestamp': time.time(),
            'access_count': 0,
            'importance': 1.0
        }
    
    def retrieve(self, key: str) -> Optional[Any]:
        """Retrieve from long-term memory"""
        if key in self.long_term:
            self.long_term[key]['access_count'] += 1
            return self.long_term[key]['content']
        return None
    
    def consolidate(self):
        """Consolidate memories from short-term to long-term"""
        while self.consolidation_queue:
            memory = self.consolidation_queue.popleft()
            key = f"memory_{time.time()}_{hash(str(memory))}"
            self.store_long_term(key, memory)
    
    def add_to_working(self, item: Any):
        """Add to working memory"""
        self.working.append(item)
        if len(self.working) > 7:  # Miller's Law: 7±2 items
            self.working.pop(0)
    
    def clear_working(self):
        """Clear working memory"""
        self.working.clear()
    
    def get_recent_memories(self, count: int = 10) -> List[Any]:
        """Get most recent short-term memories"""
        return [m['content'] for m in list(self.short_term)[-count:]]
    
    def search_memories(self, query: str) -> List[Any]:
        """Search through long-term memories"""
        results = []
        query_lower = query.lower()
        
        for key, memory_data in self.long_term.items():
            content_str = str(memory_data['content']).lower()
            if query_lower in content_str:
                memory_data['access_count'] += 1
                results.append(memory_data['content'])
        
        return results
