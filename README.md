# Nazanin v1 - سیستم هوش مصنوعی پیشرفته و ماژولار

🤖 **ربات پایتونی پیشرفته با قابلیت شبیه‌سازی مغز، پردازش کوانتومی، شبکه‌های عصبی و سیستم ایجنت هوشمند**

## 📋 فهرست مطالب

- [معرفی](#معرفی)
- [ویژگی‌ها](#ویژگی-ها)
- [معماری سیستم](#معماری-سیستم)
- [نصب و راه‌اندازی](#نصب-و-راه-اندازی)
- [استفاده](#استفاده)
- [ماژول‌ها](#ماژول-ها)
- [مثال‌ها](#مثال-ها)

## 🌟 معرفی

Nazanin v1 یک سیستم هوش مصنوعی پیشرفته و ماژولار است که چهار زیرسیستم قدرتمند را با هم ترکیب می‌کند:

1. **🧠 Brain Simulation** - شبیه‌سازی مغز انسان با نورون‌ها و حافظه
2. **⚛️ Quantum Computing** - پردازش کوانتومی برای محاسبات پیچیده
3. **🤖 Neural Networks** - شبکه‌های عصبی عمیق برای یادگیری
4. **🎯 Intelligent Agents** - ایجنت‌های هوشمند برای تصمیم‌گیری

## ✨ ویژگی‌ها

### سیستم شبیه‌سازی مغز
- شبیه‌سازی 1000 نورون با اتصالات سیناپسی
- سیستم حافظه کوتاه‌مدت، بلندمدت و کاری
- یادگیری Hebbian (نورون‌هایی که با هم فعال می‌شوند، با هم سیم می‌شوند)
- تحلیل فعالیت مناطق مختلف مغز

### پردازنده کوانتومی
- شبیه‌سازی 8 کیوبیت
- گیت‌های کوانتومی (Hadamard, Pauli, Rotation)
- الگوریتم جستجوی کوانتومی (Grover's)
- Quantum Fourier Transform
- تحلیل مزیت کوانتومی

### شبکه عصبی
- معماری چند لایه قابل تنظیم
- توابع فعال‌سازی: ReLU, Sigmoid, Tanh, Leaky ReLU
- Dropout و Batch Normalization
- Early Stopping و Cross Validation
- Learning Rate Finder

### سیستم ایجنت هوشمند
- استدلال و تصمیم‌گیری
- برنامه‌ریزی و اجرای اهداف
- یادگیری تقویتی (Q-Learning)
- پایگاه دانش و سیستم باور

## 🏗️ معماری سیستم

```
nazanin_v1/
├── core/                    # هسته اصلی سیستم
│   ├── __init__.py
│   ├── config.py           # مدیریت تنظیمات
│   └── logger.py           # سیستم لاگ‌گیری
│
├── brain_simulation/        # شبیه‌سازی مغز
│   ├── __init__.py
│   ├── brain.py            # سیستم اصلی مغز
│   ├── neuron.py           # شبیه‌سازی نورون
│   └── memory.py           # سیستم حافظه
│
├── quantum_system/          # سیستم کوانتومی
│   ├── __init__.py
│   ├── quantum_processor.py # پردازنده کوانتومی
│   └── qubit.py            # شبیه‌سازی کیوبیت
│
├── neural_network/          # شبکه عصبی
│   ├── __init__.py
│   ├── neural_net.py       # شبکه عصبی
│   ├── layers.py           # لایه‌های مختلف
│   └── training.py         # ابزارهای آموزش
│
├── agent_system/            # سیستم ایجنت
│   ├── __init__.py
│   ├── agent.py            # ایجنت هوشمند
│   ├── rl_agent.py         # یادگیری تقویتی
│   └── environment.py      # محیط شبیه‌سازی
│
├── integration/             # لایه یکپارچه‌سازی
│   ├── __init__.py
│   ├── unified_system.py   # سیستم یکپارچه
│   └── coordinator.py      # هماهنگ‌کننده
│
├── bot.py                   # رابط اصلی ربات
├── config.json              # فایل تنظیمات
└── requirements.txt         # وابستگی‌ها
```

## 📦 نصب و راه‌اندازی

### پیش‌نیازها
- Python 3.8 یا بالاتر
- pip

### نصب

```bash
# کلون کردن یا دانلود پروژه
cd nazanin_v1

# نصب وابستگی‌ها
pip install -r requirements.txt
```

## 🚀 استفاده

### حالت تعاملی (Interactive Mode)

```bash
python bot.py --interactive
```

این حالت یک رابط CLI تعاملی ارائه می‌دهد که می‌توانید با ربات گفتگو کنید.

**دستورات موجود:**
- پیام خود را تایپ کنید برای تعامل
- `status` - نمایش وضعیت ربات
- `optimize` - بهینه‌سازی سیستم‌ها
- `save` - ذخیره وضعیت
- `help` - نمایش راهنما
- `quit` یا `exit` - خروج

### پردازش تک مرحله‌ای

```bash
python bot.py --process "سلام، چطوری؟" --task-type general
```

### تنظیم سفارشی

```bash
python bot.py --config my_config.json --interactive
```

## 🔧 ماژول‌ها

### 1. Brain Simulation (شبیه‌سازی مغز)

```python
from brain_simulation import BrainSimulator

brain = BrainSimulator(neuron_count=1000, learning_rate=0.01)
result = brain.process_input("test input")
print(result)
```

### 2. Quantum System (سیستم کوانتومی)

```python
from quantum_system import QuantumProcessor

quantum = QuantumProcessor(qubit_count=8)
quantum.apply_to_qubit(0, 'H')  # Hadamard gate
quantum.create_bell_state(0, 1)  # Bell state
results = quantum.measure_all()
```

### 3. Neural Network (شبکه عصبی)

```python
from neural_network import NeuralNetwork
import numpy as np

nn = NeuralNetwork(architecture=[10, 64, 32, 10])
X = np.random.randn(100, 10)
y = np.random.randn(100, 10)
nn.fit(X, y, epochs=50)
predictions = nn.predict(X)
```

### 4. Intelligent Agent (ایجنت هوشمند)

```python
from agent_system import IntelligentAgent

agent = IntelligentAgent(agent_id="my_agent")
perception = agent.perceive("environment observation")
reasoning = agent.reason("problem to solve")
decision = agent.decide(["option1", "option2", "option3"])
```

### 5. Unified System (سیستم یکپارچه)

```python
from integration import UnifiedAISystem

ai = UnifiedAISystem()
result = ai.process("input data", task_type="pattern_recognition")
print(result)
```

## 📚 مثال‌ها

### مثال 1: پردازش ساده

```python
from bot import NazaninBot

bot = NazaninBot()
bot.start()

result = bot.process("Hello, how are you?")
print(f"Response: {result['primary_result']}")
print(f"Confidence: {result['combined_confidence']}")

bot.stop()
```

### مثال 2: یادگیری از داده

```python
from integration import UnifiedAISystem
import numpy as np

ai = UnifiedAISystem()

# آموزش با داده‌های نمونه
X_train = np.random.randn(100, 10)
y_train = np.random.randn(100, 10)

ai.learn(X_train, y_train, task_type="learning")

# تست
X_test = np.random.randn(10, 10)
result = ai.process(X_test, task_type="prediction")
```

### مثال 3: حل مسئله با ایجنت

```python
from agent_system import IntelligentAgent

agent = IntelligentAgent(agent_id="problem_solver")

# تعریف مسئله
problem = "How to optimize resource allocation?"

# استدلال
reasoning = agent.reason(problem)
print(f"Solution: {reasoning['solution']}")
print(f"Confidence: {reasoning['confidence']}")

# برنامه‌ریزی
goal = {'description': 'Optimize resource allocation'}
plan = agent.plan(goal)

for step in plan:
    print(f"Step {step['step_number']}: {step['action']}")
```

### مثال 4: محاسبات کوانتومی

```python
from quantum_system import QuantumProcessor

qp = QuantumProcessor(qubit_count=4)

# جستجوی کوانتومی
target = 5  # State to search for
result = qp.quantum_search(target)
print(f"Found state: {result}")

# Quantum Fourier Transform
qp.reset()
qp.quantum_fourier_transform([0, 1, 2, 3])
measurements = qp.measure_all()
print(f"QFT results: {measurements}")
```

## ⚙️ پیکربندی

فایل `config.json` تنظیمات مختلف سیستم را مدیریت می‌کند:

```json
{
  "bot_name": "Nazanin v1",
  "version": "1.0.0",
  "brain_simulation": {
    "enabled": true,
    "neuron_count": 1000,
    "learning_rate": 0.01,
    "memory_capacity": 10000
  },
  "quantum": {
    "enabled": true,
    "qubit_count": 8,
    "simulation_shots": 1024
  },
  "neural_network": {
    "enabled": true,
    "hidden_layers": [10, 64, 32, 10],
    "activation": "relu"
  },
  "agent": {
    "enabled": true,
    "max_iterations": 100,
    "exploration_rate": 0.1
  }
}
```

## 📊 نوع وظایف پشتیبانی شده

- `general` - پردازش عمومی
- `pattern_recognition` - تشخیص الگو
- `optimization` - بهینه‌سازی
- `decision_making` - تصمیم‌گیری
- `learning` - یادگیری
- `prediction` - پیش‌بینی
- `search` - جستجو
- `memory` - حافظه و ذخیره‌سازی
- `reasoning` - استدلال
- `planning` - برنامه‌ریزی

## 🔍 ویژگی‌های پیشرفته

### مسیریابی هوشمند وظایف
سیستم به طور خودکار وظایف را به مناسب‌ترین زیرسیستم‌ها هدایت می‌کند.

### یادگیری ترکیبی
از چندین روش یادگیری (عصبی، مغزی، تقویتی) به طور همزمان استفاده می‌کند.

### تحلیل مزیت کوانتومی
تشخیص می‌دهد چه زمانی استفاده از پردازش کوانتومی مفید است.

### حافظه چندلایه
سیستم حافظه شامل حافظه کوتاه‌مدت، بلندمدت و کاری است.

## 🛠️ توسعه و گسترش

### افزودن ماژول جدید

1. ماژول جدید را در دایرکتوری مناسب ایجاد کنید
2. در `integration/coordinator.py` مسیریابی وظایف را به‌روزرسانی کنید
3. در `integration/unified_system.py` متد پردازش جدید اضافه کنید

### سفارشی‌سازی شبکه عصبی

```python
from neural_network import NeuralNetwork, Trainer

nn = NeuralNetwork(
    architecture=[20, 128, 64, 32, 10],
    activation='leaky_relu'
)

trainer = Trainer(nn)
history = trainer.train_with_validation(
    X_train, y_train,
    X_val, y_val,
    epochs=100,
    early_stopping_patience=15
)
```

## 📝 لاگ‌گیری

تمام فعالیت‌های سیستم در دایرکتوری `logs/` ذخیره می‌شوند.

```python
from core import Logger

logger = Logger("MyModule")
logger.info("Information message")
logger.warning("Warning message")
logger.error("Error message")
```

## 💾 ذخیره و بازیابی وضعیت

```python
bot = NazaninBot()
bot.start()

# پردازش...

# ذخیره وضعیت
bot.save_state("my_state.json")

# بهینه‌سازی
bot.optimize()
```

## 🎯 موارد استفاده

- سیستم‌های کمک تصمیم‌گیری هوشمند
- تحلیل و پردازش داده‌های پیچیده
- شبیه‌سازی فرآیندهای شناختی
- بهینه‌سازی کوانتومی
- یادگیری و تطبیق خودکار
- پردازش زبان طبیعی
- سیستم‌های خبره

## 🤝 مشارکت

برای مشارکت در توسعه این پروژه:

1. Fork کنید
2. برنچ جدید ایجاد کنید
3. تغییرات را commit کنید
4. Push کنید
5. Pull Request ایجاد کنید

## 📄 مجوز

این پروژه تحت مجوز MIT منتشر شده است.

## 🙏 تشکر

این پروژه با الهام از:
- شبکه‌های عصبی زیستی
- محاسبات کوانتومی
- هوش مصنوعی شناختی
- یادگیری تقویتی

---

**ساخته شده با ❤️ برای آینده هوش مصنوعی**