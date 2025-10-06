# معماری سیستم نازنین

## نمای کلی

نازنین یک سیستم هوش مصنوعی پیشرفته و ماژولار است که شامل:

1. **سیستم‌های پایه** - مدیریت داده، API، و ایجنت‌ها
2. **سیستم‌های پلتفرم** - Twitter و Telegram
3. **سیستم‌های هوش مصنوعی پیشرفته** - شبیه‌سازی مغز، کوانتوم، و شبکه‌های عصبی

## معماری کلی

```
┌─────────────────────────────────────────────────────────────┐
│                         MAIN.PY                              │
│                    (Orchestrator)                            │
└────────────────────────┬────────────────────────────────────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
         ▼               ▼               ▼
    ┌────────┐     ┌─────────┐    ┌──────────┐
    │ Sheets │     │   API   │    │  Agents  │
    │Manager │     │ Manager │    │Orchestr. │
    └────────┘     └─────────┘    └──────────┘
         │               │               │
         └───────────────┼───────────────┘
                         │
         ┌───────────────┼───────────────────────┐
         │               │                       │
         ▼               ▼                       ▼
    ┌─────────┐    ┌──────────┐         ┌────────────┐
    │ Twitter │    │ Telegram │         │ Advanced   │
    │ System  │    │  System  │         │ AI Systems │
    └─────────┘    └──────────┘         └────────────┘
                                              │
                        ┌─────────────────────┼─────────────────────┐
                        │                     │                     │
                        ▼                     ▼                     ▼
                   ┌────────┐          ┌─────────┐          ┌──────────┐
                   │ Brain  │          │Quantum  │          │ Neural   │
                   │Simul.  │          │ Agent   │          │ Agent    │
                   └────────┘          └─────────┘          └──────────┘
```

## مؤلفه‌های اصلی

### 1. Sheets Manager (sheets_manager.py)
**وظیفه**: مدیریت تمام عملیات Google Sheets

**قابلیت‌ها**:
- Cache با TTL 5 دقیقه
- خواندن/نوشتن داده‌ها
- مدیریت شخصیت، قوانین، و API keys
- لاگ کردن توییت‌ها و پست‌ها

**روش‌های کلیدی**:
```python
await sheets_manager.get_sheet_data('sheet_name')
await sheets_manager.append_row('sheet_name', data)
await sheets_manager.get_personality()
await sheets_manager.get_api_keys()
```

### 2. API Manager (api_manager.py)
**وظیفه**: مدیریت چندین AI provider با load balancing

**قابلیت‌ها**:
- پشتیبانی از Gemini, GPT-4, Claude, DeepSeek
- Round-robin load balancing
- Fallback خودکار
- Task routing هوشمند

**مسیریابی کارها**:
```python
video_analysis → Gemini
content_generation → GPT-4
data_analysis → DeepSeek
twitter_specific → Grok
general → Claude
```

### 3. Agent Orchestrator (agents.py)
**وظیفه**: مدیریت ایجنت‌های تخصصی

**ایجنت‌ها**:
- **CategorizerAgent**: دسته‌بندی خودکار محتوا
- **ContentCreatorAgent**: تولید محتوای حرفه‌ای
- **ScraperAgent**: جمع‌آوری اطلاعات از وب
- **NewsCollectorAgent**: جمع‌آوری اخبار AI
- **AdvertiserAgent**: تبلیغات ظریف
- **TaskManagerAgent**: مدیریت صف کارها

### 4. Twitter System (twitter_system.py)
**وظیفه**: مدیریت عملیات Twitter

**قابلیت‌ها**:
- پست توییت ساده
- Thread خودکار (برای محتوای >270 کاراکتر)
- نظارت بر mention‌ها
- پاسخ هوشمند
- دسته‌بندی خودکار

**جریان کار**:
```
محتوا → بررسی طول → 
  ├─ کوتاه: توییت ساده
  └─ بلند: تبدیل به Thread → شماره‌گذاری → پست زنجیره‌ای
```

### 5. Telegram System (telegram_system.py)
**وظیفه**: مدیریت ربات و چت فارسی

**قابلیت‌ها**:
- Bot Client برای تعامل با ادمین
- User Client برای Scraping (اختیاری)
- چت فارسی هوشمند
- گزارش‌دهی Real-time
- دستورات مدیریتی

**دستورات**:
- `/start`, `/status`, `/stats`, `/post`, `/tasks`, `/reload`

### 6. Brain Simulation (brain_simulation.py)
**وظیفه**: شبیه‌سازی فرآیندهای شناختی مغز انسان

**زیرسیستم‌ها**:

#### EmotionSystem
- 10 احساس پایه (شادی، اعتماد، ترس، ...)
- Decay خودکار به baseline
- بروزرسانی پویا

#### CognitionSystem
- Short-term memory
- Long-term memory (حداکثر 10,000 آیتم)
- Working memory (7 آیتم - قانون میلر)
- پردازش اطلاعات
- Consolidation خودکار

#### DecisionMakingSystem
- ترکیب cognitive + emotional evaluation
- محاسبه confidence
- ارزیابی ریسک

**جریان پردازش**:
```
ورودی → پردازش شناختی → پاسخ احساسی → تصمیم‌گیری
```

### 7. Quantum Agent (quantum_agent.py)
**وظیفه**: الگوریتم‌های کوانتومی برای تصمیم‌گیری

**مؤلفه‌ها**:

#### QuantumCircuit
- State vector simulation
- Hadamard gates (superposition)
- Entanglement
- Measurement

#### QuantumInspiredOptimizer
- Quantum interference
- Quantum tunneling
- Population-based optimization

#### QuantumPatternRecognition
- Quantum fidelity matching
- Pattern learning
- Recognition با confidence

**کاربردها**:
- بهینه‌سازی تصمیمات
- تشخیص الگو
- پردازش موازی (superposition)

### 8. Neural Agent (neural_agent.py)
**وظیفه**: یادگیری و بهینه‌سازی با شبکه‌های عصبی

**مؤلفه‌ها**:

#### NeuralNetwork
- Deep neural network با PyTorch
- Hidden layers قابل تنظیم
- Dropout برای regularization

#### ExperienceReplay
- Buffer 10,000 تجربه
- Sampling تصادفی برای training

#### AdaptiveLearningSystem
- یادگیری از تجربه
- Training batch-wise
- Tracking performance

#### SentimentAnalysisNeural
- تحلیل احساسات متن
- 3 کلاس: منفی، خنثی، مثبت

#### ContentOptimizationNeural
- پیش‌بینی engagement
- یادگیری از عملکرد واقعی
- بهینه‌سازی محتوا

## جریان داده

### 1. تولید محتوا
```
موضوع → ContentCreatorAgent
  ↓
دریافت شخصیت از Sheets
  ↓
ساخت پرامپت JSON
  ↓
درخواست به API Manager
  ↓
انتخاب بهترین AI
  ↓
تولید محتوا
  ↓
پست در Twitter/Telegram
  ↓
دسته‌بندی (CategorizerAgent)
  ↓
ذخیره در Sheets
```

### 2. پردازش هوش مصنوعی پیشرفته
```
ورودی
  ↓
┌─────────────┬──────────────┬────────────┐
│             │              │            │
▼             ▼              ▼            ▼
Brain     Quantum       Neural       Regular
Simulation  Agent        Agent       Agents
  ↓             ↓              ↓            ↓
Emotional  Quantum      Sentiment    Content
Analysis   Decision     Analysis   Generation
  ↓             ↓              ↓            ↓
└─────────────┴──────────────┴────────────┘
                    ↓
            ترکیب نتایج
                    ↓
            خروجی نهایی
```

### 3. پاسخ به Mention
```
Twitter API → Monitor mentions
  ↓
فیلتر (بر اساس قوانین خودمختاری)
  ↓
Brain: تحلیل احساسی و شناختی
  ↓
Quantum: ارزیابی بهترین پاسخ
  ↓
Neural: پیش‌بینی engagement
  ↓
ContentCreator: تولید پاسخ
  ↓
Post reply
  ↓
Log در Sheets
```

## حلقه‌های اجرا

### Twitter Loop (هر 10 دقیقه)
```python
while True:
    check_mentions()
    respond_to_relevant_ones()
    update_daily_stats()
    sleep(600)
```

### News Loop (هر 3 ساعت)
```python
while True:
    collect_ai_news()
    summarize()
    create_tweet()
    post()
    sleep(10800)
```

### Maintenance Loop (هر 6-12 ساعت)
```python
while True:
    # Every 6 hours
    clear_cache()
    consolidate_memory()
    
    # Every 12 hours
    reload_api_keys()
    
    # Every hour
    send_stats_report()
```

### Brain Update Loop (هر 5 دقیقه)
```python
while True:
    decay_emotions()
    consolidate_memory()
    sleep(300)
```

## مدیریت خطا

### سطح 1: تلاش مجدد
- خطاهای شبکه
- Rate limiting
- Timeout‌ها

### سطح 2: Fallback
- اگر یک AI fail کرد → استفاده از AI دیگر
- اگر یک API key fail کرد → کلید بعدی

### سطح 3: Graceful Degradation
- اگر Twitter down است → ادامه Telegram
- اگر AI unavailable → استفاده از template‌ها

### سطح 4: لاگ و گزارش
- تمام خطاها در `nazanin.log`
- گزارش فوری به کانال تلگرام
- ذخیره در sheets برای تحلیل

## بهینه‌سازی‌ها

### 1. Caching
- Google Sheets: 5 دقیقه TTL
- API responses: In-memory برای requests تکراری

### 2. Rate Limiting
- Twitter: 2 ثانیه بین توییت‌ها
- API calls: respect provider limits
- Scraping: 1 ثانیه بین requests

### 3. Async Operations
- همه I/O operations async
- Concurrent API calls
- Non-blocking loops

### 4. Memory Management
- Limit long-term memory size
- Periodic memory consolidation
- Cleanup old cache entries

## امنیت

### 1. Credentials
- هیچ credential در کد
- استفاده از config.json (gitignored)
- Service accounts برای Google

### 2. Data Protection
- Encryption برای sensitive data
- Limited API scopes
- Regular key rotation

### 3. Access Control
- تنها admin می‌تواند دستورات بزند
- Validation برای همه ورودی‌ها
- Sanitization قبل از ذخیره

## مقیاس‌پذیری

### Horizontal Scaling
- هر ماژول می‌تواند جداگانه اجرا شود
- Load balancing بین چندین instance
- Shared state در Google Sheets

### Vertical Scaling
- Increase memory برای neural networks
- More CPU cores برای quantum simulation
- بهینه‌سازی database queries

## نظارت و دیباگ

### لاگ‌ها
```python
logging.INFO    # عملیات عادی
logging.DEBUG   # جزئیات فنی
logging.WARNING # مشکلات غیر بحرانی
logging.ERROR   # خطاهای قابل برگشت
```

### متریک‌ها
- تعداد توییت‌ها/روز
- تعداد reply‌ها
- API call success rate
- Memory usage
- Brain emotional state

### دستورات دیباگ
```bash
# مشاهده لاگ‌های زنده
tail -f nazanin.log

# فیلتر خطاها
grep ERROR nazanin.log

# آمار عملکرد
/stats در تلگرام
```

## توسعه آینده

### پیشنهادات:
1. افزودن Instagram integration
2. Voice synthesis برای پادکست
3. Image generation برای محتوای بصری
4. Multi-language support
5. A/B testing برای بهینه‌سازی محتوا
6. Reinforcement learning برای استراتژی
7. Blockchain integration برای transparency
8. Advanced analytics dashboard

---

این معماری قابل توسعه، maintainable، و production-ready است! 🚀
