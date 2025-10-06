"""
AI API Manager
Handles multiple AI providers with load balancing and fallback
"""

import asyncio
import random
import logging
from typing import Dict, List, Any, Optional
import anthropic
import openai
import google.generativeai as genai
import aiohttp

logger = logging.getLogger(__name__)


class AIProvider:
    """Base class for AI providers"""
    
    def __init__(self, name: str, keys: List[str]):
        self.name = name
        self.keys = keys
        self.current_key_index = 0
        self.failed_keys = set()
    
    def get_next_key(self) -> Optional[str]:
        """Get next available key using round-robin"""
        if len(self.failed_keys) >= len(self.keys):
            logger.error(f"❌ All keys failed for {self.name}")
            return None
        
        for _ in range(len(self.keys)):
            key = self.keys[self.current_key_index]
            self.current_key_index = (self.current_key_index + 1) % len(self.keys)
            if key not in self.failed_keys:
                return key
        return None
    
    def mark_key_failed(self, key: str):
        """Mark a key as failed"""
        self.failed_keys.add(key)
        logger.warning(f"⚠️ Marked key as failed for {self.name}")
    
    async def generate(self, prompt: str, **kwargs) -> Optional[str]:
        """Generate response - to be implemented by subclasses"""
        raise NotImplementedError


class GeminiProvider(AIProvider):
    """Google Gemini provider"""
    
    async def generate(self, prompt: str, **kwargs) -> Optional[str]:
        key = self.get_next_key()
        if not key:
            return None
        
        try:
            genai.configure(api_key=key)
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.error(f"❌ Gemini error: {e}")
            self.mark_key_failed(key)
            return None


class GPT4Provider(AIProvider):
    """OpenAI GPT-4 provider"""
    
    async def generate(self, prompt: str, **kwargs) -> Optional[str]:
        key = self.get_next_key()
        if not key:
            return None
        
        try:
            client = openai.AsyncOpenAI(api_key=key)
            response = await client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                **kwargs
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"❌ GPT-4 error: {e}")
            self.mark_key_failed(key)
            return None


class ClaudeProvider(AIProvider):
    """Anthropic Claude provider"""
    
    async def generate(self, prompt: str, **kwargs) -> Optional[str]:
        key = self.get_next_key()
        if not key:
            return None
        
        try:
            client = anthropic.AsyncAnthropic(api_key=key)
            message = await client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=4096,
                messages=[{"role": "user", "content": prompt}],
                **kwargs
            )
            return message.content[0].text
        except Exception as e:
            logger.error(f"❌ Claude error: {e}")
            self.mark_key_failed(key)
            return None


class DeepSeekProvider(AIProvider):
    """DeepSeek provider"""
    
    async def generate(self, prompt: str, **kwargs) -> Optional[str]:
        key = self.get_next_key()
        if not key:
            return None
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    'https://api.deepseek.com/v1/chat/completions',
                    headers={'Authorization': f'Bearer {key}'},
                    json={
                        'model': 'deepseek-chat',
                        'messages': [{'role': 'user', 'content': prompt}]
                    }
                ) as response:
                    data = await response.json()
                    return data['choices'][0]['message']['content']
        except Exception as e:
            logger.error(f"❌ DeepSeek error: {e}")
            self.mark_key_failed(key)
            return None


class APIManager:
    """Manages multiple AI providers with intelligent routing"""
    
    def __init__(self):
        self.providers: Dict[str, AIProvider] = {}
        self.task_routing = {
            'video_analysis': 'gemini',
            'content_generation': 'gpt4',
            'data_analysis': 'deepseek',
            'twitter_specific': 'grok',
            'general': 'claude'
        }
    
    async def initialize(self, api_keys: Dict[str, List[Dict[str, Any]]]):
        """Initialize all AI providers"""
        logger.info("🤖 Initializing AI providers...")
        
        # Extract keys for each provider
        for provider_name, key_list in api_keys.items():
            keys = [k.get('کلید', '') for k in key_list if k.get('کلید')]
            
            if provider_name.lower() == 'gemini':
                self.providers['gemini'] = GeminiProvider('gemini', keys)
            elif provider_name.lower() == 'gpt4':
                self.providers['gpt4'] = GPT4Provider('gpt4', keys)
            elif provider_name.lower() == 'claude':
                self.providers['claude'] = ClaudeProvider('claude', keys)
            elif provider_name.lower() == 'deepseek':
                self.providers['deepseek'] = DeepSeekProvider('deepseek', keys)
            
            logger.info(f"✅ Initialized {provider_name} with {len(keys)} keys")
    
    async def generate(
        self, 
        prompt: str, 
        task_type: str = 'general',
        fallback: bool = True,
        **kwargs
    ) -> Optional[str]:
        """Generate response using appropriate AI provider"""
        
        # Determine which provider to use
        provider_name = self.task_routing.get(task_type, 'general')
        provider = self.providers.get(provider_name)
        
        if not provider:
            logger.warning(f"⚠️ Provider {provider_name} not available, using fallback")
            provider_name = list(self.providers.keys())[0]
            provider = self.providers[provider_name]
        
        # Try primary provider
        logger.debug(f"🤖 Generating with {provider_name}...")
        response = await provider.generate(prompt, **kwargs)
        
        if response:
            return response
        
        # Fallback to other providers if enabled
        if fallback:
            logger.info(f"🔄 Primary provider failed, trying fallback...")
            for backup_name, backup_provider in self.providers.items():
                if backup_name != provider_name:
                    response = await backup_provider.generate(prompt, **kwargs)
                    if response:
                        logger.info(f"✅ Fallback to {backup_name} succeeded")
                        return response
        
        logger.error("❌ All providers failed")
        return None
    
    async def reload_keys(self, api_keys: Dict[str, List[Dict[str, Any]]]):
        """Reload API keys without restart"""
        logger.info("🔄 Reloading API keys...")
        await self.initialize(api_keys)
