# 🆓 سرویس‌های API رایگان برای نازنین

لیست کامل API ها و سرویس‌های رایگان

---

## 🤖 AI APIs (رایگان)

### 1. **Google Gemini**
```
🔗 URL: https://makersuite.google.com/app/apikey
💰 رایگان: 60 request/min
📊 مدل: gemini-pro
```

**نصب:**
```bash
pip install google-generativeai
```

**استفاده:**
```python
import google.generativeai as genai

genai.configure(api_key='YOUR_API_KEY')
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content('سلام')
```

---

### 2. **Groq** (خیلی سریع!)
```
🔗 URL: https://console.groq.com
💰 رایگان: 14,400 request/day
📊 مدل‌ها: 
   - Mixtral-8x7B
   - Llama2-70B
   - Gemma-7B
⚡ سرعت: تا 500 tokens/sec!
```

**نصب:**
```bash
pip install groq
```

**استفاده:**
```python
from groq import Groq

client = Groq(api_key='YOUR_API_KEY')
response = client.chat.completions.create(
    model="mixtral-8x7b-32768",
    messages=[{"role": "user", "content": "سلام"}]
)
```

---

### 3. **Together AI**
```
🔗 URL: https://api.together.xyz
💰 رایگان: $25 credit
📊 مدل‌ها: 50+ مدل open-source
```

**نصب:**
```bash
pip install together
```

---

### 4. **Cohere**
```
🔗 URL: https://cohere.com
💰 رایگان: 100 calls/min
📊 مدل‌ها: Command, Embed
```

---

### 5. **Hugging Face Inference API**
```
🔗 URL: https://huggingface.co/inference-api
💰 رایگان: محدود
📊 مدل‌ها: 1000+ مدل
```

---

### 6. **Mistral AI** (جدید!)
```
🔗 URL: https://console.mistral.ai
💰 رایگان: $5 credit
📊 مدل‌ها: 
   - Mistral-7B
   - Mixtral-8x7B
```

---

## 📊 Google Sheets API

```
🔗 URL: https://console.cloud.google.com
💰 رایگان: نامحدود
📝 نیاز: Service Account
```

---

## 🐦 Twitter API

```
🔗 URL: https://developer.twitter.com
💰 رایگان (Basic): 
   - 1,500 tweets/month
   - Read + Write
💰 Free tier جدید: $100/month
   - 10,000 tweets/month
```

---

## 📱 Telegram API

```
🔗 URL: https://my.telegram.org
💰 رایگان: کاملاً رایگان!
📊 محدودیت: 20 msg/sec
💾 Storage: 2GB per file رایگان
```

---

## 🗄️ Database (رایگان)

### 1. **Supabase**
```
🔗 URL: https://supabase.com
💰 رایگان: 
   - 500MB database
   - 1GB file storage
   - 50,000 monthly active users
```

### 2. **MongoDB Atlas**
```
🔗 URL: https://www.mongodb.com/cloud/atlas
💰 رایگان:
   - 512MB storage
   - Shared cluster
```

### 3. **PlanetScale**
```
🔗 URL: https://planetscale.com
💰 رایگان:
   - 10GB storage
   - 100M rows read/month
```

### 4. **Airtable**
```
🔗 URL: https://airtable.com
💰 رایگان:
   - 1,200 records per base
   - Unlimited bases
```

---

## ☁️ Cloud Storage (رایگان)

### 1. **Cloudflare R2**
```
🔗 URL: https://cloudflare.com/products/r2
💰 رایگان:
   - 10GB storage
   - No egress fees
```

### 2. **Backblaze B2**
```
🔗 URL: https://www.backblaze.com/b2
💰 رایگان:
   - 10GB storage
   - 1GB download/day
```

### 3. **Storj**
```
🔗 URL: https://www.storj.io
💰 رایگان:
   - 25GB storage
   - 25GB bandwidth
```

---

## 🔍 Search & Scraping

### 1. **SerpAPI** (Google Search)
```
🔗 URL: https://serpapi.com
💰 رایگان: 100 searches/month
```

### 2. **ScraperAPI**
```
🔗 URL: https://www.scraperapi.com
💰 رایگان: 1,000 requests/month
```

### 3. **Beautiful Soup + Requests**
```
💰 رایگان: کاملاً رایگان
⚠️ احتمال block شدن
```

---

## 📰 News APIs

### 1. **NewsAPI**
```
🔗 URL: https://newsapi.org
💰 رایگان: 100 requests/day
```

### 2. **Google News RSS**
```
💰 رایگان: نامحدود
🔗 URL: https://news.google.com/rss
```

### 3. **Reddit API**
```
🔗 URL: https://www.reddit.com/dev/api
💰 رایگان: 60 requests/min
```

---

## 🖼️ Image Generation

### 1. **Stable Diffusion (Hugging Face)**
```
🔗 URL: https://huggingface.co/spaces
💰 رایگان: محدود
```

### 2. **Replicate**
```
🔗 URL: https://replicate.com
💰 $0.006 per image (خیلی ارزون)
```

### 3. **Craiyon (DALL-E mini)**
```
🔗 URL: https://www.craiyon.com
💰 رایگان: با کیفیت پایین
```

---

## 🎙️ Voice & Audio

### 1. **ElevenLabs** (محدود رایگان)
```
🔗 URL: https://elevenlabs.io
💰 رایگان: 10,000 characters/month
```

### 2. **Google Cloud Text-to-Speech**
```
🔗 URL: https://cloud.google.com/text-to-speech
💰 رایگان: 1M characters/month
```

---

## 📧 Email

### 1. **SendGrid**
```
🔗 URL: https://sendgrid.com
💰 رایگان: 100 emails/day
```

### 2. **Mailgun**
```
🔗 URL: https://www.mailgun.com
💰 رایگان: 5,000 emails/month (3 months)
```

---

## 📊 Analytics

### 1. **Google Analytics**
```
💰 رایگان: کاملاً رایگان
```

### 2. **Plausible** (محدود)
```
🔗 URL: https://plausible.io
💰 رایگان: 30-day trial
```

---

## 🔐 Authentication

### 1. **Supabase Auth**
```
💰 رایگان: 50,000 users
```

### 2. **Auth0**
```
💰 رایگان: 7,000 active users
```

---

## 🌐 Hosting & Deployment

### 1. **Railway**
```
🔗 URL: https://railway.app
💰 رایگان: $5 credit/month
```

### 2. **Render**
```
🔗 URL: https://render.com
💰 رایگان: 750 hours/month
```

### 3. **Fly.io**
```
🔗 URL: https://fly.io
💰 رایگان: 3 VMs
```

### 4. **Vercel**
```
🔗 URL: https://vercel.com
💰 رایگان: Unlimited deployments
```

### 5. **Netlify**
```
🔗 URL: https://netlify.com
💰 رایگان: 100GB bandwidth
```

---

## 📱 SMS & Phone

### 1. **Twilio**
```
💰 رایگان: $15 trial credit
```

### 2. **Vonage**
```
💰 رایگان: €2 credit
```

---

## 🔔 Notifications

### 1. **OneSignal**
```
💰 رایگان: Unlimited
```

### 2. **Firebase Cloud Messaging**
```
💰 رایگان: Unlimited
```

---

## 🎨 Image/Video APIs

### 1. **Cloudinary**
```
💰 رایگان: 
   - 25GB storage
   - 25GB bandwidth
```

### 2. **ImageKit**
```
💰 رایگان:
   - 20GB bandwidth
   - 20GB storage
```

---

## 🗺️ Maps & Location

### 1. **Mapbox**
```
💰 رایگان: 50,000 requests/month
```

### 2. **OpenStreetMap** (Nominatim)
```
💰 رایگان: محدود
```

---

## 💱 Currency & Crypto

### 1. **ExchangeRate-API**
```
💰 رایگان: 1,500 requests/month
```

### 2. **CoinGecko**
```
💰 رایگان: 50 calls/min
```

---

## 🎯 پیشنهاد ترکیب برای نازنین

### Setup پیشنهادی (100% رایگان):

```json
{
  "ai": "Groq (سریع) + Gemini (قدرتمند)",
  "database": "Google Sheets + Supabase",
  "storage": "Telegram + Cloudflare R2",
  "hosting": "Railway یا Render",
  "news": "Google News RSS + NewsAPI",
  "search": "Google (manual scraping)",
  "analytics": "Google Analytics",
  "notifications": "Telegram"
}
```

---

## 📋 API Keys Management

**config.enhanced.json:**
```json
{
  "ai_apis": {
    "groq": {
      "keys": ["gsk_xxx1", "gsk_xxx2"],
      "model": "mixtral-8x7b-32768"
    },
    "gemini": {
      "keys": ["AIza_xxx1", "AIza_xxx2"],
      "model": "gemini-pro"
    },
    "together": {
      "keys": ["xxx"],
      "model": "mistralai/Mixtral-8x7B-Instruct-v0.1"
    }
  }
}
```

---

## ⚡ نکات مهم

### ✅ توصیه می‌شه:

1. چند کلید از هر سرویس بگیر (Load Balancing)
2. از Groq برای سرعت استفاده کن
3. از Gemini برای کیفیت استفاده کن
4. Telegram = بهترین storage رایگان
5. Google Sheets = بهترین database ساده

### ⚠️ هشدارها:

- Rate limit ها رو رعایت کن
- API key ها رو امن نگه دار
- از fallback استفاده کن
- استفاده رو monitor کن

---

**همه اینا رایگان! 🎉**
