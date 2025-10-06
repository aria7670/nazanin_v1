# 🚦 راهنمای گام‌به‌گام کامل - از صفر تا اجرا

راهنمای جامع برای راه‌اندازی کامل ربات نازنین

---

## 📋 فهرست

1. [پیش‌نیازها](#پیش-نیازها)
2. [مرحله 1: تنظیمات Google](#مرحله-1-تنظیمات-google)
3. [مرحله 2: تنظیمات Twitter](#مرحله-2-تنظیمات-twitter)
4. [مرحله 3: تنظیمات Telegram](#مرحله-3-تنظیمات-telegram)
5. [مرحله 4: دانلود و نصب پروژه](#مرحله-4-دانلود-و-نصب-پروژه)
6. [مرحله 5: ساخت Google Sheets](#مرحله-5-ساخت-google-sheets)
7. [مرحله 6: تنظیم Config](#مرحله-6-تنظیم-config)
8. [مرحله 7: اجرا و تست](#مرحله-7-اجرا-و-تست)
9. [مرحله 8: نظارت و بهبود](#مرحله-8-نظارت-و-بهبود)

---

## ✅ پیش‌نیازها

### چیزهایی که باید داشته باشی:

- [ ] یک کامپیوتر با Python 3.8+ نصب شده
- [ ] اتصال به اینترنت
- [ ] یک حساب Gmail
- [ ] یک حساب Twitter (اختیاری)
- [ ] یک حساب Telegram (اختیاری)
- [ ] کارت اعتباری برای Google Cloud (اختیاری - نسخه رایگان کافیه)

### زمان مورد نیاز:
- ⏱️ نصب اولیه: **30-60 دقیقه**
- ⏱️ ساخت Sheets: **20-30 دقیقه**
- ⏱️ تنظیمات: **15-20 دقیقه**
- **⏱️ جمع کل: 1-2 ساعت**

---

## 🔧 مرحله 1: تنظیمات Google

### قدم 1.1: ساخت Google Cloud Project

1. **برو به Google Cloud Console**
   ```
   🔗 https://console.cloud.google.com
   ```

2. **ساخت پروژه جدید**
   - کلیک روی "Select a project" بالای صفحه
   - کلیک روی "NEW PROJECT"
   - نام پروژه: `Nazanin Bot`
   - Location: No organization
   - کلیک روی **CREATE**
   - ⏱️ صبر کن تا پروژه ساخته بشه (10-20 ثانیه)

3. **انتخاب پروژه**
   - مطمئن شو که "Nazanin Bot" انتخاب شده

### قدم 1.2: فعال‌سازی Google Sheets API

1. **رفتن به API Library**
   ```
   منوی سمت چپ → APIs & Services → Library
   ```

2. **جستجو و فعال‌سازی**
   - در کادر جستجو بنویس: `Google Sheets API`
   - کلیک روی نتیجه اول
   - کلیک روی دکمه آبی **ENABLE**
   - ⏱️ صبر کن تا فعال بشه (5-10 ثانیه)

### قدم 1.3: ساخت Service Account

1. **رفتن به Credentials**
   ```
   منوی سمت چپ → APIs & Services → Credentials
   ```

2. **ساخت Service Account**
   - کلیک روی **CREATE CREDENTIALS** بالا
   - انتخاب: **Service Account**
   
3. **تکمیل فرم**
   - **Service account name**: `nazanin-bot`
   - **Service account ID**: (خودکار پر میشه)
   - **Description**: `Nazanin AI Bot Service Account`
   - کلیک روی **CREATE AND CONTINUE**
   
4. **تعیین Role**
   - **Select a role**: Editor
   - کلیک روی **CONTINUE**
   - کلیک روی **DONE**

### قدم 1.4: دانلود فایل JSON

1. **پیدا کردن Service Account**
   - در صفحه Credentials
   - قسمت **Service Accounts**
   - پیدا کن: `nazanin-bot@...iam.gserviceaccount.com`

2. **ساخت Key**
   - کلیک روی آدرس ایمیل service account
   - برو به تب **KEYS**
   - کلیک روی **ADD KEY** → **Create new key**
   - نوع: **JSON**
   - کلیک روی **CREATE**

3. **ذخیره فایل**
   - فایل JSON دانلود میشه
   - **خیلی مهم**: اسمش رو بذار `credentials.json`
   - فعلاً یه جای امن نگهش دار

✅ **چک‌کن**: یه فایل `credentials.json` داری که شبیه اینه:
```json
{
  "type": "service_account",
  "project_id": "...",
  "private_key_id": "...",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...",
  "client_email": "nazanin-bot@....iam.gserviceaccount.com",
  ...
}
```

---

## 🐦 مرحله 2: تنظیمات Twitter

### قدم 2.1: ساخت Twitter Developer Account

1. **رفتن به Twitter Developer**
   ```
   🔗 https://developer.twitter.com
   ```

2. **Sign up**
   - کلیک روی **Sign up**
   - وارد شو با حساب Twitter خودت
   - تکمیل فرم (اطلاعات شخصی)

3. **توضیح Use Case**
   - **How will you use the Twitter API?**
     ```
     I'm building an AI-powered bot that posts educational content
     about AI, Python, and technology in Persian language.
     It will also respond to user mentions and questions.
     ```
   - **Will you make Twitter content available to a government entity?** → No
   - تیک زدن Terms
   - **Submit**

4. **تأیید ایمیل**
   - چک کن inbox ایمیلت
   - کلیک روی لینک تأیید

### قدم 2.2: ساخت App

1. **ساخت App جدید**
   - برو به Developer Portal Dashboard
   - کلیک روی **+ Create App**
   - نام: `Nazanin AI Bot`
   - **Complete**

2. **تنظیمات App**
   - **App permissions**: Read and Write
   - **Type of App**: Bot
   - **Save**

### قدم 2.3: دریافت API Keys

1. **Keys and Tokens**
   - در صفحه App
   - تب **Keys and tokens**

2. **API Key and Secret**
   - کلیک روی **Generate** (اگه نداری)
   - **کپی کن** و یه جا یادداشت کن:
     ```
     API Key: ...
     API Secret Key: ...
     ```

3. **Access Token and Secret**
   - کلیک روی **Generate** در قسمت Access Token
   - **کپی کن**:
     ```
     Access Token: ...
     Access Token Secret: ...
     ```

4. **Bearer Token**
   - کپی کن Bearer Token رو هم
     ```
     Bearer Token: ...
     ```

✅ **چک‌کن**: 5 تا کلید داری:
- ✅ API Key
- ✅ API Secret Key
- ✅ Access Token
- ✅ Access Token Secret
- ✅ Bearer Token

---

## 📱 مرحله 3: تنظیمات Telegram

### قدم 3.1: ساخت Bot با BotFather

1. **باز کردن Telegram**
   - در موبایل یا دسکتاپ

2. **جستجو برای BotFather**
   ```
   در Telegram جستجو کن: @BotFather
   ```

3. **ساخت Bot جدید**
   ```
   /newbot
   ```
   
4. **انتخاب نام**
   ```
   Bot Name: Nazanin AI
   Username: nazanin_ai_bot (باید با _bot تموم بشه)
   ```

5. **دریافت Token**
   - BotFather یه token میده
   - **کپی کن**:
     ```
     Bot Token: 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
     ```

### قدم 3.2: دریافت API ID و Hash

1. **رفتن به my.telegram.org**
   ```
   🔗 https://my.telegram.org
   ```

2. **ورود**
   - شماره موبایلت رو وارد کن
   - کد تأیید رو وارد کن

3. **API development tools**
   - کلیک روی **API development tools**

4. **ساخت Application**
   - App title: `Nazanin Bot`
   - Short name: `nazanin`
   - Platform: Other
   - **Create application**

5. **دریافت اطلاعات**
   - **کپی کن**:
     ```
     App api_id: 1234567
     App api_hash: abcdef1234567890abcdef1234567890
     ```

### قدم 3.3: ساخت کانال/گروه

1. **ساخت کانال**
   - در Telegram: New Channel
   - نام: `Nazanin Reports` (یا هر اسم دیگه)
   - نوع: Private یا Public (دلخواه)

2. **دریافت Channel ID**
   
   **روش 1 (ساده)**:
   ```
   - ربات @userinfobot رو به کانال اضافه کن
   - کانال ID رو بهت میده (مثل: -1001234567890)
   - ربات رو حذف کن
   ```
   
   **روش 2 (دستی)**:
   ```
   - بعد از اجرای ربات، یه پیام توی کانال بفرست
   - در log ها Channel ID رو می‌بینی
   ```

3. **افزودن Bot به کانال**
   - ربات نازنینت رو به کانال اضافه کن
   - Admin کن با دسترسی Post messages

### قدم 3.4: دریافت User ID خودت

1. **استفاده از userinfobot**
   ```
   در Telegram جستجو کن: @userinfobot
   /start
   ```
   
2. **دریافت ID**
   - بهت یه عدد میده (مثل: 123456789)
   - این Admin User ID توئه

✅ **چک‌کن**: این اطلاعات رو داری:
- ✅ Bot Token
- ✅ API ID
- ✅ API Hash
- ✅ Channel ID (با - شروع میشه)
- ✅ Admin User ID

---

## 💻 مرحله 4: دانلود و نصب پروژه

### قدم 4.1: دانلود پروژه

**روش 1: با Git**
```bash
# باز کردن Terminal/Command Prompt
git clone https://github.com/aria7670/nazanin_v1.git
cd nazanin_v1
```

**روش 2: دانلود ZIP**
```
1. برو به: https://github.com/aria7670/nazanin_v1
2. کلیک روی دکمه سبز "Code"
3. کلیک روی "Download ZIP"
4. Extract کن فایل ZIP
5. Terminal رو باز کن در پوشه extract شده
```

### قدم 4.2: ساخت Virtual Environment

```bash
# ساخت محیط مجازی
python3 -m venv venv

# فعال‌سازی

# Linux/macOS:
source venv/bin/activate

# Windows (PowerShell):
venv\Scripts\Activate.ps1

# Windows (CMD):
venv\Scripts\activate.bat
```

✅ **چک‌کن**: باید `(venv)` رو اول خط ببینی

### قدم 4.3: نصب Dependencies

```bash
# ارتقا pip
pip install --upgrade pip

# نصب کتابخانه‌ها
pip install -r requirements.txt
```

⏱️ **زمان**: 5-10 دقیقه (بسته به سرعت اینترنت)

✅ **چک‌کن**: نصب بدون error تموم بشه

### قدم 4.4: کپی فایل credentials.json

```bash
# فایل credentials.json که از Google دانلود کردی
# رو کپی کن به پوشه اصلی پروژه (کنار main.py)

# چک کردن
ls credentials.json  # باید فایل رو ببینی
```

---

## 📊 مرحله 5: ساخت Google Sheets

### قدم 5.1: ساخت Master Sheet

1. **باز کردن Google Sheets**
   ```
   🔗 https://sheets.google.com
   ```

2. **ساخت Spreadsheet جدید**
   - کلیک روی Blank (سفید خالی)
   - نام: `Nazanin Master Sheet`

3. **دریافت Spreadsheet ID**
   ```
   از URL کپی کن:
   https://docs.google.com/spreadsheets/d/SPREADSHEET_ID_HERE/edit
   
   فقط قسمت SPREADSHEET_ID_HERE رو کپی کن
   ```

4. **اشتراک‌گذاری با Service Account**
   - کلیک روی **Share** (گوشه بالا راست)
   - باز کن `credentials.json`
   - پیدا کن `client_email` (شبیه: nazanin-bot@....iam.gserviceaccount.com)
   - این ایمیل رو توی Share اضافه کن
   - دسترسی: **Editor**
   - **Send**

### قدم 5.2: ساخت 11 شیت

در Google Sheet که باز کردی، این 11 تا شیت رو بساز:

#### شیت 1: Personality

1. پایین صفحه، کلیک روی **+** (Add sheet)
2. نام: `Personality`
3. ستون‌ها (ردیف اول):
   ```
   A1: Key
   B1: Value
   C1: Description
   ```
4. داده‌های نمونه:
   ```
   A2: name          | B2: نازنین              | C2: نام ربات
   A3: tone          | B3: friendly            | C3: لحن
   A4: emoji_usage   | B4: medium              | C4: میزان استفاده ایموجی
   A5: language_style| B5: persian-modern      | C5: سبک زبان
   A6: personality_type | B6: ENFP             | C6: تیپ شخصیتی
   ```

#### شیت 2: Rules

1. **+ Add sheet** → نام: `Rules`
2. ستون‌ها:
   ```
   A1: Rule_ID
   B1: Category
   C1: Rule
   D1: Priority
   E1: Active
   F1: Examples
   ```
3. داده نمونه:
   ```
   A2: R001 | B2: content | C2: Always use Persian | D2: 10 | E2: TRUE | F2: همیشه فارسی
   A3: R002 | B3: tone    | C3: Be friendly        | D3: 9  | E3: TRUE | F3: دوستانه باش
   A4: R003 | B4: quality | C4: Proofread first    | D4: 9  | E4: TRUE | F4: قبل پست چک کن
   ```

#### شیت 3: API_Keys

1. **+ Add sheet** → نام: `API_Keys`
2. ستون‌ها:
   ```
   A1: Provider
   B1: API_Key
   C1: Status
   D1: Usage_Count
   E1: Last_Used
   F1: Daily_Limit
   G1: Notes
   ```
3. داده نمونه:
   ```
   A2: Gemini | B2: AIza...key1 | C2: active | D2: 0 | E2: 2025-10-06 | F2: 1000 | G2: Main key
   A3: GPT-4  | B3: sk-...key1  | C3: active | D3: 0 | E3: 2025-10-06 | F3: 100  | G3: Premium
   ```

#### شیت 4: Channels

1. **+ Add sheet** → نام: `Channels`
2. ستون‌ها:
   ```
   A1: Platform
   B1: Channel_ID
   C1: Channel_Name
   D1: Type
   E1: Active
   F1: Post_Schedule
   G1: Audience_Size
   H1: Last_Post
   ```
3. داده نمونه:
   ```
   A2: Twitter  | B2: @nazanin_ai | C2: Nazanin AI | D2: main | E2: TRUE | F2: 8,12,16,20 | G2: 0 | H2: -
   A3: Telegram | B3: -1001234... | C3: کانال نازنین | D3: main | E3: TRUE | F3: 9,14,19,22 | G3: 0 | H3: -
   ```

#### شیت‌های 5-11: (به همین ترتیب)

5. **Tweet_Log**: `Tweet_ID | Timestamp | Content | Type | Category | Engagement | Impressions | AI_Used | Status`

6. **Telegram_Log**: `Message_ID | Timestamp | User_ID | Username | Message | Response | Category | Sentiment | Response_Time`

7. **Emotions**: `Timestamp | Joy | Trust | Fear | Surprise | Sadness | Disgust | Anger | Anticipation | Curiosity | Confidence | Dominant | Overall`

8. **Content_Ideas**: `Idea_ID | Date_Added | Topic | Content_Type | Priority | Status | Scheduled_For | Notes`

9. **User_Behavior**: `User_ID | Username | Total_Interactions | Avg_Sentiment | Favorite_Topics | Active_Hours | Preferred_Length | Response_Rate | Last_Interaction`

10. **Performance**: `Date | Tweets_Posted | Replies_Sent | Total_Engagement | New_Followers | Avg_Response_Time | API_Calls | Errors | Uptime_Percent`

11. **Tasks**: `Task_ID | Task_Type | Description | Scheduled_Time | Status | Priority | Assigned_Agent | Result | Completed_At`

✅ **چک‌کن**: 11 تا شیت داری با ستون‌های درست

**💡 نکته**: برای جزئیات بیشتر هر شیت، فایل `GOOGLE_SHEETS_SETUP.md` رو ببین

---

## ⚙️ مرحله 6: تنظیم Config

### قدم 6.1: کپی فایل نمونه

```bash
cp config/config.example.json config/config.json
```

### قدم 6.2: ویرایش config.json

باز کن فایل `config/config.json` با یه text editor:

```bash
# Linux/macOS
nano config/config.json

# یا
code config/config.json  # اگه VS Code داری

# Windows
notepad config/config.json
```

### قدم 6.3: پر کردن اطلاعات

```json
{
  "telegram": {
    "bot_token": "توکن ربات از BotFather اینجا",
    "api_id": "API ID از my.telegram.org اینجا",
    "api_hash": "API Hash از my.telegram.org اینجا",
    "report_channel_id": "Channel ID اینجا (مثل: -1001234567890)",
    "admin_user_id": "User ID خودت اینجا (مثل: 123456789)"
  },
  "twitter": {
    "api_key": "Twitter API Key اینجا",
    "api_secret": "Twitter API Secret اینجا",
    "access_token": "Twitter Access Token اینجا",
    "access_secret": "Twitter Access Secret اینجا",
    "bearer_token": "Twitter Bearer Token اینجا"
  },
  "google_sheets": {
    "credentials_file": "credentials.json",
    "master_spreadsheet_id": "Spreadsheet ID از Google Sheets اینجا"
  },
  "brain_simulation": {
    "enabled": true,
    "emotion_update_interval": 300,
    "cognition_depth": 5,
    "memory_capacity": 10000
  },
  "quantum_agent": {
    "enabled": true,
    "quantum_states": 64,
    "entanglement_enabled": true,
    "superposition_layers": 3
  },
  "neural_agent": {
    "enabled": true,
    "hidden_layers": [512, 256, 128],
    "activation": "relu",
    "learning_rate": 0.001
  }
}
```

✅ **چک‌کن**: همه فیلدها پر شدن

---

## 🚀 مرحله 7: اجرا و تست

### قدم 7.1: تست اولیه

```bash
# مطمئن شو venv فعاله
source venv/bin/activate  # Linux/macOS

# تست import ها
python tests/test_basic.py
```

✅ **انتظار**: باید Config رو بخونه (حتی اگه API ها کار نکنن)

### قدم 7.2: اجرای Demo

```bash
# Demo سیستم‌های AI (بدون نیاز به API)
python tests/demo.py
```

✅ **انتظار**: باید Brain, Quantum, Neural رو ببینی

### قدم 7.3: اجرای اصلی (نسخه ساده)

```bash
python main.py
```

✅ **انتظار**:
```
🚀 Starting Nazanin Bot...
✅ Config loaded
✅ Sheets Manager initialized
✅ API Manager initialized
✅ Agents initialized
✅ Brain Simulation initialized
✅ Quantum Agent initialized
✅ Neural Agent initialized
🌟 Nazanin is running!
```

### قدم 7.4: اجرای نسخه پیشرفته

```bash
# Ctrl+C برای متوقف کردن main.py

python main_advanced.py
```

✅ **انتظار**: همه 16 ایجنت initialize بشن

### قدم 7.5: تست با Telegram

1. **باز کن ربات توی Telegram**
   ```
   جستجو: @nazanin_ai_bot (یا هر اسمی که دادی)
   /start
   ```

2. **دستورات رو تست کن**
   ```
   /status
   /stats
   ```

✅ **انتظار**: ربات جواب بده

---

## 📊 مرحله 8: نظارت و بهبود

### قدم 8.1: چک کردن Logs

```bash
# مشاهده log فایل
tail -f nazanin.log

# یا اگه systemd استفاده می‌کنی
journalctl -u nazanin -f
```

### قدم 8.2: چک کردن Google Sheets

1. باز کن Master Sheet
2. چک کن شیت‌های Log:
   - Tweet_Log
   - Telegram_Log
   - Performance
   - Emotions

✅ **انتظار**: داده‌ها اتوماتیک ثبت بشن

### قدم 8.3: مانیتورینگ Performance

```bash
# استفاده از htop
htop

# یا top
top

# چک کردن Memory
free -h

# چک کردن Disk
df -h
```

### قدم 8.4: Backup روزانه

```bash
# اضافه کردن به crontab
crontab -e

# اضافه کن این خط:
0 2 * * * /path/to/nazanin_v1/backup.sh
```

---

## ✅ چک‌لیست نهایی

قبل از استفاده واقعی، چک کن:

### Google:
- [ ] Google Cloud Project ساخته شده
- [ ] Google Sheets API فعال شده
- [ ] Service Account ساخته شده
- [ ] credentials.json دانلود شده
- [ ] Master Sheet ساخته شده
- [ ] 11 شیت با ستون‌های صحیح
- [ ] Service Account دسترسی Editor داره
- [ ] Spreadsheet ID کپی شده

### Twitter:
- [ ] Developer Account ساخته شده
- [ ] App ساخته شده
- [ ] API Keys دریافت شده (5 تا)
- [ ] Permissions: Read and Write

### Telegram:
- [ ] Bot ساخته شده با BotFather
- [ ] Bot Token دریافت شده
- [ ] API ID و Hash دریافت شده
- [ ] کانال ساخته شده
- [ ] Channel ID دریافت شده
- [ ] Bot به کانال اضافه شده (Admin)
- [ ] User ID دریافت شده

### پروژه:
- [ ] پروژه دانلود شده
- [ ] Virtual environment ساخته شده
- [ ] Dependencies نصب شده
- [ ] credentials.json کپی شده
- [ ] config.json پر شده
- [ ] تست‌ها OK شدن
- [ ] ربات اجرا شد بدون error

---

## 🎯 مراحل بعدی

حالا که همه چیز آماده‌ست:

### 1. **شخصی‌سازی**
   - شیت Personality رو ویرایش کن
   - قوانین دلخواهت رو اضافه کن
   - تمپلت‌های خودت رو بساز

### 2. **تست و یادگیری**
   - چند روز اول ربات رو مانیتور کن
   - ببین چطور یاد می‌گیره
   - performance رو بررسی کن

### 3. **بهینه‌سازی**
   - بر اساس آمار، تنظیمات رو بهبود بده
   - الگوریتم‌ها رو tune کن
   - محتوا رو optimize کن

### 4. **Scale Up**
   - اگه خوب کار کرد، deploy کن روی VPS
   - Docker استفاده کن
   - Monitoring حرفه‌ای اضافه کن

---

## 🆘 مشکلات متداول

### مشکل: "No module named 'src'"
```bash
# چک کن که در پوشه اصلی هستی
pwd

# چک کن venv فعاله
source venv/bin/activate
```

### مشکل: "credentials.json not found"
```bash
# مطمئن شو فایل کنار main.py هست
ls credentials.json

# اگه نیست، کپی کن
cp /path/to/downloaded/credentials.json .
```

### مشکل: "Permission denied" در Google Sheets
```bash
# مطمئن شو service account email رو share کردی
# با دسترسی Editor
```

### مشکل: Twitter API rate limit
```bash
# صبر کن 15 دقیقه
# یا یه API Key دیگه اضافه کن به شیت API_Keys
```

---

## 📚 مستندات بیشتر

- 📖 `GOOGLE_SHEETS_SETUP.md` - جزئیات کامل Sheets
- 📖 `HOW_NAZANIN_WORKS.md` - نحوه کار دقیق
- 📖 `DOWNLOAD_AND_RUN.md` - راهنمای دانلود
- 📖 `docs/DEPLOYMENT.md` - راهنمای Deploy
- 📖 `README.md` - معرفی کلی

---

## 🎉 موفق باشی!

اگه تا اینجا اومدی، یعنی نازنین الان در حال اجراست! 🚀

**برای سوالات**:
- 🐛 GitHub Issues
- 💬 Telegram Support
- 📧 Email

**بهترین آرزوها برات! ❤️**
