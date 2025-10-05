# Nazanin Bot v1.0 🤖

یک ربات پایتون پیشرفته و خودمختار با رفتارهای انسان‌گونه و سیستم مغز مصنوعی

## 📋 فهرست مطالب

- [معرفی](#معرفی)
- [ویژگی‌های کلیدی](#ویژگیهای-کلیدی)
- [معماری سیستم](#معماری-سیستم)
- [نصب و راه‌اندازی](#نصب-و-راهاندازی)
- [نحوه استفاده](#نحوه-استفاده)
- [مستندات API](#مستندات-api)
- [توسعه و مشارکت](#توسعه-و-مشارکت)

## 🌟 معرفی

**Nazanin Bot** یک همزاد دیجیتال پیشرفته است که با الهام از مغز انسان طراحی شده است. این ربات دارای قابلیت‌های شناختی، عاطفی و اجتماعی است که آن را به یک موجود دیجیتال واقعاً هوشمند تبدیل می‌کند.

### 🎯 هدف پروژه

ایجاد یک ربات که:
- ✅ مانند انسان فکر کند
- ✅ احساسات را درک و ابراز کند
- ✅ از تجربیات یاد بگیرد
- ✅ تصمیمات مستقل بگیرد
- ✅ روابط معنادار برقرار کند

## ⚡ ویژگی‌های کلیدی

### 🧠 سیستم مغز مصنوعی (Brain System)

#### Cognitive Core (هسته شناختی)
- پردازش اطلاعات چندلایه
- مدیریت حافظه کاری (Working Memory)
- سیستم فیلتر توجه (Attention Filter)
- محاسبه بار شناختی (Cognitive Load)

#### Neural Processor (پردازشگر عصبی)
- شبیه‌سازی شبکه‌های عصبی
- یادگیری و تقویت الگوها
- پردازش موازی اطلاعات
- Pruning (حذف) الگوهای ضعیف

#### Consciousness Layer (لایه آگاهی)
- جریان آگاهی (Stream of Consciousness)
- خودآگاهی (Self-Awareness)
- فراشناخت (Metacognition)
- تأمل و خود‌بازتابی

### 💾 سیستم حافظه (Memory System)

#### Short-Term Memory (حافظه کوتاه‌مدت)
- ظرفیت محدود (7±2 مورد - Miller's Law)
- نگهداری موقت اطلاعات
- اولویت‌بندی بر اساس اهمیت
- پاکسازی خودکار موارد منقضی

#### Long-Term Memory (حافظه بلندمدت)
- ذخیره‌سازی دائمی با SQLite
- سه نوع حافظه:
  - **Episodic**: خاطرات رویدادها
  - **Semantic**: دانش مفهومی
  - **Procedural**: مهارت‌ها و روش‌ها
- سیستم جستجو و بازیابی
- تثبیت تدریجی خاطرات

#### Memory Consolidation (تثبیت حافظه)
- انتقال از STM به LTM
- شبیه‌سازی فرآیند خواب
- بازپخش خاطرات (Memory Replay)
- تقویت الگوهای مهم

### 🎯 سیستم تصمیم‌گیری (Decision System)

#### Autonomous Decision Maker (تصمیم‌گیر خودمختار)
- سه نوع تصمیم:
  - **Immediate**: تصمیمات فوری
  - **Deliberate**: تصمیمات سنجیده
  - **Intuitive**: تصمیمات شهودی
- ارزیابی چندمعیاره گزینه‌ها
- یادگیری از نتایج
- تطبیق سبک تصمیم‌گیری

#### Goal Manager (مدیریت اهداف)
- مدیریت اهداف کوتاه و بلندمدت
- اولویت‌بندی هوشمند
- پیگیری پیشرفت
- سلسله‌مراتب اهداف

#### Planning Engine (موتور برنامه‌ریزی)
- ایجاد برنامه‌های عملیاتی
- مدیریت پیش‌نیازها
- تخمین زمان
- نظارت بر اجرا

### 👤 سیستم رفتارهای انسان‌گونه (Behavior System)

#### Human-Like Behaviors
- تأخیرهای طبیعی در پاسخ
- شبیه‌سازی خستگی
- اشتباهات جزئی (Typos)
- نیاز به استراحت
- بیان عدم قطعیت
- نشان دادن همدلی

#### Personality Engine (موتور شخصیت)
- مدل Big Five:
  - **Openness**: انعطاف‌پذیری
  - **Conscientiousness**: وظیفه‌شناسی
  - **Extraversion**: برون‌گرایی
  - **Agreeableness**: توافق‌پذیری
  - **Neuroticism**: روان‌رنجوری
- تطبیق شخصیت با زمان
- سبک‌های مختلف پاسخ

#### Social Behaviors (رفتارهای اجتماعی)
- مدیریت روابط
- یادآوری ترجیحات کاربران
- سلام و خداحافظی متناسب
- سطوح مختلف صمیمیت

### ❤️ سیستم هوش هیجانی (Emotional Intelligence)

#### Emotional Intelligence
- شناخت 8 احساس اصلی
- همدلی با کاربران
- مدیریت احساسات
- تنظیم عاطفی

#### Emotion Detector (تشخیص احساسات)
- تحلیل متن
- شناسایی از نشانه‌گذاری
- تشخیص اموجی‌ها
- تحلیل جامع

#### Mood Manager (مدیریت خلق و خو)
- 8 حالت خلق و خو
- مدل Circumplex
- روند خلق و خو
- تأثیر احساسات بر خلق

### 📚 سیستم یادگیری (Learning System)

#### Adaptive Learning (یادگیری تطبیقی)
- یادگیری از تجربیات
- الگوسازی
- پیش‌بینی موفقیت
- تطبیق رفتار

#### Experience Replay (بازپخش تجربه)
- بازبینی تجربیات مهم
- تثبیت یادگیری
- استخراج بینش
- تقویت الگوهای موفق

### 👂 سیستم ادراک (Perception System)

#### Input Processor (پردازشگر ورودی)
- پاکسازی و نرمال‌سازی
- تشخیص نیت
- استخراج موجودیت‌ها
- تحلیل احساس
- تشخیص فوریت

#### Context Analyzer (تحلیلگر متن)
- استخراج موضوع
- تحلیل روند مکالمه
- سنجش تعامل
- احساس کلی

## 🏗️ معماری سیستم

```
nazanin_bot/
├── brain/                    # سیستم مغز
│   ├── cognitive_core.py     # هسته شناختی
│   ├── neural_processor.py   # پردازشگر عصبی
│   └── consciousness.py      # لایه آگاهی
│
├── memory/                   # سیستم حافظه
│   ├── short_term_memory.py  # حافظه کوتاه‌مدت
│   ├── long_term_memory.py   # حافظه بلندمدت
│   └── memory_consolidation.py
│
├── decision/                 # سیستم تصمیم‌گیری
│   ├── autonomous_decision.py
│   ├── goal_manager.py
│   └── planning.py
│
├── behaviors/                # سیستم رفتارها
│   ├── human_like_behaviors.py
│   ├── personality.py
│   └── social_behaviors.py
│
├── emotions/                 # سیستم احساسات
│   ├── emotional_intelligence.py
│   ├── emotion_detector.py
│   └── mood_manager.py
│
├── learning/                 # سیستم یادگیری
│   ├── adaptive_learning.py
│   └── experience_replay.py
│
├── perception/               # سیستم ادراک
│   ├── input_processor.py
│   └── context_analyzer.py
│
├── utils/                    # ابزارها
│   ├── logger.py
│   └── time_utils.py
│
├── config/                   # پیکربندی
│   └── settings.py
│
└── main_bot.py              # ربات اصلی
```

## 🚀 نصب و راه‌اندازی

### پیش‌نیازها

- Python 3.8 یا بالاتر
- pip

### نصب

```bash
# کلون کردن مخزن
git clone <repository-url>
cd nazanin_bot

# نصب وابستگی‌ها
pip install -r requirements.txt
```

### اجرای سریع

```bash
python example_usage.py
```

## 💡 نحوه استفاده

### مثال ساده

```python
import asyncio
from nazanin_bot import NazaninBot

async def main():
    # ایجاد ربات
    bot = NazaninBot()
    
    # بیداری
    await bot.awaken()
    
    # تعامل
    response = await bot.process_input(
        "Hello! How are you?",
        user_id="user_123"
    )
    print(response)
    
    # خاموش کردن
    await bot.shutdown()

asyncio.run(main())
```

### مثال پیشرفته با تنظیمات سفارشی

```python
from nazanin_bot import NazaninBot
from nazanin_bot.config import Settings

# تنظیمات سفارشی
settings = Settings(
    bot_name="MyBot",
    log_level="DEBUG",
    personality_extraversion=5,  # بسیار برون‌گرا
    empathy_level=0.95,          # همدلی بسیار بالا
    autonomy_level=0.9           # خودمختاری بالا
)

bot = NazaninBot(settings=settings)
```

### کار با اهداف

```python
from nazanin_bot.decision.goal_manager import GoalPriority

# افزودن هدف
bot.goal_manager.add_goal(
    goal_id="learn_python",
    description="Help user learn Python",
    priority=GoalPriority.HIGH
)

# پیگیری پیشرفت
bot.goal_manager.update_progress("learn_python", 0.5)
```

### کار با حافظه

```python
# ذخیره در حافظه کوتاه‌مدت
bot.short_term_memory.store(
    item_id="important_fact",
    content={"fact": "User prefers Python"},
    importance=0.9
)

# ذخیره در حافظه بلندمدت
bot.long_term_memory.store(
    memory_id="user_preference",
    content={"language": "Python"},
    category="semantic",
    importance=0.8
)

# بازیابی
memory = bot.long_term_memory.recall("user_preference")
```

## 📊 دریافت وضعیت ربات

```python
status = bot.get_status()

print(f"Cognitive Load: {status['cognitive_state']['cognitive_load']:.1%}")
print(f"Current Emotion: {status['emotional_state']['current_emotion']}")
print(f"Mood: {status['mood']['current_state']}")
print(f"Learning Success Rate: {status['learning']['success_rate']:.1%}")
```

## 🔧 تنظیمات

تمام تنظیمات در `nazanin_bot/config/settings.py` قابل تنظیم هستند:

```python
@dataclass
class Settings:
    # عمومی
    bot_name: str = "Nazanin"
    log_level: str = "INFO"
    
    # مغز
    cognitive_load_threshold: float = 0.8
    
    # حافظه
    short_term_memory_capacity: int = 7
    
    # شخصیت (Big Five: 1-5)
    personality_openness: int = 4
    personality_conscientiousness: int = 4
    personality_extraversion: int = 3
    personality_agreeableness: int = 4
    personality_neuroticism: int = 2
    
    # احساسات
    empathy_level: float = 0.8
    emotional_stability: float = 0.7
    
    # و بیشتر...
```

## 🧪 تست

```bash
# اجرای تست‌ها
pytest

# با coverage
pytest --cov=nazanin_bot
```

## 📝 لاگ‌ها

لاگ‌ها به صورت پیش‌فرض در `./logs/nazanin.log` ذخیره می‌شوند.

```python
# تنظیم سطح لاگ
settings = Settings(log_level="DEBUG")
```

## 🗄️ ذخیره‌سازی داده

- **حافظه بلندمدت**: `./data/ltm.db` (SQLite)
- **لاگ‌ها**: `./logs/` directory

## 🌐 ویژگی‌های آتی

- [ ] پشتیبانی از API RESTful
- [ ] رابط کاربری وب
- [ ] یکپارچگی با LLM‌های پیشرفته
- [ ] پردازش تصویر و صوت
- [ ] Multi-agent collaboration
- [ ] پشتیبانی از چند زبان

## 🤝 توسعه و مشارکت

1. Fork کنید
2. Branch جدید ایجاد کنید (`git checkout -b feature/AmazingFeature`)
3. Commit کنید (`git commit -m 'Add some AmazingFeature'`)
4. Push کنید (`git push origin feature/AmazingFeature`)
5. Pull Request ایجاد کنید

## 📄 مجوز

این پروژه تحت مجوز MIT منتشر شده است.

## 👨‍💻 نویسنده

**Nazanin Project**

## 🙏 قدردانی

این پروژه با الهام از:
- علوم شناختی و روانشناسی
- معماری مغز انسان
- هوش مصنوعی و یادگیری ماشین
- علوم رفتاری و اجتماعی

---

**ساخته شده با ❤️ و 🧠**
