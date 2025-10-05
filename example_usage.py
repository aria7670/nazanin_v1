"""
Example Usage - نمونه استفاده
نحوه استفاده از ربات نازنین
"""

import asyncio
from nazanin_bot import NazaninBot
from nazanin_bot.config import Settings


async def main():
    """مثال اصلی"""
    print("=" * 60)
    print("🤖 Nazanin Bot - Example Usage")
    print("=" * 60)
    
    # ایجاد تنظیمات سفارشی (اختیاری)
    settings = Settings(
        bot_name="Nazanin",
        log_level="INFO",
        personality_extraversion=4,  # ربات برون‌گراتر
        empathy_level=0.9  # همدلی بیشتر
    )
    
    # ایجاد ربات
    bot = NazaninBot(settings=settings)
    
    # بیداری ربات
    await bot.awaken()
    
    # تعامل با ربات
    print("\n" + "=" * 60)
    print("💬 Starting Conversation")
    print("=" * 60 + "\n")
    
    # مکالمه نمونه
    conversations = [
        "Hello! How are you today?",
        "I'm feeling a bit stressed about work.",
        "Can you help me understand how to manage my time better?",
        "Thank you so much for your help!",
        "Goodbye!"
    ]
    
    for user_input in conversations:
        print(f"👤 User: {user_input}")
        
        response = await bot.process_input(user_input, user_id="user_123")
        
        print(f"🤖 Nazanin: {response}")
        print()
        
        # تأخیر کوتاه برای طبیعی بودن
        await asyncio.sleep(1)
    
    # نمایش وضعیت ربات
    print("\n" + "=" * 60)
    print("📊 Bot Status")
    print("=" * 60)
    
    status = bot.get_status()
    
    print(f"\n🤖 Bot Name: {status['name']}")
    print(f"⏱️  Uptime: {status['uptime']}")
    print(f"🧠 Cognitive Load: {status['cognitive_state']['cognitive_load']:.2%}")
    print(f"💭 Awareness Level: {status['cognitive_state']['awareness_level']:.2%}")
    print(f"😊 Current Emotion: {status['emotional_state']['current_emotion']}")
    print(f"🎭 Mood: {status['mood']['current_state']}")
    print(f"📚 Total Experiences: {status['learning']['total_experiences']}")
    print(f"✅ Learning Success Rate: {status['learning']['success_rate']:.1%}")
    print(f"💾 Short-term Memory: {status['memory']['short_term']['count']}/{status['memory']['short_term']['capacity']}")
    print(f"🗄️  Long-term Memories: {status['memory']['long_term']['total_memories']}")
    print(f"🤝 Total Relationships: {status['relationships']['total_relationships']}")
    
    # نمایش شخصیت
    print(f"\n🎭 Personality Profile:")
    personality = status['personality']
    print(f"   Summary: {personality['summary']}")
    print(f"   Curiosity Level: {personality['curiosity_level']:.1%}")
    print(f"   Risk Tolerance: {personality['risk_tolerance']:.1%}")
    
    # خاموش کردن ربات
    print("\n" + "=" * 60)
    print("Shutting down...")
    print("=" * 60)
    
    await bot.shutdown()
    
    print("\n✅ Example completed successfully!")


async def advanced_example():
    """مثال پیشرفته با ویژگی‌های بیشتر"""
    print("\n" + "=" * 60)
    print("🚀 Advanced Features Demo")
    print("=" * 60)
    
    bot = NazaninBot()
    await bot.awaken()
    
    # تنظیم هدف
    from nazanin_bot.decision.goal_manager import GoalPriority
    bot.goal_manager.add_goal(
        goal_id="learn_user_preferences",
        description="Learn user preferences and adapt",
        priority=GoalPriority.HIGH
    )
    
    # ایجاد برنامه
    plan = bot.planning_engine.create_plan(
        goal_id="learn_user_preferences",
        goal_description="Learn user preferences"
    )
    
    print(f"\n📋 Created plan with {len(plan.actions)} actions")
    
    # شبیه‌سازی یادگیری
    print("\n📚 Learning from experience...")
    bot.adaptive_learning.learn_from_experience(
        context={'type': 'greeting', 'category': 'social'},
        action='friendly_greeting',
        outcome={'user_satisfaction': 0.9},
        success=True,
        reward=0.8
    )
    
    # تأمل
    print("\n🤔 Contemplating...")
    insight = await bot.consciousness.ponder("the nature of consciousness")
    print(f"💡 Insight: {insight}")
    
    # خود‌بازتابی
    print("\n🪞 Self-reflection...")
    reflection = await bot.consciousness.self_reflect()
    print(f"   Emotional State: {reflection.get('emotional_state', 'N/A')}")
    print(f"   Engagement Level: {reflection.get('engagement_level', 'N/A')}")
    
    # شبیه‌سازی خواب (تثبیت حافظه)
    print("\n💤 Entering sleep mode for memory consolidation...")
    await bot.sleep(duration=5.0)
    
    print("\n✨ Advanced demo completed!")
    
    await bot.shutdown()


if __name__ == "__main__":
    print("\nRunning basic example...\n")
    asyncio.run(main())
    
    print("\n" + "=" * 60)
    print("\nRunning advanced example...\n")
    asyncio.run(advanced_example())
