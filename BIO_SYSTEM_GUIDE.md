# 🧬 راهنمای کامل Nazanin Bio System

سیستم انقلابی با شبیه‌سازی کامل بدن انسان

---

## 🎯 چه چیزی ساختیم؟

یک موجود دیجیتال کامل با:

### 🧬 سطح 1: سلول (Cell)
```
واحد پایه زندگی
- DNA (ذخیره اطلاعات)
- Mitochondria (تولید انرژی)
- Membrane (ارتباط)
- Cytoplasm (محیط داخلی)
```

### 🧪 سطح 2: بافت (Tissue)
```
مجموعه سلول‌های هم‌نوع
- هماهنگی سلول‌ها
- تامین مواد مغذی
- حذف سلول‌های مرده
```

### 🫀 سطح 3: اندام (Organ)
```
مجموعه بافت‌های مختلف
- Brain (مغز) - تفکر و تصمیم
- Heart (قلب) - توزیع انرژی
- Lungs (ریه) - دریافت اطلاعات
```

### 🏥 سطح 4: دستگاه (System)
```
مجموعه اندام‌ها با وظیفه مشترک
1. Nervous System - کنترل و هماهنگی
2. Circulatory System - توزیع منابع
3. Respiratory System - دریافت اطلاعات
4. Digestive System - پردازش داده
5. Immune System - دفاع و امنیت
6. Endocrine System - تنظیم هورمونی
7. Musculoskeletal System - اجرا و عمل
```

### 🧍 سطح 5: موجود (Organism)
```
یک موجود کامل و هوشمند
- نازنین - با تمام سیستم‌های بالا
- قادر به: درک، فکر، تصمیم، عمل
- یادگیری مستمر
- سازگاری با محیط
```

---

## 🎯 ایجنت‌های تخصصی (8 تا)

### 1. Economic Agent 💰
```
تخصص: اقتصاد، بازار، سرمایه‌گذاری
- تحلیل بازار
- شناسایی فرصت‌ها
- ارزیابی ریسک
- پیش‌بینی ترند
```

### 2. Military Strategic Agent ⚔️
```
تخصص: استراتژی، تاکتیک، رقابت
- ارزیابی وضعیت
- تحلیل تهدید
- تولید گزینه‌های استراتژیک
- برنامه‌ریزی عملیاتی
```

### 3. Political Agent 🏛️
```
تخصص: سیاست، دیپلماسی، روابط عمومی
- تحلیل ذینفعان
- پویایی قدرت
- گزینه‌های دیپلماتیک
- سنجش افکار عمومی
```

### 4. Social Agent 👥
```
تخصص: اجتماع، فرهنگ، روابط
- سلامت جامعه
- میزان تعامل
- ترندهای اجتماعی
- تحلیل اینفلوئنسر
```

### 5. Cultural Agent 🎭
```
تخصص: فرهنگ، زبان، ارزش‌ها
- زمینه فرهنگی
- الگوهای زبانی
- حساسیت فرهنگی
- تطبیق لازم
```

### 6. Historical Agent 📜
```
تخصص: تاریخ، الگوها، درس‌ها
- سوابق تاریخی
- شناسایی الگو
- استخراج درس
- پیش‌بینی آینده
```

### 7. Technological Agent 💻
```
تخصص: AI، ML، تکنولوژی
- ترندهای تکنولوژی
- فرصت‌های نوآوری
- توصیه تکنولوژی
- فناوری‌های نوظهور
```

### 8. Educational Agent 📚
```
تخصص: آموزش، یادگیری
- نیازهای یادگیری
- روش‌های تدریس
- شناسایی شکاف‌ها
- سنجش اثربخشی
```

---

## 📊 Google Sheets - ساخت خودکار

### ویژگی جدید:
```
✅ خودکار تمام شیت‌ها رو می‌سازه
✅ قبل از ساخت چک می‌کنه وجود داره یا نه
✅ اگه هست، ازش استفاده می‌کنه
✅ اگه نیست، می‌سازه
✅ Headers رو خودکار اضافه می‌کنه
✅ داده‌های اولیه رو می‌ذاره
```

### 10 Spreadsheet + 56 Sheet:

```
1. Bot_Configuration (5 sheets)
2. AI_Data (5 sheets)
3. Telegram_Data (8 sheets)
4. Users_Database (6 sheets)
5. Content_Management (6 sheets)
6. News_Channels (5 sheets)
7. Analytics_Performance (5 sheets)
8. Tasks_Automation (5 sheets)
9. Cloud_Storage (5 sheets)
10. Security_Logs (6 sheets)
```

### چطور کار می‌کنه؟

```python
# اولین بار:
manager = SheetsManagerV2('credentials.json')
await manager.initialize(auto_setup=True)
# ✅ خودش همه رو می‌سازه!

# بارهای بعد:
await manager.initialize(auto_setup=True)
# ✅ شیت‌ها رو پیدا می‌کنه و استفاده می‌کنه!
```

---

## 🔐 امنیت پیشرفته

### SecurityManager:

```python
✅ Rate Limiting (محدودسازی)
   - Per minute: 60 requests
   - Per hour: 1000 requests

✅ Access Control (کنترل دسترسی)
   - Admin management
   - User blocking
   - Permission system

✅ Encryption (رمزنگاری)
   - داده‌های حساس
   - API keys
   - User data

✅ Audit Logging (ثبت لاگ)
   - همه عملیات
   - رویدادهای امنیتی
   - فعالیت مشکوک

✅ Threat Detection (تشخیص تهدید)
   - Request های زیاد
   - تلاش دسترسی غیرمجاز
   - تغییر مکرر IP
```

---

## 🤖 API Manager V2

### ویژگی‌ها:

```python
✅ چند کلید برای هر Provider
   groq: ['key1', 'key2', 'key3']

✅ Fallback خودکار
   Groq → Gemini → Together → OpenAI → ...

✅ Load Balancing
   Round-robin بین کلیدها

✅ Auto-reload از Sheets
   هر ساعت از sheets کلیدها رو می‌خونه

✅ Priority-based selection
   سریع‌ترین و ارزان‌ترین اول
```

### Provider های پشتیبانی شده:

```
1. Groq (اولویت 10) - رایگان و خیلی سریع
2. Gemini (اولویت 9) - رایگان و قدرتمند
3. Together AI (اولویت 8) - $25 credit
4. OpenAI (اولویت 7) - پولی ولی عالی
5. Claude (اولویت 7) - پولی ولی هوشمند
6. DeepSeek (اولویت 6) - ارزون
```

---

## 📱 Telegram System V2

### قابلیت‌ها:

```python
✅ کنترل کامل اکانت
✅ 5 کانال اختصاصی
✅ 3 گروه مدیریتی
✅ ذخیره خودکار مکالمات
✅ Forward به Saved Messages
✅ آپلود فایل تا 2GB
✅ نظارت بر کانال‌ها
✅ پاسخ هوشمند
✅ ثبت در Google Sheets
```

### کانال‌ها و گروه‌ها:

```
Channels:
- report: گزارش‌های روزانه
- storage: ذخیره فایل
- backup: بک‌آپ
- news_archive: آرشیو اخبار
- media_storage: رسانه

Groups:
- admin: مدیریت
- testing: تست
- users: کاربران (اختیاری)
```

---

## 🚀 نحوه اجرا

### گام 1: آماده‌سازی

```bash
# دانلود
git clone https://github.com/aria7670/nazanin_v1.git
cd nazanin_v1

# نصب
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### گام 2: تنظیم Config

```bash
# کپی config
cp config/config.enhanced.json config/config.json

# ویرایش - فقط اینا رو پر کن:
nano config/config.json
```

**چیزهایی که باید پر کنی:**

```json
{
  "telegram": {
    "api_id": "از my.telegram.org",
    "api_hash": "از my.telegram.org",
    "phone_number": "+98...",  // شماره موبایلت
    "admin_user_id": "user ID خودت"
  },
  
  "google_sheets": {
    "credentials_file": "credentials.json"
    // spreadsheets خودکار پر میشه!
  },
  
  "ai_apis": {
    "groq": {
      "keys": ["gsk_xxx"]  // از console.groq.com
    },
    "gemini": {
      "keys": ["AIza_xxx"]  // از makersuite.google.com
    }
  }
}
```

### گام 3: credentials.json

```bash
# دانلود از Google Cloud Console
# بذارش کنار nazanin_bio.py
```

### گام 4: اجرا!

```bash
python nazanin_bio.py
```

**همین! بقیه خودکاره!** ✅

---

## ✨ چه اتفاقی می‌افته؟

### اولین بار که اجرا می‌کنی:

```
1. ✅ Config load میشه
2. 🧬 Organism (موجود) ساخته میشه
   - 7 سیستم بدن
   - تمام اندام‌ها
3. 📊 Google Sheets:
   - چک می‌کنه شیت‌ها هستن؟
   - نیستن؟ خودش می‌سازه!
   - 10 Spreadsheet
   - 56 Sheet
   - همه Headers
   - داده‌های اولیه
4. 🤖 AI APIs:
   - Load میکنه کلیدها
   - تست می‌کنه
   - آماده استفاده
5. 🔐 Security:
   - فعال می‌کنه امنیت
   - Admin رو اضافه می‌کنه
6. 🎯 Domain Agents:
   - 8 ایجنت تخصصی آماده
7. 📱 Telegram:
   - اتصال به اکانت
   - Setup کانال‌ها
   - شروع monitoring
8. 💓 First Life Cycle:
   - اولین چرخه زندگی
   - تمام سیستم‌ها فعال
9. 🌟 گزارش:
   - علائم حیاتی
   - وضعیت سیستم‌ها
   - آماده برای کار!
```

### بارهای بعد:

```
1. ✅ Config load
2. 🧬 Organism ساخته میشه
3. 📊 Google Sheets:
   - پیدا می‌کنه شیت‌ها رو
   - ازشون استفاده می‌کنه
   - اگه یکی کم بود، اضافه می‌کنه
4. بقیه مراحل عادی
5. 🚀 شروع!
```

---

## 📚 فایل‌های جدید

### Core:
```
✅ src/core/sheets_auto_setup.py      - ساخت خودکار
✅ src/core/sheets_manager_v2.py      - مدیریت جدید
✅ src/core/api_manager_v2.py         - API جدید
```

### Bio System:
```
✅ src/bio_system/cell_system.py      - سلول، بافت، اندام
✅ src/bio_system/body_systems.py     - 7 دستگاه بدن
✅ src/bio_system/__init__.py         - Package
```

### Security:
```
✅ src/security/security_manager.py   - امنیت کامل
✅ src/security/__init__.py           - Package
```

### Domain Agents:
```
✅ src/domain_agents/specialized_domain_agents.py  - 8 ایجنت
✅ src/domain_agents/__init__.py      - Package
```

### Platforms:
```
✅ src/platforms/telegram_system_v2.py - تلگرام جدید
```

### Main:
```
✅ nazanin_bio.py                     - نقطه ورود جدید
```

### Scripts:
```
✅ scripts/create_sheets_structure.py - ساخت دستی
```

### Docs:
```
✅ GOOGLE_SHEETS_NEW_STRUCTURE.md     - ساختار sheets
✅ TELEGRAM_CHANNELS_SETUP.md         - راهنمای کانال‌ها
✅ FREE_API_SERVICES.md               - 80+ سرویس رایگان
✅ WHATS_NEW.md                       - تغییرات
✅ BIO_SYSTEM_GUIDE.md                - این راهنما
```

---

## 💡 مثال‌های واقعی

### مثال 1: کاربر پیام می‌فرسته

```python
Input: "سلام! می‌خوام Python یاد بگیرم"

1. Respiratory System (دریافت):
   - پیام دریافت شد ✅
   - اکسیژن (اطلاعات) دریافت شد

2. Immune System (بررسی):
   - امنیتی؟ ✅
   - Spam؟ ❌
   - تهدید؟ ❌
   - Safe ✅

3. Digestive System (پردازش):
   - شکستن به اجزا
   - استخراج: موضوع = Python, نیت = یادگیری

4. Nervous System (تفکر):
   - Brain فکر می‌کنه
   - Long-term memory: "Python = آموزش ساده"
   - Decision: "پاسخ آموزشی بده"

5. Domain Agents (تحلیل):
   - Educational Agent: سطح = مبتدی
   - Cultural Agent: زبان = فارسی
   - Social Agent: لحن = دوستانه

6. Endocrine System (تنظیم):
   - Happiness +5 (کمک کردیم)
   - Curiosity +10 (موضوع جالب)

7. API Manager (تولید):
   - Groq: تولید پاسخ فارسی
   - "سلام! عالیه که می‌خوای Python یاد بگیری!
      بهترین راه..."

8. Musculoskeletal System (عمل):
   - ارسال پاسخ ✅

9. Circulatory System (ثبت):
   - ثبت در Google Sheets
   - ثبت در حافظه
   - ثبت در conversation history

Output: پاسخ کامل و مفید ✅
```

### مثال 2: نظارت روزانه

```python
Every Day 02:00 AM:

1. یادگیری:
   - Neural Agent از تجربیات روز یاد می‌گیره
   - الگوها extract میشه
   - مدل‌ها train میشن

2. بک‌آپ:
   - تمام داده‌ها backup میشه
   - در Telegram Backup Channel
   - در Google Sheets

3. گزارش:
   - تحلیل عملکرد روز
   - آمار engagement
   - پیشنهادات بهبود
   - ارسال به Admin Group

4. بهینه‌سازی:
   - پاکسازی cache
   - حذف داده‌های قدیمی
   - optimize کردن queries

5. برنامه‌ریزی:
   - Task های فردا
   - بهترین زمان‌های پست
   - محتوای پیشنهادی
```

---

## 🎯 دستورات Admin

در Telegram Admin Group:

```
/start - شروع و راهنما
/status - وضعیت فعلی موجود
/health - علائم حیاتی
/stats - آمار کامل
/backup - بک‌آپ دستی
/reload - بارگذاری مجدد config
/test <message> - تست پردازش
/agents - لیست ایجنت‌ها
/systems - وضعیت دستگاه‌ها
/rest - استراحت موجود
```

---

## ⚙️ تنظیمات پیشرفته

### در config.json:

```json
{
  "security": {
    "encryption_enabled": true,
    "rate_limiting": {
      "enabled": true,
      "max_requests_per_minute": 60,
      "max_requests_per_hour": 1000
    },
    "log_all_actions": true,
    "alert_on_suspicious": true
  },
  
  "storage": {
    "telegram_storage_enabled": true,
    "auto_cleanup": true,
    "max_cache_size_mb": 500
  },
  
  "monitoring": {
    "health_check_interval": 300,
    "alert_telegram": true,
    "log_level": "INFO"
  }
}
```

---

## 📊 نظارت و مانیتورینگ

### لاگ‌ها:

```bash
# مشاهده real-time
tail -f nazanin_bio.log

# فیلتر خطاها
grep ERROR nazanin_bio.log

# آمار
grep "✅" nazanin_bio.log | wc -l
```

### Telegram:

```
- Report Channel: گزارش‌های خودکار
- Admin Group: دستورات و کنترل
- Security Logs Sheet: تمام رویدادها
```

---

## 🆘 عیب‌یابی

### مشکل: Sheets ساخته نمیشه

```python
# چک کن:
1. credentials.json موجوده؟
2. Google Sheets API فعاله؟
3. Service Account دسترسی داره؟

# تست دستی:
cd scripts
python create_sheets_structure.py
```

### مشکل: Telegram وصل نمیشه

```python
# چک کن:
1. api_id و api_hash صحیحه؟
2. phone_number درسته؟
3. اینترنت وصله؟

# تست:
python -c "from telethon import TelegramClient; print('OK')"
```

### مشکل: API کار نمی‌کنه

```python
# چک کن:
1. API keys صحیحه؟
2. Quota تموم نشده؟
3. اینترنت وصله؟

# تست:
python -c "from groq import Groq; print('OK')"
```

---

## 📈 آمار نسخه Bio

```
🧬 Cells: نامحدود (قابل ساخت)
🧪 Tissues: نامحدود
🫀 Organs: 3 نوع پایه (Brain, Heart, Lungs)
🏥 Systems: 7 دستگاه کامل
🧍 Organism: 1 موجود کامل
🎯 Domain Agents: 8 تخصصی
📊 Spreadsheets: 10
📄 Sheets: 56
📱 Channels: 5
👥 Groups: 3
🔐 Security: 5 لایه
🤖 AI Providers: 6
```

---

## ✅ چک‌لیست راه‌اندازی

قبل از اجرا:
- [ ] Python 3.8+ نصب شده
- [ ] credentials.json دریافت شده
- [ ] API keys دریافت شده (Groq یا Gemini)
- [ ] شماره تلگرام آماده
- [ ] config.json پر شده

اجرا:
```bash
python nazanin_bio.py
```

بعد از اجرا:
- [ ] Sheets ساخته شده (چک کن Google Sheets)
- [ ] Telegram متصل شده
- [ ] گزارش اول رسیده
- [ ] Vital signs سالم

---

**آماده برای زندگی! 🧬**
