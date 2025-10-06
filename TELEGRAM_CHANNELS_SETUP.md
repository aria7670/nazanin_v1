# 📱 راهنمای کامل کانال‌ها و گروه‌های تلگرام

راهنمای ساخت و تنظیم کانال‌ها و گروه‌های مورد نیاز نازنین

---

## 🎯 کانال‌ها و گروه‌های مورد نیاز

نازنین به **5 کانال** و **3 گروه** نیاز داره:

### 📢 کانال‌ها (Channels):

1. **Report Channel** - گزارش‌های ربات
2. **Storage Channel** - ذخیره‌سازی فایل‌ها
3. **Backup Channel** - بک‌آپ اطلاعات
4. **News Archive** - آرشیو اخبار جمع‌آوری شده
5. **Media Storage** - ذخیره رسانه (عکس، ویدیو)

### 👥 گروه‌ها (Groups):

1. **Admin Group** - مدیریت و کنترل
2. **Testing Group** - تست ویژگی‌ها
3. **Users Group** - تعامل با کاربران (اختیاری)

---

## 📢 ساخت کانال‌ها

### 1️⃣ Report Channel

**هدف**: دریافت گزارش‌های روزانه، آمار، و اعلان‌های مهم

**مراحل ساخت:**

1. در Telegram: **New Channel**
2. اسم: `Nazanin Reports` (یا هر اسم دلخواه)
3. توضیحات: `گزارش‌های خودکار ربات نازنین`
4. نوع: **Private** (توصیه می‌شه)
5. **Create**

**تنظیمات:**
- Subscribers: فقط خودت
- History for new members: Hidden
- Sign messages: No

**استفاده:**
```
- گزارش روزانه عملکرد
- اعلان خطاها
- آمار engagement
- هشدارهای امنیتی
```

---

### 2️⃣ Storage Channel

**هدف**: ذخیره‌سازی فایل‌ها، عکس‌ها، و داده‌ها

**مراحل ساخت:**

1. **New Channel**
2. اسم: `Nazanin Storage`
3. توضیحات: `ذخیره‌سازی فایل‌های ربات`
4. نوع: **Private**
5. **Create**

**استفاده:**
```
- ذخیره تصاویر تولید شده
- فایل‌های JSON
- فایل‌های backup کوچک
- لاگ فایل‌ها
```

**نکته**: Telegram تا 2GB فایل رایگان ذخیره می‌کنه!

---

### 3️⃣ Backup Channel

**هدف**: بک‌آپ روزانه اطلاعات مهم

**مراحل ساخت:**

1. **New Channel**
2. اسم: `Nazanin Backups`
3. توضیحات: `بک‌آپ خودکار روزانه`
4. نوع: **Private**
5. **Create**

**استفاده:**
```
- بک‌آپ روزانه database
- بک‌آپ config
- بک‌آپ مدل‌های ML
- نقاط بازگردانی
```

---

### 4️⃣ News Archive

**هدف**: آرشیو اخبار جمع‌آوری شده

**مراحل ساخت:**

1. **New Channel**
2. اسم: `Nazanin News Archive`
3. توضیحات: `آرشیو اخبار AI و تکنولوژی`
4. نوع: **Private** یا **Public** (دلخواه)
5. **Create**

**استفاده:**
```
- ذخیره اخبار scrape شده
- آرشیو مقالات مهم
- ترندهای روز
- منابع برای محتوا
```

---

### 5️⃣ Media Storage

**هدف**: ذخیره رسانه‌های چندرسانه‌ای

**مراحل ساخت:**

1. **New Channel**
2. اسم: `Nazanin Media`
3. توضیحات: `ذخیره‌ فایل‌های رسانه‌ای`
4. نوع: **Private**
5. **Create**

**استفاده:**
```
- عکس‌های تولید شده
- ویدیوهای کوتاه
- GIF ها
- اینفوگرافیک‌ها
```

---

## 👥 ساخت گروه‌ها

### 1️⃣ Admin Group

**هدف**: کنترل و مدیریت ربات

**مراحل ساخت:**

1. **New Group**
2. اسم: `Nazanin Admin`
3. اضافه کردن اعضا: فقط خودت (و دیگه ادمین‌ها اگه هستن)
4. **Create**

**اضافه کردن ربات:**
1. در گروه: Add Members
2. جستجو: `@nazanin_ai_bot` (یا اسم رباتت)
3. اضافه کن و **Admin** کن

**تنظیمات Admin:**
```
✅ Change Group Info
✅ Delete Messages
✅ Ban Users
✅ Invite Users
✅ Pin Messages
✅ Add Admins
```

**دستورات ادمین:**
```
/start - شروع ربات
/status - وضعیت فعلی
/stats - آمار
/reload - بارگذاری مجدد
/backup - بک‌آپ دستی
/task add <task> - افزودن وظیفه
/task list - لیست وظایف
/api status - وضعیت API ها
/users stats - آمار کاربران
```

---

### 2️⃣ Testing Group

**هدف**: تست ویژگی‌های جدید

**مراحل ساخت:**

1. **New Group**
2. اسم: `Nazanin Testing`
3. اعضا: خودت + ربات
4. **Create**

**استفاده:**
```
- تست دستورات جدید
- تست پاسخ‌ها
- تست فرمت‌های مختلف
- Debug کردن
```

---

### 3️⃣ Users Group (اختیاری)

**هدف**: تعامل عمومی با کاربران

**مراحل ساخت:**

1. **New Group**
2. اسم: `Nazanin Community`
3. نوع: **Public** یا **Private**
4. **Create**

**تنظیمات:**
```
- Slow Mode: 30s
- Permissions:
  ✅ Send Messages
  ✅ Send Media
  ❌ Add Users (فقط ادمین)
  ❌ Pin Messages
```

**استفاده:**
```
- پاسخ به سوالات کاربران
- دریافت feedback
- اطلاع‌رسانی‌های عمومی
- Community building
```

---

## 🔑 دریافت Channel/Group ID

### روش 1: با @userinfobot

1. ربات @userinfobot رو به کانال/گروه اضافه کن
2. یه پیام بفرست
3. ID رو بهت میده (مثل: `-1001234567890`)
4. ربات رو حذف کن

### روش 2: با @getidsbot

1. پیام forward کن از کانال/گروه به @getidsbot
2. ID رو بهت میده

### روش 3: با کد Python

```python
from telethon import TelegramClient

async with TelegramClient('session', api_id, api_hash) as client:
    # برای کانال
    channel = await client.get_entity('nazanin_storage')
    print(f"Channel ID: {channel.id}")
    
    # برای گروه
    group = await client.get_entity('Nazanin Admin')
    print(f"Group ID: {group.id}")
```

---

## ⚙️ تنظیم در Config

بعد از ساخت همه کانال‌ها و گروه‌ها، در `config.json`:

```json
{
  "telegram": {
    "channels": {
      "report": "-1001234567890",
      "storage": "-1001234567891",
      "backup": "-1001234567892",
      "news_archive": "-1001234567893",
      "media_storage": "-1001234567894"
    },
    "groups": {
      "admin": "-1001234567895",
      "testing": "-1001234567896",
      "users": "-1001234567897"
    }
  }
}
```

---

## 🤖 دسترسی‌های ربات

### در همه کانال‌ها:

```
✅ Post Messages
✅ Edit Messages
✅ Delete Messages
✅ Post Media
```

### در گروه Admin:

```
✅ همه دسترسی‌های Admin
```

### در گروه Testing:

```
✅ Post Messages
✅ Delete Messages
```

### در گروه Users:

```
✅ Post Messages
✅ Delete Messages
✅ Pin Messages
✅ Ban Users
```

---

## 📊 استفاده از کانال‌ها در کد

```python
from telethon import TelegramClient

client = TelegramClient('nazanin_user', api_id, api_hash)

# ارسال به کانال Report
await client.send_message(
    config['telegram']['channels']['report'],
    "📊 گزارش روزانه:\n\n✅ 45 پیام پردازش شد\n✅ 12 توییت ارسال شد"
)

# ذخیره فایل در Storage
await client.send_file(
    config['telegram']['channels']['storage'],
    'backup.json',
    caption='Backup - 2025-10-06'
)

# ارسال به گروه Admin
await client.send_message(
    config['telegram']['groups']['admin'],
    "⚠️ هشدار: API rate limit reached!"
)
```

---

## 🔐 امنیت و نکات مهم

### ✅ انجام بده:

- همه کانال‌ها رو **Private** کن (به جز اگه می‌خوای عمومی باشه)
- فقط ربات و خودت عضو باشید
- دسترسی‌های ربات رو محدود کن
- پیام‌های حساس رو بعد از مدتی حذف کن
- از 2FA استفاده کن

### ❌ انجام نده:

- کانال‌ها رو عمومی نکن (مگه اینکه بخوای)
- لینک‌های کانال رو share نکن
- اطلاعات حساس (API keys) رو توی کانال نفرست
- ربات رو در کانال‌های ناشناس admin نکن

---

## 📈 بهینه‌سازی استفاده

### Storage Optimization:

```python
# فشرده‌سازی قبل از آپلود
import gzip
import json

data = {"key": "value"}
compressed = gzip.compress(json.dumps(data).encode())

await client.send_file(
    storage_channel,
    compressed,
    attributes=[DocumentAttributeFilename('data.json.gz')]
)
```

### Auto-cleanup:

```python
# حذف خودکار فایل‌های قدیمی (بیش از 30 روز)
async def cleanup_old_files():
    async for message in client.iter_messages(storage_channel, limit=1000):
        if (datetime.now() - message.date).days > 30:
            await message.delete()
```

---

## 🎯 خلاصه

### چک‌لیست:

- [ ] 5 کانال ساخته شده
- [ ] 3 گروه ساخته شده (حداقل Admin و Testing)
- [ ] ربات به همه اضافه شده
- [ ] ربات Admin شده
- [ ] همه ID ها دریافت شده
- [ ] ID ها در config قرار گرفتن
- [ ] تست ارسال پیام OK
- [ ] همه کانال‌ها Private هستن

---

**حالا آماده‌ای! نازنین می‌تونه از کانال‌ها استفاده کنه! 🚀**
