#!/usr/bin/env python3
"""
تست ساختار جدید پروژه
Test script for new project structure
"""

import sys
import os

# اضافه کردن پوشه root به path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """تست import های اصلی"""
    print("🧪 Testing imports...")
    print()
    
    tests = []
    
    # Test 1: Main app
    try:
        from nazanin import NazaninNora
        print("✅ Test 1: from nazanin import NazaninNora")
        tests.append(True)
    except Exception as e:
        print(f"❌ Test 1 Failed: {e}")
        tests.append(False)
    
    # Test 2: Bio system
    try:
        from nazanin.bio_system import Organism
        print("✅ Test 2: from nazanin.bio_system import Organism")
        tests.append(True)
    except Exception as e:
        print(f"❌ Test 2 Failed: {e}")
        tests.append(False)
    
    # Test 3: Consciousness
    try:
        from nazanin.consciousness import MetacognitionEngine
        print("✅ Test 3: from nazanin.consciousness import MetacognitionEngine")
        tests.append(True)
    except Exception as e:
        print(f"❌ Test 3 Failed: {e}")
        tests.append(False)
    
    # Test 4: Core
    try:
        from nazanin.core import SheetsManagerV2, APIManagerV2
        print("✅ Test 4: from nazanin.core import SheetsManagerV2, APIManagerV2")
        tests.append(True)
    except Exception as e:
        print(f"❌ Test 4 Failed: {e}")
        tests.append(False)
    
    # Test 5: Domain Agents
    try:
        from nazanin.domain_agents import DomainAgentOrchestrator
        print("✅ Test 5: from nazanin.domain_agents import DomainAgentOrchestrator")
        tests.append(True)
    except Exception as e:
        print(f"❌ Test 5 Failed: {e}")
        tests.append(False)
    
    # Test 6: Security
    try:
        from nazanin.security import SecurityManager
        print("✅ Test 6: from nazanin.security import SecurityManager")
        tests.append(True)
    except Exception as e:
        print(f"❌ Test 6 Failed: {e}")
        tests.append(False)
    
    # Test 7: __main__
    try:
        import nazanin.__main__
        print("✅ Test 7: import nazanin.__main__")
        tests.append(True)
    except Exception as e:
        print(f"❌ Test 7 Failed: {e}")
        tests.append(False)
    
    print()
    print("=" * 60)
    print(f"📊 نتیجه: {sum(tests)}/{len(tests)} تست موفق")
    print("=" * 60)
    
    if all(tests):
        print("🎉 همه تست‌ها موفق! ساختار کامل و صحیح است!")
        return True
    else:
        print("⚠️ برخی تست‌ها ناموفق! نیاز به بررسی بیشتر.")
        return False


def test_structure():
    """تست ساختار پوشه‌ها"""
    print("\n🗂️ Testing directory structure...")
    print()
    
    required_dirs = [
        'nazanin',
        'nazanin/bio_system',
        'nazanin/consciousness',
        'nazanin/core',
        'nazanin/domain_agents',
        'nazanin/platforms',
        'nazanin/security',
        'config',
        'docs',
        'tests'
    ]
    
    all_exist = True
    for directory in required_dirs:
        if os.path.isdir(directory):
            print(f"✅ {directory}")
        else:
            print(f"❌ {directory} - وجود ندارد!")
            all_exist = False
    
    print()
    if all_exist:
        print("✅ تمام پوشه‌های ضروری وجود دارند")
    else:
        print("❌ برخی پوشه‌ها وجود ندارند")
    
    return all_exist


def test_files():
    """تست وجود فایل‌های مهم"""
    print("\n📄 Testing important files...")
    print()
    
    required_files = [
        'nazanin/__init__.py',
        'nazanin/__main__.py',
        'nazanin/app.py',
        'run.py',
        'requirements.txt',
        'README.md',
        'config/config.enhanced.json'
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.isfile(file):
            size = os.path.getsize(file)
            print(f"✅ {file} ({size} bytes)")
        else:
            print(f"❌ {file} - وجود ندارد!")
            all_exist = False
    
    print()
    if all_exist:
        print("✅ تمام فایل‌های مهم وجود دارند")
    else:
        print("❌ برخی فایل‌ها وجود ندارند")
    
    return all_exist


if __name__ == '__main__':
    print("\n")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║           🧪 تست ساختار پروژه نازنین-نورا                ║")
    print("║           Project Structure Test                           ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print()
    
    # اجرای تست‌ها
    structure_ok = test_structure()
    files_ok = test_files()
    imports_ok = test_imports()
    
    print("\n")
    print("=" * 60)
    print("📋 نتیجه نهایی:")
    print("=" * 60)
    print(f"   ساختار پوشه‌ها: {'✅ OK' if structure_ok else '❌ FAIL'}")
    print(f"   فایل‌های مهم: {'✅ OK' if files_ok else '❌ FAIL'}")
    print(f"   Import ها: {'✅ OK' if imports_ok else '❌ FAIL'}")
    print("=" * 60)
    
    if structure_ok and files_ok and imports_ok:
        print("\n🎉 همه چیز عالیه! پروژه آماده اجراست!")
        sys.exit(0)
    else:
        print("\n⚠️ برخی مشکلات وجود دارد. لطفاً بررسی کنید.")
        sys.exit(1)
