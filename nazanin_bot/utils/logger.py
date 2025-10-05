"""
Logger - سیستم ثبت لاگ
"""

import logging
import sys
from pathlib import Path
from datetime import datetime


def setup_logger(name: str = 'nazanin_bot', level: str = 'INFO', log_file: str = None) -> logging.Logger:
    """
    راه‌اندازی لاگر
    
    Args:
        name: نام لاگر
        level: سطح لاگ (DEBUG, INFO, WARNING, ERROR)
        log_file: مسیر فایل لاگ (اختیاری)
        
    Returns:
        لاگر پیکربندی شده
    """
    logger = logging.getLogger(name)
    
    # تنظیم سطح
    log_level = getattr(logging, level.upper(), logging.INFO)
    logger.setLevel(log_level)
    
    # فرمت لاگ
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Handler برای کنسول
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # Handler برای فایل (اختیاری)
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger
