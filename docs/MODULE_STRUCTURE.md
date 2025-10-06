# 📦 ساختار ماژولار نازنین

## راهنمای کامل ساختار پوشه‌ها و ماژول‌ها

---

## 🗂️ ساختار کلی

```
nazanin_v1/
│
├── src/                    # تمام کدهای منبع
├── docs/                   # تمام مستندات
├── tests/                  # تمام تست‌ها و demo‌ها
├── config/                 # تمام تنظیمات
├── main.py                 # نقطه ورود اصلی
├── main_advanced.py        # نقطه ورود پیشرفته
├── requirements.txt        # وابستگی‌ها
└── nazanin_complete.zip    # کل پروژه
```

---

## 📦 src/ - کدهای منبع

### 🔷 src/core/ - هسته اصلی

**مسئولیت**: سیستم‌های بنیادی پروژه

```
src/core/
├── __init__.py
├── sheets_manager.py      # مدیریت Google Sheets
└── api_manager.py         # مدیریت AI APIs
```

**استفاده**:
```python
from src.core import SheetsManager, APIManager

sheets = SheetsManager(creds, sheet_id)
api = APIManager()
```

---

### 🧠 src/ai/ - سیستم‌های هوش مصنوعی

**مسئولیت**: سیستم‌های AI پیشرفته

```
src/ai/
├── __init__.py
├── brain_simulation.py    # شبیه‌سازی مغز
├── quantum_agent.py       # سیستم کوانتومی
└── neural_agent.py        # شبکه‌های عصبی
```

**استفاده**:
```python
from src.ai import BrainSimulation, QuantumAgent, NeuralAgent

brain = BrainSimulation(config)
quantum = QuantumAgent(config)
neural = NeuralAgent(config)
```

---

### 🤖 src/agents/ - سیستم ایجنت‌ها

**مسئولیت**: 16 ایجنت تخصصی

```
src/agents/
├── __init__.py
├── agents.py              # 6 ایجنت پایه
└── specialized_agents.py  # 10 ایجنت تخصصی
```

**ایجنت‌های پایه**:
1. CategorizerAgent
2. ContentCreatorAgent
3. ScraperAgent
4. NewsCollectorAgent
5. AdvertiserAgent
6. TaskManagerAgent

**ایجنت‌های تخصصی**:
1. ContentOptimizationAgent
2. EngagementPredictorAgent
3. TrendAnalysisAgent
4. SchedulingOptimizerAgent
5. HashtagGeneratorAgent
6. SentimentAnalysisAgent
7. FactCheckerAgent
8. LanguageDetectorAgent
9. AudienceSegmentationAgent
10. CompetitorMonitorAgent

**استفاده**:
```python
from src.agents import AgentOrchestrator, SpecializedAgentOrchestrator

agents = AgentOrchestrator(api, sheets)
specialized = SpecializedAgentOrchestrator(api, sheets)
```

---

### 🌐 src/platforms/ - پلتفرم‌ها

**مسئولیت**: یکپارچگی با شبکه‌های اجتماعی

```
src/platforms/
├── __init__.py
├── twitter_system.py      # Twitter (پست، thread، mentions)
└── telegram_system.py     # Telegram (ربات، چت فارسی)
```

**استفاده**:
```python
from src.platforms import TwitterSystem, TelegramSystem

twitter = TwitterSystem(config, sheets, agents)
telegram = TelegramSystem(config, sheets, agents)
```

---

### 🛠️ src/utils/ - ابزارهای کمکی

**مسئولیت**: سیستم‌های کمکی و یادگیری

```
src/utils/
├── __init__.py
├── message_classifier.py   # دسته‌بندی پیام (10 دسته)
├── behavioral_learning.py  # یادگیری از رفتار
├── template_system.py      # تمپلت‌ها و الگوها
└── advanced_algorithms.py  # 5 الگوریتم پیچیده
```

**استفاده**:
```python
from src.utils import MessageClassifier, HumanizationEngine
from src.utils import ContentGenerator, AlgorithmOrchestrator

classifier = MessageClassifier()
engine = HumanizationEngine()
generator = ContentGenerator()
algorithms = AlgorithmOrchestrator()
```

---

### 💾 src/storage/ - ذخیره‌سازی

**مسئولیت**: ذخیره داده و فایل

```
src/storage/
├── __init__.py
└── telegram_storage.py    # ذخیره در Telegram
```

**استفاده**:
```python
from src.storage import TelegramStorage, DataBackupSystem

storage = TelegramStorage(client, channel_id)
backup = DataBackupSystem(storage)
```

---

## 📚 docs/ - مستندات

```
docs/
├── START_HERE.md               # راهنمای شروع
├── QUICKSTART.md               # شروع سریع
├── INSTALLATION.md             # نصب کامل
├── ARCHITECTURE.md             # معماری
├── ADVANCED_FEATURES.md        # ویژگی‌های پیشرفته
├── COMPLETE_SUMMARY.md         # خلاصه کامل
├── PROJECT_SUMMARY.md          # خلاصه پروژه
├── FINAL_SUMMARY_FA.md         # خلاصه فارسی
├── FEATURE_SUGGESTIONS_FA.md   # پیشنهادات
├── FUTURE_FEATURES.md          # ویژگی‌های آینده
├── QUICK_IDEAS.md              # ایده‌های سریع
└── MODULE_STRUCTURE.md         # این فایل
```

---

## 🧪 tests/ - تست و Demo

```
tests/
├── test_basic.py          # تست‌های پایه
├── demo.py                # Demo سیستم‌های AI
└── demo_advanced.py       # Demo کامل
```

**اجرا**:
```bash
python tests/test_basic.py      # تست سریع
python tests/demo.py            # Demo AI
python tests/demo_advanced.py   # Demo کامل
```

---

## ⚙️ config/ - تنظیمات

```
config/
├── config.json            # تنظیمات اصلی (gitignored)
└── config.example.json    # نمونه
```

---

## 💡 نحوه استفاده از ساختار ماژولار

### 1. Import کامل یک ماژول
```python
from src.core import SheetsManager
from src.ai import BrainSimulation
from src.agents import AgentOrchestrator
```

### 2. Import چند کلاس از یک ماژول
```python
from src.utils import (
    MessageClassifier,
    PromptBuilder,
    HumanizationEngine
)
```

### 3. Import با alias
```python
from src.ai import BrainSimulation as Brain
from src.ai import QuantumAgent as Quantum

brain = Brain(config)
quantum = Quantum(config)
```

### 4. Import تمام یک package
```python
from src import ai
from src import agents

brain = ai.BrainSimulation(config)
agent_orch = agents.AgentOrchestrator(api, sheets)
```

---

## 🔧 افزودن ماژول جدید

### مثال: افزودن Image Generator

#### 1. ساخت فایل در پوشه مناسب:
```bash
touch src/utils/image_generator.py
```

#### 2. نوشتن کد:
```python
# src/utils/image_generator.py
class ImageGenerator:
    def __init__(self, api_manager):
        self.api_manager = api_manager
    
    async def generate(self, prompt: str):
        # کد تولید تصویر
        pass
```

#### 3. افزودن به __init__.py:
```python
# src/utils/__init__.py
from .image_generator import ImageGenerator

__all__ = [..., 'ImageGenerator']
```

#### 4. استفاده:
```python
from src.utils import ImageGenerator

image_gen = ImageGenerator(api_manager)
image = await image_gen.generate("AI robot")
```

---

## 🎯 مزایای ساختار ماژولار

### ✅ سازماندهی بهتر
- هر چیز جای مشخصی دارد
- پیدا کردن فایل‌ها راحت‌تر

### ✅ Import آسان‌تر
```python
# قبل
from brain_simulation import BrainSimulation

# بعد (واضح‌تر)
from src.ai import BrainSimulation
```

### ✅ توسعه راحت‌تر
- افزودن ماژول جدید ساده
- جایگزینی بخش‌ها بدون تأثیر روی بقیه

### ✅ تست بهتر
- تست هر بخش جداگانه
- Mock کردن آسان‌تر

### ✅ مقیاس‌پذیر
- می‌شه هر بخش رو جدا deploy کرد
- Microservices ممکن

---

## 📖 مثال‌های عملی

### ساخت یک فیچر جدید:

#### 1. تصمیم: کجا باید باشه؟
- AI system → `src/ai/`
- Agent → `src/agents/`
- Utility → `src/utils/`
- Platform → `src/platforms/`

#### 2. ساخت فایل در پوشه مناسب

#### 3. Import و استفاده

---

## 🚀 خلاصه

ساختار جدید:
- ✅ **کاملاً ماژولار**
- ✅ **سازماندهی شده**
- ✅ **قابل توسعه**
- ✅ **حرفه‌ای**

همه چیز در جای مناسبش! 🎯
