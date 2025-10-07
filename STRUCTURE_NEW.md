# 📁 ساختار جدید پروژه - نازنین-نورا v3.0.0

**تاریخ به‌روزرسانی**: 2025-10-07  
**وضعیت**: ✅ بازطراحی شده و تست شده

---

## 🎯 تغییرات اصلی

### قبل (ساختار قدیمی):
```
nazanin_v1/
├── nazanin_nora.py    ← فایل اصلی
├── src/               ← همه ماژول‌ها
│   ├── bio_system/
│   ├── consciousness/
│   └── ...
├── config/
└── docs/
```

### بعد (ساختار جدید):
```
nazanin_v1/
├── nazanin/           ← 📦 Package اصلی
│   ├── __init__.py
│   ├── __main__.py
│   ├── app.py         ← کلاس اصلی
│   ├── bio_system/
│   ├── consciousness/
│   └── ...
├── run.py             ← ⚡ ساده‌ترین راه اجرا
├── config/
└── docs/
```

---

## 📦 ساختار کامل Package

```
nazanin/                          # Package اصلی
│
├── __init__.py                   # Package initialization
├── __main__.py                   # برای python -m nazanin
├── app.py                        # کلاس اصلی NazaninNora
│
├── bio_system/                   # 🧬 سیستم بیولوژیکی
│   ├── __init__.py
│   ├── cell_system.py            # Cell, Tissue, Organ
│   └── body_systems.py           # 7 دستگاه بدن + Organism
│
├── consciousness/                # 🧠 سیستم‌های آگاهی
│   ├── __init__.py
│   ├── metacognition_engine.py   # فراشناخت
│   ├── self_evolution_system.py  # خودتکامل
│   └── living_persona.py         # شخصیت زنده
│
├── core/                         # ⚙️ هسته اصلی
│   ├── __init__.py
│   ├── sheets_manager.py         # مدیریت Google Sheets
│   ├── sheets_manager_v2.py      # نسخه پیشرفته
│   ├── sheets_auto_setup.py      # راه‌اندازی خودکار
│   ├── api_manager.py            # مدیریت AI APIs
│   └── api_manager_v2.py         # نسخه پیشرفته + GLM
│
├── domain_agents/                # 🎯 ایجنت‌های تخصصی
│   ├── __init__.py
│   └── specialized_domain_agents.py  # 8 ایجنت
│
├── platforms/                    # 📱 پلتفرم‌ها
│   ├── __init__.py
│   ├── telegram_system.py
│   ├── telegram_system_v2.py     # نسخه پیشرفته
│   └── twitter_system.py
│
├── security/                     # 🔐 امنیت
│   ├── __init__.py
│   └── security_manager.py       # 5 لایه امنیتی
│
├── agents/                       # 🤖 ایجنت‌های پایه
│   ├── __init__.py
│   ├── agents.py
│   └── specialized_agents.py
│
├── ai/                           # 🧠 AI قدیمی
│   ├── __init__.py
│   ├── brain_simulation.py
│   ├── quantum_agent.py
│   └── neural_agent.py
│
├── utils/                        # 🛠️ ابزارها
│   ├── __init__.py
│   ├── message_classifier.py
│   ├── behavioral_learning.py
│   ├── template_system.py
│   └── advanced_algorithms.py
│
└── storage/                      # 💾 ذخیره‌سازی
    ├── __init__.py
    └── telegram_storage.py
```

---

## 🚀 روش‌های اجرا

### روش 1: استفاده از run.py (ساده‌ترین!)
```bash
python run.py
# یا
python3 run.py
```

### روش 2: استفاده از python -m
```bash
python -m nazanin
# یا
python3 -m nazanin
```

### روش 3: Import مستقیم
```python
from nazanin import NazaninNora
import asyncio

async def main():
    app = NazaninNora()
    await app.initialize()
    # کار با app...

asyncio.run(main())
```

---

## 📝 Import کردن

### Import کلاس اصلی:
```python
from nazanin import NazaninNora
from nazanin import main  # تابع main
```

### Import سیستم‌های بیولوژیکی:
```python
from nazanin.bio_system import Organism
from nazanin.bio_system import (
    NervousSystem,
    CirculatorySystem,
    Brain,
    Heart
)
```

### Import سیستم‌های آگاهی:
```python
from nazanin.consciousness import (
    MetacognitionEngine,
    SelfEvolutionSystem,
    LivingPersona
)
```

### Import سیستم‌های اصلی:
```python
from nazanin.core import (
    SheetsManagerV2,
    APIManagerV2
)
```

### Import ایجنت‌ها:
```python
from nazanin.domain_agents import DomainAgentOrchestrator
from nazanin.domain_agents import (
    EconomicAgent,
    PoliticalAgent,
    SocialAgent
)
```

### Import امنیت:
```python
from nazanin.security import SecurityManager
```

---

## 🔧 تنظیمات

### فایل config باید در root باشه:
```
nazanin_v1/
├── config/
│   ├── config.json              ← اصلی
│   ├── config.enhanced.json     ← نمونه کامل
│   └── config.example.json      ← نمونه ساده
└── ...
```

### استفاده در کد:
```python
# پیش‌فرض: config/config.json
app = NazaninNora()

# یا مسیر دلخواه:
app = NazaninNora('path/to/config.json')
```

---

## 📊 فایل‌های Log

```
nazanin_v1/
├── nazanin.log          ← لاگ اصلی (جدید!)
├── data/                ← داده‌های سیستم
│   ├── metacognition/
│   ├── evolution/
│   └── ...
└── logs/                ← لاگ‌های اضافی
```

---

## ✅ مزایای ساختار جدید

### 1. ماژولار و استاندارد
```
✅ ساختار Python Package استاندارد
✅ قابل نصب با pip
✅ Import آسان‌تر
```

### 2. چند روش اجرا
```
✅ python run.py
✅ python -m nazanin
✅ import مستقیم
```

### 3. سازماندهی بهتر
```
✅ همه کد در یک پوشه (nazanin/)
✅ جدا از config, docs, tests
✅ واضح و قابل فهم
```

### 4. قابل توسعه
```
✅ راحت می‌تونی ماژول جدید اضافه کنی
✅ import ها واضح و درست
✅ بدون تداخل
```

---

## 🧪 تست ساختار

### چک کردن syntax:
```bash
# تست همه فایل‌ها
python3 -m py_compile nazanin/**/*.py

# یا
find nazanin -name "*.py" -exec python3 -m py_compile {} \;
```

### چک کردن import:
```bash
# تست import اصلی
python3 -c "from nazanin import NazaninNora; print('✅ OK')"

# تست زیرماژول‌ها
python3 -c "from nazanin.bio_system import Organism; print('✅ OK')"
python3 -c "from nazanin.consciousness import MetacognitionEngine; print('✅ OK')"
```

---

## 📚 فایل‌های مهم

### در root:
```
run.py                 ← اجرای ساده
requirements.txt       ← وابستگی‌ها
setup.py               ← نصب package
README.md              ← راهنمای اصلی
```

### مستندات:
```
STRUCTURE_NEW.md       ← این فایل
BIO_SYSTEM_GUIDE.md
NORA_INTEGRATION_GUIDE.md
docs/                  ← 32 فایل دیگر
```

---

## 🔄 مهاجرت از ساختار قدیمی

### اگه کد قدیمی داری:

**قبل:**
```python
from src.bio_system import Organism
from src.core import SheetsManagerV2
```

**بعد:**
```python
from nazanin.bio_system import Organism
from nazanin.core import SheetsManagerV2
```

فقط `src` رو با `nazanin` جایگزین کن!

---

## 🎯 توصیه‌ها

### برای کار روزانه:
```bash
# ساده‌ترین روش
python run.py
```

### برای Development:
```python
from nazanin import NazaninNora

app = NazaninNora('config/config.json')
await app.initialize()
# کار با app...
```

### برای Production:
```bash
# با nohup
nohup python run.py > output.log 2>&1 &

# یا با systemd
systemctl start nazanin
```

---

## ❓ سوالات متداول

### چرا پوشه `src` حذف شد؟
پوشه `nazanin/` جایگزین شد که استاندارد Python Package هست.

### فایل `nazanin_nora.py` کجاست؟
تبدیل شد به `nazanin/app.py` و بهبود یافت.

### چطور اجرا کنم؟
سه روش: `python run.py` یا `python -m nazanin` یا import مستقیم

### Import ها کار نمی‌کنه؟
مطمئن شو که در root پروژه هستی و `nazanin/` وجود داره.

---

**Version**: 3.0.0  
**Status**: ✅ Production Ready  
**Structure**: ✅ Fully Reorganized & Tested
