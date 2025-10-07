

# 📊 راهنمای کامل سیستم Google Sheets

**نسخه**: 5.0.0  
**تاریخ**: 2025-10-07  
**وضعیت**: ✅ کامل و آماده

---

## 📋 فهرست مطالب

1. [معرفی](#معرفی)
2. [ساختار 15 اسپردشیت](#ساختار-15-اسپردشیت)
3. [نحوه راه‌اندازی](#نحوه-راه-اندازی)
4. [ماژول‌ها و ایجنت‌ها](#ماژول-ها-و-ایجنت-ها)
5. [API و استفاده](#api-و-استفاده)
6. [عیب‌یابی](#عیب-یابی)

---

## 🎯 معرفی

سیستم Google Sheets نازنین یک سیستم **جامع** و **خودکار** برای مدیریت اطلاعات است که شامل:

✅ **15 اسپردشیت اصلی**  
✅ **75+ زیرشیت**  
✅ **6 ماژول تخصصی**  
✅ **6 ایجنت هوشمند**  
✅ **راه‌اندازی خودکار**  
✅ **اطلاعات اولیه کامل**

---

## 📊 ساختار 15 اسپردشیت

### 1️⃣ CORE_DATA - داده‌های اصلی

**توضیح**: داده‌های بنیادی و پیکربندی سیستم

**زیرشیت‌ها** (5 sheet):
- `System_Config` - تنظیمات سیستم
- `API_Keys` - کلیدهای API
- `User_Profiles` - پروفایل کاربران
- `Platform_Credentials` - اطلاعات احراز هویت
- `System_Status` - وضعیت اجزای سیستم

**اطلاعات اولیه**:
- نسخه سیستم
- تنظیمات پیش‌فرض
- کلیدهای API (placeholder)
- کاربران پیش‌فرض (admin, byteline_bot)

---

### 2️⃣ CONVERSATION_DATA - داده‌های مکالمه

**توضیح**: ذخیره تمام تعاملات و مکالمات

**زیرشیت‌ها** (5 sheet):
- `Messages` - تمام پیام‌ها
- `Conversations` - مکالمات کامل
- `User_Preferences` - ترجیحات یادگرفته شده
- `Response_Templates` - قالب‌های پاسخ
- `Conversation_Patterns` - الگوهای مکالمه

**اطلاعات اولیه**:
- پیام راه‌اندازی
- 5 قالب پاسخ (سلام، تشکر، خداحافظی، سوال، کمک)
- 3 الگوی اولیه

---

### 3️⃣ KNOWLEDGE_BASE - پایگاه دانش

**توضیح**: دانش عمومی و تخصصی

**زیرشیت‌ها** (6 sheet):
- `Facts` - حقایق و دانسته‌ها
- `Definitions` - تعاریف
- `FAQs` - سوالات متداول
- `Tutorials` - آموزش‌ها
- `References` - منابع و مراجع
- `Glossary` - واژه‌نامه

**اطلاعات اولیه**:
- 4 حقیقت درباره AI و تکنولوژی
- 3 تعریف (AI, ML, NLP)
- 3 سوال متداول
- 2 آموزش
- 3 واژه در Glossary

---

### 4️⃣ LEARNING_DATA - داده‌های یادگیری

**توضیح**: یادگیری و بهبود مستمر

**زیرشیت‌ها** (5 sheet):
- `Training_Sessions` - جلسات آموزش
- `Feedback` - بازخوردها
- `Mistakes` - اشتباهات و یادگیری
- `Performance_Metrics` - معیارهای عملکرد
- `Improvements` - بهبودها

**اطلاعات اولیه**:
- 1 جلسه آموزش اولیه
- 1 بازخورد مثبت
- 3 metric اولیه (response_time, accuracy, satisfaction)
- 1 بهبود (initialization)

---

### 5️⃣ CONTENT_LIBRARY - کتابخانه محتوا

**توضیح**: محتوای تولید شده و ذخیره شده

**زیرشیت‌ها** (5 sheet):
- `Posts` - پست‌ها
- `Media_Files` - فایل‌های رسانه‌ای
- `Templates` - قالب‌ها
- `Hashtags` - هشتگ‌ها
- `Content_Calendar` - تقویم محتوا

**اطلاعات اولیه**:
- 2 قالب محتوا (Tech News, Tutorial)
- 4 هشتگ (#AI, #MachineLearning, #Python, #ByteLine)

---

### 6️⃣ ANALYTICS_DATA - داده‌های تحلیلی

**توضیح**: تحلیل‌ها و آمار

**زیرشیت‌ها** (5 sheet):
- `Daily_Stats` - آمار روزانه
- `User_Behavior` - رفتار کاربران
- `Engagement_Metrics` - معیارهای تعامل
- `Trend_Analysis` - تحلیل روندها
- `Performance_Reports` - گزارش‌های عملکرد

---

### 7️⃣ MEMORY_SYSTEM - سیستم حافظه

**توضیح**: حافظه کوتاه‌مدت و بلندمدت (عین مغز انسان)

**زیرشیت‌ها** (5 sheet):
- `Short_Term_Memory` - حافظه کوتاه‌مدت
- `Long_Term_Memory` - حافظه بلندمدت
- `Episodic_Memory` - حافظه اپیزودیک
- `Semantic_Memory` - حافظه معنایی
- `Working_Memory` - حافظه کاری

**اطلاعات اولیه**:
- 1 حافظه بلندمدت (تاریخ راه‌اندازی)
- 1 حافظه اپیزودیک (رویداد راه‌اندازی)
- 1 حافظه معنایی (تعریف نازنین)

---

### 8️⃣ PERSONALITY_DATA - داده‌های شخصیتی

**توضیح**: شخصیت و رفتار

**زیرشیت‌ها** (5 sheet):
- `Traits` - صفات شخصیتی (Big Five)
- `Emotions` - احساسات
- `Moods` - خلق و خو
- `Behaviors` - رفتارها
- `Values` - ارزش‌ها

**اطلاعات اولیه**:
- 5 صفت Big Five (openness, conscientiousness, extraversion, agreeableness, neuroticism)
- 1 احساس اولیه (joy)
- 1 mood (optimistic)
- 2 behavior (helpful, curious)
- 3 value (helpfulness, honesty, learning)

---

### 9️⃣ TASK_MANAGEMENT - مدیریت وظایف

**توضیح**: مدیریت تسک‌ها و برنامه‌ریزی

**زیرشیت‌ها** (5 sheet):
- `Tasks` - وظایف
- `Schedules` - برنامه‌زمانی
- `Goals` - اهداف
- `Projects` - پروژه‌ها
- `Reminders` - یادآوری‌ها

**اطلاعات اولیه**:
- 1 task (راه‌اندازی)
- 2 schedule (daily_report, memory_consolidation)
- 2 goal (یادگیری، رشد ByteLine)
- 1 project (Nazanin v4.0)

---

### 🔟 SOCIAL_DATA - داده‌های اجتماعی

**توضیح**: شبکه اجتماعی و روابط

**زیرشیت‌ها** (5 sheet):
- `Relationships` - روابط
- `Communities` - جوامع
- `Influencers` - تاثیرگذاران
- `Social_Events` - رویدادهای اجتماعی
- `Network_Analysis` - تحلیل شبکه

**اطلاعات اولیه**:
- 1 community (ByteLine Community)

---

### 1️⃣1️⃣ SECURITY_LOGS - لاگ‌های امنیتی

**توضیح**: امنیت و ممیزی

**زیرشیت‌ها** (5 sheet):
- `Access_Logs` - لاگ دسترسی
- `Security_Events` - رویدادهای امنیتی
- `Blocked_Users` - کاربران مسدود شده
- `Suspicious_Activities` - فعالیت‌های مشکوک
- `Audit_Trail` - رد ممیزی

**اطلاعات اولیه**:
- 1 access log (initialization)
- 1 security event (system started)
- 1 audit trail (create spreadsheets)

---

### 1️⃣2️⃣ BYTELINE_DATA - داده‌های ByteLine

**توضیح**: داده‌های کانال ByteLine

**زیرشیت‌ها** (5 sheet):
- `Channel_Posts` - پست‌های کانال
- `Subscribers` - مشترکین
- `Content_Ideas` - ایده‌های محتوا
- `Campaign_Tracking` - پیگیری کمپین‌ها
- `Feedback_FA` - بازخورد فارسی

**اطلاعات اولیه**:
- 3 ایده محتوا (AI Trends, Python Tips, ML Algorithms)

---

### 1️⃣3️⃣ RESEARCH_DATA - داده‌های تحقیقاتی

**توضیح**: تحقیقات و آزمایش‌ها

**زیرشیت‌ها** (5 sheet):
- `Experiments` - آزمایش‌ها
- `Datasets` - مجموعه داده‌ها
- `Research_Papers` - مقالات تحقیقاتی
- `Hypotheses` - فرضیه‌ها
- `Observations` - مشاهدات

**اطلاعات اولیه**:
- 2 مقاله تحقیقاتی (Attention Is All You Need, BERT)

---

### 1️⃣4️⃣ AUTOMATION_DATA - داده‌های اتوماسیون

**توضیح**: اتوماسیون و فرآیندها

**زیرشیت‌ها** (5 sheet):
- `Workflows` - گردش کارها
- `Rules` - قوانین خودکار
- `Scripts` - اسکریپت‌ها
- `Triggers` - ماشه‌ها
- `Job_Queue` - صف کارها

**اطلاعات اولیه**:
- 2 workflow (Daily Backup, Memory Consolidation)
- 2 rule (user_greeting, inappropriate_content)
- 2 trigger (daily_midnight, new_user)

---

### 1️⃣5️⃣ INTEGRATION_DATA - داده‌های یکپارچه‌سازی

**توضیح**: یکپارچه‌سازی با سیستم‌های خارجی

**زیرشیت‌ها** (5 sheet):
- `External_APIs` - API های خارجی
- `Webhooks` - وب‌هوک‌ها
- `Data_Sync` - همگام‌سازی داده
- `Third_Party_Services` - سرویس‌های شخص ثالث
- `Integration_Logs` - لاگ یکپارچه‌سازی

**اطلاعات اولیه**:
- 2 External API (Groq, Gemini)
- 1 Data Sync (local to sheets)
- 2 Third Party Service (Google Sheets, Telegram)
- 1 Integration Log

---

## 🚀 نحوه راه‌اندازی

### مرحله 1: ساخت اسپردشیت‌ها در Google Sheets

1. به Google Sheets بروید
2. **15 اسپردشیت جدید** بسازید با این نام‌ها:

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

3. **ID هر اسپردشیت** را یادداشت کنید (از URL)

---

### مرحله 2: دانلود Credentials

1. به [Google Cloud Console](https://console.cloud.google.com) بروید
2. یک پروژه جدید بسازید (یا از موجود استفاده کنید)
3. Google Sheets API را فعال کنید
4. یک Service Account بسازید
5. JSON credentials را دانلود کنید
6. فایل را با نام `credentials.json` در root پروژه قرار دهید
7. ایمیل service account را به تمام 15 اسپردشیت **Editor** access بدهید

---

### مرحله 3: تنظیم Config

فایل `config/config.json` را باز کنید و قسمت `google_sheets` را پر کنید:

```json
{
  "google_sheets": {
    "credentials_file": "credentials.json",
    "spreadsheets": {
      "CORE_DATA": "YOUR_SPREADSHEET_ID_1",
      "CONVERSATION_DATA": "YOUR_SPREADSHEET_ID_2",
      "KNOWLEDGE_BASE": "YOUR_SPREADSHEET_ID_3",
      "LEARNING_DATA": "YOUR_SPREADSHEET_ID_4",
      "CONTENT_LIBRARY": "YOUR_SPREADSHEET_ID_5",
      "ANALYTICS_DATA": "YOUR_SPREADSHEET_ID_6",
      "MEMORY_SYSTEM": "YOUR_SPREADSHEET_ID_7",
      "PERSONALITY_DATA": "YOUR_SPREADSHEET_ID_8",
      "TASK_MANAGEMENT": "YOUR_SPREADSHEET_ID_9",
      "SOCIAL_DATA": "YOUR_SPREADSHEET_ID_10",
      "SECURITY_LOGS": "YOUR_SPREADSHEET_ID_11",
      "BYTELINE_DATA": "YOUR_SPREADSHEET_ID_12",
      "RESEARCH_DATA": "YOUR_SPREADSHEET_ID_13",
      "AUTOMATION_DATA": "YOUR_SPREADSHEET_ID_14",
      "INTEGRATION_DATA": "YOUR_SPREADSHEET_ID_15"
    }
  }
}
```

---

### مرحله 4: اجرای Initialization

```bash
python initialize_sheets.py
```

این اسکریپت:
1. ✅ به Google Sheets متصل می‌شود
2. ✅ 15 اسپردشیت را بررسی می‌کند
3. ✅ 75+ شیت می‌سازد
4. ✅ Headers را اضافه می‌کند
5. ✅ اطلاعات اولیه را وارد می‌کند (200+ row)
6. ✅ تست امنیتی انجام می‌دهد

**زمان**: حدود 2-3 دقیقه

---

### مرحله 5: اجرای نازنین

```bash
python run_v4.py
```

حالا نازنین با سیستم Sheets کامل کار می‌کند!

---

## 📦 ماژول‌ها و ایجنت‌ها

### 6 ماژول تخصصی:

#### 1. SheetsMemoryModule
- ذخیره حافظه‌ها
- بازیابی حافظه‌ها
- مدیریت حافظه کوتاه‌مدت و بلندمدت

```python
await memory_module.store_memory('long_term', 'important fact', importance=0.9)
memories = await memory_module.retrieve_memories('query')
```

#### 2. SheetsLearningModule
- ثبت جلسات یادگیری
- ثبت بازخورد
- تحلیل پیشرفت

```python
await learning_module.log_learning_session('AI', 1000, 0.95)
await learning_module.log_feedback('user123', 5, 'عالی!')
```

#### 3. SheetsAnalyticsModule
- ثبت آمار روزانه
- تحلیل روندها
- گزارش‌های عملکرد

```python
await analytics_module.log_daily_stats(100, 50, 98, 0.5, 0.95)
summary = await analytics_module.get_stats_summary(days=7)
```

#### 4. SheetsContentModule
- ذخیره پست‌ها
- مدیریت قالب‌ها
- مدیریت محتوا

```python
await content_module.save_post('telegram', 'content', ['media_url'])
templates = await content_module.get_templates('news')
```

#### 5. SheetsSecurityModule
- ثبت لاگ دسترسی
- ثبت رویدادهای امنیتی
- ممیزی

```python
await security_module.log_access('user1', 'login', 'system', '1.2.3.4', 'success')
await security_module.log_security_event('login_attempt', 'info', 'successful login')
```

#### 6. SheetsKnowledgeModule
- اضافه کردن دانش
- جستجو در پایگاه دانش
- مدیریت حقایق

```python
await knowledge_module.add_fact('technology', 'AI fact', 'source', 0.95)
results = await knowledge_module.search_knowledge('AI')
```

---

### 6 ایجنت هوشمند:

#### 1. DataValidationAgent
- اعتبارسنجی داده‌ها
- تشخیص داده‌های ناقص
- گزارش مشکلات

```python
result = await validation_agent.validate_data('CORE_DATA', 'API_Keys')
```

#### 2. DataSyncAgent
- همگام‌سازی داده بین sheets
- تبدیل داده
- ثبت لاگ sync

```python
result = await sync_agent.sync_data(
    source=('SPREADSHEET1', 'Sheet1'),
    destination=('SPREADSHEET2', 'Sheet2')
)
```

#### 3. DataCleanupAgent
- پاکسازی داده‌های قدیمی
- بهینه‌سازی فضا
- آرشیو

```python
result = await cleanup_agent.cleanup_old_data('MEMORY_SYSTEM', 'Short_Term_Memory', days_old=7)
```

#### 4. DataBackupAgent
- پشتیبان‌گیری
- بازیابی
- مدیریت نسخه‌ها

```python
backup = await backup_agent.backup_spreadsheet('CORE_DATA')
```

#### 5. DataAnalysisAgent
- تحلیل الگوها
- تشخیص روندها
- پیش‌بینی

```python
analysis = await analysis_agent.analyze_usage_patterns()
```

#### 6. ReportGenerationAgent
- تولید گزارش روزانه
- تولید گزارش هفتگی
- تولید گزارش ماهانه

```python
report = await report_agent.generate_weekly_report()
```

---

## 💻 API و استفاده

### استفاده در کد نازنین:

```python
from nazanin.sheets_system import InitializationManager
from nazanin.sheets_system.sheets_modules import SheetsModuleManager
from nazanin.sheets_system.sheets_agents import SheetsAgentManager

# Initialization (فقط یکبار)
init_manager = InitializationManager(credentials_file, spreadsheet_ids)
result = await init_manager.initialize_all()

# استفاده از ماژول‌ها
module_manager = SheetsModuleManager(sheets_manager)

# ذخیره حافظه
await module_manager.memory.store_memory('long_term', 'important info')

# ثبت یادگیری
await module_manager.learning.log_feedback('user1', 5, 'excellent')

# ثبت آمار
await module_manager.analytics.log_daily_stats(100, 50, 98, 0.5, 0.95)

# استفاده از ایجنت‌ها
agent_manager = SheetsAgentManager(sheets_manager)

# اعتبارسنجی
validation = await agent_manager.validation.validate_data('CORE_DATA', 'API_Keys')

# گزارش
report = await agent_manager.report.generate_weekly_report()

# تسک‌های روزانه
daily_results = await agent_manager.run_daily_tasks()
```

---

## 🔧 عیب‌یابی

### مشکل: "Permission denied"

**راه حل**:
- ایمیل service account را به تمام اسپردشیت‌ها Editor access بدهید

---

### مشکل: "Spreadsheet not found"

**راه حل**:
- ID های اسپردشیت را دوباره چک کنید
- مطمئن شوید URL صحیح است

---

### مشکل: "Rate limit exceeded"

**راه حل**:
- سیستم خودکار delay دارد
- در صورت نیاز delay را افزایش دهید

---

### مشکل: "Credentials file not found"

**راه حل**:
- `credentials.json` را در root پروژه قرار دهید
- مسیر را در config چک کنید

---

## 📊 آمار و اطلاعات

```
📁 تعداد اسپردشیت‌ها: 15
📄 تعداد زیرشیت‌ها: 75
📦 تعداد ماژول‌ها: 6
🎯 تعداد ایجنت‌ها: 6
💾 اطلاعات اولیه: 200+ row
🔐 تست‌های امنیتی: 5
```

---

## ✅ چک‌لیست راه‌اندازی

- [ ] 15 اسپردشیت در Google Sheets ساخته شد
- [ ] ID های همه اسپردشیت‌ها یادداشت شد
- [ ] Service Account ساخته شد
- [ ] credentials.json دانلود شد
- [ ] Service Account به تمام اسپردشیت‌ها Editor access داده شد
- [ ] config.json پر شد با 15 ID
- [ ] `python initialize_sheets.py` اجرا شد
- [ ] تمام تست‌های امنیتی pass شد
- [ ] نازنین با موفقیت اجرا شد

---

**تمام شد!** 🎉

سیستم Google Sheets شما آماده است!

