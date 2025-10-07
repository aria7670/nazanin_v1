#!/usr/bin/env python3
"""
Google Sheets Initialization Script
اسکریپت راه‌اندازی و پر کردن خودکار اسپردشیت‌ها

این اسکریپت:
1. به Google Sheets متصل می‌شود
2. 15 اسپردشیت را بررسی می‌کند
3. شیت‌های لازم را می‌سازد
4. Headers را اضافه می‌کند
5. اطلاعات اولیه را وارد می‌کند
6. تست امنیتی انجام می‌دهد

استفاده:
    python initialize_sheets.py
"""

import asyncio
import json
import sys
import os
from pathlib import Path

# اضافه کردن به path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from nazanin.sheets_system import InitializationManager, get_summary


async def main():
    """نقطه ورود اصلی"""
    
    print("\n")
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║                                                               ║")
    print("║     📊 GOOGLE SHEETS INITIALIZATION SYSTEM 📊               ║")
    print("║         Nazanin v4.0 Advanced Edition                        ║")
    print("║                                                               ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    print("\n")
    
    # خواندن config
    config_path = 'config/config.json'
    
    if not os.path.exists(config_path):
        config_path = 'config/config.enhanced.json'
    
    if not os.path.exists(config_path):
        print("❌ Config file not found!")
        print("   Please create config/config.json")
        return
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
    except Exception as e:
        print(f"❌ Error loading config: {e}")
        return
    
    # دریافت تنظیمات sheets
    google_sheets_config = config.get('google_sheets', {})
    credentials_file = google_sheets_config.get('credentials_file', 'credentials.json')
    spreadsheets = google_sheets_config.get('spreadsheets', {})
    
    # بررسی credentials
    if not os.path.exists(credentials_file):
        print(f"❌ Credentials file not found: {credentials_file}")
        print("   Please download your Google Service Account credentials")
        return
    
    # بررسی spreadsheet IDs
    summary = get_summary()
    
    print(f"📋 Expected: {summary['total_spreadsheets']} spreadsheets")
    print(f"   Total sheets: {summary['total_sheets']}")
    print()
    
    if len(spreadsheets) == 0:
        print("❌ No spreadsheet IDs provided in config!")
        print()
        print("📝 Please add spreadsheet IDs to your config:")
        print()
        print("   \"google_sheets\": {")
        print("       \"credentials_file\": \"credentials.json\",")
        print("       \"spreadsheets\": {")
        
        for name in summary['spreadsheet_names']:
            print(f"           \"{name}\": \"YOUR_SPREADSHEET_ID_HERE\",")
        
        print("       }")
        print("   }")
        print()
        return
    
    if len(spreadsheets) < summary['total_spreadsheets']:
        print(f"⚠️  Warning: Only {len(spreadsheets)}/{summary['total_spreadsheets']} spreadsheets configured")
        print()
        print("Missing:")
        for name in summary['spreadsheet_names']:
            if name not in spreadsheets:
                print(f"   - {name}")
        print()
        
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            return
    
    # ساخت InitializationManager
    print("\n🚀 Starting initialization...\n")
    
    manager = InitializationManager(
        credentials_file=credentials_file,
        spreadsheet_ids=spreadsheets
    )
    
    # اجرای راه‌اندازی
    result = await manager.initialize_all()
    
    # نمایش نتایج
    print("\n")
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║                    FINAL RESULTS                              ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    print()
    
    if result['success']:
        print("✅ Initialization completed successfully!")
        print()
        print("📊 Summary:")
        print(f"   • Spreadsheets checked: {result['stats']['spreadsheets_checked']}")
        print(f"   • Sheets created: {result['stats']['sheets_created']}")
        print(f"   • Headers added: {result['stats']['headers_added']}")
        print(f"   • Rows inserted: {result['stats']['rows_inserted']}")
        print(f"   • Errors: {len(result['stats']['errors'])}")
        print(f"   • Duration: {result['duration']:.2f}s")
        print()
        
        if result['security']['all_passed']:
            print("🔐 Security tests: ✅ ALL PASSED")
        else:
            print(f"⚠️  Security tests: {result['security']['tests_passed']}/{result['security']['tests_total']} passed")
        
        print()
        print("═" * 63)
        print()
        print("✨ Your Google Sheets are ready!")
        print("   You can now run Nazanin with: python run_v4.py")
        print()
        
    else:
        print("❌ Initialization failed!")
        print()
        print(f"Error: {result.get('error', 'Unknown error')}")
        print()
        
        if result['stats']['errors']:
            print("Errors encountered:")
            for error in result['stats']['errors'][:5]:
                print(f"   • {error}")
            
            if len(result['stats']['errors']) > 5:
                print(f"   ... and {len(result['stats']['errors']) - 5} more")
    
    print()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
