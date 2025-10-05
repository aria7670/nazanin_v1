"""
Time Utils - ابزارهای زمان
"""

from datetime import datetime, timedelta
from typing import Optional


class TimeUtils:
    """ابزارهای کار با زمان"""
    
    @staticmethod
    def get_time_of_day() -> str:
        """
        دریافت زمان روز
        
        Returns:
            morning, afternoon, evening, night
        """
        hour = datetime.now().hour
        
        if 5 <= hour < 12:
            return 'morning'
        elif 12 <= hour < 17:
            return 'afternoon'
        elif 17 <= hour < 21:
            return 'evening'
        else:
            return 'night'
    
    @staticmethod
    def get_greeting_for_time() -> str:
        """
        دریافت سلام مناسب بر اساس زمان
        
        Returns:
            پیام سلام
        """
        time_of_day = TimeUtils.get_time_of_day()
        
        greetings = {
            'morning': 'Good morning',
            'afternoon': 'Good afternoon',
            'evening': 'Good evening',
            'night': 'Good evening'
        }
        
        return greetings.get(time_of_day, 'Hello')
    
    @staticmethod
    def format_duration(seconds: float) -> str:
        """
        فرمت زمان به صورت خوانا
        
        Args:
            seconds: ثانیه
            
        Returns:
            رشته فرمت شده
        """
        if seconds < 60:
            return f"{seconds:.1f}s"
        elif seconds < 3600:
            minutes = seconds / 60
            return f"{minutes:.1f}m"
        else:
            hours = seconds / 3600
            return f"{hours:.1f}h"
    
    @staticmethod
    def time_since(timestamp: datetime) -> str:
        """
        زمان گذشته از یک timestamp
        
        Args:
            timestamp: زمان
            
        Returns:
            توضیح زمان گذشته
        """
        now = datetime.now()
        delta = now - timestamp
        
        seconds = delta.total_seconds()
        
        if seconds < 60:
            return "just now"
        elif seconds < 3600:
            minutes = int(seconds / 60)
            return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
        elif seconds < 86400:
            hours = int(seconds / 3600)
            return f"{hours} hour{'s' if hours > 1 else ''} ago"
        else:
            days = int(seconds / 86400)
            return f"{days} day{'s' if days > 1 else ''} ago"
    
    @staticmethod
    def should_sleep(current_hour: Optional[int] = None) -> bool:
        """
        بررسی اینکه آیا ربات باید بخوابد
        
        Args:
            current_hour: ساعت فعلی (اختیاری)
            
        Returns:
            نیاز به خواب یا خیر
        """
        if current_hour is None:
            current_hour = datetime.now().hour
        
        # ساعت خواب: 2 صبح تا 5 صبح
        return 2 <= current_hour < 5
