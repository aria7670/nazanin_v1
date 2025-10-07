# 🚀 راهنمای نهایی راه‌اندازی نازنین v5.0

**تاریخ**: 2025-10-07  
**نسخه**: 5.0.0-complete  
**وضعیت**: ✅ کامل و آماده

---

## 📋 فهرست مطالب

1. [نمای کلی](#نمای-کلی)
2. [پیش‌نیازها](#پیش-نیازها)
3. [نصب](#نصب)
4. [راه‌اندازی Google Sheets](#راه-اندازی-google-sheets)
5. [اجرا](#اجرا)
6. [مستندات](#مستندات)

---

## 🎯 نمای کلی

**نازنین v5.0 شامل:**

```
🧠 مغز عصبی 12 لایه
👂 ادراک و آگاهی بالا
🤖 خودمختاری کامل
📦 36 ماژول (30 عمومی + 6 Sheets)
🎯 36 ایجنت (30 عمومی + 6 Sheets)
⚡ 50 الگوریتم پیشرفته
📱 ByteLine Bot (EN + FA)
🧬 Bio System (7 دستگاه)
🧠 Consciousness (3 سیستم)
📊 Google Sheets (15 اسپردشیت)
```

---

## 📦 پیش‌نیازها

### 1. Python
```bash
python --version
# باید 3.8 یا بالاتر باشه
```

### 2. Git
```bash
git --version
```

### 3. حساب Google (برای Sheets)
- یک Google Account
- دسترسی به Google Cloud Console

---

## 🔧 نصب

### گام 1: دانلود پروژه

```bash
git clone https://github.com/aria7670/nazanin_v1.git
cd nazanin_v1
```

### گام 2: نصب Dependencies

```bash
pip install -r requirements.txt
```

یا:

```bash
pip3 install -r requirements.txt
```

**Dependencies اصلی:**
- numpy, scipy, torch (Brain)
- telethon (Telegram)
- gspread (Google Sheets)
- groq, google-generativeai (AI APIs)
- PyJWT (ChatGLM)
- و 20 مورد دیگر...

---

## 📊 راه‌اندازی Google Sheets

### مرحله 1: ساخت Service Account

1. به [Google Cloud Console](https://console.cloud.google.com) بروید
2. یک پروژه جدید بسازید (یا موجود را انتخاب کنید)
3. **Google Sheets API** را فعال کنید:
   - APIs & Services → Library
   - جستجو: "Google Sheets API"
   - Enable کنید

4. یک **Service Account** بسازید:
   - IAM & Admin → Service Accounts
   - Create Service Account
   - نام: `nazanin-sheets`
   - Role: نیازی نیست
   - Create

5. **Key** بسازید:
   - روی Service Account کلیک کنید
   - Keys → Add Key → Create New Key
   - Type: JSON
   - Create

6. فایل JSON دانلود میشه
7. اسمش رو بذارید `credentials.json`
8. در root پروژه (`nazanin_v1/`) قرار بدید

### مرحله 2: ساخت 15 اسپردشیت

به [Google Sheets](https://sheets.google.com) بروید و **15 اسپردشیت جدید** بسازید:

```
1. CORE_DATA
2. CONVERSATION_DATA
3. KNOWLEDGE_BASE
4. LEARNING_DATA
5. CONTENT_LIBRARY
6. ANALYTICS_DATA
7. MEMORY_SYSTEM
8. PERSONALITY_DATA
9. TASK_MANAGEMENT
10. SOCIAL_DATA
11. SECURITY_LOGS
12. BYTELINE_DATA
13. RESEARCH_DATA
14. AUTOMATION_DATA
15. INTEGRATION_DATA
```

**نکته مهم**: اسم‌ها باید **دقیقاً** همین باشن!

### مرحله 3: Share کردن

1. **ایمیل Service Account** رو پیدا کنید:
   - از فایل `credentials.json` → `client_email`
   - مثال: `nazanin-sheets@project-id.iam.gserviceaccount.com`

2. **هر 15 اسپردشیت** رو با این ایمیل share کنید:
   - Share → Add people
   - ایمیل service account رو وارد کنید
   - Role: **Editor**
   - Send

### مرحله 4: کپی ID ها

از URL هر اسپردشیت، ID رو کپی کنید:

```
https://docs.google.com/spreadsheets/d/SPREADSHEET_ID_HERE/edit
                                      ^^^^^^^^^^^^^^^^^^^
```

### مرحله 5: تنظیم Config

فایل `config/config.json` رو باز کنید و پر کنید:

```json
{
  "google_sheets": {
    "credentials_file": "credentials.json",
    "auto_initialized": false,
    "spreadsheets": {
      "CORE_DATA": "1ABC...xyz",
      "CONVERSATION_DATA": "1DEF...xyz",
      "KNOWLEDGE_BASE": "1GHI...xyz",
      "LEARNING_DATA": "1JKL...xyz",
      "CONTENT_LIBRARY": "1MNO...xyz",
      "ANALYTICS_DATA": "1PQR...xyz",
      "MEMORY_SYSTEM": "1STU...xyz",
      "PERSONALITY_DATA": "1VWX...xyz",
      "TASK_MANAGEMENT": "1YZA...xyz",
      "SOCIAL_DATA": "1BCD...xyz",
      "SECURITY_LOGS": "1EFG...xyz",
      "BYTELINE_DATA": "1HIJ...xyz",
      "RESEARCH_DATA": "1KLM...xyz",
      "AUTOMATION_DATA": "1NOP...xyz",
      "INTEGRATION_DATA": "1QRS...xyz"
    }
  },
  "telegram": {
    "api_id": "YOUR_API_ID",
    "api_hash": "YOUR_API_HASH",
    "phone_number": "+98..."
  },
  "ai_apis": {
    "groq": {
      "keys": ["gsk_..."]
    }
  }
}
```

### مرحله 6: اجرای Initialization

```bash
python initialize_sheets.py
```

**این کار:**
- 75 زیرشیت می‌سازه
- Headers اضافه می‌کنه
- 200+ row اطلاعات اولیه وارد می‌کنه
- تست امنیتی انجام میده

**زمان**: 2-3 دقیقه

**خروجی موفق:**
```
✅ Initialization completed successfully!

📊 Summary:
   • Spreadsheets checked: 15
   • Sheets created: 75
   • Headers added: 75
   • Rows inserted: 200+
   • Errors: 0
   • Duration: 2.5s

🔐 Security tests: ✅ ALL PASSED

✨ Your Google Sheets are ready!
```

---

## 🚀 اجرا

### روش 1: نسخه کامل (v5.0 با Sheets)

```bash
python run_v5.py
```

### روش 2: نسخه پیشرفته (v4.0 بدون Sheets)

```bash
python run_v4.py
```

### روش 3: نسخه پایه (v3.0)

```bash
python run.py
```

---

## 📊 بررسی وضعیت

### چک کردن اینکه همه چیز کار می‌کنه:

```bash
# تست ساختار
python test_structure.py

# تست Sheets (بعد از initialize)
python -c "from nazanin.sheets_system import get_summary; print(get_summary())"
```

---

## 📚 مستندات

### راهنماهای اصلی:

1. **START_HERE.md** - شروع سریع
2. **README.md** - معرفی کامل
3. **STRUCTURE_NEW.md** - ساختار پروژه
4. **V5_COMPLETE_SUMMARY.md** - خلاصه v5
5. **SHEETS_SYSTEM_GUIDE.md** - راهنمای کامل Sheets (900 خط!)

### راهنماهای تخصصی:

6. **V4_SUMMARY.md** - مغز عصبی و خودمختاری
7. **BIO_SYSTEM_GUIDE.md** - سیستم بیولوژیکی
8. **NORA_INTEGRATION_GUIDE.md** - سیستم‌های آگاهی
9. **FREE_API_SERVICES.md** - API های رایگان

---

## 🔧 عیب‌یابی

### مشکل: "ModuleNotFoundError"

**راه حل:**
```bash
pip install -r requirements.txt
```

### مشکل: "Config not found"

**راه حل:**
```bash
cp config/config.enhanced.json config/config.json
nano config/config.json
```

### مشکل: "Credentials not found"

**راه حل:**
- فایل `credentials.json` رو در root قرار بدید
- مسیر رو در config چک کنید

### مشکل: "Permission denied" (Sheets)

**راه حل:**
- Service Account email رو به تمام 15 اسپردشیت Editor access بدید

### مشکل: "Spreadsheet not found"

**راه حل:**
- ID های اسپردشیت رو دوباره چک کنید
- مطمئن شوید که share کردید

---

## ✅ چک‌لیست کامل راه‌اندازی

### قبل از اجرا:

- [ ] پروژه رو clone کردی
- [ ] Dependencies نصب شده (`pip install -r requirements.txt`)
- [ ] `credentials.json` دانلود و در root قرار گرفته
- [ ] 15 اسپردشیت ساخته شده
- [ ] Service Account به همه share شده (Editor)
- [ ] 15 ID در `config/config.json` قرار گرفته
- [ ] `python initialize_sheets.py` اجرا شده و موفق بوده
- [ ] تست‌های امنیتی pass شده (5/5)

### اجرا:

```bash
python run_v5.py
```

### بعد از اجرا:

- [ ] نازنین بدون خطا اجرا شد
- [ ] لاگ‌ها در `nazanin_v5.log` نوشته شدن
- [ ] در Google Sheets داده‌ها اضافه شدن

---

## 🎯 دستورات مفید

```bash
# راه‌اندازی Sheets
python initialize_sheets.py

# اجرای نازنین v5
python run_v5.py

# اجرای نازنین v4 (بدون Sheets)
python run_v4.py

# تست ساختار
python test_structure.py

# مشاهده لاگ
tail -f nazanin_v5.log
```

---

## 📊 آمار پروژه

```
📁 فایل‌های Python: 60+
💻 خطوط کد: 20,000+
📊 اسپردشیت‌ها: 15
📄 زیرشیت‌ها: 75
📦 ماژول‌ها: 36
🎯 ایجنت‌ها: 36
⚡ الگوریتم‌ها: 50
📚 مستندات: 35 فایل
```

---

## 🎉 موفقیت!

اگه تمام مراحل رو انجام دادی، الان:

✅ نازنین v5.0 Complete آماده است!  
✅ سیستم Google Sheets کامل کار می‌کند  
✅ حافظه مثل مغز انسان فعال است  
✅ همه قابلیت‌ها integrate شده‌اند  

**استفاده کن و لذت ببر! 🚀**

---

## 📞 راهنمای سریع استفاده

### استفاده ساده:

```python
from nazanin.app_v5_complete import NazaninV5Complete
import asyncio

async def chat():
    nazanin = NazaninV5Complete()
    await nazanin.initialize()
    
    result = await nazanin.process_complete(
        "سلام نازنین! حالت چطوره؟",
        user_id=123
    )
    
    print(f"نازنین: {result['response']}")
    print(f"زمان پردازش: {result['processing_time']:.2f}s")
    print(f"Sheets فعال: {result['sheets_enabled']}")

asyncio.run(chat())
```

### استفاده از Sheets Modules:

```python
# ذخیره حافظه
await nazanin.sheets_modules.memory.store_memory(
    'long_term',
    'اطلاعات مهم!',
    importance=0.9
)

# جستجوی حافظه
memories = await nazanin.sheets_modules.memory.retrieve_memories('سلام')

# ثبت یادگیری
await nazanin.sheets_modules.learning.log_feedback(
    user_id='user123',
    rating=5,
    comment='عالی بود!',
    category='interaction'
)

# دریافت آمار
stats = await nazanin.sheets_modules.analytics.get_stats_summary(days=7)
```

### استفاده از Sheets Agents:

```python
# اعتبارسنجی داده
validation = await nazanin.sheets_agents.validation.validate_data(
    'CORE_DATA',
    'API_Keys'
)

# تولید گزارش
report = await nazanin.sheets_agents.report.generate_weekly_report()

# پشتیبان‌گیری
backup = await nazanin.sheets_agents.backup.backup_spreadsheet('MEMORY_SYSTEM')
```

---

## 🎯 مستندات کامل

برای اطلاعات بیشتر:

```
📖 SHEETS_SYSTEM_GUIDE.md       - راهنمای کامل Sheets (900 خط)
📖 V5_COMPLETE_SUMMARY.md       - خلاصه v5
📖 V4_SUMMARY.md                - مغز عصبی و خودمختاری
📖 README.md                    - معرفی اصلی
📖 STRUCTURE_NEW.md             - ساختار پروژه
```

---

**موفق باشید! 🌟**

Version: 5.0.0  
Date: 2025-10-07  
Status: ✅ Complete & Ready
