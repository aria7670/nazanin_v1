# راهنمای سریع شروع نازنین

## شروع سریع در 5 دقیقه! ⚡

### گام 1: کلون کردن پروژه
```bash
git clone <repository-url>
cd nazanin
```

### گام 2: نصب وابستگی‌ها
```bash
pip install -r requirements.txt
```

### گام 3: تنظیم config.json

فایل `config.example.json` را به `config.json` کپی کنید و ویرایش کنید:

```bash
cp config.example.json config.json
nano config.json
```

### گام 4: اجرا!
```bash
python main.py
```

## تست بدون API‌های واقعی

می‌توانید سیستم را با تنظیمات شبیه‌سازی تست کنید:

```json
{
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

فقط `twitter` و `telegram` را خالی بگذارید.

## تست سیستم‌های هوش مصنوعی پیشرفته

### تست Brain Simulation
```python
from brain_simulation import BrainSimulation

config = {
    'emotion_update_interval': 300,
    'cognition_depth': 5,
    'memory_capacity': 10000
}

brain = BrainSimulation(config)

# پردازش ورودی
result = await brain.process(
    "This is amazing AI technology!",
    context={'importance': 0.8}
)

print(result['emotional_state'])
print(result['dominant_emotion'])
```

### تست Quantum Agent
```python
from quantum_agent import QuantumAgent

config = {
    'quantum_states': 64,
    'entanglement_enabled': True,
    'superposition_layers': 3
}

quantum = QuantumAgent(config)

# تصمیم‌گیری کوانتومی
options = [
    {'name': 'option1', 'value': 0.8, 'risk': 0.3},
    {'name': 'option2', 'value': 0.6, 'risk': 0.1},
]

decision = await quantum.quantum_decision(options)
print(decision)
```

### تست Neural Agent
```python
from neural_agent import NeuralAgent

config = {
    'hidden_layers': [512, 256, 128],
    'learning_rate': 0.001
}

neural = NeuralAgent(config)

# تحلیل محتوا
analysis = await neural.analyze_content(
    "Breaking: New AI breakthrough announced today!"
)

print(analysis['sentiment'])
print(analysis['engagement_prediction'])
```

## مثال استفاده ترکیبی

```python
import asyncio
from main import Nazanin

async def demo():
    # راه‌اندازی نازنین
    nazanin = Nazanin('config.json')
    await nazanin.initialize()
    
    # پردازش با تمام سیستم‌ها
    input_text = "AI is transforming the world rapidly!"
    
    result = await nazanin.process_with_all_systems(
        input_text,
        context={'importance': 0.9}
    )
    
    print("🧠 Brain Analysis:", result['brain'])
    print("⚛️ Quantum Analysis:", result['quantum'])
    print("🧬 Neural Analysis:", result['neural'])

asyncio.run(demo())
```

## سناریوهای مختلف

### سناریو 1: فقط شبیه‌سازی مغز
```json
{
  "brain_simulation": {"enabled": true},
  "quantum_agent": {"enabled": false},
  "neural_agent": {"enabled": false}
}
```

### سناریو 2: همه سیستم‌های هوش مصنوعی + Twitter
```json
{
  "twitter": {...},
  "brain_simulation": {"enabled": true},
  "quantum_agent": {"enabled": true},
  "neural_agent": {"enabled": true}
}
```

### سناریو 3: کامل (پروداکشن)
```json
{
  "telegram": {...},
  "twitter": {...},
  "google_sheets": {...},
  "brain_simulation": {"enabled": true},
  "quantum_agent": {"enabled": true},
  "neural_agent": {"enabled": true}
}
```

## دستورات مفید

### چک کردن وضعیت
```bash
# در تلگرام
/status

# یا در لاگ
tail -f nazanin.log | grep "✅"
```

### نظارت بر عملکرد
```bash
# CPU و RAM usage
htop

# مشاهده لاگ‌های خطا
grep ERROR nazanin.log

# آمار سیستم
/stats  # در تلگرام
```

### توقف و راه‌اندازی مجدد
```bash
# توقف
Ctrl+C

# راه‌اندازی مجدد
python main.py

# یا با systemd
sudo systemctl restart nazanin
```

## نکات مهم 💡

### 1. منابع سیستم
- **حداقل RAM**: 2GB
- **توصیه شده**: 4GB+
- **فضای دیسک**: 1GB

### 2. شبکه
- اتصال پایدار به اینترنت
- باز بودن portهای لازم
- VPN در صورت نیاز

### 3. امنیت
```bash
# تنظیم دسترسی فایل‌ها
chmod 600 config.json
chmod 600 credentials.json

# اجرا با کاربر غیر-root
sudo useradd -m nazanin
sudo su - nazanin
```

### 4. Backup
```bash
# Backup روزانه
crontab -e

# افزودن این خط:
0 3 * * * cp /path/to/nazanin.log /path/to/backups/nazanin-$(date +\%Y\%m\%d).log
```

## عیب‌یابی سریع 🔧

### مشکل: پکیج‌ها نصب نمی‌شوند
```bash
# ارتقای pip
pip install --upgrade pip

# نصب با sudo (اگر لازم بود)
sudo pip install -r requirements.txt
```

### مشکل: خطای PyTorch
```bash
# نصب CPU-only version
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

### مشکل: خطای Quantum libraries
```bash
# نصب جداگانه
pip install pennylane qiskit qiskit-aer
```

### مشکل: خطای Google Sheets
```bash
# چک کردن credentials
ls -la credentials.json

# تست اتصال
python -c "import gspread; print('OK')"
```

## مثال‌های واقعی

### مثال 1: پست خودکار در Twitter
```python
# سیستم خودکار توییت می‌کند:
# 1. جمع‌آوری اخبار AI (NewsCollectorAgent)
# 2. تحلیل با Brain Simulation
# 3. بهینه‌سازی با Neural Agent
# 4. تصمیم با Quantum Agent
# 5. تولید محتوا (ContentCreatorAgent)
# 6. پست در Twitter (خودکار Thread اگر بلند باشد)
```

### مثال 2: پاسخ هوشمند به Mention
```python
# جریان کار:
# 1. تشخیص mention
# 2. تحلیل احساسی (Neural Agent)
# 3. پردازش شناختی (Brain Simulation)
# 4. انتخاب بهترین پاسخ (Quantum Agent)
# 5. تولید پاسخ شخصی‌سازی شده
# 6. پست reply
```

### مثال 3: چت فارسی در تلگرام
```python
# شما: سلام نازنین، وضعیت چطوره؟
# نازنین: سلام! من الان کاملاً فعال هستم. 
#          احساسم خوب است (شادی: 72.3) و 
#          حافظه‌ام 2,450 آیتم داره. 
#          چیزی می‌خوای بپرسی؟
```

## منابع بیشتر

- 📖 [ARCHITECTURE.md](ARCHITECTURE.md) - معماری کامل سیستم
- 🔧 [INSTALLATION.md](INSTALLATION.md) - راهنمای نصب جامع
- 📚 [README.md](README.md) - مستندات اصلی پروژه

## پشتیبانی

اگر مشکلی داشتید:
1. لاگ‌ها را چک کنید: `cat nazanin.log`
2. دستور `/status` را در تلگرام امتحان کنید
3. مستندات را مطالعه کنید
4. Issue در GitHub باز کنید

---

🎉 **موفق باشید! نازنین آماده کمک به شما است!**
