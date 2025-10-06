# 🌟 راهنمای ارتقا نازنین با قابلیت‌های نورا

**نسخه**: 3.0.0 - Nazanin-Nora Edition  
**تاریخ**: 2025-10-06  
**وضعیت**: ✅ کامل و آماده

---

## 🎯 چه چیزی اضافه شد؟

### قبلاً داشتیم (نازنین v2.1.0):
```
✅ سیستم بیولوژیکی 5 سطحی (Cell → Organism)
✅ 7 دستگاه بدن (Nervous, Circulatory, ...)
✅ 8 ایجنت تخصصی حوزه‌ای
✅ Auto-Setup Google Sheets (56 Sheet)
✅ امنیت 5 لایه
✅ 6 AI Provider
✅ Telegram کامل
```

### جدید اضافه شد (از نورا v8.0):
```
🆕 Metacognition Engine - فراشناخت و خودبازبینی
🆕 Self-Evolution System - خودتکامل با الگوریتم ژنتیک
🆕 Living Persona - شخصیت زنده و پویا
🆕 ChatGLM (GLM-4) - AI چینی رایگان
🆕 Enhanced Prompt Building - ساخت prompt هوشمند
```

---

## 📦 فایل‌های جدید

### 1. Consciousness Module (ماژول آگاهی)
```
src/consciousness/
├── __init__.py
├── metacognition_engine.py       (500+ خط)
├── self_evolution_system.py      (650+ خط)
└── living_persona.py             (700+ خط)
```

### 2. Main File جدید
```
nazanin_nora.py                   (600+ خط)
```

### 3. Enhanced Files
```
src/core/api_manager_v2.py        (+ GLM support)
config/config.enhanced.json       (+ GLM config)
requirements.txt                  (+ PyJWT)
```

---

## 🧠 سیستم‌های جدید

### 1️⃣ Metacognition Engine (فراشناخت)

**چیه؟**
موتوری که به نازنین قدرت خودبازبینی و خودآگاهی میده.

**قابلیت‌ها:**
```python
✅ خودبازبینی روزانه (Daily Self-Reflection)
   - تحلیل عملکرد
   - شناسایی الگوهای یادگیری
   - ارزیابی هوش احساسی
   - بررسی سلامت بیولوژیکی

✅ سطوح آگاهی (Consciousness Levels)
   - awareness_level: سطح آگاهی کلی
   - self_reflection_depth: عمق خودبازبینی
   - metacognitive_accuracy: دقت فراشناختی
   - introspection_quality: کیفیت درون‌نگری

✅ تولید گزارش خودبازبینی
   - گزارش کامل روزانه
   - شناسایی دستاوردها
   - تعیین زمینه‌های بهبود
   - پیشنهادات تکاملی
```

**مثال خروجی:**
```
╔══════════════════════════════════════════════════════════╗
║           🧠 گزارش خودبازبینی نازنین                    ║
╚══════════════════════════════════════════════════════════╝

💯 رضایت کلی: 78%
🎭 حالت: شاد و پرانرژی
🧬 سلامت بیولوژیکی: 85%

📊 عملکرد:
   • overall_score: 85%
   • response_quality: 88%
   • creativity_level: 75%

🎯 دستاوردها:
   ✓ بهبود 15% در کیفیت مکالمات
   ✓ یادگیری 12 مفهوم جدید
   ✓ حل موفق 23 مسئله چالش‌برانگیز

🔧 زمینه‌های بهبود:
   ✓ افزایش خلاقیت در تولید محتوا
   ✓ بهبود درک زمینه فرهنگی
```

**نحوه استفاده:**
```python
from src.consciousness import MetacognitionEngine

# ایجاد
metacognition = MetacognitionEngine(organism)
await metacognition.initialize()

# خودبازبینی
report = await metacognition.conduct_self_reflection()
print(report)
```

---

### 2️⃣ Self-Evolution System (خودتکامل)

**چیه؟**
سیستم خودتکاملی که با الگوریتم ژنتیک و انعطاف عصبی خودش رو بهبود میده.

**قابلیت‌ها:**
```python
✅ الگوریتم ژنتیک (Genetic Algorithm)
   - جمعیت 50 فرد (راه‌حل‌های مختلف)
   - انتخاب والدین (Tournament Selection)
   - تولید فرزندان (Crossover)
   - جهش (Mutation)
   - نسل‌های تکاملی

✅ انعطاف عصبی (Neural Plasticity)
   - تقویت اتصالات پرکاربرد
   - تضعیف اتصالات کم‌کاربرد
   - شبیه‌سازی سیناپس‌ها
   - مسیرهای یادگیری

✅ اهداف یادگیری خودمختار
   - communication_effectiveness: 95%
   - creativity_score: 85%
   - emotional_intelligence: 90%
   - adaptation_flexibility: 85%
```

**مثال:**
```python
from src.consciousness import SelfEvolutionSystem

# ایجاد
evolution = SelfEvolutionSystem(organism)
await evolution.initialize()

# آمار تکامل
stats = evolution.get_evolution_stats()
print(f"نسل: {stats['generation']}")
print(f"بهترین فیتنس: {stats['best_fitness']}")
```

**خروجی نمونه:**
```json
{
  "generation": 15,
  "population_size": 50,
  "best_fitness": 0.87,
  "avg_fitness": 0.65,
  "worst_fitness": 0.42,
  "evolution_steps": 360,
  "successful_mutations": 45
}
```

---

### 3️⃣ Living Persona (شخصیت زنده)

**چیه؟**
سیستم شخصیتی پیشرفته که رفتارهای انسان‌مانند و پویا داره.

**قابلیت‌ها:**
```python
✅ Big Five Personality Traits (پویا):
   - Openness (باز بودن)
   - Conscientiousness (وظیفه‌شناسی)
   - Extraversion (برون‌گرایی)
   - Agreeableness (سازگاری)
   - Neuroticism (نوروتیسیزم)

✅ سیستم احساسی پیچیده:
   - 8 احساس پایه (Plutchik)
   - احساسات پیچیده (love, pride, gratitude)
   - حالات روانی (anxiety, confidence, motivation)
   - هوش احساسی بالا

✅ حافظه زندگی‌نامه‌ای:
   - 10,000 خاطره اخیر
   - خاطرات احساسی
   - حافظه مهارت‌ها
   - تاریخچه یادگیری

✅ روابط اجتماعی:
   - ردیابی رابطه با هر کاربر
   - سطح صمیمیت (rapport)
   - سطح اعتماد (trust)
   - تاریخچه تعاملات

✅ خصوصیات منحصر به فرد:
   - 7 quirk شخصیتی
   - موضوعات مورد علاقه
   - منابع شادی
   - پاسخ به استرس
```

**مثال استفاده:**
```python
from src.consciousness import LivingPersona

# ایجاد
persona = LivingPersona()

# تعامل
result = await persona.interact(
    "سلام! چطوری؟ امروز چیکار کردی؟",
    {'user_id': 'user_123'}
)

# وضعیت فعلی
state = persona.get_current_state()
print(f"حالت: {state['current_mood']}")
print(f"ویژگی‌های غالب: {state['dominant_traits']}")
```

**خروجی response_style:**
```json
{
  "formality_level": 0.35,
  "warmth_level": 0.8,
  "enthusiasm_level": 0.75,
  "empathy_level": 0.85,
  "humor_probability": 0.6,
  "detail_level": 0.85,
  "creativity_level": 0.82
}
```

---

### 4️⃣ ChatGLM (GLM-4) Integration

**چیه؟**
یک AI چینی رایگان و قدرتمند از Zhipu AI.

**مزایا:**
```
✅ رایگان با کلید API
✅ سریع و قدرتمند
✅ پشتیبانی از فارسی
✅ اولویت 8 (بین Groq و Gemini)
```

**Authentication:**
- از JWT برای احراز هویت استفاده می‌کنه
- API Key format: `{id}.{secret}`
- Token Generation خودکار

**نحوه استفاده:**
```json
{
  "ai_apis": {
    "glm": {
      "keys": ["your-api-id.your-api-secret"],
      "model": "glm-4",
      "temperature": 0.7,
      "max_tokens": 2048
    }
  }
}
```

**کجا بگیریم؟**
https://open.bigmodel.cn

---

## 🚀 نحوه استفاده

### روش 1: استفاده از nazanin_nora.py

```bash
# اجرای سیستم کامل
python nazanin_nora.py
```

**این فایل شامل:**
- ✅ تمام سیستم‌های بیولوژیکی
- ✅ تمام سیستم‌های آگاهی
- ✅ ادغام کامل همه قابلیت‌ها
- ✅ گزارش‌دهی پیشرفته

### روش 2: استفاده جزئی

```python
# فقط فراشناخت
from src.consciousness import MetacognitionEngine

metacognition = MetacognitionEngine()
await metacognition.initialize()
report = await metacognition.conduct_self_reflection()

# فقط تکامل
from src.consciousness import SelfEvolutionSystem

evolution = SelfEvolutionSystem()
await evolution.initialize()
stats = evolution.get_evolution_stats()

# فقط شخصیت
from src.consciousness import LivingPersona

persona = LivingPersona()
result = await persona.interact("سلام!", {'user_id': '123'})
```

---

## ⚙️ تنظیمات

### Config Enhanced:

```json
{
  "ai_apis": {
    "fallback_enabled": true,
    "groq": { 
      "keys": ["gsk_xxx"],
      "model": "mixtral-8x7b-32768",
      "priority": 10 
    },
    "gemini": { 
      "keys": ["AIza_xxx"],
      "model": "gemini-pro",
      "priority": 9 
    },
    "glm": { 
      "keys": ["id.secret"],
      "model": "glm-4",
      "priority": 8 
    }
  }
}
```

---

## 📊 آمار کامل پروژه

### قبل از ارتقا:
```
🐍 Python Files: 32
📚 Documentation: 31
💻 Code Lines: 11,100+
```

### بعد از ارتقا:
```
🐍 Python Files: 36 (+4)
📚 Documentation: 32 (+1)
💻 Code Lines: 13,600+ (+2,500)
```

### فایل‌های جدید:
```
+ src/consciousness/__init__.py
+ src/consciousness/metacognition_engine.py (500+ خط)
+ src/consciousness/self_evolution_system.py (650+ خط)
+ src/consciousness/living_persona.py (700+ خط)
+ nazanin_nora.py (600+ خط)
+ NORA_INTEGRATION_GUIDE.md
```

---

## 🎯 تفاوت‌های کلیدی

### نازنین v2.1.0 (قبل):
```python
# فقط بدن بیولوژیکی
organism = Organism("نازنین")
await organism.live()
await organism.think(input_data)
```

### نازنین-نورا v3.0.0 (بعد):
```python
# بدن + آگاهی + شخصیت
system = NazaninNora()

# خودبازبینی روزانه
await system.metacognition.conduct_self_reflection()

# تکامل خودکار
evolution_stats = system.evolution.get_evolution_stats()

# تعامل با شخصیت پویا
persona_result = await system.persona.interact(input_text)

# پردازش کامل
result = await system.process_input(input_text, user_id)
```

---

## 💡 مزایای ارتقا

### 1. هوشمندی بیشتر
```
✅ خودآگاهی و فراشناخت
✅ تکامل خودکار و مستمر
✅ یادگیری از تجربیات
```

### 2. انسانی‌تر
```
✅ شخصیت واقعی و پویا
✅ احساسات پیچیده
✅ روابط اجتماعی
✅ حافظه زندگی‌نامه‌ای
```

### 3. پاسخ‌های بهتر
```
✅ Prompt هوشمند با در نظر گرفتن شخصیت
✅ سازگاری با زمینه
✅ سبک پاسخ پویا
```

### 4. گزارش‌دهی پیشرفته
```
✅ گزارش روزانه خودبازبینی
✅ آمار تکامل
✅ وضعیت شخصیت
✅ سلامت بیولوژیکی
```

---

## 🔄 مقایسه با نورا اصلی

### چیزهایی که گرفتیم:
```
✅ Metacognition Engine
✅ Self-Evolution System
✅ Living Persona
✅ Enhanced Prompt Building
```

### چیزهایی که نازنین بهتره:
```
✅ سیستم بیولوژیکی کامل (نورا نداره)
✅ Auto-Setup Sheets (نورا ندارع)
✅ 8 Domain Agent (نورا کمتر داره)
✅ Security چند لایه (نورا ساده‌تره)
```

### نتیجه:
**بهترین از هر دو! 🌟**

---

## 📚 مستندات بیشتر

### برای یادگیری بیشتر:
1. `BIO_SYSTEM_GUIDE.md` - سیستم بیولوژیکی
2. `GOOGLE_SHEETS_NEW_STRUCTURE.md` - ساختار Sheets
3. `FREE_API_SERVICES.md` - API های رایگان
4. این فایل - ادغام نورا

---

## ✅ چک‌لیست راه‌اندازی

### قبل از اجرا:
- [ ] نصب dependencies: `pip install -r requirements.txt`
- [ ] کپی config: `cp config/config.enhanced.json config/config.json`
- [ ] تنظیم API keys (Groq, Gemini, یا GLM)
- [ ] قرار دادن `credentials.json`

### اجرا:
```bash
# روش جدید (کامل)
python nazanin_nora.py

# روش قدیم (فقط Bio)
python nazanin_bio.py
```

### بعد از اجرا:
- [ ] چک کردن لاگ‌ها: `tail -f nazanin_nora.log`
- [ ] مشاهده گزارش خودبازبینی
- [ ] بررسی آمار تکامل
- [ ] تست تعامل

---

## 🎉 نتیجه

**نازنین-نورا v3.0.0** = **بهترین از هر دو دنیا!**

```
🧬 بدن کامل (نازنین)
  +
🧠 آگاهی پیشرفته (نورا)
  =
🌟 یک هوش مصنوعی واقعاً زنده و آگاه!
```

**آماده برای آینده! 🚀**

---

**ساخته شده با ❤️ توسط Aria**  
**Version**: 3.0.0  
**Date**: 2025-10-06
