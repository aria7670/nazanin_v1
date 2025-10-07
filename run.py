#!/usr/bin/env python3
"""
ساده‌ترین راه برای اجرای نازنین-نورا
Simplest way to run Nazanin-Nora

استفاده:
    python run.py
"""

import asyncio
from nazanin.app import main

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 خداحافظ! Goodbye!")
    except Exception as e:
        print(f"\n❌ خطا! Error: {e}")
        import traceback
        traceback.print_exc()
