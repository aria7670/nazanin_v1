#!/usr/bin/env python3
"""
Nazanin v4.0.0 - Advanced Edition Runner
نازنین نسخه 4.0 - اجرا

قابلیت‌ها:
✅ مغز عصبی 12 لایه
✅ ادراک و آگاهی بالا  
✅ خودمختاری کامل
✅ 30 ماژول + 30 ایجنت + 50 الگوریتم
✅ ByteLine Bot (Frontend انگلیسی + Backend فارسی)
✅ Bio + Consciousness Systems

استفاده:
    python run_v4.py
"""

import asyncio
import sys

# اضافه کردن به path
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from nazanin.app_v4_advanced import NazaninV4Advanced, main

if __name__ == '__main__':
    try:
        print("\n🚀 Starting Nazanin v4.0.0 Advanced Edition...\n")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 خداحافظ! Goodbye!")
    except Exception as e:
        print(f"\n\n❌ خطا! Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
