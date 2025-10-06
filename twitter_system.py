"""
Twitter System
Handles all Twitter operations including posting, threading, mentions, and engagement
"""

import asyncio
import logging
import tweepy
from typing import Dict, List, Any, Optional
from datetime import datetime
import json

logger = logging.getLogger(__name__)


class TwitterSystem:
    """Manages Twitter operations"""
    
    def __init__(self, config: Dict[str, Any], sheets_manager, agent_orchestrator):
        self.config = config
        self.sheets_manager = sheets_manager
        self.agent_orchestrator = agent_orchestrator
        
        # Twitter API clients
        self.api_v1 = None
        self.api_v2 = None
        self.client = None
        
        # Configuration
        self.max_tweet_length = 270  # Leave buffer for threading
        self.daily_tweet_target = (6, 10)  # Min, max tweets per day
        self.daily_reply_target = (15, 25)
        
        # State tracking
        self.tweets_today = 0
        self.replies_today = 0
        self.last_reset = datetime.now().date()
        
    async def initialize(self):
        """Initialize Twitter API clients"""
        try:
            # API v1.1 for media upload
            auth = tweepy.OAuthHandler(
                self.config['api_key'],
                self.config['api_secret']
            )
            auth.set_access_token(
                self.config['access_token'],
                self.config['access_secret']
            )
            self.api_v1 = tweepy.API(auth)
            
            # API v2 for modern features
            self.client = tweepy.Client(
                bearer_token=self.config['bearer_token'],
                consumer_key=self.config['api_key'],
                consumer_secret=self.config['api_secret'],
                access_token=self.config['access_token'],
                access_token_secret=self.config['access_secret'],
                wait_on_rate_limit=True
            )
            
            logger.info("✅ Twitter API initialized")
        except Exception as e:
            logger.error(f"❌ Failed to initialize Twitter: {e}")
            raise
    
    async def post_tweet(self, content: str, in_reply_to: Optional[str] = None) -> Optional[str]:
        """Post a single tweet"""
        try:
            # Check if threading is needed
            if len(content) > self.max_tweet_length and not in_reply_to:
                return await self.post_thread(content)
            
            # Post tweet
            response = self.client.create_tweet(
                text=content,
                in_reply_to_tweet_id=in_reply_to
            )
            
            tweet_id = response.data['id']
            
            # Update counter
            if not in_reply_to:
                self.tweets_today += 1
            else:
                self.replies_today += 1
            
            logger.info(f"🐦 Tweet posted: {tweet_id}")
            
            # Categorize and log
            await self._categorize_and_log(content, tweet_id)
            
            return tweet_id
            
        except Exception as e:
            logger.error(f"❌ Failed to post tweet: {e}")
            return None
    
    async def post_thread(self, content: str) -> Optional[List[str]]:
        """Post a thread if content is too long"""
        
        logger.info("🧵 Creating thread...")
        
        # Split content into parts
        parts = self._split_for_thread(content)
        
        # Add numbering
        total = len(parts)
        numbered_parts = [
            f"{i+1}/{total}\n\n{part}" 
            for i, part in enumerate(parts)
        ]
        
        # Post thread
        tweet_ids = []
        previous_id = None
        
        for i, part in enumerate(numbered_parts):
            await asyncio.sleep(2)  # Delay between tweets
            
            tweet_id = await self.post_tweet(part, in_reply_to=previous_id)
            if tweet_id:
                tweet_ids.append(tweet_id)
                previous_id = tweet_id
            else:
                logger.error(f"❌ Failed to post thread part {i+1}")
                break
        
        logger.info(f"✅ Thread posted with {len(tweet_ids)} tweets")
        return tweet_ids if tweet_ids else None
    
    def _split_for_thread(self, content: str) -> List[str]:
        """Split content into tweet-sized parts"""
        max_length = 250  # Leave room for numbering
        
        # Try to split at sentence boundaries
        sentences = content.split('. ')
        parts = []
        current_part = ""
        
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
            
            # Add period back if it was removed
            if not sentence.endswith('.'):
                sentence += '.'
            
            # Check if adding this sentence would exceed limit
            if len(current_part) + len(sentence) + 1 > max_length:
                if current_part:
                    parts.append(current_part.strip())
                current_part = sentence
            else:
                current_part += (" " if current_part else "") + sentence
        
        # Add remaining content
        if current_part:
            parts.append(current_part.strip())
        
        # If still empty or single very long part, do hard split
        if not parts or (len(parts) == 1 and len(parts[0]) > max_length):
            parts = [content[i:i+max_length] for i in range(0, len(content), max_length)]
        
        return parts
    
    async def _categorize_and_log(self, content: str, tweet_id: str):
        """Categorize tweet and log to sheets"""
        
        # Get categorizer agent
        categorizer = self.agent_orchestrator.get_agent('categorizer')
        
        if categorizer:
            result = await categorizer.categorize(content, 'twitter')
            category = result['category']
        else:
            category = 'general'
        
        # Log to sheets
        metrics = {
            'likes': 0,
            'retweets': 0,
            'replies': 0,
            'posted_at': datetime.now().isoformat()
        }
        
        await self.sheets_manager.log_tweet(content, tweet_id, category, metrics)
        
        logger.debug(f"📋 Tweet categorized as: {category}")
    
    async def monitor_mentions(self) -> List[Dict[str, Any]]:
        """Monitor and retrieve mentions"""
        try:
            # Get authenticated user ID
            me = self.client.get_me()
            user_id = me.data.id
            
            # Get mentions
            mentions = self.client.get_users_mentions(
                user_id,
                max_results=10,
                tweet_fields=['created_at', 'author_id', 'conversation_id']
            )
            
            if not mentions.data:
                return []
            
            mention_list = []
            for mention in mentions.data:
                mention_list.append({
                    'id': mention.id,
                    'text': mention.text,
                    'author_id': mention.author_id,
                    'created_at': mention.created_at,
                    'conversation_id': mention.conversation_id
                })
            
            logger.info(f"👀 Found {len(mention_list)} mentions")
            return mention_list
            
        except Exception as e:
            logger.error(f"❌ Failed to monitor mentions: {e}")
            return []
    
    async def respond_to_mention(self, mention: Dict[str, Any]) -> Optional[str]:
        """Respond to a mention intelligently"""
        
        # Check if we should respond
        if not await self._should_respond(mention):
            logger.info(f"⏭️ Skipping mention {mention['id']}")
            return None
        
        # Generate response using content creator
        content_creator = self.agent_orchestrator.get_agent('content_creator')
        
        if content_creator:
            context = {
                'mention_text': mention['text'],
                'platform': 'twitter',
                'type': 'reply'
            }
            
            response = await content_creator.create_content(
                content_type='reply',
                topic=mention['text'],
                platform='twitter',
                extra_context=context
            )
            
            if response:
                # Post reply
                tweet_id = await self.post_tweet(response, in_reply_to=mention['id'])
                return tweet_id
        
        return None
    
    async def _should_respond(self, mention: Dict[str, Any]) -> bool:
        """Decide if we should respond to a mention"""
        
        # Get autonomy rules from sheets
        autonomy_rules = await self.sheets_manager.get_sheet_data('خودمختاری')
        
        # Find mention response rule
        response_rule = None
        for rule in autonomy_rules:
            if rule.get('نوع_کار') == 'پاسخ به mention':
                response_rule = rule
                break
        
        if not response_rule:
            return True  # Default to responding
        
        # Check relevance (simplified)
        text = mention['text'].lower()
        relevant_keywords = ['ai', 'technology', 'geopolitics', 'analysis', 'byte-line', 'byteline']
        
        is_relevant = any(keyword in text for keyword in relevant_keywords)
        
        return is_relevant
    
    async def create_content_tweet(self, topic: str, content_type: str = 'general') -> Optional[str]:
        """Create and post a content tweet"""
        
        content_creator = self.agent_orchestrator.get_agent('content_creator')
        
        if not content_creator:
            logger.error("❌ Content creator not available")
            return None
        
        # Generate content
        content = await content_creator.create_content(
            content_type='tweet',
            topic=topic,
            platform='twitter'
        )
        
        if content:
            # Post tweet
            tweet_id = await self.post_tweet(content)
            return tweet_id
        
        return None
    
    async def post_news_tweet(self) -> Optional[str]:
        """Collect AI news and post tweet"""
        
        news_collector = self.agent_orchestrator.get_agent('news_collector')
        
        if not news_collector:
            logger.error("❌ News collector not available")
            return None
        
        # Collect news
        news_items = await news_collector.collect_ai_news()
        
        if not news_items:
            logger.warning("⚠️ No news items found")
            return None
        
        # Create summary tweet
        summary = await news_collector.create_news_summary(news_items)
        
        if summary:
            tweet_id = await self.post_tweet(summary)
            return tweet_id
        
        return None
    
    async def daily_reset(self):
        """Reset daily counters"""
        today = datetime.now().date()
        if today != self.last_reset:
            logger.info(f"📊 Daily stats: {self.tweets_today} tweets, {self.replies_today} replies")
            self.tweets_today = 0
            self.replies_today = 0
            self.last_reset = today
    
    async def get_stats(self) -> Dict[str, Any]:
        """Get current statistics"""
        return {
            'tweets_today': self.tweets_today,
            'replies_today': self.replies_today,
            'target_tweets': self.daily_tweet_target,
            'target_replies': self.daily_reply_target,
            'last_reset': self.last_reset.isoformat()
        }
