# 🚀 شروع سریع - نازنین-نورا v3.0.0

**تاریخ**: 2025-10-07  
**نسخه**: 3.0.0  
**وضعیت**: ✅ بازطراحی کامل شده

---

## ⚡ اجرای فوری (3 دقیقه!)

### 1. دانلود
```bash
git clone https://github.com/aria7670/nazanin_v1.git
cd nazanin_v1
```

### 2. نصب
```bash
pip install -r requirements.txt
```

### 3. تنظیم (فقط 3 خط!)
```bash
cp config/config.enhanced.json config/config.json
nano config/config.json
```

**پر کن:**
```json
{
  "telegram": {
    "api_id": "123456",
    "api_hash": "...",
    "phone_number": "+98..."
  },
  "ai_apis": {
    "groq": {"keys": ["gsk_..."]}
  }
}
```

### 4. اجرا!
```bash
python run.py
```

**تمام! ✅**

---

## 📁 ساختار جدید (مهم!)

### قبل:
```
❌ src/
❌ nazanin_nora.py
❌ main.py
```

### بعد:
```
✅ nazanin/            # همه چیز اینجا!
✅ run.py              # اجرا با این!
```

---

## 🎯 روش‌های اجرا

### روش 1: run.py (ساده‌ترین!)
```bash
python run.py
```

### روش 2: Module
```bash
python -m nazanin
```

### روش 3: Import
```python
from nazanin import NazaninNora
import asyncio

async def main():
    app = NazaninNora()
    await app.run()

asyncio.run(main())
```

---

## 🆓 API رایگان

### گزینه 1: Groq (توصیه می‌شه!)
```
🔗 https://console.groq.com
✅ رایگان
✅ خیلی سریع
```

### گزینه 2: Gemini
```
🔗 https://makersuite.google.com
✅ رایگان
✅ قدرتمند
```

### گزینه 3: ChatGLM (جدید!)
```
🔗 https://open.bigmodel.cn
✅ رایگان
✅ چینی
```

---

## 📚 مستندات

### اول اینا رو بخون:
1. **این فایل** ← شروع اینجا!
2. **STRUCTURE_NEW.md** ← ساختار جدید
3. **README.md** ← راهنمای کامل

### بعد اینا:
4. **BIO_SYSTEM_GUIDE.md** ← سیستم بیولوژیکی
5. **NORA_INTEGRATION_GUIDE.md** ← قابلیت‌های نورا
6. **FREE_API_SERVICES.md** ← API های رایگان

---

## 🧪 تست

```bash
# تست ساختار
python test_structure.py

# باید ببینی:
✅ ساختار پوشه‌ها: OK
✅ فایل‌های مهم: OK
```

---

## ❓ سوالات متداول

### کجا اجرا کنم؟
```bash
python run.py
```

### فایل main کجاست؟
```
nazanin/app.py
```

### Import ها چطوری؟
```python
from nazanin.xxx import yyy
```

### src/ کجا رفت؟
```
تبدیل شد به nazanin/
```

---

## ✅ چک‌لیست

قبل از اجرا:
- [ ] Python 3.8+ نصب شده
- [ ] pip install -r requirements.txt
- [ ] config.json پر شده
- [ ] credentials.json دانلود شده (Google)

اجرا:
```bash
python run.py
```

---

**همین! موفق باشی! 🎉**

Version: 3.0.0  
Updated: 2025-10-07
