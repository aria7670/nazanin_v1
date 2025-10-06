# نصب و راه‌اندازی نازنین

## پیش‌نیازها

### 1. نصب Python 3.8+
```bash
python --version  # باید 3.8 یا بالاتر باشد
```

### 2. نصب پکیج‌های مورد نیاز
```bash
pip install -r requirements.txt
```

## تنظیمات اولیه

### 1. Google Sheets API

1. به [Google Cloud Console](https://console.cloud.google.com/) بروید
2. یک پروژه جدید بسازید
3. Google Sheets API را فعال کنید
4. یک Service Account بسازید
5. کلید JSON را دانلود کنید و به نام `credentials.json` ذخیره کنید

### 2. Twitter API

1. به [Twitter Developer Portal](https://developer.twitter.com/) بروید
2. یک اپلیکیشن بسازید
3. API keys و tokens را دریافت کنید:
   - API Key
   - API Secret
   - Access Token
   - Access Token Secret
   - Bearer Token

### 3. Telegram Bot

1. با [@BotFather](https://t.me/botfather) در تلگرام چت کنید
2. دستور `/newbot` را بزنید
3. Bot Token را دریافت کنید
4. API ID و API Hash از [my.telegram.org](https://my.telegram.org) بگیرید

### 4. تنظیم config.json

فایل `config.json` را ویرایش کنید:

```json
{
  "telegram": {
    "bot_token": "YOUR_BOT_TOKEN",
    "api_id": "YOUR_API_ID",
    "api_hash": "YOUR_API_HASH",
    "report_channel_id": "YOUR_REPORT_CHANNEL_ID",
    "admin_user_id": "YOUR_USER_ID"
  },
  "twitter": {
    "api_key": "YOUR_API_KEY",
    "api_secret": "YOUR_API_SECRET",
    "access_token": "YOUR_ACCESS_TOKEN",
    "access_secret": "YOUR_ACCESS_SECRET",
    "bearer_token": "YOUR_BEARER_TOKEN"
  },
  "google_sheets": {
    "credentials_file": "credentials.json",
    "master_spreadsheet_id": "YOUR_SPREADSHEET_ID"
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

## ساختار Google Sheets

### شیت‌های مورد نیاز:

1. **کانال_اطلاعات**
   - ستون‌ها: کلید | مقدار

2. **شخصیت**
   - ستون‌ها: ویژگی | توضیحات

3. **خودمختاری**
   - ستون‌ها: نوع_کار | قانون | اولویت

4. **یادگیری_قوانین**
   - ستون‌ها: عنوان | قانون | دسته

5. **پست_دسته_بندی**
   - ستون‌ها: تاریخ_زمان | پلتفرم | محتوا | دسته | post_id | metrics

6. **احساسات**
   - ستون‌ها: احساس | امتیاز | آخرین_بروزرسانی

7. **API_Keys**
   - ستون‌ها: نام | کلید | وضعیت | تاریخ_اضافه | یادداشت

## اجرای سیستم

### روش 1: اجرای مستقیم
```bash
python main.py
```

### روش 2: در پس‌زمینه با screen
```bash
screen -S nazanin
python main.py
# برای خروج: Ctrl+A, D
# برای بازگشت: screen -r nazanin
```

### روش 3: با systemd (برای سرور)

فایل `/etc/systemd/system/nazanin.service` بسازید:

```ini
[Unit]
Description=Nazanin AI Bot
After=network.target

[Service]
Type=simple
User=YOUR_USER
WorkingDirectory=/path/to/nazanin
ExecStart=/usr/bin/python3 main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

سپس:
```bash
sudo systemctl enable nazanin
sudo systemctl start nazanin
sudo systemctl status nazanin
```

## دستورات تلگرام

بعد از راه‌اندازی، این دستورات در ربات تلگرام موجود است:

- `/start` - شروع
- `/status` - وضعیت سیستم
- `/stats` - آمار ایجنت‌ها
- `/post [متن]` - ارسال پست دستی
- `/tasks` - لیست کارها
- `/reload` - بارگذاری مجدد تنظیمات

## عیب‌یابی

### خطا: Google Sheets credentials
```bash
# مطمئن شوید credentials.json در همان مسیر است
ls credentials.json
```

### خطا: Twitter API
```bash
# توکن‌های Twitter را چک کنید
# مطمئن شوید اپ شما Elevated access دارد
```

### خطا: Telegram connection
```bash
# API ID و Hash را چک کنید
# مطمئن شوید Bot Token درست است
```

### خطا: Missing packages
```bash
# نصب مجدد پکیج‌ها
pip install -r requirements.txt --upgrade
```

## لاگ‌ها

لاگ‌های سیستم در فایل `nazanin.log` ذخیره می‌شوند:

```bash
tail -f nazanin.log  # مشاهده لاگ‌های زنده
```

## توصیه‌های امنیتی

1. ❗ هیچ‌وقت `config.json` را commit نکنید
2. ❗ از `.gitignore` استفاده کنید
3. ❗ کلیدهای API را در متغیرهای محیطی ذخیره کنید
4. ❗ دسترسی به Google Sheets را محدود کنید
5. ❗ به طور منظم کلیدها را بازنشانی کنید

## پشتیبانی

برای مشکلات و سوالات:
- لاگ‌ها را چک کنید: `nazanin.log`
- دستور `/status` را در تلگرام بزنید
- README.md اصلی را مطالعه کنید
