# 🚀 راهنمای Deploy کردن Nazanin

راهنمای کامل برای deploy کردن ربات Nazanin در محیط‌های مختلف

---

## 📋 فهرست

- [Local Development](#local-development)
- [Docker](#docker)
- [VPS/Cloud Server](#vpscloud-server)
- [Heroku](#heroku)
- [AWS](#aws)
- [Google Cloud](#google-cloud)
- [Monitoring](#monitoring)

---

## 💻 Local Development

### نصب ساده:
```bash
# Clone
git clone https://github.com/aria7670/nazanin_v1.git
cd nazanin_v1

# اجرای اسکریپت نصب
bash run.sh
```

### نصب دستی:
```bash
# Virtual environment
python3 -m venv venv
source venv/bin/activate

# Dependencies
pip install -r requirements.txt

# Config
cp config/config.example.json config/config.json
# ویرایش config.json

# اجرا
python main_advanced.py
```

---

## 🐳 Docker

### ساخت Image:
```bash
docker build -t nazanin-ai-bot .
```

### اجرا با Docker:
```bash
docker run -d \
  --name nazanin \
  -v $(pwd)/config:/app/config \
  -v $(pwd)/logs:/app/logs \
  -v $(pwd)/credentials.json:/app/credentials.json \
  --restart unless-stopped \
  nazanin-ai-bot
```

### اجرا با Docker Compose:
```bash
# Start
docker-compose up -d

# Logs
docker-compose logs -f

# Stop
docker-compose down

# Restart
docker-compose restart
```

### Logs:
```bash
docker logs -f nazanin
```

---

## 🖥️ VPS/Cloud Server

### امکانات مورد نیاز:
- **RAM**: حداقل 2GB (پیشنهاد 4GB)
- **CPU**: 2 cores
- **Storage**: 10GB
- **OS**: Ubuntu 20.04+ / Debian 10+

### نصب روی Ubuntu:

#### 1. آماده‌سازی:
```bash
# Update
sudo apt update && sudo apt upgrade -y

# Dependencies
sudo apt install -y python3 python3-pip python3-venv git

# Clone project
git clone https://github.com/aria7670/nazanin_v1.git
cd nazanin_v1
```

#### 2. نصب:
```bash
# Virtual environment
python3 -m venv venv
source venv/bin/activate

# Install
pip install -r requirements.txt

# Config
cp config/config.example.json config/config.json
nano config/config.json  # ویرایش
```

#### 3. اجرا با systemd (پیشنهادی):

ساخت service file:
```bash
sudo nano /etc/systemd/system/nazanin.service
```

محتوا:
```ini
[Unit]
Description=Nazanin AI Bot
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/nazanin_v1
Environment="PATH=/home/ubuntu/nazanin_v1/venv/bin"
ExecStart=/home/ubuntu/nazanin_v1/venv/bin/python main_advanced.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

فعال‌سازی:
```bash
sudo systemctl daemon-reload
sudo systemctl enable nazanin
sudo systemctl start nazanin
sudo systemctl status nazanin
```

مدیریت:
```bash
# Start
sudo systemctl start nazanin

# Stop
sudo systemctl stop nazanin

# Restart
sudo systemctl restart nazanin

# Logs
sudo journalctl -u nazanin -f
```

#### 4. استفاده از Screen (جایگزین):
```bash
# نصب screen
sudo apt install screen

# ساخت session
screen -S nazanin

# اجرا
python main_advanced.py

# Detach: Ctrl+A, D
# Attach: screen -r nazanin
```

---

## 🌐 Heroku

### 1. آماده‌سازی:

ساخت `Procfile`:
```
worker: python main_advanced.py
```

ساخت `runtime.txt`:
```
python-3.10.8
```

### 2. Deploy:
```bash
# نصب Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# ساخت app
heroku create nazanin-ai-bot

# Set config
heroku config:set TELEGRAM_BOT_TOKEN=your_token
heroku config:set TWITTER_API_KEY=your_key
# ... سایر configs

# Deploy
git push heroku main

# Scale worker
heroku ps:scale worker=1

# Logs
heroku logs --tail
```

---

## ☁️ AWS

### روی EC2:

#### 1. Launch EC2:
- AMI: Ubuntu 20.04
- Instance Type: t3.medium (2 vCPU, 4GB RAM)
- Storage: 20GB

#### 2. نصب:
همون دستورات VPS رو اجرا کن

#### 3. Auto Scaling (اختیاری):
- استفاده از Auto Scaling Groups
- Load Balancer برای multiple instances

---

## 🔵 Google Cloud

### روی Compute Engine:

#### 1. ساخت VM:
```bash
gcloud compute instances create nazanin-bot \
  --machine-type=e2-medium \
  --image-family=ubuntu-2004-lts \
  --image-project=ubuntu-os-cloud \
  --boot-disk-size=20GB
```

#### 2. SSH و نصب:
```bash
gcloud compute ssh nazanin-bot

# بعد دستورات VPS
```

---

## 📊 Monitoring

### 1. Logs:

#### Application logs:
```python
# در config
LOG_FILE=nazanin.log
LOG_LEVEL=INFO
```

#### systemd logs:
```bash
journalctl -u nazanin -f
```

### 2. Health Check:

ساخت `health_check.sh`:
```bash
#!/bin/bash

if pgrep -f "python.*main_advanced.py" > /dev/null
then
    echo "✅ Nazanin is running"
    exit 0
else
    echo "❌ Nazanin is not running"
    systemctl restart nazanin
    exit 1
fi
```

Cron job:
```bash
crontab -e

# Check every 5 minutes
*/5 * * * * /home/ubuntu/nazanin_v1/health_check.sh
```

### 3. Resource Monitoring:

```bash
# htop
sudo apt install htop
htop

# Memory usage
free -h

# Disk usage
df -h
```

---

## 🔒 امنیت

### 1. Firewall:
```bash
# UFW
sudo ufw allow 22/tcp  # SSH
sudo ufw enable
```

### 2. محدود کردن SSH:
```bash
# فقط با SSH key
sudo nano /etc/ssh/sshd_config
# PasswordAuthentication no
sudo systemctl restart sshd
```

### 3. Environment Variables:
```bash
# استفاده از .env به جای config.json
# نگه داشتن credentials امن
```

---

## 🔄 Backup

### 1. Config و Data:
```bash
#!/bin/bash
# backup.sh

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backups/nazanin_$DATE"

mkdir -p $BACKUP_DIR
cp -r config $BACKUP_DIR/
cp -r data $BACKUP_DIR/
cp credentials.json $BACKUP_DIR/

tar -czf $BACKUP_DIR.tar.gz $BACKUP_DIR
rm -rf $BACKUP_DIR

echo "Backup created: $BACKUP_DIR.tar.gz"
```

### 2. Automated Backup (cron):
```bash
crontab -e

# Daily backup at 2 AM
0 2 * * * /home/ubuntu/nazanin_v1/backup.sh
```

---

## 🆘 Troubleshooting

### ربات start نمی‌شه:
```bash
# چک کردن logs
journalctl -u nazanin -n 50

# چک کردن config
python -m json.tool config/config.json

# چک کردن dependencies
pip list
```

### Memory issues:
```bash
# افزایش swap
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

### Port conflicts:
```bash
# پیدا کردن process
sudo lsof -i :8080
sudo kill -9 PID
```

---

## 📚 منابع بیشتر

- [Docker Documentation](https://docs.docker.com/)
- [systemd Guide](https://www.freedesktop.org/wiki/Software/systemd/)
- [AWS EC2 Guide](https://docs.aws.amazon.com/ec2/)
- [Heroku Python](https://devcenter.heroku.com/articles/python-support)

---

**موفق باشی! 🚀**
