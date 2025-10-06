"""
Basic Test Script
Quick verification that all modules can be imported
"""

import sys

def test_imports():
    """Test that all modules can be imported"""
    
    print("🧪 Testing module imports...\n")
    
    modules_to_test = [
        ('sheets_manager', 'SheetsManager'),
        ('api_manager', 'APIManager'),
        ('agents', 'AgentOrchestrator'),
        ('twitter_system', 'TwitterSystem'),
        ('telegram_system', 'TelegramSystem'),
        ('brain_simulation', 'BrainSimulation'),
        ('quantum_agent', 'QuantumAgent'),
        ('neural_agent', 'NeuralAgent'),
    ]
    
    results = []
    
    for module_name, class_name in modules_to_test:
        try:
            module = __import__(module_name)
            cls = getattr(module, class_name)
            results.append((module_name, '✅ OK'))
            print(f"✅ {module_name}.{class_name}")
        except Exception as e:
            results.append((module_name, f'❌ {str(e)}'))
            print(f"❌ {module_name}: {str(e)}")
    
    print("\n" + "="*60)
    
    success_count = sum(1 for _, status in results if status == '✅ OK')
    total_count = len(results)
    
    print(f"\n📊 Results: {success_count}/{total_count} modules OK")
    
    if success_count == total_count:
        print("✅ All modules imported successfully!")
        return True
    else:
        print("⚠️ Some modules failed to import")
        return False


def test_config():
    """Test config file"""
    
    print("\n🔧 Testing configuration...\n")
    
    try:
        import json
        with open('config.json', 'r') as f:
            config = json.load(f)
        
        required_keys = ['telegram', 'twitter', 'google_sheets', 
                        'brain_simulation', 'quantum_agent', 'neural_agent']
        
        for key in required_keys:
            if key in config:
                print(f"✅ {key} config found")
            else:
                print(f"⚠️ {key} config missing")
        
        return True
        
    except FileNotFoundError:
        print("⚠️ config.json not found")
        print("💡 Copy config.example.json to config.json")
        return False
    except Exception as e:
        print(f"❌ Error reading config: {e}")
        return False


def test_requirements():
    """Test that key requirements are installed"""
    
    print("\n📦 Testing key dependencies...\n")
    
    packages = [
        'asyncio',
        'logging',
        'json',
        'datetime',
        'numpy',
    ]
    
    success = 0
    
    for package in packages:
        try:
            __import__(package)
            print(f"✅ {package}")
            success += 1
        except ImportError:
            print(f"❌ {package} not found")
    
    print(f"\n📊 {success}/{len(packages)} packages available")
    
    return success == len(packages)


def main():
    """Run all tests"""
    
    print("\n" + "="*60)
    print("🧪 NAZANIN BASIC TESTS")
    print("="*60 + "\n")
    
    test_results = []
    
    # Test imports
    test_results.append(('Imports', test_imports()))
    
    # Test config
    test_results.append(('Config', test_config()))
    
    # Test requirements
    test_results.append(('Dependencies', test_requirements()))
    
    # Summary
    print("\n" + "="*60)
    print("📊 SUMMARY")
    print("="*60 + "\n")
    
    for test_name, passed in test_results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    all_passed = all(result for _, result in test_results)
    
    print("\n" + "="*60)
    
    if all_passed:
        print("✅ ALL TESTS PASSED!")
        print("\n💡 Next steps:")
        print("   1. Run: python demo.py")
        print("   2. Or: python main.py")
    else:
        print("⚠️ SOME TESTS FAILED")
        print("\n💡 Check:")
        print("   1. Install requirements: pip install -r requirements.txt")
        print("   2. Copy config: cp config.example.json config.json")
    
    print("="*60 + "\n")
    
    return 0 if all_passed else 1


if __name__ == '__main__':
    sys.exit(main())
