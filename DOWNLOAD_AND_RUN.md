# 🚀 راهنمای دانلود و اجرا روی لپتاپ

راهنمای کامل برای دانلود، نصب و اجرای ربات نازنین روی سیستم شخصی

---

## 📦 دانلود پروژه

### روش 1: با Git (پیشنهادی)

```bash
# 1. دانلود پروژه
git clone https://github.com/aria7670/nazanin_v1.git

# 2. ورود به پوشه
cd nazanin_v1

# 3. چک کردن فایل‌ها
ls -la
```

### روش 2: دانلود ZIP

1. برو به: https://github.com/aria7670/nazanin_v1
2. کلیک کن روی دکمه سبز **Code**
3. کلیک کن روی **Download ZIP**
4. فایل رو Extract کن
5. ترمینال رو باز کن توی پوشه extract شده

---

## ⚙️ نیازمندی‌ها

### چیزهایی که باید نصب باشه:

#### ✅ Python 3.8+
```bash
# چک کردن نسخه Python
python3 --version

# اگه نصب نبود:
# Ubuntu/Debian:
sudo apt update && sudo apt install python3 python3-pip python3-venv

# macOS (با Homebrew):
brew install python3

# Windows:
# دانلود از python.org
```

#### ✅ Git (اختیاری)
```bash
# Ubuntu/Debian:
sudo apt install git

# macOS:
brew install git

# Windows:
# دانلود از git-scm.com
```

---

## 🔧 نصب و راه‌اندازی

### روش 1: با اسکریپت خودکار (آسان‌ترین)

```bash
# اجرای اسکریپت نصب
bash run.sh
```

این اسکریپت همه چیز رو خودکار انجام میده:
- ✅ ساخت virtual environment
- ✅ نصب dependencies
- ✅ کپی کردن config
- ✅ پرسیدن کدوم نسخه رو می‌خوای اجرا کنی

---

### روش 2: نصب دستی (گام به گام)

#### 1️⃣ ساخت Virtual Environment

```bash
# ساخت محیط مجازی
python3 -m venv venv

# فعال کردن محیط مجازی

# Linux/macOS:
source venv/bin/activate

# Windows (PowerShell):
venv\Scripts\Activate.ps1

# Windows (CMD):
venv\Scripts\activate.bat
```

بعد از activate شدن، باید `(venv)` رو اول خط ببینی.

#### 2️⃣ نصب Dependencies

```bash
# ارتقا pip
pip install --upgrade pip

# نصب همه کتابخانه‌ها
pip install -r requirements.txt
```

**⏰ زمان نصب**: 5-10 دقیقه (بستگی به سرعت اینترنت)

#### 3️⃣ تنظیم Config

```bash
# کپی کردن فایل نمونه
cp config/config.example.json config/config.json

# ویرایش config
# Linux/macOS:
nano config/config.json
# یا
vim config/config.json
# یا
code config/config.json  # اگه VS Code داری

# Windows:
notepad config/config.json
```

#### 4️⃣ پر کردن API Keys

فایل `config/config.json` رو ویرایش کن و اطلاعات زیر رو پر کن:

```json
{
  "telegram": {
    "bot_token": "توکن ربات تلگرام از @BotFather",
    "api_id": "API ID از my.telegram.org",
    "api_hash": "API Hash از my.telegram.org",
    "report_channel_id": "آیدی کانال گزارش",
    "admin_user_id": "آیدی عددی خودت"
  },
  "twitter": {
    "api_key": "کلید API از developer.twitter.com",
    "api_secret": "سکرت API",
    "access_token": "توکن دسترسی",
    "access_secret": "سکرت توکن",
    "bearer_token": "توکن Bearer"
  },
  "google_sheets": {
    "credentials_file": "credentials.json",
    "master_spreadsheet_id": "آیدی گوگل شیت"
  }
}
```

#### 5️⃣ Google Sheets Credentials

برای استفاده از Google Sheets:

1. برو به: https://console.cloud.google.com
2. یه پروژه جدید بساز
3. Google Sheets API رو فعال کن
4. Service Account بساز
5. فایل JSON رو دانلود کن
6. اسمش رو بذار `credentials.json` و کنار `main.py` بذارش

---

## 🚀 اجرا

### قبل از اجرا - تست سریع

```bash
# تست کردن که همه چیز درست نصب شده
python tests/test_basic.py
```

### اجرای ربات

#### نسخه پیشرفته (پیشنهادی)

```bash
python main_advanced.py
```

این نسخه شامل:
- ✅ همه 16 ایجنت
- ✅ Brain Simulation
- ✅ Quantum & Neural Agents
- ✅ سیستم‌های یادگیری
- ✅ تمام ویژگی‌های پیشرفته

#### نسخه ساده

```bash
python main.py
```

این نسخه شامل:
- ✅ 6 ایجنت پایه
- ✅ Twitter & Telegram
- ✅ Brain, Quantum, Neural Systems

---

## 🐳 اجرا با Docker (اختیاری)

اگه Docker داری:

```bash
# 1. Build کردن image
docker build -t nazanin-bot .

# یا اجرا با docker-compose
docker-compose up -d

# مشاهده logs
docker-compose logs -f

# متوقف کردن
docker-compose down
```

---

## 🛠️ استفاده از Makefile

اگه `make` داری (Linux/macOS):

```bash
# مشاهده همه دستورات
make help

# نصب کامل
make setup

# اجرا
make run-advanced

# تست
make test

# Docker
make docker-build
make docker-run
```

---

## 🧪 تست کردن

### 1. تست Import ها

```bash
python -c "from src.core import SheetsManager; print('✅ OK')"
python -c "from src.ai import BrainSimulation; print('✅ OK')"
```

### 2. اجرای Demo

```bash
# Demo سیستم‌های AI
python tests/demo.py

# Demo کامل
python tests/demo_advanced.py
```

### 3. تست کامل

```bash
python tests/test_basic.py
```

---

## 🔍 حل مشکلات رایج

### مشکل 1: `ModuleNotFoundError`

```bash
# اطمینان از activate بودن venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# نصب مجدد
pip install -r requirements.txt
```

### مشکل 2: `No module named 'src'`

```bash
# چک کردن که توی پوشه اصلی هستی
pwd  # باید nazanin_v1 رو نشون بده

# اطمینان از وجود src/
ls -la src/
```

### مشکل 3: خطای `config.json not found`

```bash
# کپی کردن config
cp config/config.example.json config/config.json

# چک کردن مسیر
ls -la config/
```

### مشکل 4: خطای Permission در run.sh

```bash
# اجازه اجرا دادن
chmod +x run.sh

# اجرا
bash run.sh
```

### مشکل 5: نصب PyTorch خیلی طول میکشه

```bash
# نصب نسخه CPU (سریع‌تر)
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

---

## 📁 ساختار پوشه‌ها

بعد از دانلود باید این ساختار رو ببینی:

```
nazanin_v1/
├── src/              ← کدهای اصلی
├── docs/             ← مستندات
├── tests/            ← تست‌ها
├── config/           ← تنظیمات
├── main.py           ← اجرای ساده
├── main_advanced.py  ← اجرای پیشرفته
├── run.sh            ← اسکریپت نصب
├── requirements.txt  ← لیست کتابخانه‌ها
└── README.md         ← راهنما
```

---

## 💡 نکات مهم

### ✅ قبل از اجرا:

1. ✅ Python 3.8+ نصب باشه
2. ✅ Virtual environment بسازی
3. ✅ Dependencies نصب کنی
4. ✅ config.json رو پر کنی
5. ✅ credentials.json رو بذاری (برای Google Sheets)

### ✅ حین اجرا:

1. ✅ همیشه venv رو activate کن
2. ✅ از پوشه اصلی پروژه اجرا کن
3. ✅ log ها رو چک کن

### ✅ امنیت:

1. ⚠️ **هرگز** `config.json` رو commit نکن
2. ⚠️ **هرگز** API keys رو share نکن
3. ⚠️ از `.env` یا `config.json` استفاده کن

---

## 🎯 مراحل دقیق (خلاصه)

```bash
# 1. دانلود
git clone https://github.com/aria7670/nazanin_v1.git
cd nazanin_v1

# 2. Virtual Environment
python3 -m venv venv
source venv/bin/activate  # Linux/macOS

# 3. نصب
pip install -r requirements.txt

# 4. Config
cp config/config.example.json config/config.json
nano config/config.json  # پر کن API keys رو

# 5. اجرا
python main_advanced.py
```

---

## 📞 کمک بیشتر

### مستندات:
- 📖 `docs/START_HERE.md` - شروع
- 📖 `docs/QUICKSTART.md` - شروع سریع
- 📖 `docs/INSTALLATION.md` - نصب کامل
- 📖 `README.md` - راهنمای اصلی

### مشکلات:
- 🐛 GitHub Issues: https://github.com/aria7670/nazanin_v1/issues
- 💬 Discussions: https://github.com/aria7670/nazanin_v1/discussions

### ویدیو (اگه بخوای بسازم):
```bash
# نمایش همه دستورات با توضیح
make help
```

---

## ✅ چک‌لیست نهایی

قبل از اجرا این‌ها رو چک کن:

- [ ] Python 3.8+ نصب شده
- [ ] پروژه دانلود شده
- [ ] Virtual environment ساخته شده
- [ ] Dependencies نصب شده (62 فایل روی git)
- [ ] config/config.json ساخته شده
- [ ] API keys پر شده
- [ ] credentials.json آماده (اگه از Sheets استفاده میکنی)
- [ ] تست‌ها اجرا شده و OK
- [ ] venv فعال است

---

**الان آماده‌ای! 🚀**

```bash
python main_advanced.py
```

**موفق باشی! 🎉**
