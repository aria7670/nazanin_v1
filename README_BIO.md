# 🧬 نازنین - نسخه بیولوژیکی v2.1.0

## اولین ربات هوش مصنوعی با شبیه‌سازی کامل بدن انسان

---

## 🌟 ویژگی‌های منحصر به فرد

### 🧬 سیستم بیولوژیکی 5 سطحی
```
Cell → Tissue → Organ → System → Organism
سلول → بافت → اندام → دستگاه → موجود
```

### 🎯 8 ایجنت تخصصی حوزه‌ای
```
اقتصادی | نظامی | سیاسی | اجتماعی | فرهنگی | تاریخی | تکنولوژی | آموزشی
```

### 📊 Auto-Setup Google Sheets
```
✅ خودش 10 Spreadsheet می‌سازه
✅ خودش 56 Sheet می‌سازه
✅ قبل از ساخت چک می‌کنه
```

### 🔐 امنیت چند لایه
```
Rate Limiting | Access Control | Encryption | Audit Log | Threat Detection
```

### 📱 کنترل کامل Telegram
```
5 کانال + 3 گروه + ذخیره خودکار + کنترل کامل اکانت
```

---

## ⚡ نصب فوری (1 دقیقه)

```bash
# 1. دانلود
git clone https://github.com/aria7670/nazanin_v1.git
cd nazanin_v1

# 2. نصب
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Config
cp config/config.enhanced.json config/config.json
nano config/config.json  # فقط 3 خط پر کن!

# 4. اجرا
python nazanin_bio.py
```

**همین! بقیه خودکاره!** ✨

---

## 📝 چیزهایی که باید پر کنی

### فقط 3 چیز:

```json
{
  "telegram": {
    "api_id": "123456",           // ← از my.telegram.org
    "api_hash": "abc...",         // ← از my.telegram.org
    "phone_number": "+98..."      // ← شماره موبایلت
  },
  
  "ai_apis": {
    "groq": {
      "keys": ["gsk_xxx"]         // ← از console.groq.com (رایگان!)
    }
  }
}
```

**+ فایل `credentials.json` از Google Cloud**

---

## 🎯 چطور کار می‌کنه؟

```
کاربر پیام می‌فرسته
↓
Respiratory System (دریافت)
↓
Immune System (بررسی امنیت)
↓
Digestive System (پردازش)
↓
Nervous System (تفکر)
↓
8 Domain Agents (تحلیل)
↓
API Manager (تولید پاسخ)
↓
Musculoskeletal System (ارسال)
↓
Circulatory System (ثبت)
↓
پاسخ هوشمند ارسال میشه ✅
```

---

## 🆓 رایگان 100%

### همه اینا رایگان:
- ✅ Groq API (14,400 req/day)
- ✅ Google Gemini (60 req/min)
- ✅ Telegram Storage (2GB per file!)
- ✅ Google Sheets (نامحدود)
- ✅ Together AI ($25 credit)

**هیچ هزینه‌ای نداره!** 💰

---

## 📊 آمار

```
🧬 Biological Cells: نامحدود
🏥 Body Systems: 7 دستگاه
🎯 Domain Agents: 8 تخصصی
📊 Spreadsheets: 10
📄 Sheets: 56
📱 Telegram Channels: 5
👥 Telegram Groups: 3
🔐 Security Layers: 5
🤖 AI Providers: 6
📚 Documentation: 24 فایل
💻 Code: 18,000+ خط
```

---

## 📚 راهنماها

### شروع کار:
1. **BIO_SYSTEM_GUIDE.md** ← ⭐ شروع اینجا!
2. **GOOGLE_SHEETS_NEW_STRUCTURE.md** - ساختار sheets
3. **TELEGRAM_CHANNELS_SETUP.md** - راهنمای کانال‌ها
4. **FREE_API_SERVICES.md** - API های رایگان

### مستندات قدیمی:
- STEP_BY_STEP_GUIDE.md
- HOW_NAZANIN_WORKS.md
- و 20 فایل دیگر در docs/

---

## 🔗 لینک‌ها

- **GitHub**: https://github.com/aria7670/nazanin_v1
- **Issues**: https://github.com/aria7670/nazanin_v1/issues
- **Docs**: مجموعه کامل در پوشه docs/

---

## 🎉 ویژگی‌های جدید v2.1.0

### ✅ Auto-Setup:
- خودکار همه Sheets رو می‌سازه
- خودکار چک می‌کنه
- نیاز به کار دستی نیست!

### ✅ Bio System:
- 5 سطح بیولوژیکی
- 7 دستگاه بدن
- Vital Signs واقعی

### ✅ Domain Intelligence:
- 8 ایجنت تخصصی
- تحلیل چندبعدی
- توصیه‌های هوشمند

### ✅ Security:
- امنیت چند لایه
- رمزنگاری
- تشخیص تهدید

### ✅ Telegram:
- کنترل کامل
- 8 کانال/گروه
- ذخیره خودکار

---

## 💡 یک مثال واقعی

```python
# کاربر می‌پرسه:
"آیا سرمایه‌گذاری در AI خوبه؟"

# نازنین:
1. Immune System: بررسی امنیت ✅
2. Brain: فکر می‌کنه
3. Economic Agent: تحلیل اقتصادی
4. Technological Agent: تحلیل فناوری
5. Historical Agent: سوابق بررسی
6. API (Groq): تولید پاسخ
7. Response: "بله! AI بازار رو به رشده.
   سوابق تاریخی نشون میده..."
```

---

## 🚀 اجرا

```bash
python nazanin_bio.py
```

**یه موجود زنده دیجیتال! 🧬**

---

**ساخته شده با ❤️ و علم**

Version: 2.1.0 Bio Edition  
Status: ✅ Alive & Running  
Date: 2025-10-06
