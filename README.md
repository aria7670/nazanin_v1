# 🤖 نازنین - Advanced Modular AI Bot

## ربات پیشرفته ماژولار با شبیه‌سازی مغز، سیستم کوانتومی و شبکه‌های عصبی

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-2.0.0-orange.svg)](https://github.com/aria7670/nazanin_v1)

---

## 📁 ساختار ماژولار پروژه

```
nazanin/
│
├── 📦 src/                          # کد اصلی پروژه
│   │
│   ├── 🔷 core/                     # سیستم‌های اصلی
│   │   ├── __init__.py
│   │   ├── sheets_manager.py       # مدیریت Google Sheets
│   │   └── api_manager.py          # مدیریت AI APIs
│   │
│   ├── 🧠 ai/                       # سیستم‌های AI پیشرفته
│   │   ├── __init__.py
│   │   ├── brain_simulation.py     # شبیه‌سازی مغز انسان
│   │   ├── quantum_agent.py        # سیستم کوانتومی
│   │   └── neural_agent.py         # شبکه‌های عصبی
│   │
│   ├── 🤖 agents/                   # ایجنت‌ها
│   │   ├── __init__.py
│   │   ├── agents.py               # 6 ایجنت پایه
│   │   └── specialized_agents.py   # 10 ایجنت تخصصی
│   │
│   ├── 🌐 platforms/                # پلتفرم‌ها
│   │   ├── __init__.py
│   │   ├── twitter_system.py       # سیستم Twitter
│   │   └── telegram_system.py      # سیستم Telegram
│   │
│   ├── 🛠️ utils/                     # ابزارها
│   │   ├── __init__.py
│   │   ├── message_classifier.py   # دسته‌بندی پیام
│   │   ├── behavioral_learning.py  # یادگیری رفتاری
│   │   ├── template_system.py      # تمپلت‌ها
│   │   └── advanced_algorithms.py  # الگوریتم‌ها
│   │
│   └── 💾 storage/                  # ذخیره‌سازی
│       ├── __init__.py
│       └── telegram_storage.py     # ذخیره در Telegram
│
├── 📚 docs/                         # مستندات
│   ├── START_HERE.md               # شروع از اینجا
│   ├── QUICKSTART.md               # شروع سریع
│   ├── INSTALLATION.md             # راهنمای نصب
│   ├── ARCHITECTURE.md             # معماری سیستم
│   ├── ADVANCED_FEATURES.md        # ویژگی‌های پیشرفته
│   ├── COMPLETE_SUMMARY.md         # خلاصه کامل
│   └── ...                         # و مستندات بیشتر
│
├── 🧪 tests/                        # تست‌ها و Demo
│   ├── test_basic.py               # تست‌های پایه
│   ├── demo.py                     # Demo سیستم‌های AI
│   └── demo_advanced.py            # Demo کامل
│
├── ⚙️ config/                       # تنظیمات
│   ├── config.json                 # تنظیمات اصلی
│   └── config.example.json         # نمونه
│
├── 🚀 main.py                       # ورودی اصلی
├── 🚀 main_advanced.py              # ورودی پیشرفته
├── 📋 requirements.txt              # وابستگی‌ها
├── 📦 nazanin_complete.zip          # کل پروژه در یک فایل
└── 🔒 .gitignore                    # Git ignore

```

---

## ✨ ویژگی‌های کلیدی

### 🔷 سیستم‌های اصلی
- ✅ **Google Sheets Manager** - مدیریت داده با cache
- ✅ **Multi-AI API Manager** - Gemini, GPT-4, Claude, DeepSeek
- ✅ **16 ایجنت تخصصی** - برای کارهای مختلف

### 🧠 AI پیشرفته
- ✅ **Brain Simulation** - شبیه‌سازی احساسات، شناخت، تصمیم‌گیری
- ✅ **Quantum Agent** - الگوریتم‌های کوانتومی
- ✅ **Neural Agent** - یادگیری عمیق

### 🎓 یادگیری و انسانی‌سازی
- ✅ **Message Classification** - دسته‌بندی به 10 دسته
- ✅ **Behavioral Learning** - یادگیری از رفتار کاربران
- ✅ **Humanization Engine** - پاسخ‌های انسانی و طبیعی

### 🌐 پلتفرم‌ها
- ✅ **Twitter** - پست خودکار، Thread، پاسخ به mentions
- ✅ **Telegram** - چت فارسی، گزارش‌دهی

### 🛠️ ابزارهای پیشرفته
- ✅ **5 الگوریتم پیچیده** - تحلیل و پیش‌بینی
- ✅ **سیستم تمپلت** - 10+ تمپلت آماده
- ✅ **ذخیره‌سازی Telegram** - بدون نیاز به دیتابیس

---

## ⚡ نصب و اجرا

### نصب:
```bash
# کلون کردن
git clone https://github.com/aria7670/nazanin_v1.git
cd nazanin_v1

# نصب وابستگی‌ها
pip install -r requirements.txt

# تنظیم config
cp config/config.example.json config/config.json
# ویرایش config/config.json
```

### اجرا:
```bash
# نسخه ساده
python main.py

# نسخه پیشرفته (با تمام ویژگی‌ها)
python main_advanced.py

# Demo
python tests/demo_advanced.py
```

---

## 📊 آمار پروژه

```
📝 کد Python:         8,007 خط
📖 مستندات:          4,840 خط
🐍 ماژول‌های Python:  19 فایل
📚 فایل‌های Doc:      12 فایل
🤖 ایجنت‌ها:          16 ایجنت
🧮 الگوریتم‌ها:       5 الگوریتم
📋 تمپلت‌ها:          10+ تمپلت
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💯 جمع کل:           12,847 خط
```

---

## 📚 مستندات

- 🚀 **[START_HERE.md](docs/START_HERE.md)** - شروع از اینجا
- ⚡ **[QUICKSTART.md](docs/QUICKSTART.md)** - شروع سریع (5 دقیقه)
- 🔧 **[INSTALLATION.md](docs/INSTALLATION.md)** - راهنمای نصب کامل
- 🏗️ **[ARCHITECTURE.md](docs/ARCHITECTURE.md)** - معماری سیستم
- 🆕 **[ADVANCED_FEATURES.md](docs/ADVANCED_FEATURES.md)** - ویژگی‌های پیشرفته
- 📋 **[COMPLETE_SUMMARY.md](docs/COMPLETE_SUMMARY.md)** - خلاصه کامل

---

## 🎯 استفاده سریع

### مثال 1: پردازش پیام با تمام سیستم‌ها
```python
from main_advanced import NazaninAdvanced

nazanin = NazaninAdvanced()
await nazanin.initialize()

# پردازش کامل
result = await nazanin.process_message_complete(
    user_id="user_123",
    message="چطوری می‌تونم AI یاد بگیرم?"
)

print(result['final_response'])
```

### مثال 2: استفاده مستقل از یک ماژول
```python
from src.utils import MessageClassifier

classifier = MessageClassifier()
result = await classifier.classify("سلام!")
print(result['primary_category'])
```

### مثال 3: استفاده از Brain Simulation
```python
from src.ai import BrainSimulation

brain = BrainSimulation(config)
result = await brain.process("This is amazing!")
print(result['dominant_emotion'])
```

---

## 🎁 دانلود کامل

فایل **nazanin_complete.zip** حاوی تمام پروژه است!

---

## 🤝 مشارکت

این پروژه open source است. مشارکت شما خوشحال می‌شویم!

---

## 📞 پشتیبانی

برای سوالات و مشکلات:
- 📖 ابتدا [docs/](docs/) را بخوانید
- 🐛 Issue در GitHub باز کنید
- 💬 در Discussions بپرسید

---

## 📄 لایسنس

MIT License - استفاده آزاد

---

**ساخته شده با ❤️ برای Byte-Line**

**نسخه**: 2.0.0 Advanced  
**تاریخ**: 2025-10-06  
**وضعیت**: ✅ Production Ready
