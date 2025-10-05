# راهنمای سریع Nazanin Bot 🚀

## نصب سریع

```bash
# کلون پروژه
git clone <repository-url>
cd nazanin_bot

# نصب وابستگی‌ها
pip install -r requirements.txt

# یا نصب با setup.py
pip install -e .
```

## اولین اجرا

```python
import asyncio
from nazanin_bot import NazaninBot

async def main():
    # ایجاد ربات
    bot = NazaninBot()
    
    # بیداری
    await bot.awaken()
    
    # تعامل
    response = await bot.process_input("Hello!", user_id="user1")
    print(response)
    
    # خاموش کردن
    await bot.shutdown()

asyncio.run(main())
```

## مثال‌های کاربردی

### 1. تعامل ساده

```python
bot = NazaninBot()
await bot.awaken()

# تعامل با کاربر
response = await bot.process_input(
    "I'm feeling stressed about work",
    user_id="user123"
)
print(response)
# خروجی: "I understand how you feel. That sounds really difficult. ..."
```

### 2. تنظیمات شخصی‌سازی

```python
from nazanin_bot.config import Settings

settings = Settings(
    bot_name="MyBot",
    personality_extraversion=5,  # خیلی برون‌گرا
    empathy_level=0.95,          # همدلی بسیار بالا
    log_level="DEBUG"
)

bot = NazaninBot(settings=settings)
```

### 3. مدیریت اهداف

```python
from nazanin_bot.decision.goal_manager import GoalPriority

# افزودن هدف
bot.goal_manager.add_goal(
    goal_id="help_user_learn",
    description="Help user learn Python programming",
    priority=GoalPriority.HIGH
)

# پیگیری پیشرفت
bot.goal_manager.update_progress("help_user_learn", 0.6)
```

### 4. کار با حافظه

```python
# ذخیره در حافظه کوتاه‌مدت
bot.short_term_memory.store(
    item_id="user_preference",
    content={"likes": "Python", "dislikes": "bugs"},
    importance=0.9
)

# بازیابی
pref = bot.short_term_memory.recall("user_preference")

# ذخیره در حافظه بلندمدت
bot.long_term_memory.store(
    memory_id="user_profile",
    content={"name": "John", "interests": ["AI", "ML"]},
    category="semantic",
    importance=0.85
)
```

### 5. تحلیل احساسات

```python
# تشخیص احساس
emotions = bot.emotion_detector.comprehensive_analysis(
    "I'm so excited about this project!"
)

print(emotions['dominant'])  # خروجی: 'joy'
print(emotions['emotions'])   # تمام احساسات شناسایی شده
```

### 6. دریافت وضعیت

```python
status = bot.get_status()

print(f"🧠 Cognitive Load: {status['cognitive_state']['cognitive_load']:.1%}")
print(f"😊 Current Emotion: {status['emotional_state']['current_emotion']}")
print(f"💭 Mood: {status['mood']['current_state']}")
print(f"📚 Learning Success: {status['learning']['success_rate']:.1%}")
print(f"💾 Memories: STM={status['memory']['short_term']['count']}, "
      f"LTM={status['memory']['long_term']['total_memories']}")
```

## ویژگی‌های پیشرفته

### خواب و تثبیت حافظه

```python
# ورود به حالت خواب (تثبیت حافظه)
await bot.sleep(duration=60.0)  # 60 ثانیه

# خواب به صورت خودکار (بر اساس زمان)
settings = Settings(
    enable_auto_sleep=True,
    sleep_hours_start=2,  # 2 صبح
    sleep_hours_end=5     # 5 صبح
)
```

### خود‌بازتابی و تأمل

```python
# تأمل درباره موضوع
insight = await bot.consciousness.ponder("the nature of intelligence")
print(insight)

# خود‌بازتابی
reflection = await bot.consciousness.self_reflect()
print(f"Emotional State: {reflection['emotional_state']}")
print(f"Engagement: {reflection['engagement_level']}")
```

### یادگیری از تجربه

```python
# یادگیری
lessons = bot.adaptive_learning.learn_from_experience(
    context={'type': 'conversation', 'topic': 'python'},
    action='provide_code_example',
    outcome={'user_satisfied': True},
    success=True,
    reward=0.9
)

print("Lessons learned:")
for lesson in lessons:
    print(f"  - {lesson}")
```

### پیش‌بینی موفقیت

```python
# پیش‌بینی احتمال موفقیت یک اقدام
probability = bot.adaptive_learning.predict_success(
    context={'type': 'conversation'},
    action='provide_code_example'
)

print(f"Success probability: {probability:.1%}")
```

## نکات مهم ⚠️

### 1. همیشه از async/await استفاده کنید

```python
# ✅ درست
await bot.awaken()
response = await bot.process_input("Hello")

# ❌ غلط (بدون await)
bot.awaken()  # کار نمی‌کند!
```

### 2. ربات را قبل از خروج خاموش کنید

```python
# ✅ درست
try:
    await bot.awaken()
    # ... کار با ربات
finally:
    await bot.shutdown()

# یا با context manager (آینده)
async with NazaninBot() as bot:
    # ... کار با ربات
```

### 3. از user_id برای پیگیری روابط استفاده کنید

```python
# هر کاربر یک شناسه منحصر به فرد
await bot.process_input("Hello", user_id="user123")
await bot.process_input("Hi", user_id="user456")

# ربات روابط جداگانه نگه می‌دارد
```

### 4. حافظه را مدیریت کنید

```python
# پاکسازی دوره‌ای حافظه کوتاه‌مدت
bot.short_term_memory.cleanup_expired()

# حذف خاطرات ضعیف
bot.long_term_memory.forget_weak_memories(threshold=0.2)
```

## عیب‌یابی

### خطای "No module named 'numpy'"

```bash
pip install numpy
```

### خطای "Database is locked"

```python
# مطمئن شوید فقط یک نمونه ربات در حال اجرا است
# یا از مسیر متفاوت برای دیتابیس استفاده کنید
settings = Settings(
    long_term_memory_path="./data/bot2_ltm.db"
)
```

### لاگ‌های زیاد

```python
# کاهش سطح لاگ
settings = Settings(log_level="WARNING")
```

## اجرای مثال‌ها

```bash
# مثال پایه
python example_usage.py

# با تنظیمات سفارشی
python -c "
from nazanin_bot import NazaninBot
from nazanin_bot.config import Settings
import asyncio

async def main():
    settings = Settings(personality_extraversion=5)
    bot = NazaninBot(settings)
    await bot.awaken()
    print(bot.personality.get_personality_summary())
    await bot.shutdown()

asyncio.run(main())
"
```

## منابع بیشتر

- 📖 [مستندات کامل](README.md)
- 🏗️ [معماری سیستم](ARCHITECTURE.md)
- 🧪 [تست‌ها](tests/)
- 💡 [مثال‌های پیشرفته](example_usage.py)

## پشتیبانی

- 🐛 گزارش باگ: [GitHub Issues]
- 💬 سوالات: [Discussions]
- 📧 ایمیل: support@nazanin-bot.com

---

**موفق باشید! 🚀**
