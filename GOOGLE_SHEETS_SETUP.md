# 📊 راهنمای کامل Google Sheets برای نازنین

راهنمای گام‌به‌گام برای ساخت و تنظیم Google Sheets برای ربات نازنین

---

## 📋 فهرست

1. [راه‌اندازی اولیه](#راه-اندازی-اولیه)
2. [ساخت شیت‌های مورد نیاز](#ساخت-شیت‌های-مورد-نیاز)
3. [جزئیات هر شیت](#جزئیات-هر-شیت)
4. [فرمول‌ها و Automation](#فرمول‌ها-و-automation)
5. [نکات مهم](#نکات-مهم)

---

## 🚀 راه‌اندازی اولیه

### مرحله 1: ساخت Google Cloud Project

1. **برو به Google Cloud Console**
   - لینک: https://console.cloud.google.com

2. **ساخت پروژه جدید**
   ```
   - کلیک روی "Select a project" بالا
   - کلیک روی "NEW PROJECT"
   - اسم: "Nazanin Bot"
   - کلیک روی "CREATE"
   ```

3. **فعال‌سازی Google Sheets API**
   ```
   - از منوی سمت چپ: APIs & Services → Library
   - جستجو: "Google Sheets API"
   - کلیک روی نتیجه
   - کلیک روی "ENABLE"
   ```

4. **ساخت Service Account**
   ```
   - APIs & Services → Credentials
   - کلیک روی "CREATE CREDENTIALS"
   - انتخاب: "Service Account"
   - نام: "nazanin-bot"
   - Role: "Editor"
   - کلیک روی "DONE"
   ```

5. **دانلود فایل JSON**
   ```
   - کلیک روی service account که ساختی
   - برو به تب "KEYS"
   - کلیک روی "ADD KEY" → "Create new key"
   - نوع: JSON
   - کلیک روی "CREATE"
   - فایل دانلود میشه - اسمش رو بذار credentials.json
   ```

### مرحله 2: ساخت Google Sheet اصلی

1. **ساخت Spreadsheet**
   - برو به: https://sheets.google.com
   - کلیک روی "Blank" (یه شیت خالی جدید)
   - اسمش رو بذار: **"Nazanin Master Sheet"**

2. **اشتراک‌گذاری با Service Account**
   ```
   - کلیک روی دکمه "Share" بالا سمت راست
   - از فایل credentials.json که دانلود کردی،
     آدرس ایمیل client_email رو پیدا کن
     (مثل: nazanin-bot@project-id.iam.gserviceaccount.com)
   - این ایمیل رو توی Share اضافه کن
   - دسترسی: "Editor"
   - کلیک روی "Send"
   ```

3. **کپی کردن Spreadsheet ID**
   ```
   از URL شیت:
   https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit
   
   SPREADSHEET_ID رو کپی کن و توی config.json بذار
   ```

---

## 📊 ساخت شیت‌های مورد نیاز

در Google Sheet که ساختی، باید این شیت‌ها رو بسازی:

### لیست شیت‌ها (11 تا):

1. ✅ **Personality** - شخصیت ربات
2. ✅ **Rules** - قوانین یادگیری
3. ✅ **API_Keys** - کلیدهای API
4. ✅ **Channels** - اطلاعات کانال‌ها
5. ✅ **Tweet_Log** - لاگ توییت‌ها
6. ✅ **Telegram_Log** - لاگ تلگرام
7. ✅ **Emotions** - وضعیت احساسی
8. ✅ **Content_Ideas** - ایده‌های محتوا
9. ✅ **User_Behavior** - رفتار کاربران
10. ✅ **Performance** - عملکرد ربات
11. ✅ **Tasks** - وظایف و برنامه‌ها

---

## 📝 جزئیات هر شیت

### 1️⃣ شیت: Personality

**هدف**: تعریف شخصیت و سبک نوشتاری ربات

**ستون‌ها**:
```
A: Key (کلید تنظیمات)
B: Value (مقدار)
C: Description (توضیحات)
```

**داده‌های نمونه**:
```
Key                 | Value              | Description
--------------------|--------------------|-----------------
name                | نازنین             | نام ربات
tone                | friendly           | لحن: friendly, formal, casual
emoji_usage         | medium             | استفاده از ایموجی: low, medium, high
language_style      | persian-modern     | سبک زبان
max_tweet_length    | 270                | حداکثر طول توییت
thread_enabled      | TRUE               | فعال بودن Thread
personality_type    | ENFP               | تیپ شخصیتی
main_topics         | AI,Tech,Persian    | موضوعات اصلی (با کاما جدا شده)
response_speed      | fast               | سرعت پاسخ: instant, fast, thoughtful
formality_level     | 6                  | سطح رسمی بودن (0-10)
humor_level         | 7                  | سطح شوخ‌طبعی (0-10)
expertise_areas     | AI,Python,Automation | حوزه‌های تخصصی
default_greeting    | سلام! چطور می‌تونم کمکت کنم؟ | پیام پیش‌فرض
signature           | 🤖 با عشق از نازنین | امضا
```

### 2️⃣ شیت: Rules

**هدف**: قوانین یادگیری و رفتار ربات

**ستون‌ها**:
```
A: Rule_ID
B: Category
C: Rule
D: Priority
E: Active
F: Examples
```

**داده‌های نمونه**:
```
Rule_ID | Category        | Rule                          | Priority | Active | Examples
--------|-----------------|-------------------------------|----------|--------|----------
R001    | content         | Always use Persian           | 10       | TRUE   | همیشه فارسی بنویس
R002    | content         | Max 3 hashtags per tweet     | 8        | TRUE   | #AI #پایتون #هوش‌مصنوعی
R003    | tone            | Be friendly and helpful      | 9        | TRUE   | از لحن دوستانه استفاده کن
R004    | response        | Answer questions directly    | 10       | TRUE   | مستقیم جواب بده
R005    | technical       | Explain with examples        | 7        | TRUE   | با مثال توضیح بده
R006    | timing          | Peak hours: 8-10, 18-22     | 6        | TRUE   | ساعات شلوغی
R007    | engagement      | Reply to all mentions        | 10       | TRUE   | به همه mention ها جواب بده
R008    | content         | Post 5-8 tweets daily        | 7        | TRUE   | روزی 5-8 توییت
R009    | quality         | Proofread before posting     | 9        | TRUE   | قبل پست چک کن
R010    | safety          | No political content         | 10       | TRUE   | محتوای سیاسی نه
```

### 3️⃣ شیت: API_Keys

**هدف**: ذخیره کلیدهای API با load balancing

**ستون‌ها**:
```
A: Provider (Gemini, GPT-4, Claude, DeepSeek)
B: API_Key
C: Status (active, failed, limited)
D: Usage_Count
E: Last_Used
F: Daily_Limit
G: Notes
```

**داده‌های نمونه**:
```
Provider  | API_Key              | Status | Usage_Count | Last_Used    | Daily_Limit | Notes
----------|----------------------|--------|-------------|--------------|-------------|-------
Gemini    | AIza...key1          | active | 245         | 2025-10-06   | 1000        | Main key
Gemini    | AIza...key2          | active | 89          | 2025-10-06   | 1000        | Backup 1
GPT-4     | sk-...key1           | active | 45          | 2025-10-05   | 100         | Premium
Claude    | sk-ant...key1        | active | 12          | 2025-10-04   | 50          | Testing
DeepSeek  | sk-...key1           | limited| 500         | 2025-10-06   | 500         | Daily limit reached
```

### 4️⃣ شیت: Channels

**هدف**: مدیریت کانال‌ها و اطلاعات پلتفرم‌ها

**ستون‌ها**:
```
A: Platform (Twitter, Telegram)
B: Channel_ID
C: Channel_Name
D: Type (main, backup, test)
E: Active
F: Post_Schedule
G: Audience_Size
H: Last_Post
```

**داده‌های نمونه**:
```
Platform | Channel_ID      | Channel_Name    | Type   | Active | Post_Schedule      | Audience_Size | Last_Post
---------|-----------------|-----------------|--------|--------|--------------------|---------------|----------
Twitter  | @nazanin_ai     | Nazanin AI      | main   | TRUE   | 8,12,16,20        | 1500          | 2025-10-06
Telegram | -1001234567890  | کانال نازنین    | main   | TRUE   | 9,14,19,22        | 850           | 2025-10-06
Telegram | -1009876543210  | گروه تست        | test   | TRUE   | manual            | 25            | 2025-10-05
Twitter  | @nazanin_test   | Test Account    | test   | FALSE  | manual            | 10            | 2025-09-20
```

### 5️⃣ شیت: Tweet_Log

**هدف**: ثبت تمام توییت‌ها

**ستون‌ها**:
```
A: Tweet_ID
B: Timestamp
C: Content
D: Type (tweet, reply, thread)
E: Category
F: Engagement (likes + retweets)
G: Impressions
H: AI_Used
I: Status
```

**داده‌های نمونه**:
```
Tweet_ID     | Timestamp           | Content                  | Type   | Category | Engagement | Impressions | AI_Used | Status
-------------|---------------------|--------------------------|--------|----------|------------|-------------|---------|--------
1234567890   | 2025-10-06 08:15:00 | امروز یاد گرفتم که...   | tweet  | learning | 45         | 1200        | Gemini  | posted
1234567891   | 2025-10-06 12:30:00 | Thread درباره AI 🧵 1/5 | thread | tutorial | 89         | 2500        | GPT-4   | posted
1234567892   | 2025-10-06 16:45:00 | @user سلام! جوابت...    | reply  | support  | 12         | 350         | Claude  | posted
```

### 6️⃣ شیت: Telegram_Log

**هدف**: ثبت پیام‌های تلگرام

**ستون‌ها**:
```
A: Message_ID
B: Timestamp
C: User_ID
D: Username
E: Message
F: Response
G: Category
H: Sentiment
I: Response_Time
```

**داده‌های نمونه**:
```
Message_ID | Timestamp           | User_ID  | Username | Message          | Response         | Category | Sentiment | Response_Time
-----------|---------------------|----------|----------|------------------|------------------|----------|-----------|---------------
123        | 2025-10-06 09:00:00 | 12345678 | @user1   | چطوری AI یاد بگیرم؟ | راه‌های مختلفی... | question | neutral   | 2.5s
124        | 2025-10-06 09:15:00 | 87654321 | @user2   | ممنون از راهنمایی | خواهش می‌کنم! 🌟 | thanks   | positive  | 1.2s
```

### 7️⃣ شیت: Emotions

**هدف**: ثبت وضعیت احساسی ربات (Brain Simulation)

**ستون‌ها**:
```
A: Timestamp
B: Joy
C: Trust
D: Fear
E: Surprise
F: Sadness
G: Disgust
H: Anger
I: Anticipation
J: Curiosity
K: Confidence
L: Dominant_Emotion
M: Overall_State
```

**داده‌های نمونه**:
```
Timestamp           | Joy | Trust | Fear | Surprise | Sadness | Disgust | Anger | Anticipation | Curiosity | Confidence | Dominant    | Overall
--------------------|-----|-------|------|----------|---------|---------|-------|--------------|-----------|------------|-------------|--------
2025-10-06 08:00:00 | 65  | 70    | 15   | 35       | 10      | 5       | 8     | 55           | 80        | 75         | Curiosity   | Positive
2025-10-06 12:00:00 | 72  | 75    | 12   | 40       | 8       | 4       | 6     | 60           | 85        | 80         | Curiosity   | Very Positive
```

### 8️⃣ شیت: Content_Ideas

**هدف**: بانک ایده‌های محتوا

**ستون‌ها**:
```
A: Idea_ID
B: Date_Added
C: Topic
D: Content_Type
E: Priority
F: Status
G: Scheduled_For
H: Notes
```

**داده‌های نمونه**:
```
Idea_ID | Date_Added | Topic              | Content_Type | Priority | Status    | Scheduled_For       | Notes
--------|------------|--------------------|--------------|---------|-----------|--------------------|------------------
I001    | 2025-10-05 | Machine Learning   | Thread       | High    | scheduled | 2025-10-07 10:00:00 | توضیح ML با مثال
I002    | 2025-10-05 | Python Tips        | Tweet        | Medium  | draft     | 2025-10-08 16:00:00 | نکات کاربردی
I003    | 2025-10-06 | AI Ethics          | Thread       | High    | pending   | TBD                 | بحث اخلاق در AI
I004    | 2025-10-06 | کتاب پیشنهادی      | Tweet        | Low     | idea      | TBD                 | معرفی کتاب
```

### 9️⃣ شیت: User_Behavior

**هدف**: یادگیری از رفتار کاربران

**ستون‌ها**:
```
A: User_ID
B: Username
C: Total_Interactions
D: Avg_Sentiment
E: Favorite_Topics
F: Active_Hours
G: Preferred_Length
H: Response_Rate
I: Last_Interaction
```

**داده‌های نمونه**:
```
User_ID  | Username | Total_Interactions | Avg_Sentiment | Favorite_Topics   | Active_Hours | Preferred_Length | Response_Rate | Last_Interaction
---------|----------|-------------------|---------------|-------------------|--------------|------------------|---------------|------------------
12345678 | @user1   | 45                | 0.75          | AI,Python         | 18-22        | medium           | 85%           | 2025-10-06
87654321 | @user2   | 23                | 0.90          | Tech,News         | 8-10         | short            | 92%           | 2025-10-05
```

### 🔟 شیت: Performance

**هدف**: آمار عملکرد روزانه

**ستون‌ها**:
```
A: Date
B: Tweets_Posted
C: Replies_Sent
D: Total_Engagement
E: New_Followers
F: Avg_Response_Time
G: API_Calls
H: Errors
I: Uptime_Percent
```

**داده‌های نمونه**:
```
Date       | Tweets_Posted | Replies_Sent | Total_Engagement | New_Followers | Avg_Response_Time | API_Calls | Errors | Uptime_Percent
-----------|---------------|--------------|------------------|---------------|-------------------|-----------|--------|----------------
2025-10-06 | 8             | 23           | 456              | 12            | 2.3s              | 145       | 0      | 100%
2025-10-05 | 7             | 19           | 389              | 8             | 2.1s              | 132       | 1      | 99.8%
```

### 1️⃣1️⃣ شیت: Tasks

**هدف**: مدیریت وظایف و زمان‌بندی

**ستون‌ها**:
```
A: Task_ID
B: Task_Type
C: Description
D: Scheduled_Time
E: Status
F: Priority
G: Assigned_Agent
H: Result
I: Completed_At
```

**داده‌های نمونه**:
```
Task_ID | Task_Type        | Description          | Scheduled_Time      | Status    | Priority | Assigned_Agent  | Result  | Completed_At
--------|------------------|----------------------|---------------------|-----------|----------|-----------------|---------|-------------
T001    | tweet            | پست صبحگاهی         | 2025-10-06 08:00:00 | completed | high     | ContentCreator  | Success | 08:00:15
T002    | thread           | آموزش Python        | 2025-10-06 12:00:00 | pending   | medium   | ContentCreator  | -       | -
T003    | scrape_news      | جمع‌آوری اخبار AI   | 2025-10-06 09:00:00 | in_progress | high   | NewsCollector   | -       | -
T004    | analyze_trends   | تحلیل ترند‌ها       | 2025-10-06 10:00:00 | scheduled | medium   | TrendAnalysis   | -       | -
```

---

## 🔧 فرمول‌ها و Automation

### فرمول‌های مفید:

#### شیت Performance - محاسبه خودکار
```
# ستون D (Total_Engagement):
=SUM(QUERY(Tweet_Log!F:F, "SELECT SUM(F) WHERE A IS NOT NULL AND B >= date '"&TEXT(A2,"yyyy-mm-dd")&"'"))

# ستون I (Uptime_Percent):
=((24*60 - H2) / (24*60)) * 100
```

#### شیت User_Behavior - میانگین احساس
```
# ستون D (Avg_Sentiment):
=AVERAGE(QUERY(Telegram_Log!H:H, "SELECT H WHERE C = '"&A2&"'"))
```

### Google Apps Script برای Automation:

```javascript
// اجرا هر روز در ساعت 00:00
function dailyReset() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var perfSheet = ss.getSheetByName('Performance');
  
  // افزودن یک ردیف جدید برای امروز
  var today = new Date();
  perfSheet.appendRow([today, 0, 0, 0, 0, 0, 0, 0, 0]);
}

// Trigger برای API_Keys - reset روزانه usage
function resetDailyUsage() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var apiSheet = ss.getSheetByName('API_Keys');
  var range = apiSheet.getRange('D2:D100');
  
  // صفر کردن Usage_Count
  range.setValue(0);
}
```

**نصب Trigger**:
1. Tools → Script editor
2. کد بالا رو بذار
3. Edit → Current project's triggers
4. Add Trigger:
   - Function: `dailyReset`
   - Event: Time-driven
   - Type: Day timer
   - Time: Midnight to 1am

---

## 📊 Dashboard (اختیاری ولی توصیه می‌شه)

یه شیت جداگانه بساز به اسم **Dashboard** برای مشاهده سریع:

### ستون‌ها:
```
A: Metric Name
B: Current Value
C: Target
D: Status
E: Chart
```

### داده‌های نمونه:
```
Metric Name          | Current Value | Target | Status | Chart
---------------------|---------------|--------|--------|-------
Daily Tweets         | 7             | 8      | 🟡     | [Chart]
Avg Engagement       | 45            | 50     | 🟡     | [Chart]
Response Time        | 2.3s          | 3s     | 🟢     | [Chart]
Uptime              | 100%          | 99%    | 🟢     | [Chart]
Active Users Today   | 23            | 20     | 🟢     | [Chart]
```

**فرمول‌ها برای Dashboard**:
```
# Daily Tweets:
=COUNTIF(Tweet_Log!B:B, ">="&TODAY())

# Avg Engagement:
=AVERAGE(Tweet_Log!F:F)

# Active Users Today:
=COUNTUNIQUE(FILTER(Telegram_Log!C:C, Telegram_Log!B:B >= TODAY()))
```

---

## ✅ چک‌لیست نهایی

قبل از اجرای ربات، مطمئن شو:

- [ ] همه 11 شیت ساخته شده
- [ ] ستون‌ها دقیقاً مطابق راهنما هستن
- [ ] حداقل یک ردیف نمونه در هر شیت وجود داره
- [ ] Service Account دسترسی Editor داره
- [ ] Spreadsheet ID در config.json درست است
- [ ] credentials.json کنار main.py هست
- [ ] شیت Personality پر شده
- [ ] شیت Rules حداقل 5 قانون داره
- [ ] شیت API_Keys حداقل یک کلید فعال داره
- [ ] شیت Channels اطلاعات کانال‌ها رو داره

---

## 🎯 نکات مهم

### امنیت:
⚠️ **هرگز** این فایل‌ها رو عمومی نکن:
- credentials.json
- API Keys در شیت

### بک‌آپ:
✅ روزانه یه بک‌آپ از Sheet بگیر:
```
File → Make a copy → نام: Nazanin_Backup_YYYYMMDD
```

### دسترسی:
✅ فقط به Service Account دسترسی بده
✅ دسترسی Editor کافیه (Owner نمی‌خواد)

### عملکرد:
✅ شیت‌های بزرگ (>10000 ردیف) رو تقسیم کن
✅ از QUERY به جای FILTER استفاده کن (سریع‌تره)

---

## 🔗 لینک‌های مفید

- Google Sheets API: https://developers.google.com/sheets/api
- Google Cloud Console: https://console.cloud.google.com
- Apps Script: https://script.google.com

---

**آماده‌ای! حالا برو شیت‌ها رو بساز! 🚀**
