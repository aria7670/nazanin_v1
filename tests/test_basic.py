"""
Basic Test Script
Quick verification that all modules can be imported
"""

import sys
import os

# Add parent directory to Python path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_imports():
    """Test that all modules can be imported"""
    
    print("🧪 Testing module imports...\n")
    
    modules_to_test = [
        ('src.core.sheets_manager', 'SheetsManager'),
        ('src.core.api_manager', 'APIManager'),
        ('src.agents.agents', 'AgentOrchestrator'),
        ('src.platforms.twitter_system', 'TwitterSystem'),
        ('src.platforms.telegram_system', 'TelegramSystem'),
        ('src.ai.brain_simulation', 'BrainSimulation'),
        ('src.ai.quantum_agent', 'QuantumAgent'),
        ('src.ai.neural_agent', 'NeuralAgent'),
    ]
    
    results = []
    
    for module_name, class_name in modules_to_test:
        try:
            # Use importlib for better import handling
            import importlib
            parts = module_name.split('.')
            module = importlib.import_module(module_name)
            
            # Navigate to the class
            obj = module
            for part in parts[1:]:
                if hasattr(obj, part):
                    obj = getattr(obj, part)
            
            if hasattr(obj, class_name):
                cls = getattr(obj, class_name)
                results.append((module_name, '✅ OK'))
                print(f"✅ {module_name}.{class_name}")
            else:
                # Try to get it from module directly
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
        import os
        
        # Check multiple possible config locations
        config_paths = ['config/config.json', 'config.json']
        config_data = None
        config_path_used = None
        
        for path in config_paths:
            if os.path.exists(path):
                with open(path, 'r') as f:
                    config_data = json.load(f)
                config_path_used = path
                break
        
        if config_data is None:
            raise FileNotFoundError("config.json not found")
        
        config = config_data
        print(f"✅ Config loaded from: {config_path_used}")
        
        required_keys = ['telegram', 'twitter', 'google_sheets', 
                        'brain_simulation', 'quantum_agent', 'neural_agent']
        
        for key in required_keys:
            if key in config:
                print(f"✅ {key} config found")
            else:
                print(f"⚠️ {key} config missing")
        
        return True
        
    except FileNotFoundError:
        print("⚠️ config.json not found in config/ or root")
        print("💡 Copy config/config.example.json to config/config.json")
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
