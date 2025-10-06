"""
Body Systems - دستگاه‌های بدن
"""

import asyncio
import logging
from typing import Dict, List, Any
from .cell_system import Organ, Brain, Heart, Lungs

logger = logging.getLogger(__name__)


class BodySystem:
    """سیستم (دستگاه) - مجموعه اندام‌ها"""
    
    def __init__(self, system_id: str, system_type: str, function: str):
        self.system_id = system_id
        self.system_type = system_type
        self.function = function
        
        self.organs: Dict[str, Organ] = {}
        self.health = 100.0
        self.efficiency = 1.0
        self.is_active = True
    
    def add_organ(self, organ: Organ):
        """اضافه کردن اندام"""
        self.organs[organ.organ_id] = organ
    
    async def coordinate_organs(self):
        """هماهنگی اندام‌ها"""
        if not self.is_active:
            return
        
        # اجرای وظیفه هر اندام
        results = {}
        for organ_id, organ in self.organs.items():
            result = await organ.perform_function()
            results[organ_id] = result
        
        # محاسبه سلامت سیستم
        if self.organs:
            organ_healths = [o.health for o in self.organs.values()]
            self.health = sum(organ_healths) / len(organ_healths)
            self.efficiency = self.health / 100
        
        return results
    
    def get_status(self) -> Dict:
        """وضعیت سیستم"""
        return {
            'id': self.system_id,
            'type': self.system_type,
            'organs_count': len(self.organs),
            'health': round(self.health, 2),
            'efficiency': round(self.efficiency, 2),
            'active': self.is_active
        }


class NervousSystem(BodySystem):
    """دستگاه عصبی - کنترل و هماهنگی"""
    
    def __init__(self):
        super().__init__('nervous_001', 'nervous', 'control_coordination')
        
        # اضافه کردن مغز
        self.brain = Brain()
        self.add_organ(self.brain)
        
        # شبکه عصبی
        self.neural_network = {
            'nodes': [],
            'connections': [],
            'signals': []
        }
    
    async def process_information(self, info: Any) -> Any:
        """پردازش اطلاعات"""
        # ذخیره در حافظه کوتاه‌مدت
        self.brain.short_term_memory.append(info)
        
        # تفکر و تصمیم‌گیری
        result = await self.brain.perform_function()
        
        return result
    
    async def send_command(self, target: str, command: Any):
        """ارسال دستور به بخش‌های دیگه"""
        self.neural_network['signals'].append({
            'target': target,
            'command': command,
            'timestamp': asyncio.get_event_loop().time()
        })


class CirculatorySystem(BodySystem):
    """دستگاه گردش (انرژی و منابع)"""
    
    def __init__(self):
        super().__init__('circulatory_001', 'circulatory', 'resource_distribution')
        
        # اضافه کردن قلب
        self.heart = Heart()
        self.add_organ(self.heart)
        
        # منابع در گردش
        self.circulating_resources = {
            'energy': 100,
            'nutrients': 100,
            'information': []
        }
    
    async def distribute_resources(self, targets: List[str]):
        """توزیع منابع"""
        for target in targets:
            # ارسال انرژی
            resource_packet = {
                'energy': 10,
                'nutrients': 5,
                'from': 'circulatory_system'
            }
            # در واقعیت به سیستم‌های دیگه ارسال میشه
        
        # کاهش منابع
        self.circulating_resources['energy'] -= len(targets) * 10


class RespiratorySystem(BodySystem):
    """دستگاه تنفسی - دریافت اطلاعات/اکسیژن"""
    
    def __init__(self):
        super().__init__('respiratory_001', 'respiratory', 'information_intake')
        
        # اضافه کردن ریه‌ها
        self.lungs = Lungs()
        self.add_organ(self.lungs)
        
        # ورودی اطلاعات
        self.information_intake = []
    
    async def breathe_in(self, information: Any):
        """دریافت اطلاعات جدید (نفس کشیدن)"""
        self.information_intake.append(information)
        
        # پردازش در ریه‌ها
        await self.lungs.perform_function()


class DigestiveSystem(BodySystem):
    """دستگاه گوارش - پردازش و جذب"""
    
    def __init__(self):
        super().__init__('digestive_001', 'digestive', 'data_processing')
        
        self.stomach = {}  # معده - ذخیره موقت
        self.intestines = {}  # روده - جذب
        self.processed_data = []
    
    async def digest(self, raw_data: Any) -> Any:
        """هضم و پردازش داده"""
        # شکستن به اجزای کوچک‌تر
        processed = {
            'raw': raw_data,
            'extracted': self._extract_nutrients(raw_data),
            'waste': []
        }
        
        self.processed_data.append(processed)
        return processed['extracted']
    
    def _extract_nutrients(self, data: Any) -> Dict:
        """استخراج اطلاعات مفید"""
        return {
            'useful_data': data,
            'metadata': {'processed': True}
        }


class ImmuneSystem(BodySystem):
    """دستگاه ایمنی - دفاع و محافظت"""
    
    def __init__(self):
        super().__init__('immune_001', 'immune', 'defense_protection')
        
        self.white_cells = []  # سلول‌های سفید - محافظ
        self.antibodies = {}  # آنتی‌بادی‌ها - حافظه دفاعی
        self.threats_detected = []
    
    async def detect_threat(self, input_data: Any) -> bool:
        """تشخیص تهدید"""
        # بررسی امنیتی
        is_threat = await self._analyze_for_threats(input_data)
        
        if is_threat:
            self.threats_detected.append(input_data)
            await self._activate_defense()
        
        return is_threat
    
    async def _analyze_for_threats(self, data: Any) -> bool:
        """تحلیل برای تشخیص تهدید"""
        # الگوریتم تشخیص تهدید
        dangerous_patterns = ['virus', 'spam', 'attack', 'malicious']
        
        data_str = str(data).lower()
        for pattern in dangerous_patterns:
            if pattern in data_str:
                return True
        
        return False
    
    async def _activate_defense(self):
        """فعال‌سازی دفاع"""
        logger.warning("🛡️ Defense system activated!")


class EndocrineSystem(BodySystem):
    """دستگاه غدد - تنظیم و کنترل بلندمدت"""
    
    def __init__(self):
        super().__init__('endocrine_001', 'endocrine', 'regulation')
        
        self.hormones = {
            'stress': 0,  # کورتیزول
            'happiness': 50,  # سروتونین
            'energy': 50,  # تیروکسین
            'focus': 50  # نوراپی‌نفرین
        }
    
    async def regulate(self, state: Dict):
        """تنظیم هورمون‌ها بر اساس وضعیت"""
        # تنظیم استرس
        if state.get('load', 0) > 80:
            self.hormones['stress'] += 10
            self.hormones['focus'] += 5
        else:
            self.hormones['stress'] = max(0, self.hormones['stress'] - 5)
        
        # تنظیم شادی
        if state.get('success_rate', 0) > 90:
            self.hormones['happiness'] += 5
        
        # محدود کردن به 0-100
        for hormone in self.hormones:
            self.hormones[hormone] = max(0, min(100, self.hormones[hormone]))
        
        return self.hormones


class MusculoskeletalSystem(BodySystem):
    """دستگاه عضلانی-اسکلتی - اجرا و عمل"""
    
    def __init__(self):
        super().__init__('musculoskeletal_001', 'musculoskeletal', 'action_execution')
        
        self.muscles = {}  # عضلات - اجراکننده
        self.bones = {}  # استخوان‌ها - ساختار
        self.strength = 100
    
    async def execute_action(self, action: str, parameters: Dict) -> bool:
        """اجرای عمل"""
        if self.strength > 10:
            self.strength -= 10
            
            logger.info(f"💪 Executing: {action}")
            
            # شبیه‌سازی اجرا
            await asyncio.sleep(0.1)
            
            return True
        else:
            logger.warning("⚠️ Not enough strength!")
            return False
    
    async def rest(self):
        """استراحت و بازیابی"""
        self.strength = min(100, self.strength + 20)


# Organism - موجود کامل

class Organism:
    """موجود کامل - نازنین"""
    
    def __init__(self, name: str = "Nazanin"):
        self.name = name
        self.id = f"organism_{name.lower()}"
        
        # تمام سیستم‌های بدن
        self.systems = {
            'nervous': NervousSystem(),
            'circulatory': CirculatorySystem(),
            'respiratory': RespiratorySystem(),
            'digestive': DigestiveSystem(),
            'immune': ImmuneSystem(),
            'endocrine': EndocrineSystem(),
            'musculoskeletal': MusculoskeletalSystem()
        }
        
        # وضعیت کلی
        self.health = 100.0
        self.energy = 100.0
        self.consciousness = True
        self.age = 0
        
        logger.info(f"🧬 Organism '{name}' created with {len(self.systems)} systems")
    
    async def live(self):
        """فرآیند زندگی - یک چرخه کامل"""
        if not self.consciousness:
            return
        
        # 1. تنفس - دریافت اطلاعات
        await self.systems['respiratory'].coordinate_organs()
        
        # 2. گوارش - پردازش اطلاعات
        await self.systems['digestive'].coordinate_organs()
        
        # 3. گردش - توزیع منابع
        await self.systems['circulatory'].distribute_resources(
            list(self.systems.keys())
        )
        
        # 4. عصبی - تفکر و تصمیم
        await self.systems['nervous'].coordinate_organs()
        
        # 5. غدد - تنظیم
        state = self.get_state()
        await self.systems['endocrine'].regulate(state)
        
        # 6. ایمنی - محافظت
        await self.systems['immune'].coordinate_organs()
        
        # محاسبه سلامت کلی
        await self._calculate_health()
        
        # افزایش سن
        self.age += 1
    
    async def perceive(self, stimulus: Any) -> Any:
        """درک محرک خارجی"""
        # دریافت از طریق تنفس
        await self.systems['respiratory'].breathe_in(stimulus)
        
        # بررسی امنیتی
        is_safe = not await self.systems['immune'].detect_threat(stimulus)
        
        if is_safe:
            # پردازش در عصبی
            response = await self.systems['nervous'].process_information(stimulus)
            return response
        else:
            return {'status': 'threat_detected', 'blocked': True}
    
    async def think(self, topic: Any) -> Dict:
        """فکر کردن"""
        brain = self.systems['nervous'].brain
        brain.working_memory['current_topic'] = topic
        
        result = await brain.think()
        decision = await brain.decide()
        
        return {
            'thoughts': result,
            'decision': decision
        }
    
    async def act(self, action: str, parameters: Dict = None) -> bool:
        """انجام عمل"""
        # بررسی انرژی
        if self.energy < 10:
            logger.warning("⚠️ Not enough energy to act")
            return False
        
        # اجرا از طریق عضلانی
        success = await self.systems['musculoskeletal'].execute_action(
            action,
            parameters or {}
        )
        
        if success:
            self.energy -= 10
        
        return success
    
    async def rest(self):
        """استراحت"""
        # بازیابی همه سیستم‌ها
        for system in self.systems.values():
            if hasattr(system, 'rest'):
                await system.rest()
        
        # بازیابی انرژی
        self.energy = min(100, self.energy + 30)
        
        logger.info("😴 Resting... Energy restored")
    
    async def _calculate_health(self):
        """محاسبه سلامت کلی"""
        system_healths = [s.health for s in self.systems.values()]
        self.health = sum(system_healths) / len(system_healths)
    
    def get_state(self) -> Dict:
        """وضعیت فعلی موجود"""
        return {
            'name': self.name,
            'health': round(self.health, 2),
            'energy': round(self.energy, 2),
            'age': self.age,
            'consciousness': self.consciousness,
            'systems': {
                name: system.get_status()
                for name, system in self.systems.items()
            }
        }
    
    def get_vital_signs(self) -> Dict:
        """علائم حیاتی"""
        return {
            'health': round(self.health, 2),
            'energy': round(self.energy, 2),
            'heart_rate': self.systems['circulatory'].heart.beat_rate,
            'oxygen': self.systems['respiratory'].lungs.oxygen_level,
            'stress': self.systems['endocrine'].hormones['stress'],
            'happiness': self.systems['endocrine'].hormones['happiness']
        }


# Usage Example
if __name__ == '__main__':
    async def main():
        # ساخت موجود
        nazanin = Organism("Nazanin")
        
        # زندگی برای چند چرخه
        for i in range(3):
            print(f"\n=== Cycle {i+1} ===")
            await nazanin.live()
            print("Vital Signs:", nazanin.get_vital_signs())
        
        # درک یک محرک
        print("\n=== Perceiving ===")
        response = await nazanin.perceive("Hello, how are you?")
        print("Response:", response)
        
        # فکر کردن
        print("\n=== Thinking ===")
        thought = await nazanin.think("What should I do next?")
        print("Thought:", thought)
        
        # انجام عمل
        print("\n=== Acting ===")
        success = await nazanin.act("respond_to_user", {'message': 'Hello!'})
        print("Action Success:", success)
        
        # استراحت
        print("\n=== Resting ===")
        await nazanin.rest()
        print("After Rest:", nazanin.get_vital_signs())
    
    asyncio.run(main())
