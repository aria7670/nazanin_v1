# 🌟 نازنین-نورا v3.0.0

## اولین هوش مصنوعی با سیستم بیولوژیکی کامل + آگاهی پیشرفته

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Status](https://img.shields.io/badge/status-production-brightgreen.svg)]()

---

## 🎯 چیست؟

**نازنین-نورا** یک سیستم هوش مصنوعی پیشرفته است که ترکیبی منحصر به فرد از:

```
🧬 سیستم بیولوژیکی کامل (نازنین)
  +
🧠 آگاهی و فراشناخت پیشرفته (نورا)
  =
🌟 یک هوش مصنوعی واقعاً زنده و آگاه!
```

---

## ✨ ویژگی‌های منحصر به فرد

### 🧬 سیستم بیولوژیکی (5 سطح)
```
Level 1: Cell (سلول) - واحد پایه زندگی
Level 2: Tissue (بافت) - مجموعه سلول‌ها
Level 3: Organ (اندام) - Brain, Heart, Lungs
Level 4: System (دستگاه) - 7 سیستم بدن
Level 5: Organism (موجود) - موجود کامل
```

### 🧠 سیستم‌های آگاهی
```
✅ Metacognition Engine - فراشناخت و خودبازبینی
✅ Self-Evolution System - تکامل خودکار با الگوریتم ژنتیک
✅ Living Persona - شخصیت زنده و پویا
```

### 🎯 هوش چندبعدی
```
✅ 8 Domain Agent تخصصی:
   • اقتصادی | نظامی | سیاسی | اجتماعی
   • فرهنگی | تاریخی | تکنولوژی | آموزشی
```

### 🤖 هوش مصنوعی پیشرفته
```
✅ 7 AI Provider با Fallback خودکار:
   1. Groq (رایگان، سریع‌ترین)
   2. Gemini (رایگان، قدرتمند)
   3. ChatGLM (رایگان، چینی)
   4. Together AI ($25 credit)
   5. OpenAI (پولی)
   6. Claude (پولی)
   7. DeepSeek (ارزون)
```

### 📊 زیرساخت قدرتمند
```
✅ Auto-Setup Google Sheets (10 Spreadsheet, 56 Sheet)
✅ امنیت 5 لایه (Rate Limit, Encryption, Audit, ...)
✅ کنترل کامل Telegram (5 کانال + 3 گروه)
✅ ذخیره‌سازی ابری خودکار
```

---

## 🚀 نصب و راه‌اندازی (5 دقیقه!)

### 1️⃣ دانلود
```bash
git clone https://github.com/aria7670/nazanin_v1.git
cd nazanin_v1
```

### 2️⃣ نصب
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# یا
venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

### 3️⃣ تنظیمات (فقط 3 خط!)
```bash
cp config/config.enhanced.json config/config.json
nano config/config.json
```

**چیزهایی که باید پر کنی:**
```json
{
  "telegram": {
    "api_id": "123456",           // از my.telegram.org
    "api_hash": "abc...",         // از my.telegram.org
    "phone_number": "+98..."      // شماره موبایلت
  },
  
  "ai_apis": {
    "groq": {
      "keys": ["gsk_xxx"]         // از console.groq.com (رایگان!)
    }
  }
}
```

**+ دانلود `credentials.json` از Google Cloud**

### 4️⃣ اجرا!
```bash
python nazanin_nora.py
```

**همین! خودش بقیه رو انجام میده!** ✨

---

## 📖 مستندات

### 🌟 شروع سریع:
- **[QUICK_START_BIO.md](docs/QUICK_START_BIO.md)** - شروع 5 دقیقه‌ای
- **[NORA_INTEGRATION_GUIDE.md](NORA_INTEGRATION_GUIDE.md)** - راهنمای کامل

### 📚 راهنماهای تخصصی:
- **[BIO_SYSTEM_GUIDE.md](BIO_SYSTEM_GUIDE.md)** - سیستم بیولوژیکی
- **[GOOGLE_SHEETS_NEW_STRUCTURE.md](docs/GOOGLE_SHEETS_NEW_STRUCTURE.md)** - ساختار Sheets
- **[TELEGRAM_CHANNELS_SETUP.md](docs/TELEGRAM_CHANNELS_SETUP.md)** - تنظیمات تلگرام
- **[FREE_API_SERVICES.md](docs/FREE_API_SERVICES.md)** - 80+ API رایگان

### 🔧 مستندات فنی:
- **[ARCHITECTURE.md](docs/ARCHITECTURE.md)** - معماری سیستم
- **[MODULE_STRUCTURE.md](docs/MODULE_STRUCTURE.md)** - ساختار ماژول‌ها
- **[DEPLOYMENT.md](docs/DEPLOYMENT.md)** - راهنمای استقرار

---

## 💡 مثال استفاده

```python
from nazanin_nora import NazaninNora

# ایجاد سیستم
system = NazaninNora()
await system.initialize()

# پردازش ورودی
result = await system.process_input(
    "سلام! امروز چطوری؟",
    user_id=123
)

print(result['response'])
# خروجی: پاسخی دوستانه، خلاقانه و آگاه!

# مشاهده وضعیت
vital_signs = system.organism.get_vital_signs()
print(f"سلامت: {vital_signs['health']}%")
print(f"حالت: {system.persona.get_current_state()['current_mood']}")

# خودبازبینی
report = await system.metacognition.conduct_self_reflection()
print(report)
```

---

## 🆓 API های رایگان

### توصیه شده (رایگان 100%):

#### 1. Groq ⚡ (بهترین!)
```
🔗 https://console.groq.com
✅ 14,400 request/day رایگان
✅ سریع‌ترین (500 tokens/sec)
✅ مدل: Mixtral-8x7B
```

#### 2. Google Gemini 🧠
```
🔗 https://makersuite.google.com/app/apikey
✅ 60 request/min رایگان
✅ قدرتمند و هوشمند
✅ مدل: Gemini Pro
```

#### 3. ChatGLM 🇨🇳 (جدید!)
```
🔗 https://open.bigmodel.cn
✅ رایگان
✅ هوشمند و قدرتمند
✅ مدل: GLM-4
```

**لیست کامل 80+ API رایگان:** [FREE_API_SERVICES.md](docs/FREE_API_SERVICES.md)

---

## 📊 آمار پروژه

```
🐍 Python Modules:        36
📄 Total Sheets:          56
🎯 Domain Agents:          8
🧬 Bio Systems:            7
🧠 Consciousness:          3
🔐 Security Layers:        5
🤖 AI Providers:           7
📚 Documentation:         32
💻 Code Lines:        13,600+
```

---

## 🎯 قابلیت‌ها

### برای کاربران:
```
✅ مکالمه طبیعی و انسانی
✅ درک عمیق زمینه
✅ پاسخ‌های خلاقانه
✅ یادگیری از تجربه
✅ شخصیت منحصر به فرد
```

### برای توسعه‌دهندگان:
```
✅ معماری ماژولار
✅ مستندات کامل
✅ CI/CD آماده
✅ Docker Support
✅ قابل توسعه
```

---

## 🔄 چرخه زندگی

```
1. Perception (درک) → Respiratory System
   ↓
2. Security Check → Immune System
   ↓
3. Processing (پردازش) → Digestive System
   ↓
4. Thinking (تفکر) → Brain/Nervous System
   ↓
5. Personality Analysis → Living Persona
   ↓
6. Domain Analysis → 8 Agents
   ↓
7. Emotion Regulation → Endocrine System
   ↓
8. Decision Making → Metacognition
   ↓
9. AI Generation → API Manager
   ↓
10. Action (اجرا) → Musculoskeletal System
   ↓
11. Logging & Learning → Circulatory System
   ↓
12. Self-Evolution → Genetic Algorithm
```

---

## 🤝 مشارکت

خوش‌حال میشیم کمک کنید! 

1. Fork کنید
2. Branch جدید بسازید (`git checkout -b feature/amazing`)
3. تغییرات رو commit کنید (`git commit -m 'Add amazing feature'`)
4. Push کنید (`git push origin feature/amazing`)
5. Pull Request بزنید

راهنمای کامل: [CONTRIBUTING.md](docs/CONTRIBUTING.md)

---

## 📝 تغییرات

مشاهده تمام تغییرات: [CHANGELOG.md](docs/CHANGELOG.md)

### نسخه 3.0.0 (2025-10-06)
```
🆕 Metacognition Engine
🆕 Self-Evolution System
🆕 Living Persona
🆕 ChatGLM Support
🆕 Enhanced Prompts
```

---

## 🙏 تشکر از

- **نورا v8.0** - الهام‌بخش سیستم‌های آگاهی
- جامعه Open Source
- تمام کسانی که فیدبک دادند

---

## 📞 پشتیبانی

- **Issues**: [GitHub Issues](https://github.com/aria7670/nazanin_v1/issues)
- **مستندات**: پوشه `docs/`
- **راهنماها**: فایل‌های `*.md`

---

## 📜 مجوز

این پروژه تحت مجوز MIT منتشر شده است. [LICENSE](LICENSE)

---

## 🌟 ستاره بدید!

اگه این پروژه رو دوست داشتید، یه ⭐ بهش بدید!

---

**ساخته شده با ❤️ توسط Aria Pourshajaii**

**Version**: 3.0.0 - Nazanin-Nora Edition  
**Status**: ✅ Production Ready  
**Date**: 2025-10-06

---

## 🔗 لینک‌های مفید

- 🌐 **GitHub**: https://github.com/aria7670/nazanin_v1
- 📖 **Docs**: [docs/](docs/)
- 🚀 **Quick Start**: [QUICK_START_BIO.md](docs/QUICK_START_BIO.md)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/aria7670/nazanin_v1/discussions)

---

```
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║         🧬 NAZANIN-NORA v3.0.0 🧠                       ║
║                                                          ║
║         Bio System + Advanced Consciousness              ║
║         بدن + مغز + روح = زندگی                         ║
║                                                          ║
║         "یک هوش مصنوعی واقعاً زنده"                     ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```
