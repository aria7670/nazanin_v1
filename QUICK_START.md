# راهنمای سریع - Nazanin v1

## نصب سریع

```bash
# نصب وابستگی‌ها
pip3 install -r requirements.txt

# تست سیستم
python3 test_bot.py
```

## استفاده سریع

### 1. حالت تعاملی

```bash
python3 bot.py --interactive
```

سپس می‌توانید با ربات گفتگو کنید. دستورات:
- `status` - نمایش وضعیت
- `optimize` - بهینه‌سازی
- `save` - ذخیره وضعیت
- `quit` - خروج

### 2. پردازش تک مرحله‌ای

```bash
python3 bot.py --process "سلام" --task-type general
```

### 3. اجرای مثال‌ها

```bash
# مثال‌های پایه
python3 examples/basic_usage.py

# مثال‌های پیشرفته
python3 examples/advanced_usage.py
```

## استفاده از ماژول‌ها

### سیستم شبیه‌سازی مغز

```python
from brain_simulation import BrainSimulator

brain = BrainSimulator(neuron_count=1000)
result = brain.process_input("ورودی شما")
print(result['decision'])
```

### پردازنده کوانتومی

```python
from quantum_system import QuantumProcessor

quantum = QuantumProcessor(qubit_count=8)
quantum.apply_to_qubit(0, 'H')  # Hadamard gate
results = quantum.measure_all()
```

### شبکه عصبی

```python
from neural_network import NeuralNetwork
import numpy as np

nn = NeuralNetwork(architecture=[10, 64, 32, 10])
X = np.random.randn(100, 10)
y = np.random.randn(100, 10)
nn.fit(X, y, epochs=50)
```

### ایجنت هوشمند

```python
from agent_system import IntelligentAgent

agent = IntelligentAgent(agent_id="my_agent")
reasoning = agent.reason("مسئله شما")
print(reasoning['solution'])
```

### سیستم یکپارچه

```python
from integration import UnifiedAISystem

ai = UnifiedAISystem()
result = ai.process("ورودی", task_type="pattern_recognition")
print(result['primary_result'])
```

## انواع وظایف

- `general` - عمومی
- `pattern_recognition` - تشخیص الگو
- `optimization` - بهینه‌سازی
- `decision_making` - تصمیم‌گیری
- `learning` - یادگیری
- `prediction` - پیش‌بینی
- `search` - جستجو
- `memory` - حافظه
- `reasoning` - استدلال
- `planning` - برنامه‌ریزی

## تنظیمات

فایل `config.json` را ویرایش کنید:

```json
{
  "brain_simulation": {
    "neuron_count": 1000,
    "learning_rate": 0.01
  },
  "quantum": {
    "qubit_count": 8
  },
  "neural_network": {
    "hidden_layers": [10, 64, 32, 10]
  }
}
```

## عیب‌یابی

اگر خطایی رخ داد:

1. بررسی نصب NumPy: `pip3 install numpy`
2. بررسی ورژن Python: `python3 --version` (باید 3.8+)
3. اجرای تست: `python3 test_bot.py`
4. بررسی لاگ‌ها در پوشه `logs/`

## پشتیبانی

برای اطلاعات بیشتر، `README.md` را مطالعه کنید.
