#!/usr/bin/env python3
"""
Nazanin v5.0.0 - Complete Edition Runner
نازنین نسخه 5.0 - اجرا

این نسخه شامل همه چیز است:
✅ مغز عصبی 12 لایه + ادراک
✅ خودمختاری کامل
✅ 30 ماژول + 30 ایجنت + 50 الگوریتم
✅ ByteLine Bot
✅ Bio + Consciousness
✅ Google Sheets System (15 اسپردشیت)

استفاده:
    python run_v5.py
"""

import asyncio
import sys
import os

# اضافه کردن به path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from nazanin.app_v5_complete import NazaninV5Complete, main

if __name__ == '__main__':
    try:
        print("\n🚀 Starting Nazanin v5.0.0 Complete Edition...\n")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 خداحافظ! Goodbye!")
    except Exception as e:
        print(f"\n\n❌ خطا! Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
