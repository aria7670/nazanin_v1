"""
Security Manager - مدیریت امنیت
"""

import hashlib
import hmac
import secrets
import time
import logging
from typing import Dict, List, Optional
from datetime import datetime, timedelta
import json

logger = logging.getLogger(__name__)


class SecurityManager:
    """مدیریت امنیت و کنترل دسترسی"""
    
    def __init__(self, config: Dict):
        self.config = config.get('security', {})
        self.rate_limiter = RateLimiter(self.config.get('rate_limiting', {}))
        self.access_control = AccessControl(self.config)
        self.encryption = DataEncryption(self.config)
        self.audit_logger = AuditLogger()
        
        logger.info("✅ Security Manager initialized")
    
    def check_access(self, user_id: int, action: str) -> bool:
        """بررسی دسترسی"""
        return self.access_control.check_permission(user_id, action)
    
    def check_rate_limit(self, user_id: int) -> bool:
        """بررسی محدودیت نرخ"""
        return self.rate_limiter.check(user_id)
    
    def encrypt_data(self, data: str) -> str:
        """رمزنگاری داده"""
        if self.config.get('encryption_enabled', True):
            return self.encryption.encrypt(data)
        return data
    
    def decrypt_data(self, encrypted_data: str) -> str:
        """رمزگشایی داده"""
        if self.config.get('encryption_enabled', True):
            return self.encryption.decrypt(encrypted_data)
        return encrypted_data
    
    def log_action(self, user_id: int, action: str, details: Dict):
        """ثبت عملیات"""
        if self.config.get('log_all_actions', True):
            self.audit_logger.log(user_id, action, details)
    
    def detect_suspicious_activity(self, user_id: int, activity: Dict) -> bool:
        """تشخیص فعالیت مشکوک"""
        # بررسی الگوهای مشکوک
        suspicious = False
        
        # 1. تعداد زیاد request در مدت کوتاه
        if self.rate_limiter.get_count(user_id) > 100:
            suspicious = True
            logger.warning(f"⚠️ High request rate from user {user_id}")
        
        # 2. تلاش برای دسترسی غیرمجاز
        if activity.get('unauthorized_attempts', 0) > 5:
            suspicious = True
            logger.warning(f"⚠️ Multiple unauthorized attempts from {user_id}")
        
        # 3. IP تغییر مکرر
        if activity.get('ip_changes', 0) > 10:
            suspicious = True
            logger.warning(f"⚠️ Frequent IP changes from {user_id}")
        
        if suspicious and self.config.get('alert_on_suspicious', True):
            self.audit_logger.log_security_event(user_id, 'suspicious_activity', activity)
        
        return suspicious


class RateLimiter:
    """محدودسازی نرخ درخواست"""
    
    def __init__(self, config: Dict):
        self.enabled = config.get('enabled', True)
        self.max_per_minute = config.get('max_requests_per_minute', 60)
        self.max_per_hour = config.get('max_requests_per_hour', 1000)
        
        self.minute_counts = {}  # {user_id: [(timestamp, count)]}
        self.hour_counts = {}
    
    def check(self, user_id: int) -> bool:
        """بررسی آیا کاربر از حد مجاز رد نشده"""
        if not self.enabled:
            return True
        
        now = time.time()
        
        # بررسی per minute
        minute_count = self._get_count(user_id, now, 60, self.minute_counts)
        if minute_count >= self.max_per_minute:
            logger.warning(f"⚠️ Rate limit exceeded (per minute) for user {user_id}")
            return False
        
        # بررسی per hour
        hour_count = self._get_count(user_id, now, 3600, self.hour_counts)
        if hour_count >= self.max_per_hour:
            logger.warning(f"⚠️ Rate limit exceeded (per hour) for user {user_id}")
            return False
        
        # اضافه کردن request جدید
        self._add_request(user_id, now)
        
        return True
    
    def get_count(self, user_id: int) -> int:
        """دریافت تعداد درخواست‌ها در دقیقه اخیر"""
        now = time.time()
        return self._get_count(user_id, now, 60, self.minute_counts)
    
    def _get_count(self, user_id: int, now: float, window: int, counts_dict: Dict) -> int:
        """محاسبه تعداد درخواست‌ها در بازه زمانی"""
        if user_id not in counts_dict:
            return 0
        
        # حذف request های قدیمی
        cutoff = now - window
        counts_dict[user_id] = [
            (ts, count) for ts, count in counts_dict[user_id]
            if ts > cutoff
        ]
        
        return sum(count for _, count in counts_dict[user_id])
    
    def _add_request(self, user_id: int, timestamp: float):
        """اضافه کردن درخواست جدید"""
        for counts_dict in [self.minute_counts, self.hour_counts]:
            if user_id not in counts_dict:
                counts_dict[user_id] = []
            counts_dict[user_id].append((timestamp, 1))


class AccessControl:
    """کنترل دسترسی"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.admin_users = set()
        self.blocked_users = set()
        self.user_permissions = {}  # {user_id: [permissions]}
    
    def add_admin(self, user_id: int):
        """افزودن ادمین"""
        self.admin_users.add(user_id)
        logger.info(f"✅ User {user_id} added as admin")
    
    def block_user(self, user_id: int, reason: str = ""):
        """مسدود کردن کاربر"""
        self.blocked_users.add(user_id)
        logger.warning(f"🚫 User {user_id} blocked. Reason: {reason}")
    
    def unblock_user(self, user_id: int):
        """رفع مسدودیت کاربر"""
        self.blocked_users.discard(user_id)
        logger.info(f"✅ User {user_id} unblocked")
    
    def is_admin(self, user_id: int) -> bool:
        """بررسی ادمین بودن"""
        return user_id in self.admin_users
    
    def is_blocked(self, user_id: int) -> bool:
        """بررسی مسدود بودن"""
        return user_id in self.blocked_users
    
    def check_permission(self, user_id: int, action: str) -> bool:
        """بررسی دسترسی برای انجام عملیات"""
        # کاربران مسدود شده دسترسی ندارن
        if self.is_blocked(user_id):
            return False
        
        # ادمین‌ها همه دسترسی دارن
        if self.is_admin(user_id):
            return True
        
        # بررسی دسترسی‌های خاص
        user_perms = self.user_permissions.get(user_id, [])
        return action in user_perms or 'all' in user_perms
    
    def grant_permission(self, user_id: int, permission: str):
        """اعطای دسترسی"""
        if user_id not in self.user_permissions:
            self.user_permissions[user_id] = []
        if permission not in self.user_permissions[user_id]:
            self.user_permissions[user_id].append(permission)


class DataEncryption:
    """رمزنگاری داده"""
    
    def __init__(self, config: Dict):
        self.enabled = config.get('encryption_enabled', True)
        # در واقعیت از یک کلید امن استفاده کنید
        self.secret_key = config.get('encryption_key', 'default_secret_key_change_me')
    
    def encrypt(self, data: str) -> str:
        """رمزنگاری ساده (در production از AES استفاده کنید)"""
        if not self.enabled:
            return data
        
        # استفاده از HMAC برای رمزنگاری ساده
        # در production از cryptography.fernet استفاده کنید
        import base64
        
        key = self.secret_key.encode()
        msg = data.encode()
        
        h = hmac.new(key, msg, hashlib.sha256)
        encrypted = base64.b64encode(h.digest() + msg).decode()
        
        return encrypted
    
    def decrypt(self, encrypted_data: str) -> str:
        """رمزگشایی"""
        if not self.enabled:
            return encrypted_data
        
        try:
            import base64
            
            data = base64.b64decode(encrypted_data.encode())
            mac = data[:32]  # SHA256 = 32 bytes
            msg = data[32:]
            
            # تأیید HMAC
            key = self.secret_key.encode()
            h = hmac.new(key, msg, hashlib.sha256)
            
            if h.digest() != mac:
                raise ValueError("Invalid MAC")
            
            return msg.decode()
        except Exception as e:
            logger.error(f"❌ Decryption failed: {e}")
            return encrypted_data


class AuditLogger:
    """ثبت لاگ‌های امنیتی"""
    
    def __init__(self):
        self.logs = []
        self.security_events = []
    
    def log(self, user_id: int, action: str, details: Dict):
        """ثبت عملیات"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'user_id': user_id,
            'action': action,
            'details': details
        }
        self.logs.append(log_entry)
        
        # نگه‌داری فقط 10000 لاگ اخیر
        if len(self.logs) > 10000:
            self.logs = self.logs[-10000:]
        
        logger.debug(f"📝 Logged: {user_id} - {action}")
    
    def log_security_event(self, user_id: int, event_type: str, details: Dict):
        """ثبت رویداد امنیتی"""
        event = {
            'timestamp': datetime.now().isoformat(),
            'user_id': user_id,
            'event_type': event_type,
            'severity': 'high',
            'details': details
        }
        self.security_events.append(event)
        
        logger.warning(f"🚨 Security event: {event_type} - User {user_id}")
    
    def get_logs(self, user_id: Optional[int] = None, limit: int = 100) -> List[Dict]:
        """دریافت لاگ‌ها"""
        logs = self.logs
        
        if user_id is not None:
            logs = [log for log in logs if log['user_id'] == user_id]
        
        return logs[-limit:]
    
    def get_security_events(self, limit: int = 100) -> List[Dict]:
        """دریافت رویدادهای امنیتی"""
        return self.security_events[-limit:]


# استفاده نمونه
if __name__ == '__main__':
    config = {
        'security': {
            'encryption_enabled': True,
            'rate_limiting': {
                'enabled': True,
                'max_requests_per_minute': 60,
                'max_requests_per_hour': 1000
            }
        }
    }
    
    security = SecurityManager(config)
    
    # تست rate limiting
    for i in range(65):
        allowed = security.check_rate_limit(12345)
        if not allowed:
            print(f"Rate limit exceeded at request {i+1}")
            break
    
    # تست encryption
    data = "sensitive information"
    encrypted = security.encrypt_data(data)
    decrypted = security.decrypt_data(encrypted)
    print(f"Original: {data}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
