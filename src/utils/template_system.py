"""
Template & Pattern System
سیستم تمپلت و الگوهای از پیش تعریف شده
"""

import asyncio
import logging
from typing import Dict, List, Any, Optional
import json
import re
from datetime import datetime
import random

logger = logging.getLogger(__name__)


class Template:
    """کلاس تمپلت"""
    
    def __init__(self, name: str, template: str, variables: List[str], 
                 category: str = 'general'):
        self.name = name
        self.template = template
        self.variables = variables
        self.category = category
        self.usage_count = 0
        self.success_rate = 0.0
        
    def render(self, **kwargs) -> str:
        """رندر کردن تمپلت با مقادیر"""
        rendered = self.template
        
        for var in self.variables:
            value = kwargs.get(var, f"[{var}]")
            rendered = rendered.replace(f"{{{var}}}", str(value))
        
        self.usage_count += 1
        return rendered
    
    def to_dict(self) -> Dict:
        """تبدیل به dictionary"""
        return {
            'name': self.name,
            'template': self.template,
            'variables': self.variables,
            'category': self.category,
            'usage_count': self.usage_count,
            'success_rate': self.success_rate
        }


class TemplateLibrary:
    """کتابخانه تمپلت‌ها"""
    
    def __init__(self):
        self.templates = {}
        self._load_default_templates()
        
    def _load_default_templates(self):
        """بارگذاری تمپلت‌های پیش‌فرض"""
        
        # تمپلت‌های توییتر
        self.add_template(Template(
            name='news_announcement',
            template='🚨 Breaking: {title}\n\n{summary}\n\n{hashtags}\n\n{link}',
            variables=['title', 'summary', 'hashtags', 'link'],
            category='twitter_news'
        ))
        
        self.add_template(Template(
            name='question_tweet',
            template='🤔 {question}\n\nWhat do you think? Let me know in comments!\n\n{hashtags}',
            variables=['question', 'hashtags'],
            category='twitter_engagement'
        ))
        
        self.add_template(Template(
            name='analysis_thread',
            template='{number}/{total} 🧵\n\n{content}\n\n{hashtags}',
            variables=['number', 'total', 'content', 'hashtags'],
            category='twitter_thread'
        ))
        
        self.add_template(Template(
            name='video_promotion',
            template='🎬 New Video: "{title}"\n\n{description}\n\n▶️ Watch: {link}\n\n{hashtags}',
            variables=['title', 'description', 'link', 'hashtags'],
            category='twitter_video'
        ))
        
        # تمپلت‌های تلگرام
        self.add_template(Template(
            name='telegram_announcement',
            template='📢 **{title}**\n\n{content}\n\n{footer}',
            variables=['title', 'content', 'footer'],
            category='telegram_post'
        ))
        
        self.add_template(Template(
            name='telegram_analysis',
            template='🔍 **تحلیل: {topic}**\n\n{analysis}\n\n📊 نتیجه:\n{conclusion}\n\n{tags}',
            variables=['topic', 'analysis', 'conclusion', 'tags'],
            category='telegram_analysis'
        ))
        
        # تمپلت‌های پاسخ
        self.add_template(Template(
            name='friendly_response',
            template='{greeting} {name}!\n\n{response}\n\n{closing}',
            variables=['greeting', 'name', 'response', 'closing'],
            category='response'
        ))
        
        self.add_template(Template(
            name='technical_answer',
            template='Here\'s the explanation:\n\n{explanation}\n\nKey points:\n{points}\n\nLet me know if you need more details!',
            variables=['explanation', 'points'],
            category='response_technical'
        ))
        
        # تمپلت‌های گزارش
        self.add_template(Template(
            name='daily_report',
            template='📊 **گزارش روزانه**\n\n📈 آمار:\n{stats}\n\n✅ موفقیت‌ها:\n{successes}\n\n⚠️ نکات:\n{notes}',
            variables=['stats', 'successes', 'notes'],
            category='report'
        ))
        
        logger.info(f"✅ Loaded {len(self.templates)} default templates")
    
    def add_template(self, template: Template):
        """افزودن تمپلت"""
        self.templates[template.name] = template
    
    def get_template(self, name: str) -> Optional[Template]:
        """دریافت تمپلت"""
        return self.templates.get(name)
    
    def get_templates_by_category(self, category: str) -> List[Template]:
        """دریافت تمپلت‌ها بر اساس دسته"""
        return [
            template for template in self.templates.values()
            if template.category == category
        ]
    
    def search_templates(self, keyword: str) -> List[Template]:
        """جستجو در تمپلت‌ها"""
        results = []
        keyword_lower = keyword.lower()
        
        for template in self.templates.values():
            if keyword_lower in template.name.lower() or keyword_lower in template.category.lower():
                results.append(template)
        
        return results
    
    def render_template(self, template_name: str, **kwargs) -> Optional[str]:
        """رندر یک تمپلت"""
        template = self.get_template(template_name)
        if template:
            return template.render(**kwargs)
        return None
    
    def get_statistics(self) -> Dict[str, Any]:
        """آمار تمپلت‌ها"""
        categories = {}
        for template in self.templates.values():
            if template.category not in categories:
                categories[template.category] = 0
            categories[template.category] += 1
        
        most_used = sorted(
            self.templates.values(),
            key=lambda t: t.usage_count,
            reverse=True
        )[:5]
        
        return {
            'total_templates': len(self.templates),
            'categories': categories,
            'most_used': [
                {'name': t.name, 'usage': t.usage_count}
                for t in most_used
            ]
        }


class PatternLibrary:
    """کتابخانه الگوها"""
    
    def __init__(self):
        self.patterns = {}
        self._load_default_patterns()
    
    def _load_default_patterns(self):
        """بارگذاری الگوهای پیش‌فرض"""
        
        # الگوهای محتوایی
        self.patterns['hook_patterns'] = [
            "🚨 Breaking: {topic}",
            "💡 Did you know that {fact}?",
            "🔥 This is huge: {announcement}",
            "⚠️ Important update on {topic}",
            "🤔 Here's something interesting about {topic}"
        ]
        
        self.patterns['cta_patterns'] = [
            "What do you think? Comment below!",
            "Share your thoughts!",
            "Let me know in the replies!",
            "Tag someone who needs to see this!",
            "Read the full analysis:"
        ]
        
        self.patterns['closing_patterns'] = [
            "Stay tuned for more updates!",
            "Follow for more insights!",
            "More coming soon!",
            "Let's discuss this!",
            "Thanks for reading!"
        ]
        
        # الگوهای ساختاری
        self.patterns['listicle_structure'] = {
            'intro': 'Here are {count} {topic}:\n\n',
            'item': '{number}. {title}\n{description}\n\n',
            'outro': 'Which one resonates with you?'
        }
        
        self.patterns['how_to_structure'] = {
            'intro': 'How to {goal}:\n\n',
            'step': 'Step {number}: {action}\n{explanation}\n\n',
            'outro': 'Try it and let me know how it goes!'
        }
        
        # الگوهای احساسی
        self.patterns['empathy_starters'] = [
            "I understand how you feel.",
            "That's a great question!",
            "I can see why that's confusing.",
            "You're absolutely right about that.",
            "That's an interesting perspective."
        ]
        
        # الگوهای تحلیلی
        self.patterns['analysis_structure'] = {
            'context': '📊 Context:\n{context}\n\n',
            'analysis': '🔍 Analysis:\n{analysis}\n\n',
            'implications': '💡 What this means:\n{implications}\n\n',
            'conclusion': '✅ Bottom line:\n{conclusion}'
        }
        
        logger.info(f"✅ Loaded {len(self.patterns)} pattern categories")
    
    def get_pattern(self, pattern_name: str) -> Optional[Any]:
        """دریافت الگو"""
        return self.patterns.get(pattern_name)
    
    def get_random_hook(self) -> str:
        """دریافت hook تصادفی"""
        return random.choice(self.patterns['hook_patterns'])
    
    def get_random_cta(self) -> str:
        """دریافت CTA تصادفی"""
        return random.choice(self.patterns['cta_patterns'])
    
    def build_listicle(self, topic: str, items: List[Dict]) -> str:
        """ساخت listicle"""
        structure = self.patterns['listicle_structure']
        
        content = structure['intro'].format(count=len(items), topic=topic)
        
        for i, item in enumerate(items, 1):
            content += structure['item'].format(
                number=i,
                title=item.get('title', ''),
                description=item.get('description', '')
            )
        
        content += structure['outro']
        
        return content
    
    def build_how_to(self, goal: str, steps: List[Dict]) -> str:
        """ساخت how-to"""
        structure = self.patterns['how_to_structure']
        
        content = structure['intro'].format(goal=goal)
        
        for i, step in enumerate(steps, 1):
            content += structure['step'].format(
                number=i,
                action=step.get('action', ''),
                explanation=step.get('explanation', '')
            )
        
        content += structure['outro']
        
        return content
    
    def build_analysis(self, topic: str, data: Dict) -> str:
        """ساخت تحلیل"""
        structure = self.patterns['analysis_structure']
        
        content = ""
        content += structure['context'].format(context=data.get('context', ''))
        content += structure['analysis'].format(analysis=data.get('analysis', ''))
        content += structure['implications'].format(implications=data.get('implications', ''))
        content += structure['conclusion'].format(conclusion=data.get('conclusion', ''))
        
        return content


class ContentGenerator:
    """تولیدکننده محتوا با استفاده از تمپلت‌ها و الگوها"""
    
    def __init__(self):
        self.template_library = TemplateLibrary()
        self.pattern_library = PatternLibrary()
        
    async def generate_tweet(self, content_type: str, data: Dict) -> str:
        """تولید توییت"""
        
        if content_type == 'news':
            return self.template_library.render_template(
                'news_announcement',
                title=data.get('title', ''),
                summary=data.get('summary', ''),
                hashtags=data.get('hashtags', ''),
                link=data.get('link', '')
            )
        
        elif content_type == 'question':
            return self.template_library.render_template(
                'question_tweet',
                question=data.get('question', ''),
                hashtags=data.get('hashtags', '')
            )
        
        elif content_type == 'video':
            return self.template_library.render_template(
                'video_promotion',
                title=data.get('title', ''),
                description=data.get('description', ''),
                link=data.get('link', ''),
                hashtags=data.get('hashtags', '')
            )
        
        return data.get('content', '')
    
    async def generate_telegram_post(self, post_type: str, data: Dict) -> str:
        """تولید پست تلگرام"""
        
        if post_type == 'announcement':
            return self.template_library.render_template(
                'telegram_announcement',
                title=data.get('title', ''),
                content=data.get('content', ''),
                footer=data.get('footer', '')
            )
        
        elif post_type == 'analysis':
            return self.template_library.render_template(
                'telegram_analysis',
                topic=data.get('topic', ''),
                analysis=data.get('analysis', ''),
                conclusion=data.get('conclusion', ''),
                tags=data.get('tags', '')
            )
        
        return data.get('content', '')
    
    async def generate_thread(self, topic: str, points: List[str]) -> List[str]:
        """تولید thread"""
        thread = []
        total = len(points) + 1  # +1 برای توییت آغازین
        
        # توییت آغازین
        intro = f"🧵 Thread: {topic}\n\n{points[0]}\n\n1/{total}"
        thread.append(intro)
        
        # بقیه توییت‌ها
        for i, point in enumerate(points[1:], 2):
            tweet = self.template_library.render_template(
                'analysis_thread',
                number=i,
                total=total,
                content=point,
                hashtags=''
            )
            thread.append(tweet)
        
        return thread
    
    async def generate_response(self, message_type: str, data: Dict) -> str:
        """تولید پاسخ"""
        
        if message_type == 'friendly':
            return self.template_library.render_template(
                'friendly_response',
                greeting=data.get('greeting', 'Hi'),
                name=data.get('name', 'there'),
                response=data.get('response', ''),
                closing=data.get('closing', 'Have a great day!')
            )
        
        elif message_type == 'technical':
            return self.template_library.render_template(
                'technical_answer',
                explanation=data.get('explanation', ''),
                points=data.get('points', '')
            )
        
        return data.get('response', '')
    
    async def enhance_with_patterns(self, content: str, 
                                   add_hook: bool = False,
                                   add_cta: bool = False) -> str:
        """بهبود محتوا با الگوها"""
        
        enhanced = content
        
        if add_hook:
            # استخراج موضوع اصلی
            topic = content.split('\n')[0] if '\n' in content else content[:50]
            hook = self.pattern_library.get_random_hook()
            hook = hook.replace('{topic}', topic)
            enhanced = f"{hook}\n\n{enhanced}"
        
        if add_cta:
            cta = self.pattern_library.get_random_cta()
            enhanced = f"{enhanced}\n\n{cta}"
        
        return enhanced
    
    def get_library_stats(self) -> Dict:
        """آمار کتابخانه‌ها"""
        return {
            'templates': self.template_library.get_statistics(),
            'patterns': {
                'total_pattern_categories': len(self.pattern_library.patterns)
            }
        }
