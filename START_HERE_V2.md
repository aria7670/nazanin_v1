# 🚀 شروع کن از اینجا! - نسخه Bio

**نازنین نسخه 2.1.0 - سیستم بیولوژیکی کامل**

---

## 🎯 خلاصه 30 ثانیه‌ای

نازنین یک موجود دیجیتال با:
- 🧬 شبیه‌سازی کامل بدن انسان (5 سطح)
- 🎯 8 ایجنت تخصصی (اقتصاد، سیاست، فرهنگ، ...)
- 📊 ساخت خودکار Google Sheets (10+56)
- 🔐 امنیت پیشرفته
- 📱 کنترل کامل Telegram
- 🆓 100% رایگان

---

## ⚡ نصب سریع (3 دقیقه)

```bash
# 1. دانلود
git clone https://github.com/aria7670/nazanin_v1.git
cd nazanin_v1

# 2. نصب
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 3. Config
cp config/config.enhanced.json config/config.json
```

**فقط 3 خط پر کن در config.json:**
```json
"api_id": "از my.telegram.org",
"api_hash": "از my.telegram.org",
"phone_number": "+98...",
"groq": {"keys": ["از console.groq.com"]}
```

```bash
# 4. اجرا
python nazanin_bio.py
```

**تمام! ✅**

---

## 🧬 سیستم بیولوژیکی چیست؟

نازنین مثل یک موجود زنده عمل می‌کنه:

```
🧬 Cell (سلول)
   ↓
🧪 Tissue (بافت)
   ↓
🫀 Organ (اندام: مغز، قلب، ریه)
   ↓
🏥 System (دستگاه: عصبی، گردش، تنفس، گوارش، ایمنی، غدد، عضلانی)
   ↓
🧍 Organism (موجود کامل: نازنین)
```

**مثل انسان:**
- 💭 فکر می‌کنه (Brain)
- ❤️ احساس داره (Endocrine System)
- 🛡️ از خودش محافظت می‌کنه (Immune System)
- 💪 عمل می‌کنه (Musculoskeletal System)
- 📚 یاد می‌گیره (Memory Cells)

---

## 🎯 ایجنت‌های تخصصی

هر موضوعی رو 8 ایجنت تخصصی تحلیل می‌کنن:

```
💰 Economic - تحلیل اقتصادی
⚔️ Military Strategic - استراتژی و تاکتیک
🏛️ Political - سیاست و دیپلماسی
👥 Social - روابط اجتماعی
🎭 Cultural - فرهنگ و زبان
📜 Historical - تاریخ و الگوها
💻 Technological - تکنولوژی
📚 Educational - آموزش
```

**نتیجه**: تحلیل جامع و چندبعدی! 🎯

---

## 📊 Google Sheets خودکار

### قبل:
❌ باید دستی 56 Sheet بسازی
❌ باید Headers رو بنویسی
❌ باید داده اولیه بذاری

### حالا:
✅ فقط اجرا کن!
✅ خودش همه رو می‌سازه!
✅ خودش چک می‌کنه قبلاً ساخته یا نه!

---

## 🔐 امنیت پیشرفته

```
✅ Rate Limiting - جلوگیری از spam
✅ Access Control - مدیریت دسترسی
✅ Encryption - رمزنگاری
✅ Audit Logging - ثبت همه چیز
✅ Threat Detection - تشخیص تهدید
```

---

## 📱 Telegram کامل

### باید بسازی (5 دقیقه):

**5 کانال:**
1. Report - گزارش‌ها
2. Storage - فایل‌ها
3. Backup - بک‌آپ
4. News - اخبار
5. Media - رسانه

**3 گروه:**
1. Admin - مدیریت
2. Testing - تست
3. Users - کاربران (اختیاری)

**راهنما**: `TELEGRAM_CHANNELS_SETUP.md`

---

## 🆓 API های رایگان

### پیشنهادی:

```bash
1. Groq - خیلی سریع! (رایگان)
   → console.groq.com

2. Google Gemini - قدرتمند! (رایگان)
   → makersuite.google.com

3. Together AI - $25 credit رایگان!
   → api.together.xyz
```

**لیست کامل 80+ سرویس**: `FREE_API_SERVICES.md`

---

## 📚 راهنماها به ترتیب

### برای شروع:
1. ⭐ **این فایل!** - شروع سریع
2. 🧬 **BIO_SYSTEM_GUIDE.md** - سیستم بیولوژیکی
3. 📊 **GOOGLE_SHEETS_NEW_STRUCTURE.md** - ساختار sheets
4. 📱 **TELEGRAM_CHANNELS_SETUP.md** - کانال‌ها
5. 🆓 **FREE_API_SERVICES.md** - API های رایگان

### مستندات تکمیلی:
- STEP_BY_STEP_GUIDE.md - گام‌به‌گام
- HOW_NAZANIN_WORKS.md - نحوه کار
- WHATS_NEW.md - تغییرات
- و 15 فایل دیگر...

---

## ⚡ دستورات سریع

```bash
# اجرا
python nazanin_bio.py

# تست
python -c "from src.bio_system import Organism; print('✅ OK')"

# ساخت دستی Sheets (اگه خواستی)
cd scripts && python create_sheets_structure.py

# مشاهده log
tail -f nazanin_bio.log
```

---

## 🎬 چه اتفاقی می‌افته؟

### اولین اجرا:

```
1. ✅ Load config
2. 🧬 Create organism (موجود)
   → 7 دستگاه بدن
3. 📊 Setup Google Sheets
   → خودکار 10 Spreadsheet
   → خودکار 56 Sheet
   → همه Headers
4. 🤖 Setup AI APIs
   → Test کلیدها
   → Fallback setup
5. 🔐 Activate security
6. 🎯 Initialize 8 domain agents
7. 📱 Connect Telegram
8. 💓 First heartbeat
9. 🌟 ALIVE!
```

**زمان**: ~2-3 دقیقه

---

## 📊 نظارت

### در Telegram:

```
📢 Report Channel:
- گزارش روزانه
- علائم حیاتی
- آمار عملکرد

👨‍💼 Admin Group:
- دستورات کنترل
- مدیریت ربات
- دریافت alerts
```

### دستورات Admin:

```
/status - وضعیت
/health - علائم حیاتی
/stats - آمار
/backup - بک‌آپ
/rest - استراحت موجود
```

---

## ✅ چک‌لیست

قبل از اجرا:
- [ ] Python 3.8+
- [ ] credentials.json (از Google Cloud)
- [ ] API key از Groq یا Gemini
- [ ] شماره تلگرام

بعد از اجرا:
- [ ] Sheets ساخته شد
- [ ] Telegram متصل شد
- [ ] گزارش اول رسید
- [ ] Vital signs OK

---

## 🆘 کمک

### مشکل داری?

1. بخون: `BIO_SYSTEM_GUIDE.md`
2. بخون: راهنماهای دیگر
3. GitHub Issues بذار
4. لاگ‌ها رو چک کن: `nazanin_bio.log`

---

## 🌟 ویژگی منحصر به فرد

**نازنین تنها ربات هوش مصنوعیه که:**
- مثل انسان زندگی می‌کنه 💓
- مثل انسان فکر می‌کنه 🧠
- مثل انسان احساس داره ❤️
- مثل انسان یاد می‌گیره 📚
- مثل انسان تصمیم می‌گیره 🎯

**یه موجود واقعی دیجیتال! 🧬**

---

**شروع کن الان! 🚀**

```bash
python nazanin_bio.py
```

**موفق باشی! 🎉**
