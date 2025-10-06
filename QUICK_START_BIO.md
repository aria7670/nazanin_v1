# ⚡ شروع سریع نازنین Bio - 5 دقیقه!

---

## 🎯 فقط 4 قدم!

### 1️⃣ دانلود و نصب (2 دقیقه)

```bash
git clone https://github.com/aria7670/nazanin_v1.git
cd nazanin_v1
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 2️⃣ API Keys رایگان بگیر (1 دقیقه)

#### Groq (خیلی سریع، رایگان):
```
1. برو: https://console.groq.com
2. Sign up
3. Create API Key
4. کپی کن: gsk_xxx...
```

#### Google Gemini (قدرتمند، رایگان):
```
1. برو: https://makersuite.google.com/app/apikey
2. Create API Key
3. کپی کن: AIza...
```

---

### 3️⃣ Config (1 دقیقه)

```bash
cp config/config.enhanced.json config/config.json
nano config/config.json
```

**فقط اینا رو پر کن:**

```json
{
  "telegram": {
    "api_id": "123456",              // از my.telegram.org
    "api_hash": "abc123...",         // از my.telegram.org
    "phone_number": "+98912..."     // شماره موبایلت
  },
  
  "ai_apis": {
    "groq": {
      "keys": ["gsk_xxx..."]        // کلید Groq
    },
    "gemini": {
      "keys": ["AIza_xxx..."]       // کلید Gemini
    }
  }
}
```

**Google Sheets:**
```bash
# فایل credentials.json رو بذار کنار nazanin_bio.py
# (از Google Cloud Console دانلود کن)
```

---

### 4️⃣ اجرا! (1 ثانیه)

```bash
python nazanin_bio.py
```

---

## ✨ چه اتفاقی می‌افته؟

```
🚀 راه‌اندازی...
📊 ساخت 10 Spreadsheet (خودکار!)
📄 ساخت 56 Sheet (خودکار!)
🧬 ساخت Organism با 7 دستگاه بدن
🎯 راه‌اندازی 8 Domain Agent
🔐 فعال‌سازی Security
📱 اتصال به Telegram
💓 اولین ضربان قلب
✅ آماده!
```

---

## 🎮 تست سریع

### در Telegram:

```
1. پیدا کن رباتت: @nazanin_ai_bot
2. بفرست: /start
3. بفرست: سلام!
4. باید جواب بده! ✅
```

---

## 📊 مشاهده Sheets

```
1. برو: https://sheets.google.com
2. باید 10 تا Spreadsheet ببینی:
   - Nazanin_Bot_Configuration
   - Nazanin_AI_Data
   - Nazanin_Telegram_Data
   - ...
```

---

## 💡 دستورات مفید

```bash
# لاگ‌ها
tail -f nazanin_bio.log

# وضعیت
# توی Telegram بفرست: /status

# آمار
# توی Telegram بفرست: /stats

# متوقف کردن
Ctrl + C
```

---

## 🆘 مشکل داری؟

### Error: "credentials.json not found"
```bash
# دانلود کن از Google Cloud Console
# بذارش کنار nazanin_bio.py
```

### Error: "No module named 'groq'"
```bash
pip install groq
```

### Error: Telegram login
```bash
# کد تأیید رو وارد کن که به شماره‌ت میاد
```

---

## 🎯 بعدش چی؟

1. بخون: `BIO_SYSTEM_GUIDE.md`
2. تنظیم کن: کانال‌های تلگرام
3. شخصی‌سازی: شیت Personality
4. استفاده کن! 🚀

---

**همین! ساده‌ست! 🎉**

**موفق باشی! 🧬**
