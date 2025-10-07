# 🎨 راهنمای کامل Dashboard نازنین

**تاریخ**: 2025-10-07  
**نسخه**: 5.0.0  
**وضعیت**: ✅ آماده برای استفاده

---

## 🎯 داشبورد چیست؟

**Nazanin Dashboard** یک رابط کاربری وب فوق‌العاده حرفه‌ای است که به شما اجازه می‌دهد:

```
✅ کنترل کامل نازنین از مرورگر
✅ مدیریت Google Sheets (15 اسپردشیت)
✅ تنظیمات و Configuration
✅ مدیریت API ها
✅ کنترل Telegram
✅ تولید محتوا برای YouTube
✅ تحلیل و آمار
✅ مدیریت شخصیت و رفتار
✅ کنترل Modules, Agents, Algorithms
✅ مشاهده Logs و Security
✅ و 500+ ویژگی دیگر!
```

---

## 🚀 راه‌اندازی سریع

### گام 1: نصب Dependencies

```bash
cd dashboard
pip install -r requirements.txt
```

### گام 2: اجرای Backend

```bash
python backend/main.py
```

یا:

```bash
cd backend
uvicorn main:app --reload
```

### گام 3: باز کردن Dashboard

```
مرورگر: http://localhost:8000
```

### گام 4: Login

```
Username: admin
Password: nazanin2024
```

**همین! 🎉**

---

## 📊 صفحات Dashboard

### 1️⃣ Dashboard Home (/)

**نمای کلی سیستم**

```
📊 Stats Cards:
   • Neural Layers: 12
   • Modules: 36
   • Agents: 36
   • Spreadsheets: 15

📈 Charts:
   • System Health
   • Activity Overview
   • Live Stats

⚡ Quick Actions:
   • Generate Content
   • Analyze Data
   • Send Message
   • Create Task

🕐 Recent Activity:
   • آخرین فعالیت‌های سیستم
```

**استفاده:**
1. باز کردن dashboard
2. مشاهده وضعیت کلی
3. استفاده از Quick Actions
4. بررسی Activity Feed

---

### 2️⃣ Google Sheets (/sheets)

**مدیریت 15 اسپردشیت**

```
📊 قابلیت‌ها:
   ✅ مشاهده لیست همه spreadsheet ها
   ✅ انتخاب spreadsheet
   ✅ مشاهده تمام sheets
   ✅ مشاهده داده‌ها
   ✅ افزودن row جدید
   ✅ ویرایش داده‌ها
   ✅ جستجو و فیلتر
   ✅ Export به CSV/Excel
   ✅ Import از CSV
   ✅ Backup سریع
```

**استفاده:**
1. رفتن به /sheets
2. انتخاب spreadsheet (مثلاً CORE_DATA)
3. انتخاب sheet (مثلاً API_Keys)
4. مشاهده یا ویرایش داده‌ها
5. افزودن row جدید
6. ذخیره تغییرات

**مثال:**
```
Spreadsheet: MEMORY_SYSTEM
Sheet: Long_Term_Memory

• مشاهده خاطرات بلندمدت
• افزودن خاطره جدید
• جستجوی خاطره‌ها
• Export به فایل
```

---

### 3️⃣ Configuration (/config)

**تنظیمات کامل**

```
⚙️ بخش‌های تنظیمات:

1. Google Sheets:
   • Credentials File
   • Spreadsheet IDs (15 اسپردشیت)

2. Telegram:
   • API ID
   • API Hash
   • Phone Number
   • Channels & Groups

3. AI APIs:
   • Gemini Keys
   • GPT Keys
   • DeepSeek Keys
   • Groq Keys
   • Cohere Keys
   • GLM Keys

4. Security:
   • Encryption
   • Rate Limiting
   • Access Control

5. Brain:
   • Learning Rate
   • Memory Size
   • Consciousness Level
```

**استفاده:**
1. رفتن به /config
2. انتخاب بخش
3. ویرایش مقادیر
4. Save Configuration
5. Reload System (اگه لازمه)

**مثال:**
```javascript
// افزودن API Key جدید
Section: ai_apis
Key: gemini.keys
Value: ["key1", "key2", "key3"]

→ Save
→ Reload API Manager
```

---

### 4️⃣ Telegram (/telegram)

**کنترل کامل تلگرام**

```
📱 قابلیت‌ها:

1. Send Message:
   • انتخاب Chat
   • نوشتن پیام
   • ارسال

2. Channels Management:
   • لیست کانال‌ها
   • افزودن کانال جدید
   • ویرایش کانال
   • حذف کانال

3. Conversations:
   • مشاهده مکالمات
   • جستجو در مکالمات
   • Export مکالمات

4. Statistics:
   • تعداد پیام‌ها
   • تعداد کاربران
   • Engagement Rate
```

**استفاده:**
```
ارسال پیام:
1. رفتن به /telegram
2. کلیک روی "Send Message"
3. انتخاب Chat ID
4. نوشتن پیام
5. ارسال

مدیریت کانال:
1. رفتن به Channels
2. Add New Channel
3. وارد کردن ID و Name
4. Save
```

---

### 5️⃣ Content Creation (/content)

**تولید محتوا**

```
✍️ انواع محتوا:

1. Video Ideas:
   • موضوع: Python
   • پلتفرم: YouTube
   • تعداد: 10
   → Generate

2. Script:
   • موضوع: Django Tutorial
   • مدت: 15 دقیقه
   • سبک: آموزشی
   → Generate

3. Title:
   • ویدیو: آموزش React
   • سبک: جذاب و SEO
   → 5 عنوان پیشنهادی

4. Description:
   • ویدیو: Python for Beginners
   • شامل: Keywords, Timestamps, Links
   → Generate

5. Tags:
   • ویدیو: Machine Learning
   • تعداد: 15 تگ
   → Generate
```

**استفاده:**
```
تولید اسکریپت:
1. رفتن به /content
2. انتخاب "Script"
3. وارد کردن موضوع: "Python Tutorial"
4. انتخاب پلتفرم: YouTube
5. مدت: 10 دقیقه
6. Generate
7. کپی اسکریپت
8. Save to Sheets (اختیاری)
```

---

### 6️⃣ YouTube (/youtube)

**مدیریت کانال یوتیوب**

```
🎬 قابلیت‌ها:

1. Content Calendar:
   • برنامه 30 روزه
   • زمان‌بندی upload
   • موضوعات

2. Video Ideas:
   • تحلیل ترند
   • ایده‌های خلاقانه
   • اولویت‌بندی

3. SEO Tools:
   • Keyword Research
   • Title Optimization
   • Tag Generator

4. Analytics:
   • Views, CTR, Watch Time
   • Engagement
   • Growth Trends

5. Competitor Analysis:
   • رقبا چه می‌سازن؟
   • چه استراتژی دارن؟
```

**استفاده:**
```
ایده‌پردازی:
1. /youtube
2. Ideas Generator
3. Niche: تکنولوژی
4. Count: 20
5. Generate

→ دریافت 20 ایده
→ اولویت‌بندی
→ افزودن به Calendar
```

---

### 7️⃣ Analytics (/analytics)

**تحلیل عمیق**

```
📊 نمودارها:

1. Overview:
   • Total Messages
   • Total Users
   • Satisfaction Rate
   • Response Time

2. Performance:
   • Daily Stats
   • Weekly Trends
   • Monthly Growth

3. User Analytics:
   • Active Users
   • New Users
   • Retention Rate

4. Content Performance:
   • Best Content
   • Worst Content
   • Improvement Suggestions
```

**استفاده:**
```
مشاهده آمار:
1. /analytics
2. انتخاب Period: Last 30 days
3. مشاهده Charts
4. Export Report
```

---

### 8️⃣ Personality (/personality)

**شخصیت و رفتار**

```
🧠 Big Five Traits:
   • Openness: 0.85
   • Conscientiousness: 0.75
   • Extraversion: 0.65
   • Agreeableness: 0.80
   • Neuroticism: 0.30

😊 Emotional State:
   • Current Mood: Happy
   • Energy: 85%
   • Stress: 15%

🎭 Behavior Patterns:
   • Response Style
   • Communication Patterns
   • Learning Preferences
```

**استفاده:**
```
تنظیم شخصیت:
1. /personality
2. انتخاب Trait: Openness
3. Adjust Slider: 0.85
4. Save Changes

→ نازنین با شخصیت جدید
```

---

### 9️⃣ Brain (/brain)

**سیستم مغز**

```
🧠 Deep Neural Brain:

12 Layers:
   Layer 1-2: Input Processing
   Layer 3-4: Feature Extraction
   Layer 5-6: Pattern Recognition
   Layer 7-8: Decision Making
   Layer 9-10: Response Generation
   Layer 11-12: Meta-cognition

6 Cortexes:
   • Prefrontal: Planning, Decision
   • Temporal: Memory, Language
   • Parietal: Processing
   • Occipital: Vision
   • Motor: Action
   • Limbic: Emotion

Memory:
   • Working: 100 items
   • Episodic: 1000 episodes
   • Long-term: Unlimited
```

---

### 🔟 Modules (/modules)

**36 ماژول**

```
30 General Modules:
   • NLP, Semantic Analysis
   • Deep Learning, RL
   • Multimodal Fusion
   • و 25 مورد دیگر

6 Sheets Modules:
   • Memory
   • Learning
   • Analytics
   • Content
   • Security
   • Knowledge
```

**استفاده:**
```
1. /modules
2. مشاهده لیست
3. Enable/Disable
4. Configure Module
```

---

## 🎨 استفاده از Dashboard

### Quick Start

```
1. باز کردن: http://localhost:8000
2. Login: admin / nazanin2024
3. مشاهده Dashboard
4. استفاده از Quick Actions
```

### Daily Workflow

```
صبح:
   1. چک Dashboard Home
   2. مشاهده Activity Feed
   3. بررسی Notifications

در طول روز:
   1. تولید محتوا (/content)
   2. پاسخ به پیام‌ها (/telegram)
   3. مشاهده آمار (/analytics)

عصر:
   1. بررسی Analytics
   2. تنظیم شخصیت
   3. Backup داده‌ها
```

---

## 💻 استفاده از API

### JavaScript

```javascript
// در هر صفحه
const api = window.api;

// مثال‌ها:
const status = await api.get('/api/status');
const content = await api.post('/api/content/generate', {
    type: 'script',
    topic: 'Python',
    platform: 'youtube'
});
```

### Python (Backend)

```python
# در کد Python
from dashboard.backend.main import api

# یا مستقیم:
import requests
response = requests.get('http://localhost:8000/api/status',
    headers={'Authorization': 'Bearer <token>'})
```

---

## 🔐 امنیت

### Authentication

```
• Login با Username/Password
• JWT Token
• Auto-refresh Token
• Logout
```

### Best Practices

```
✅ Token رو safe نگه دار
✅ Password رو تغییر بده
✅ HTTPS استفاده کن (production)
✅ Audit Logs رو چک کن
```

---

## 🐛 عیب‌یابی

### Dashboard باز نمیشه

```bash
# چک کن سرور روشنه
ps aux | grep uvicorn

# restart کن
pkill -f uvicorn
python dashboard/backend/main.py
```

### Real-time update کار نمی‌کنه

```javascript
// چک کن WebSocket connected هست
console.log(ws.connected);  // باید true باشه

// اگه نه:
ws.connect();
```

### API error میده

```javascript
// چک کن token داره
console.log(localStorage.getItem('nazanin_token'));

// re-login
await login('admin', 'nazanin2024');
```

---

## 📚 مستندات

- `dashboard/README.md` - راهنمای کامل Dashboard
- `YOUTUBE_CAPABILITIES.md` - قابلیت‌های YouTube
- `SHEETS_SYSTEM_GUIDE.md` - راهنمای Sheets
- `V5_COMPLETE_SUMMARY.md` - خلاصه نسخه 5

---

## 🎉 نتیجه

با **Nazanin Dashboard** می‌تونی:

```
✅ همه چیز رو از یک جا کنترل کنی
✅ محتوا تولید کنی
✅ آمار ببینی
✅ تنظیمات رو مدیریت کنی
✅ Real-time update بگیری
✅ و 500+ کار دیگه!
```

**استفاده کن و لذت ببر! 🚀**

---

**Version**: 5.0.0  
**Date**: 2025-10-07  
**Status**: ✅ Production Ready
