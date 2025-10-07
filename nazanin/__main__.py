"""
Entry point for python -m nazanin
نقطه ورود برای اجرا با python -m nazanin
"""

import asyncio
from nazanin.app import main

if __name__ == '__main__':
    asyncio.run(main())
