# 🤝 Contributing to Nazanin AI Bot

ممنون که می‌خوای به پروژه Nazanin کمک کنی! 🎉

## 📋 فهرست

- [شروع کردن](#شروع-کردن)
- [راهنمای توسعه](#راهنمای-توسعه)
- [استانداردهای کد](#استانداردهای-کد)
- [Pull Request Process](#pull-request-process)
- [گزارش باگ](#گزارش-باگ)
- [پیشنهاد فیچر](#پیشنهاد-فیچر)

---

## 🚀 شروع کردن

### 1. Fork کردن پروژه
```bash
# Fork کن روی GitHub
# بعد clone کن
git clone https://github.com/YOUR_USERNAME/nazanin_v1.git
cd nazanin_v1
```

### 2. نصب Dependencies
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# یا
venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

### 3. ساخت Branch جدید
```bash
git checkout -b feature/amazing-feature
# یا
git checkout -b fix/bug-fix
```

---

## 🛠️ راهنمای توسعه

### ساختار پروژه

```
src/
├── core/       # Core systems (Sheets, API)
├── ai/         # AI systems (Brain, Quantum, Neural)
├── agents/     # Agent systems
├── platforms/  # Twitter, Telegram
├── utils/      # Utilities
└── storage/    # Storage systems
```

### افزودن فیچر جدید

#### 1. تصمیم بگیر کجا باید باشه:
- **AI system** → `src/ai/`
- **Agent** → `src/agents/`
- **Utility** → `src/utils/`
- **Platform** → `src/platforms/`

#### 2. ساخت فایل:
```bash
touch src/utils/my_new_feature.py
```

#### 3. نوشتن کد:
```python
"""
Module description
توضیحات ماژول
"""

class MyNewFeature:
    """
    Class description
    """
    
    def __init__(self, config):
        self.config = config
    
    async def process(self, data):
        """
        Method description
        
        Args:
            data: Input data
            
        Returns:
            Processed result
        """
        # Implementation
        pass
```

#### 4. افزودن به __init__.py:
```python
# src/utils/__init__.py
from .my_new_feature import MyNewFeature

__all__ = [..., 'MyNewFeature']
```

#### 5. نوشتن تست:
```python
# tests/test_my_feature.py
import pytest
from src.utils import MyNewFeature

def test_my_feature():
    feature = MyNewFeature({})
    result = await feature.process("test")
    assert result is not None
```

---

## 📝 استانداردهای کد

### Python Style Guide
- از **PEP 8** پیروی کن
- استفاده از **type hints**
- Docstrings برای همه توابع و کلاس‌ها

### نمونه:
```python
from typing import Dict, List, Optional

async def process_message(
    message: str,
    user_id: int,
    options: Optional[Dict] = None
) -> Dict[str, any]:
    """
    Process a user message.
    
    Args:
        message: The message text
        user_id: User identifier
        options: Optional processing options
        
    Returns:
        Dictionary with processing results
        
    Raises:
        ValueError: If message is empty
    """
    if not message:
        raise ValueError("Message cannot be empty")
    
    # Implementation
    return {"status": "success"}
```

### Naming Conventions
- **Classes**: `PascalCase` (e.g., `BrainSimulation`)
- **Functions**: `snake_case` (e.g., `process_message`)
- **Constants**: `UPPER_CASE` (e.g., `MAX_RETRIES`)
- **Private**: `_leading_underscore` (e.g., `_internal_method`)

### Import Order
```python
# 1. Standard library
import asyncio
import logging
from typing import Dict

# 2. Third-party
import numpy as np
from telethon import TelegramClient

# 3. Local
from src.core import SheetsManager
from src.utils import MessageClassifier
```

---

## 🔄 Pull Request Process

### 1. قبل از PR:
```bash
# Run tests
python tests/test_basic.py

# Check code style
flake8 src/

# Format code (optional)
black src/
```

### 2. ساخت PR:
- عنوان واضح و مختصر
- توضیحات کامل
- لینک به issue مربوطه (اگه هست)
- Screenshot (اگه لازم باشه)

### نمونه PR Description:
```markdown
## 📝 توضیحات

این PR یک سیستم جدید برای تحلیل احساسات اضافه می‌کنه.

## 🎯 تغییرات

- ✅ افزودن `SentimentAnalyzer` در `src/utils/`
- ✅ Integration با `MessageClassifier`
- ✅ تست‌های جدید
- ✅ مستندات به‌روز شده

## 🧪 تست

- [x] همه تست‌ها pass شدن
- [x] تست‌های جدید اضافه شده
- [x] Code style چک شده

## 📸 Screenshots

(اگه لازم باشه)

Closes #123
```

### 3. بعد از Review:
- تغییرات requested رو اعمال کن
- Push کن به همون branch
- منتظر approve بمون

---

## 🐛 گزارش باگ

### قبل از گزارش:
1. چک کن issue مشابهی وجود نداره
2. مطمئن شو آخرین نسخه رو داری
3. سعی کن باگ رو reproduce کنی

### نمونه Bug Report:
```markdown
## 🐛 توضیح باگ

BrainSimulation وقتی emotion شدید داریم crash می‌کنه.

## 🔄 مراحل Reproduce

1. Run `python main.py`
2. Send message با محتوای خیلی احساسی
3. ببین error

## ✅ انتظار

باید emotion رو به درستی process کنه.

## ❌ واقعیت

Error می‌ده: `IndexError: list index out of range`

## 📋 Environment

- OS: Ubuntu 20.04
- Python: 3.10.5
- Version: 2.0.0

## 📸 Screenshot/Logs

```
Traceback (most recent call last):
  ...
```
```

---

## 💡 پیشنهاد فیچر

### نمونه Feature Request:
```markdown
## 🚀 فیچر پیشنهادی

افزودن سیستم تحلیل صدا برای Telegram voice messages.

## 🎯 مشکلی که حل می‌کنه

الان فقط text رو می‌تونیم پردازش کنیم.

## 💭 پیشنهاد Solution

- استفاده از speech-to-text API
- Integration با MessageClassifier
- ذخیره transcription در storage

## 🔄 Alternatives

می‌شه از Google Speech API یا Whisper استفاده کرد.

## 📊 اولویت

Medium
```

---

## ✅ Checklist قبل از Submit

- [ ] کد clean و readable است
- [ ] همه تست‌ها pass می‌شن
- [ ] Docstrings اضافه شده
- [ ] Type hints استفاده شده
- [ ] مستندات به‌روز شده (اگه لازم باشه)
- [ ] No breaking changes (یا توضیح داده شده)

---

## 🎨 Code Review Guidelines

### برای Reviewers:
- ✅ Constructive باش
- ✅ مثال بده
- ✅ سوال بپرس، دستور نده
- ✅ تمرکز روی code، نه person

### نمونه‌های خوب:
✅ "What do you think about using X instead of Y here? It might be more efficient."
✅ "Could you add a docstring here? It would help others understand the logic."

### نمونه‌های بد:
❌ "This is wrong."
❌ "Why did you do it this way?"

---

## 📞 ارتباط

- **Issues**: برای باگ و فیچر
- **Discussions**: برای سوالات کلی
- **Email**: برای موارد خصوصی

---

## 🙏 تشکر

ممنون که به Nazanin کمک می‌کنی! هر contribution، کوچیک یا بزرگ، ارزشمنده! 🎉

---

**Happy Coding! 🚀**
