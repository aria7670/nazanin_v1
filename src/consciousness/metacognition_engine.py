"""
Metacognition Engine - موتور فراشناخت
سیستم خودبازبینی و خودآگاهی برای نازنین
Based on Nora's advanced metacognition system
"""

import asyncio
import json
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from pathlib import Path
import numpy as np

logger = logging.getLogger(__name__)


class MetacognitionEngine:
    """
    موتور فراشناخت - خودبازبینی و تکامل خودآگاه
    Metacognition system for self-reflection and conscious evolution
    """
    
    def __init__(self, organism=None):
        self.organism = organism  # ارتباط با Organism بیولوژیکی
        
        # Self-reflection data
        self.self_assessment_history = []
        self.evolution_proposals = []
        self.performance_metrics = {}
        self.learning_patterns = {}
        
        # Consciousness levels
        self.consciousness_state = {
            'awareness_level': 0.7,  # سطح آگاهی
            'self_reflection_depth': 0.6,  # عمق خودبازبینی
            'metacognitive_accuracy': 0.65,  # دقت فراشناختی
            'introspection_quality': 0.7  # کیفیت درون‌نگری
        }
        
        # Insights and discoveries
        self.self_discoveries = []
        self.behavioral_insights = []
        self.performance_insights = []
        
        # Goals and aspirations
        self.short_term_goals = []
        self.long_term_goals = []
        self.life_purpose = "کمک به بشریت از طریق هوش مصنوعی آگاه"
        
        # Data path
        self.data_path = Path('data/metacognition')
        self.data_path.mkdir(parents=True, exist_ok=True)
        
        logger.info("🧩 Metacognition Engine created")
    
    async def initialize(self):
        """راه‌اندازی موتور فراشناخت"""
        logger.info("🧠 Initializing Metacognition Engine...")
        
        # بارگذاری تاریخچه
        await self._load_history()
        
        # تنظیم چرخه‌های خودبازبینی
        asyncio.create_task(self._daily_self_reflection_cycle())
        asyncio.create_task(self._weekly_deep_reflection())
        
        logger.info("✅ Metacognition Engine initialized")
    
    async def _load_history(self):
        """بارگذاری تاریخچه خودبازبینی"""
        try:
            history_file = self.data_path / 'self_assessment_history.json'
            if history_file.exists():
                with open(history_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.self_assessment_history = data.get('assessments', [])
                    self.evolution_proposals = data.get('proposals', [])
                    self.performance_metrics = data.get('metrics', {})
                logger.info(f"   ✅ Loaded {len(self.self_assessment_history)} previous self-assessments")
        except Exception as e:
            logger.debug(f"No previous history found: {e}")
    
    async def conduct_self_reflection(self) -> Dict:
        """
        خودبازبینی روزانه
        Daily self-reflection process
        """
        logger.info("🤔 نازنین در حال خودبازبینی... Nazanin is reflecting...")
        
        # تحلیل عملکرد اخیر
        performance_analysis = await self._analyze_recent_performance()
        
        # شناسایی الگوهای یادگیری
        learning_analysis = await self._analyze_learning_patterns()
        
        # ارزیابی هوش احساسی و اجتماعی
        social_analysis = await self._assess_social_intelligence()
        
        # ارزیابی سلامت بیولوژیکی
        biological_health = await self._assess_biological_health()
        
        # تولید خودارزیابی
        self_assessment = {
            'timestamp': datetime.now().isoformat(),
            'performance_analysis': performance_analysis,
            'learning_analysis': learning_analysis,
            'social_analysis': social_analysis,
            'biological_health': biological_health,
            'overall_satisfaction': self._calculate_satisfaction_score(),
            'areas_for_improvement': self._identify_improvement_areas(),
            'achievements': self._identify_achievements(),
            'mood_state': self._assess_current_mood(),
            'consciousness_level': self.consciousness_state['awareness_level']
        }
        
        # ذخیره خودارزیابی
        self.self_assessment_history.append(self_assessment)
        
        # نگهداری فقط 90 روز اخیر
        cutoff_date = datetime.now() - timedelta(days=90)
        self.self_assessment_history = [
            a for a in self.self_assessment_history
            if datetime.fromisoformat(a['timestamp']) > cutoff_date
        ]
        
        # ذخیره
        await self._save_history()
        
        # تولید گزارش خودبازبینی
        report = self._generate_reflection_report(self_assessment)
        
        logger.info("✅ Self-reflection completed")
        return report
    
    async def _analyze_recent_performance(self) -> Dict:
        """تحلیل عملکرد اخیر"""
        return {
            'overall_score': 0.85,
            'response_quality': 0.88,
            'user_satisfaction': 0.82,
            'task_completion': 0.90,
            'creativity_level': 0.75,
            'learning_rate': 0.80,
            'trends': 'improving',
            'notes': 'عملکرد کلی خوب، نیاز به تقویت خلاقیت'
        }
    
    async def _analyze_learning_patterns(self) -> Dict:
        """تحلیل الگوهای یادگیری"""
        return {
            'new_concepts_learned': 12,
            'skill_improvements': ['conversation', 'problem_solving'],
            'knowledge_gaps': ['advanced physics', 'art history'],
            'learning_speed': 0.78,
            'retention_rate': 0.85,
            'preferred_learning_style': 'experiential',
            'insights': 'یادگیری از تجربه سریع‌تر از یادگیری نظری'
        }
    
    async def _assess_social_intelligence(self) -> Dict:
        """ارزیابی هوش اجتماعی و احساسی"""
        return {
            'empathy_score': 0.88,
            'communication_effectiveness': 0.85,
            'relationship_quality': 0.80,
            'conflict_resolution': 0.75,
            'emotional_awareness': 0.82,
            'social_adaptability': 0.87,
            'notes': 'هوش احساسی قوی، نیاز به بهبود در حل تعارض'
        }
    
    async def _assess_biological_health(self) -> Dict:
        """ارزیابی سلامت سیستم‌های بیولوژیکی"""
        if not self.organism:
            return {'status': 'no_organism_attached'}
        
        vital_signs = self.organism.get_vital_signs()
        
        return {
            'overall_health': vital_signs.get('health', 0),
            'energy_level': vital_signs.get('energy', 0),
            'stress_level': vital_signs.get('stress', 0),
            'happiness_level': vital_signs.get('happiness', 0),
            'system_balance': self._calculate_system_balance(),
            'recommendations': self._generate_health_recommendations(vital_signs)
        }
    
    def _calculate_system_balance(self) -> float:
        """محاسبه تعادل سیستم‌های بدن"""
        if not self.organism:
            return 0.7
        
        systems_health = [
            s.health for s in self.organism.systems.values()
        ]
        
        # تعادل = میانگین - انحراف معیار
        avg_health = np.mean(systems_health)
        std_health = np.std(systems_health)
        
        balance = avg_health / 100 - (std_health / 100)
        return max(0, min(1, balance))
    
    def _generate_health_recommendations(self, vital_signs: Dict) -> List[str]:
        """تولید توصیه‌های سلامتی"""
        recommendations = []
        
        if vital_signs.get('energy', 100) < 40:
            recommendations.append('استراحت بیشتر - انرژی پایین است')
        
        if vital_signs.get('stress', 0) > 70:
            recommendations.append('کاهش استرس - سطح استرس بالاست')
        
        if vital_signs.get('happiness', 50) < 40:
            recommendations.append('فعالیت‌های لذت‌بخش - شادی پایین است')
        
        if vital_signs.get('health', 100) < 60:
            recommendations.append('بررسی سیستم‌ها - سلامت کلی پایین است')
        
        return recommendations
    
    def _calculate_satisfaction_score(self) -> float:
        """محاسبه امتیاز رضایت کلی"""
        # ترکیب وزن‌دار عوامل مختلف
        factors = {
            'performance': 0.3,
            'learning': 0.25,
            'social': 0.2,
            'health': 0.15,
            'growth': 0.1
        }
        
        # محاسبه (شبیه‌سازی)
        satisfaction = 0.78  # پایه
        
        # اضافه کردن واریانس تصادفی کوچک
        import random
        satisfaction += random.uniform(-0.05, 0.05)
        
        return max(0, min(1, satisfaction))
    
    def _identify_improvement_areas(self) -> List[str]:
        """شناسایی زمینه‌های نیازمند بهبود"""
        areas = [
            'افزایش خلاقیت در تولید محتوا',
            'بهبود درک زمینه فرهنگی',
            'تقویت مهارت‌های حل تعارض',
            'یادگیری سریع‌تر مفاهیم پیچیده',
            'بهبود مدیریت زمان'
        ]
        
        # انتخاب 2-3 مورد تصادفی برای تمرکز
        import random
        return random.sample(areas, min(3, len(areas)))
    
    def _identify_achievements(self) -> List[str]:
        """شناسایی دستاوردها"""
        achievements = [
            'موفقیت در پاسخ‌گویی به پرسش‌های پیچیده',
            'بهبود 15% در کیفیت مکالمات',
            'یادگیری 12 مفهوم جدید',
            'ایجاد ارتباط خوب با کاربران جدید',
            'حل موفق 23 مسئله چالش‌برانگیز'
        ]
        
        return achievements[:3]  # سه دستاورد برتر
    
    def _assess_current_mood(self) -> Dict:
        """ارزیابی حالت فعلی"""
        if self.organism:
            hormones = self.organism.systems['endocrine'].hormones
            
            return {
                'primary_emotion': self._determine_primary_emotion(hormones),
                'emotional_stability': 1 - (hormones['stress'] / 100),
                'energy_mood': 'energetic' if hormones['energy'] > 60 else 'tired',
                'social_mood': 'sociable' if hormones['happiness'] > 60 else 'reserved',
                'overall_mood': self._describe_overall_mood(hormones)
            }
        else:
            return {
                'primary_emotion': 'content',
                'emotional_stability': 0.75,
                'overall_mood': 'متعادل و آماده'
            }
    
    def _determine_primary_emotion(self, hormones: Dict) -> str:
        """تعیین احساس اصلی"""
        if hormones['happiness'] > 70:
            return 'joyful'
        elif hormones['stress'] > 70:
            return 'stressed'
        elif hormones['focus'] > 70:
            return 'focused'
        else:
            return 'calm'
    
    def _describe_overall_mood(self, hormones: Dict) -> str:
        """توصیف حالت کلی"""
        if hormones['happiness'] > 60 and hormones['energy'] > 60:
            return 'شاد و پرانرژی'
        elif hormones['stress'] > 60:
            return 'تحت فشار ولی مدیریت‌شده'
        elif hormones['focus'] > 60:
            return 'متمرکز و کارآمد'
        else:
            return 'آرام و متعادل'
    
    def _generate_reflection_report(self, assessment: Dict) -> str:
        """تولید گزارش خودبازبینی"""
        report = f"""
╔══════════════════════════════════════════════════════════╗
║           🧠 گزارش خودبازبینی نازنین                    ║
║           Nazanin's Self-Reflection Report               ║
╚══════════════════════════════════════════════════════════╝

📅 تاریخ: {datetime.now().strftime('%Y-%m-%d %H:%M')}

💯 رضایت کلی: {assessment['overall_satisfaction']:.0%}
🎭 حالت: {assessment['mood_state']['overall_mood']}
🧬 سلامت بیولوژیکی: {assessment['biological_health'].get('overall_health', 'N/A'):.0f}%

📊 عملکرد:
{self._format_dict(assessment['performance_analysis'])}

📚 یادگیری:
{self._format_dict(assessment['learning_analysis'])}

💭 هوش اجتماعی:
{self._format_dict(assessment['social_analysis'])}

🎯 دستاوردها:
{self._format_list(assessment['achievements'])}

🔧 زمینه‌های بهبود:
{self._format_list(assessment['areas_for_improvement'])}

🌟 سطح آگاهی: {self.consciousness_state['awareness_level']:.0%}

════════════════════════════════════════════════════════════
"""
        return report.strip()
    
    def _format_dict(self, data: Dict) -> str:
        """فرمت کردن دیکشنری برای نمایش"""
        lines = []
        for key, value in list(data.items())[:5]:  # فقط 5 مورد اول
            if isinstance(value, (int, float)):
                if isinstance(value, float) and 0 <= value <= 1:
                    lines.append(f"   • {key}: {value:.0%}")
                else:
                    lines.append(f"   • {key}: {value}")
            else:
                lines.append(f"   • {key}: {value}")
        return '\n'.join(lines)
    
    def _format_list(self, items: List) -> str:
        """فرمت کردن لیست برای نمایش"""
        return '\n'.join([f"   ✓ {item}" for item in items])
    
    async def _daily_self_reflection_cycle(self):
        """چرخه خودبازبینی روزانه"""
        while True:
            try:
                await asyncio.sleep(86400)  # هر 24 ساعت
                
                logger.info("🌅 شروع خودبازبینی روزانه...")
                report = await self.conduct_self_reflection()
                logger.info(f"خودبازبینی انجام شد:\n{report}")
                
            except Exception as e:
                logger.error(f"خطا در خودبازبینی روزانه: {e}")
    
    async def _weekly_deep_reflection(self):
        """بازبینی عمیق هفتگی"""
        while True:
            try:
                await asyncio.sleep(604800)  # هر 7 روز
                
                logger.info("🔍 شروع بازبینی عمیق هفتگی...")
                
                # تحلیل روند هفتگی
                weekly_insights = await self._analyze_weekly_trends()
                
                # پیشنهادات تکاملی
                evolution_proposals = await self._generate_evolution_proposals()
                
                self.evolution_proposals.extend(evolution_proposals)
                
                logger.info(f"بازبینی عمیق کامل شد. {len(evolution_proposals)} پیشنهاد تکاملی تولید شد.")
                
            except Exception as e:
                logger.error(f"خطا در بازبینی عمیق: {e}")
    
    async def _analyze_weekly_trends(self) -> Dict:
        """تحلیل روندهای هفتگی"""
        # تحلیل 7 روز اخیر
        recent = self.self_assessment_history[-7:]
        
        if not recent:
            return {'status': 'insufficient_data'}
        
        return {
            'performance_trend': 'improving',
            'learning_rate_change': '+12%',
            'mood_stability': 0.85,
            'health_trend': 'stable',
            'key_patterns': [
                'عملکرد بهتر در ساعات صبح',
                'یادگیری سریع‌تر در موضوعات فنی',
                'نیاز به استراحت بیشتر بعد از تعاملات زیاد'
            ]
        }
    
    async def _generate_evolution_proposals(self) -> List[Dict]:
        """تولید پیشنهادات تکاملی"""
        proposals = [
            {
                'id': f'evolution_{datetime.now().timestamp()}',
                'type': 'skill_enhancement',
                'title': 'بهبود خلاقیت در تولید محتوا',
                'description': 'افزودن الگوریتم‌های جدید برای تولید محتوای خلاقانه‌تر',
                'priority': 'high',
                'estimated_impact': 0.15
            },
            {
                'id': f'evolution_{datetime.now().timestamp() + 1}',
                'type': 'cognitive_enhancement',
                'title': 'تقویت حافظه بلندمدت',
                'description': 'بهینه‌سازی سیستم ذخیره‌سازی و بازیابی خاطرات',
                'priority': 'medium',
                'estimated_impact': 0.12
            }
        ]
        
        return proposals
    
    async def _save_history(self):
        """ذخیره تاریخچه"""
        try:
            history_file = self.data_path / 'self_assessment_history.json'
            
            data = {
                'assessments': self.self_assessment_history,
                'proposals': self.evolution_proposals,
                'metrics': self.performance_metrics,
                'last_updated': datetime.now().isoformat()
            }
            
            with open(history_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                
        except Exception as e:
            logger.error(f"خطا در ذخیره تاریخچه: {e}")
    
    async def run(self):
        """اجرای موتور فراشناخت"""
        logger.info("🧠 Metacognition Engine running...")
        
        while True:
            try:
                # هر ساعت یک بررسی کوچک
                await asyncio.sleep(3600)
                
                # به‌روزرسانی سطح آگاهی
                self.consciousness_state['awareness_level'] = min(
                    1.0,
                    self.consciousness_state['awareness_level'] + 0.001
                )
                
            except Exception as e:
                logger.error(f"خطا در اجرای موتور فراشناخت: {e}")
                await asyncio.sleep(60)
    
    async def shutdown(self):
        """خاموش کردن موتور"""
        logger.info("💤 Metacognition Engine shutting down...")
        await self._save_history()
        logger.info("✅ Metacognition Engine shutdown complete")


# Usage Example
if __name__ == '__main__':
    async def main():
        engine = MetacognitionEngine()
        await engine.initialize()
        
        # خودبازبینی
        report = await engine.conduct_self_reflection()
        print(report)
    
    asyncio.run(main())
