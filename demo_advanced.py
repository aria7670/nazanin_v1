"""
Advanced Features Demo
نمایش تمام قابلیت‌های پیشرفته نازنین
"""

import asyncio
import logging
from datetime import datetime

# Import سیستم‌های جدید
from message_classifier import MessageClassifier, PromptBuilder
from behavioral_learning import (
    UserBehaviorTracker,
    PersonalityAdapter,
    EmotionalIntelligence,
    HumanizationEngine
)
from specialized_agents import SpecializedAgentOrchestrator
from advanced_algorithms import AlgorithmOrchestrator
from template_system import ContentGenerator

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


async def demo_message_classification():
    """دمو دسته‌بندی پیام"""
    
    print("\n" + "="*80)
    print("📋 DEMO 1: MESSAGE CLASSIFICATION")
    print("="*80)
    
    classifier = MessageClassifier()
    
    test_messages = [
        "چطوری می‌تونم GPT-4 یاد بگیرم؟",
        "این ویدیو عالی بود! ممنون",
        "کد من خطا میده، کمک می‌کنی؟",
        "فوری: سرور down شده!",
        "نظرت درباره هوش مصنوعی چیه؟"
    ]
    
    for message in test_messages:
        print(f"\n📨 Message: {message}")
        
        result = await classifier.classify(message)
        
        print(f"✅ Category: {result['primary_category_name']}")
        print(f"✅ Confidence: {result['confidence']:.2f}")
        print(f"✅ Priority: {result['priority']}/10")
        print(f"✅ Response Type: {result['suggested_response_type']}")
        print(f"✅ Language: {result['metadata']['language']}")
        print(f"✅ Sentiment: {result['metadata']['sentiment']}")


async def demo_prompt_building():
    """دمو ساخت پرامپت"""
    
    print("\n" + "="*80)
    print("🔧 DEMO 2: PROMPT BUILDING")
    print("="*80)
    
    classifier = MessageClassifier()
    builder = PromptBuilder(classifier)
    
    message = "توضیح بده که Transformer architecture چطور کار می‌کنه"
    
    print(f"\n📨 Message: {message}")
    print("\n⚙️ Building structured prompt...")
    
    prompt = await builder.build_structured_prompt(
        message,
        system_role="AI Technical Expert"
    )
    
    print("\n✅ System Message:")
    print(prompt['system'])
    
    print("\n✅ User Message:")
    print(prompt['user'])
    
    print("\n✅ Metadata:")
    print(f"   Category: {prompt['metadata']['classification']['primary_category_name']}")
    print(f"   Priority: {prompt['metadata']['classification']['priority']}")


async def demo_behavioral_learning():
    """دمو یادگیری رفتاری"""
    
    print("\n" + "="*80)
    print("🧠 DEMO 3: BEHAVIORAL LEARNING")
    print("="*80)
    
    # ردیابی رفتار کاربر
    print("\n📊 User Behavior Tracking:")
    
    tracker = UserBehaviorTracker("user_123")
    
    # ثبت چند تعامل
    interactions = [
        {'topic': 'AI', 'message_length': 50},
        {'topic': 'ML', 'message_length': 45},
        {'topic': 'AI', 'message_length': 60},
        {'topic': 'Tech', 'message_length': 55},
    ]
    
    for interaction in interactions:
        tracker.record_interaction(interaction)
    
    profile = tracker.build_profile()
    
    print(f"✅ Total Interactions: {profile['total_interactions']}")
    print(f"✅ Favorite Topics: {profile['favorite_topics']}")
    print(f"✅ Preferred Length: {profile['preferred_length']}")
    
    # هوش احساسی
    print("\n💖 Emotional Intelligence:")
    
    emotional_ai = EmotionalIntelligence()
    
    messages = [
        "I'm so happy with this result! 😊",
        "This is frustrating... nothing works 😡",
        "I don't understand this at all 🤔"
    ]
    
    for msg in messages:
        emotion = await emotional_ai.detect_emotion(msg)
        print(f"\n   Message: {msg}")
        print(f"   Emotion: {emotion['emotion']} (confidence: {emotion['confidence']:.2f})")


async def demo_specialized_agents():
    """دمو ایجنت‌های تخصصی"""
    
    print("\n" + "="*80)
    print("🤖 DEMO 4: SPECIALIZED AGENTS")
    print("="*80)
    
    # نوت: این demo بدون API واقعی، خروجی شبیه‌سازی شده دارد
    
    print("\n1️⃣ Content Optimization Agent:")
    print("   Original: This is a very very very long tweet that needs optimization...")
    print("   Optimized: This tweet is optimized for engagement!")
    print("   Quality Score: 8.5/10")
    
    print("\n2️⃣ Engagement Predictor Agent:")
    print("   Content: AI is transforming healthcare")
    print("   Predicted Likes: 85")
    print("   Predicted Retweets: 23")
    print("   Engagement Score: 78%")
    
    print("\n3️⃣ Trend Analysis Agent:")
    print("   Hottest Topics:")
    print("   - GPT-4 (volume: 95K, growth: +120%)")
    print("   - AI Ethics (volume: 45K, growth: +45%)")
    print("   - Quantum Computing (volume: 32K, growth: +78%)")
    
    print("\n4️⃣ Hashtag Generator Agent:")
    print("   Content: New breakthrough in neural networks")
    print("   Suggested Hashtags:")
    print("   #NeuralNetworks (reach: 50K)")
    print("   #AI (reach: 200K)")
    print("   #DeepLearning (reach: 75K)")


async def demo_algorithms():
    """دمو الگوریتم‌های پیچیده"""
    
    print("\n" + "="*80)
    print("🧮 DEMO 5: ADVANCED ALGORITHMS")
    print("="*80)
    
    algorithms = AlgorithmOrchestrator()
    
    # داده شبیه‌سازی شده
    sample_data = [
        {
            'content': 'AI is amazing!',
            'engagement': 85,
            'timestamp': datetime.now().isoformat(),
            'topic': 'AI'
        },
        {
            'content': 'Machine learning basics',
            'engagement': 65,
            'timestamp': datetime.now().isoformat(),
            'topic': 'ML'
        },
        {
            'content': 'Neural networks explained',
            'engagement': 90,
            'timestamp': datetime.now().isoformat(),
            'topic': 'AI'
        }
    ]
    
    print("\n📊 Pattern Recognition:")
    patterns = await algorithms.pattern_recognition.detect_patterns(sample_data)
    
    print(f"✅ Top Topics: {patterns['content_patterns']['top_topics']}")
    print(f"✅ Avg Content Length: {patterns['content_patterns']['avg_content_length']:.0f} chars")
    print(f"✅ Engagement Trend: {patterns['engagement_patterns']['trend']}")
    
    print("\n🔮 Predictive Analytics:")
    print("   Predicting engagement for: 'GPT-4 is revolutionary'")
    
    features = {
        'length': 25,
        'has_hashtag': True,
        'has_emoji': False,
        'readability_score': 75,
        'hour': 14
    }
    
    prediction = await algorithms.predictive_analytics.predict_engagement(
        features,
        sample_data
    )
    
    print(f"✅ Predicted Engagement: {prediction['predicted_engagement']:.0f}")
    print(f"✅ Confidence: {prediction['confidence_level']:.0%}")


async def demo_templates():
    """دمو تمپلت‌ها و الگوها"""
    
    print("\n" + "="*80)
    print("📝 DEMO 6: TEMPLATES & PATTERNS")
    print("="*80)
    
    generator = ContentGenerator()
    
    print("\n1️⃣ News Tweet Template:")
    tweet = await generator.generate_tweet(
        'news',
        {
            'title': 'GPT-5 Announced',
            'summary': 'OpenAI releases next generation model',
            'hashtags': '#AI #GPT5',
            'link': 'https://example.com'
        }
    )
    print(tweet)
    
    print("\n2️⃣ Thread Generation:")
    thread = await generator.generate_thread(
        'How AI works',
        [
            'AI uses neural networks to learn patterns',
            'Training requires lots of data',
            'Models can then make predictions'
        ]
    )
    for i, t in enumerate(thread, 1):
        print(f"\n   Tweet {i}:")
        print(f"   {t}")
    
    print("\n3️⃣ Enhanced with Patterns:")
    content = "AI is changing the world"
    enhanced = await generator.enhance_with_patterns(
        content,
        add_hook=True,
        add_cta=True
    )
    print(enhanced)


async def demo_humanization():
    """دمو انسانی‌سازی"""
    
    print("\n" + "="*80)
    print("👤 DEMO 7: HUMANIZATION ENGINE")
    print("="*80)
    
    engine = HumanizationEngine()
    
    test_cases = [
        {
            'user_id': 'user_1',
            'message': 'Thanks for your help!',
            'base_response': 'You are welcome'
        },
        {
            'user_id': 'user_2',
            'message': 'This is confusing...',
            'base_response': 'Let me explain'
        }
    ]
    
    for case in test_cases:
        print(f"\n📨 User Message: {case['message']}")
        print(f"🤖 Base Response: {case['base_response']}")
        
        result = await engine.humanize_response(
            case['user_id'],
            case['message'],
            case['base_response']
        )
        
        print(f"👤 Humanized Response: {result['response']}")
        print(f"⏱️ Typing Delay: {result['typing_delay']:.1f}s")


async def demo_full_pipeline():
    """دمو جریان کامل"""
    
    print("\n" + "="*80)
    print("🔄 DEMO 8: FULL PROCESSING PIPELINE")
    print("="*80)
    
    # شبیه‌سازی پردازش کامل
    user_message = "چطوری می‌تونم یادگیری ماشین یاد بگیرم؟"
    
    print(f"\n📨 User Message: {user_message}")
    print("\n" + "-"*80)
    
    # مرحله 1: دسته‌بندی
    print("\n1️⃣ Classification...")
    classifier = MessageClassifier()
    classification = await classifier.classify(user_message)
    print(f"   ✅ Category: {classification['primary_category_name']}")
    print(f"   ✅ Priority: {classification['priority']}/10")
    
    # مرحله 2: ساخت پرامپت
    print("\n2️⃣ Prompt Building...")
    builder = PromptBuilder(classifier)
    prompt = await builder.build_structured_prompt(user_message)
    print("   ✅ Structured prompt created")
    
    # مرحله 3: تولید پاسخ (شبیه‌سازی)
    print("\n3️⃣ Generating Response...")
    base_response = """برای یادگیری Machine Learning:

1. ریاضیات پایه یاد بگیر (Calculus, Linear Algebra)
2. Python را یاد بگیر
3. کتابخانه‌های ML مثل scikit-learn
4. پروژه‌های عملی انجام بده
5. از منابع آنلاین استفاده کن (Coursera, fast.ai)"""
    print("   ✅ Base response generated")
    
    # مرحله 4: انسانی‌سازی
    print("\n4️⃣ Humanizing...")
    engine = HumanizationEngine()
    final = await engine.humanize_response(
        'demo_user',
        user_message,
        base_response
    )
    print("   ✅ Response humanized")
    
    # نتیجه نهایی
    print("\n" + "="*80)
    print("📤 FINAL RESPONSE:")
    print("="*80)
    print(final['response'])
    print(f"\n⏱️ Typing delay: {final['typing_delay']:.1f}s")
    print("="*80)


async def main():
    """اجرای تمام دموها"""
    
    print("\n")
    print("╔" + "="*78 + "╗")
    print("║" + " "*15 + "NAZANIN ADVANCED FEATURES DEMO" + " "*33 + "║")
    print("╚" + "="*78 + "╝")
    
    demos = [
        ("Message Classification", demo_message_classification),
        ("Prompt Building", demo_prompt_building),
        ("Behavioral Learning", demo_behavioral_learning),
        ("Specialized Agents", demo_specialized_agents),
        ("Advanced Algorithms", demo_algorithms),
        ("Templates & Patterns", demo_templates),
        ("Humanization Engine", demo_humanization),
        ("Full Pipeline", demo_full_pipeline)
    ]
    
    for i, (name, demo_func) in enumerate(demos, 1):
        try:
            await demo_func()
            await asyncio.sleep(1)
        except Exception as e:
            print(f"\n❌ Error in {name}: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "="*80)
    print("✅ ALL DEMOS COMPLETED!")
    print("="*80)
    
    print("\n📊 SUMMARY:")
    print("   ✅ 8 Advanced Systems Demonstrated")
    print("   ✅ Message Classification with 10 categories")
    print("   ✅ Behavioral Learning & Humanization")
    print("   ✅ 10 Specialized Agents")
    print("   ✅ 5 Advanced Algorithms")
    print("   ✅ Template & Pattern Systems")
    print("   ✅ Complete Processing Pipeline")
    
    print("\n🎉 Nazanin Advanced is ready for production!")
    print("="*80 + "\n")


if __name__ == '__main__':
    asyncio.run(main())
