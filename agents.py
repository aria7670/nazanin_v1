"""
Intelligent Agent System
Contains all specialized agents for different tasks
"""

import asyncio
import logging
import json
from typing import Dict, List, Any, Optional
from datetime import datetime
import aiohttp
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class BaseAgent:
    """Base class for all agents"""
    
    def __init__(self, name: str, api_manager, sheets_manager):
        self.name = name
        self.api_manager = api_manager
        self.sheets_manager = sheets_manager
        logger.info(f"✅ {name} agent initialized")
    
    async def execute(self, *args, **kwargs):
        """Execute agent task - to be implemented by subclasses"""
        raise NotImplementedError


class CategorizerAgent(BaseAgent):
    """Automatically categorizes content"""
    
    CATEGORIES = [
        'interaction', 'video', 'topic', 'ai_info', 
        'fact', 'news', 'analysis', 'promotional'
    ]
    
    async def categorize(self, content: str, platform: str) -> Dict[str, Any]:
        """Categorize content and return category with confidence"""
        
        prompt = {
            "task": "categorize_content",
            "content": content,
            "platform": platform,
            "categories": self.CATEGORIES,
            "instruction": "Analyze the content and return ONLY a JSON with 'category' and 'confidence' (0-1)"
        }
        
        response = await self.api_manager.generate(
            json.dumps(prompt, ensure_ascii=False),
            task_type='data_analysis'
        )
        
        try:
            result = json.loads(response)
            category = result.get('category', 'general')
            confidence = result.get('confidence', 0.5)
            
            logger.info(f"📋 Categorized as '{category}' (confidence: {confidence:.2f})")
            return {
                'category': category,
                'confidence': confidence
            }
        except:
            logger.warning("⚠️ Failed to parse categorization, using default")
            return {
                'category': 'general',
                'confidence': 0.3
            }


class ContentCreatorAgent(BaseAgent):
    """Creates high-quality content"""
    
    async def create_content(
        self, 
        content_type: str,
        topic: str,
        platform: str,
        extra_context: Optional[Dict] = None
    ) -> Optional[str]:
        """Generate content based on personality and rules"""
        
        # Get configuration from sheets
        personality = await self.sheets_manager.get_personality()
        channel_info = await self.sheets_manager.get_channel_info()
        learning_rules = await self.sheets_manager.get_learning_rules(platform)
        
        # Build structured JSON prompt
        prompt = {
            "task": "generate_content",
            "content_type": content_type,
            "platform": platform,
            "topic": topic,
            "personality": personality,
            "channel": channel_info,
            "learning_rules": [r.get('قانون', '') for r in learning_rules],
            "constraints": {
                "max_length": 280 if platform == 'twitter' else 4000,
                "language": "English",
                "tone": "professional, analytical, engaging"
            },
            "requirements": [
                "Be data-driven",
                "Provide value",
                "Engage audience",
                "Maintain brand voice"
            ]
        }
        
        if extra_context:
            prompt["context"] = extra_context
        
        logger.info(f"✍️ Creating {content_type} for {platform}...")
        
        response = await self.api_manager.generate(
            json.dumps(prompt, ensure_ascii=False, indent=2),
            task_type='content_generation'
        )
        
        if response:
            logger.info("✅ Content created successfully")
        
        return response


class ScraperAgent(BaseAgent):
    """Scrapes and collects information from various sources"""
    
    async def scrape_news(self, topic: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Scrape news articles about a topic"""
        
        logger.info(f"🔍 Scraping news about '{topic}'...")
        
        articles = []
        
        try:
            # Search Google News
            search_url = f"https://news.google.com/search?q={topic}&hl=en-US&gl=US&ceid=US:en"
            
            async with aiohttp.ClientSession() as session:
                async with session.get(search_url) as response:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'lxml')
                    
                    # Parse articles (simplified)
                    for article in soup.find_all('article')[:limit]:
                        try:
                            title = article.find('h3').text if article.find('h3') else 'No title'
                            link = article.find('a')['href'] if article.find('a') else ''
                            
                            articles.append({
                                'title': title,
                                'link': link,
                                'source': 'Google News',
                                'scraped_at': datetime.now().isoformat()
                            })
                        except:
                            continue
            
            logger.info(f"✅ Scraped {len(articles)} articles")
            
        except Exception as e:
            logger.error(f"❌ Scraping failed: {e}")
        
        return articles
    
    async def scrape_wikipedia(self, topic: str) -> Optional[str]:
        """Get Wikipedia summary for a topic"""
        
        try:
            url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.json()
                    return data.get('extract', '')
        except Exception as e:
            logger.error(f"❌ Wikipedia scraping failed: {e}")
            return None


class NewsCollectorAgent(BaseAgent):
    """Collects and processes AI news"""
    
    async def collect_ai_news(self) -> List[Dict[str, Any]]:
        """Collect latest AI news"""
        
        logger.info("📰 Collecting AI news...")
        
        topics = [
            'Artificial Intelligence breakthrough',
            'AI regulation',
            'OpenAI news',
            'Google AI',
            'AI geopolitics'
        ]
        
        all_news = []
        
        scraper = ScraperAgent('Scraper', self.api_manager, self.sheets_manager)
        
        for topic in topics:
            news = await scraper.scrape_news(topic, limit=3)
            all_news.extend(news)
            await asyncio.sleep(1)  # Rate limiting
        
        logger.info(f"✅ Collected {len(all_news)} news items")
        
        return all_news
    
    async def create_news_summary(self, news_items: List[Dict]) -> Optional[str]:
        """Create a summary tweet/post from news items"""
        
        if not news_items:
            return None
        
        # Prepare news data for AI
        news_text = "\n".join([
            f"- {item.get('title', 'Untitled')}"
            for item in news_items[:5]
        ])
        
        prompt = f"""Create an engaging tweet about these AI news items:

{news_text}

Requirements:
- Professional and analytical tone
- Data-driven
- Engaging and valuable
- Under 270 characters (for potential threading)
- Include relevant insights
"""
        
        response = await self.api_manager.generate(
            prompt,
            task_type='content_generation'
        )
        
        return response


class AdvertiserAgent(BaseAgent):
    """Creates subtle, professional promotional content"""
    
    async def create_video_promotion(self, video_data: Dict) -> Optional[str]:
        """Create promotional content for a video"""
        
        prompt = {
            "task": "create_promotion",
            "type": "video",
            "video_data": video_data,
            "style": "subtle, value-focused, professional",
            "requirements": [
                "Focus on the value and insights",
                "Not pushy or salesy",
                "Highlight key findings",
                "Include CTA naturally"
            ]
        }
        
        logger.info("📢 Creating video promotion...")
        
        response = await self.api_manager.generate(
            json.dumps(prompt, ensure_ascii=False, indent=2),
            task_type='content_generation'
        )
        
        return response


class TaskManagerAgent(BaseAgent):
    """Manages and prioritizes tasks"""
    
    def __init__(self, name: str, api_manager, sheets_manager):
        super().__init__(name, api_manager, sheets_manager)
        self.task_queue = []
        self.running_tasks = []
    
    async def add_task(self, task: Dict[str, Any]):
        """Add a task to the queue"""
        task['added_at'] = datetime.now().isoformat()
        task['priority'] = task.get('priority', 5)
        
        self.task_queue.append(task)
        self.task_queue.sort(key=lambda x: x['priority'], reverse=True)
        
        logger.info(f"✅ Task added: {task.get('name', 'Unnamed')}")
    
    async def get_next_task(self) -> Optional[Dict[str, Any]]:
        """Get the next highest priority task"""
        if self.task_queue:
            return self.task_queue.pop(0)
        return None
    
    async def get_status(self) -> Dict[str, Any]:
        """Get current task status"""
        return {
            'queued': len(self.task_queue),
            'running': len(self.running_tasks),
            'queue_preview': [t.get('name') for t in self.task_queue[:5]]
        }


class AgentOrchestrator:
    """Orchestrates all agents"""
    
    def __init__(self, api_manager, sheets_manager):
        self.api_manager = api_manager
        self.sheets_manager = sheets_manager
        self.agents = {}
    
    async def initialize(self):
        """Initialize all agents"""
        logger.info("🤖 Initializing agents...")
        
        self.agents['categorizer'] = CategorizerAgent(
            'Categorizer', self.api_manager, self.sheets_manager
        )
        self.agents['content_creator'] = ContentCreatorAgent(
            'ContentCreator', self.api_manager, self.sheets_manager
        )
        self.agents['scraper'] = ScraperAgent(
            'Scraper', self.api_manager, self.sheets_manager
        )
        self.agents['news_collector'] = NewsCollectorAgent(
            'NewsCollector', self.api_manager, self.sheets_manager
        )
        self.agents['advertiser'] = AdvertiserAgent(
            'Advertiser', self.api_manager, self.sheets_manager
        )
        self.agents['task_manager'] = TaskManagerAgent(
            'TaskManager', self.api_manager, self.sheets_manager
        )
        
        logger.info(f"✅ All {len(self.agents)} agents initialized")
    
    def get_agent(self, name: str) -> Optional[BaseAgent]:
        """Get an agent by name"""
        return self.agents.get(name)
