"""
AI API Manager V2
مدیریت پیشرفته API های هوش مصنوعی با Fallback و Load Balancing
"""

import asyncio
import random
import logging
from typing import Dict, List, Any, Optional
import time

logger = logging.getLogger(__name__)


class APIManagerV2:
    """مدیریت هوشمند API های AI"""
    
    def __init__(self, config: Dict, sheets_manager=None):
        self.config = config
        self.sheets_manager = sheets_manager
        
        # Providers
        self.providers = {}
        self.current_provider = None
        
        # Statistics
        self.stats = {
            'total_calls': 0,
            'successful_calls': 0,
            'failed_calls': 0,
            'total_cost': 0.0
        }
        
        # Initialize providers
        self._initialize_providers()
        
        logger.info(f"✅ API Manager V2 initialized with {len(self.providers)} providers")
    
    def _initialize_providers(self):
        """راه‌اندازی providers"""
        ai_config = self.config.get('ai_apis', {})
        
        # Groq (رایگان و سریع)
        if 'groq' in ai_config and ai_config['groq'].get('keys'):
            self.providers['groq'] = AIProviderV2(
                'groq',
                ai_config['groq']['keys'],
                ai_config['groq'].get('model', 'mixtral-8x7b-32768'),
                priority=10  # بالاترین اولویت (رایگان و سریع)
            )
        
        # Gemini
        if 'gemini' in ai_config and ai_config['gemini'].get('keys'):
            self.providers['gemini'] = AIProviderV2(
                'gemini',
                ai_config['gemini']['keys'],
                ai_config['gemini'].get('model', 'gemini-pro'),
                priority=9
            )
        
        # Together AI
        if 'together' in ai_config and ai_config['together'].get('keys'):
            self.providers['together'] = AIProviderV2(
                'together',
                ai_config['together']['keys'],
                ai_config['together'].get('model', 'mistralai/Mixtral-8x7B'),
                priority=8
            )
        
        # OpenAI
        if 'openai' in ai_config and ai_config['openai'].get('keys'):
            self.providers['openai'] = AIProviderV2(
                'openai',
                ai_config['openai']['keys'],
                ai_config['openai'].get('model', 'gpt-4'),
                priority=7
            )
        
        # Claude
        if 'claude' in ai_config and ai_config['claude'].get('keys'):
            self.providers['claude'] = AIProviderV2(
                'claude',
                ai_config['claude']['keys'],
                ai_config['claude'].get('model', 'claude-3-sonnet'),
                priority=7
            )
        
        # DeepSeek
        if 'deepseek' in ai_config and ai_config['deepseek'].get('keys'):
            self.providers['deepseek'] = AIProviderV2(
                'deepseek',
                ai_config['deepseek']['keys'],
                ai_config['deepseek'].get('model', 'deepseek-chat'),
                priority=6
            )
    
    async def reload_keys_from_sheets(self):
        """بارگذاری مجدد کلیدها از Google Sheets"""
        if not self.sheets_manager:
            return
        
        try:
            api_keys = await self.sheets_manager.get_api_keys()
            
            # به‌روزرسانی هر provider
            for provider_name, keys in api_keys.items():
                if provider_name in self.providers:
                    self.providers[provider_name].update_keys(keys)
                    logger.info(f"✅ Reloaded {len(keys)} keys for {provider_name}")
        
        except Exception as e:
            logger.error(f"❌ Failed to reload keys from sheets: {e}")
            logger.info("💡 Using keys from config file")
    
    async def generate(
        self,
        prompt: str,
        preferred_provider: Optional[str] = None,
        max_retries: int = 3
    ) -> Optional[str]:
        """تولید پاسخ با fallback خودکار"""
        
        # انتخاب ترتیب providers
        if preferred_provider and preferred_provider in self.providers:
            providers_order = [preferred_provider] + [
                p for p in sorted(
                    self.providers.keys(),
                    key=lambda x: self.providers[x].priority,
                    reverse=True
                ) if p != preferred_provider
            ]
        else:
            # مرتب‌سازی بر اساس اولویت
            providers_order = sorted(
                self.providers.keys(),
                key=lambda x: self.providers[x].priority,
                reverse=True
            )
        
        # تلاش با هر provider
        for provider_name in providers_order:
            provider = self.providers[provider_name]
            
            # اگه تمام کلیدهاش fail شده، برو بعدی
            if provider.all_keys_failed():
                logger.warning(f"⚠️ All keys failed for {provider_name}, skipping...")
                continue
            
            # تلاش تا max_retries بار
            for attempt in range(max_retries):
                try:
                    logger.info(f"🤖 Trying {provider_name} (attempt {attempt+1}/{max_retries})...")
                    
                    response = await provider.generate(prompt)
                    
                    if response:
                        self.stats['total_calls'] += 1
                        self.stats['successful_calls'] += 1
                        self.current_provider = provider_name
                        
                        logger.info(f"✅ Success with {provider_name}")
                        return response
                
                except Exception as e:
                    logger.error(f"❌ {provider_name} failed: {e}")
                    self.stats['failed_calls'] += 1
                    
                    if attempt < max_retries - 1:
                        await asyncio.sleep(1)  # کمی صبر قبل از retry
        
        logger.error("❌ All providers failed!")
        return None
    
    def get_stats(self) -> Dict:
        """دریافت آمار"""
        return {
            **self.stats,
            'success_rate': self.stats['successful_calls'] / max(1, self.stats['total_calls']),
            'providers': {
                name: provider.get_stats()
                for name, provider in self.providers.items()
            }
        }
    
    def _is_cache_valid(self, cache_key: str) -> bool:
        """بررسی اعتبار cache"""
        if cache_key not in self._cache:
            return False
        timestamp = self._cache_timestamps.get(cache_key, 0)
        return (time.time() - timestamp) < self.cache_duration
    
    def _clear_cache_key(self, cache_key: str):
        """پاک کردن کلید از cache"""
        self._cache.pop(cache_key, None)
        self._cache_timestamps.pop(cache_key, None)


class AIProviderV2:
    """ارائه‌دهنده AI با پشتیبانی از چند کلید"""
    
    def __init__(self, name: str, keys: List[str], model: str, priority: int = 5):
        self.name = name
        self.keys = keys or []
        self.model = model
        self.priority = priority
        
        self.current_key_index = 0
        self.failed_keys = set()
        
        self.stats = {
            'calls': 0,
            'successes': 0,
            'failures': 0,
            'avg_response_time': 0
        }
    
    def update_keys(self, new_keys: List[str]):
        """به‌روزرسانی کلیدها"""
        self.keys = new_keys
        self.failed_keys.clear()  # Reset failed keys
        self.current_key_index = 0
    
    def get_next_key(self) -> Optional[str]:
        """دریافت کلید بعدی (Round-robin)"""
        if not self.keys:
            return None
        
        # پیدا کردن اولین کلید که fail نشده
        attempts = 0
        while attempts < len(self.keys):
            key = self.keys[self.current_key_index]
            self.current_key_index = (self.current_key_index + 1) % len(self.keys)
            
            if key not in self.failed_keys:
                return key
            
            attempts += 1
        
        return None
    
    def mark_key_failed(self, key: str):
        """علامت‌گذاری کلید به عنوان ناموفق"""
        self.failed_keys.add(key)
        logger.warning(f"⚠️ Key failed for {self.name}: {key[:10]}...")
    
    def all_keys_failed(self) -> bool:
        """بررسی اینکه همه کلیدها fail شدن"""
        return len(self.failed_keys) >= len(self.keys)
    
    async def generate(self, prompt: str) -> Optional[str]:
        """تولید پاسخ"""
        key = self.get_next_key()
        if not key:
            logger.error(f"❌ No available keys for {self.name}")
            return None
        
        self.stats['calls'] += 1
        start_time = time.time()
        
        try:
            # فراخوانی API بر اساس provider
            response = await self._call_api(key, prompt)
            
            # محاسبه زمان پاسخ
            response_time = time.time() - start_time
            self.stats['avg_response_time'] = (
                (self.stats['avg_response_time'] * (self.stats['calls'] - 1) + response_time)
                / self.stats['calls']
            )
            
            self.stats['successes'] += 1
            return response
        
        except Exception as e:
            self.stats['failures'] += 1
            self.mark_key_failed(key)
            raise e
    
    async def _call_api(self, api_key: str, prompt: str) -> str:
        """فراخوانی API (باید برای هر provider پیاده‌سازی بشه)"""
        
        if self.name == 'groq':
            return await self._call_groq(api_key, prompt)
        elif self.name == 'gemini':
            return await self._call_gemini(api_key, prompt)
        elif self.name == 'together':
            return await self._call_together(api_key, prompt)
        elif self.name == 'openai':
            return await self._call_openai(api_key, prompt)
        elif self.name == 'claude':
            return await self._call_claude(api_key, prompt)
        elif self.name == 'deepseek':
            return await self._call_deepseek(api_key, prompt)
        else:
            raise NotImplementedError(f"Provider {self.name} not implemented")
    
    async def _call_groq(self, api_key: str, prompt: str) -> str:
        """Groq API"""
        try:
            from groq import Groq
            client = Groq(api_key=api_key)
            
            response = client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=2048
            )
            
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Groq error: {e}")
            raise
    
    async def _call_gemini(self, api_key: str, prompt: str) -> str:
        """Gemini API"""
        try:
            import google.generativeai as genai
            genai.configure(api_key=api_key)
            
            model = genai.GenerativeModel(self.model)
            response = model.generate_content(prompt)
            
            return response.text
        except Exception as e:
            logger.error(f"Gemini error: {e}")
            raise
    
    async def _call_together(self, api_key: str, prompt: str) -> str:
        """Together AI API"""
        import aiohttp
        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                'https://api.together.xyz/inference',
                json={
                    'model': self.model,
                    'prompt': prompt,
                    'max_tokens': 2048,
                    'temperature': 0.7
                },
                headers={'Authorization': f'Bearer {api_key}'}
            ) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data['output']['choices'][0]['text']
                else:
                    raise Exception(f"Together AI error: {resp.status}")
    
    async def _call_openai(self, api_key: str, prompt: str) -> str:
        """OpenAI API"""
        try:
            import openai
            openai.api_key = api_key
            
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=2048
            )
            
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"OpenAI error: {e}")
            raise
    
    async def _call_claude(self, api_key: str, prompt: str) -> str:
        """Claude API"""
        try:
            import anthropic
            client = anthropic.Anthropic(api_key=api_key)
            
            response = client.messages.create(
                model=self.model,
                max_tokens=2048,
                messages=[{"role": "user", "content": prompt}]
            )
            
            return response.content[0].text
        except Exception as e:
            logger.error(f"Claude error: {e}")
            raise
    
    async def _call_deepseek(self, api_key: str, prompt: str) -> str:
        """DeepSeek API"""
        import aiohttp
        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                'https://api.deepseek.com/v1/chat/completions',
                json={
                    'model': self.model,
                    'messages': [{"role": "user", "content": prompt}],
                    'temperature': 0.7
                },
                headers={'Authorization': f'Bearer {api_key}'}
            ) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data['choices'][0]['message']['content']
                else:
                    raise Exception(f"DeepSeek error: {resp.status}")
    
    def get_stats(self) -> Dict:
        """دریافت آمار کلی"""
        return self.stats


# Usage Example
if __name__ == '__main__':
    async def main():
        config = {
            'ai_apis': {
                'fallback_enabled': True,
                'groq': {
                    'keys': ['gsk_xxx1', 'gsk_xxx2'],
                    'model': 'mixtral-8x7b-32768'
                },
                'gemini': {
                    'keys': ['AIza_xxx'],
                    'model': 'gemini-pro'
                }
            }
        }
        
        manager = APIManagerV2(config)
        
        # تولید پاسخ
        response = await manager.generate("سلام! چطوری؟")
        if response:
            print(f"Response: {response}")
        
        # آمار
        stats = manager.get_stats()
        print(f"Stats: {stats}")
    
    asyncio.run(main())
