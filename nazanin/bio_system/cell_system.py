"""
Biological Cell System
سیستم سلولی - واحد بنیادی زندگی
"""

import asyncio
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
import random

logger = logging.getLogger(__name__)


class Cell:
    """سلول - کوچک‌ترین واحد زنده"""
    
    def __init__(self, cell_id: str, cell_type: str, function: str):
        self.cell_id = cell_id
        self.cell_type = cell_type  # نوع سلول
        self.function = function  # وظیفه
        
        # ویژگی‌های سلول
        self.energy = 100.0  # انرژی
        self.health = 100.0  # سلامت
        self.age = 0  # سن
        self.is_active = True
        
        # هسته سلول (ذخیره اطلاعات - DNA)
        self.nucleus = {
            'dna': {},  # اطلاعات ژنتیکی
            'rna': {},  # دستورالعمل‌های فعال
            'proteins': []  # پروتئین‌های ساخته شده
        }
        
        # میتوکندری (تولید انرژی)
        self.mitochondria = {
            'atp_production': 0,  # تولید انرژی
            'efficiency': 1.0
        }
        
        # سیتوپلاسم (محیط داخلی)
        self.cytoplasm = {
            'nutrients': [],
            'waste': [],
            'enzymes': []
        }
        
        # غشای سلولی (ارتباط با محیط)
        self.membrane = {
            'receptors': [],  # گیرنده‌ها
            'channels': [],  # کانال‌ها
            'signals_received': []
        }
    
    async def metabolize(self):
        """متابولیسم - تبدیل مواد به انرژی"""
        if not self.is_active:
            return
        
        # مصرف مواد مغذی و تولید انرژی
        if len(self.cytoplasm['nutrients']) > 0:
            nutrient = self.cytoplasm['nutrients'].pop(0)
            
            # تولید ATP (انرژی)
            energy_produced = 10 * self.mitochondria['efficiency']
            self.energy = min(100, self.energy + energy_produced)
            self.mitochondria['atp_production'] += energy_produced
            
            # تولید ضایعات
            self.cytoplasm['waste'].append('CO2')
        
        # مصرف انرژی برای فعالیت
        self.energy -= 1
        
        # اگه انرژی کمه، سلامت کم می‌شه
        if self.energy < 20:
            self.health -= 0.5
    
    async def receive_signal(self, signal: Dict):
        """دریافت سیگنال از سلول‌های دیگه یا محیط"""
        self.membrane['signals_received'].append(signal)
        
        # پردازش سیگنال
        if signal['type'] == 'nutrient':
            self.cytoplasm['nutrients'].append(signal['data'])
        elif signal['type'] == 'damage':
            self.health -= signal.get('amount', 10)
        elif signal['type'] == 'heal':
            self.health = min(100, self.health + signal.get('amount', 10))
        elif signal['type'] == 'activate':
            self.is_active = True
        elif signal['type'] == 'deactivate':
            self.is_active = False
    
    async def divide(self) -> Optional['Cell']:
        """تقسیم سلولی - ایجاد سلول جدید"""
        if self.health > 70 and self.energy > 60:
            # ساخت سلول جدید
            new_cell = Cell(
                f"{self.cell_id}_daughter",
                self.cell_type,
                self.function
            )
            
            # کپی کردن DNA
            new_cell.nucleus['dna'] = self.nucleus['dna'].copy()
            
            # تقسیم انرژی
            self.energy /= 2
            new_cell.energy = self.energy
            
            logger.debug(f"🧬 Cell {self.cell_id} divided")
            return new_cell
        
        return None
    
    async def produce_protein(self, protein_type: str) -> str:
        """ساخت پروتئین (ترجمه DNA به عملکرد)"""
        if protein_type in self.nucleus['dna']:
            # استفاده از انرژی برای ساخت
            if self.energy > 10:
                self.energy -= 10
                protein = f"{protein_type}_protein_{len(self.nucleus['proteins'])}"
                self.nucleus['proteins'].append(protein)
                return protein
        return None
    
    def get_status(self) -> Dict:
        """وضعیت سلول"""
        return {
            'id': self.cell_id,
            'type': self.cell_type,
            'health': round(self.health, 2),
            'energy': round(self.energy, 2),
            'age': self.age,
            'active': self.is_active,
            'atp_produced': self.mitochondria['atp_production']
        }


class Tissue:
    """بافت - مجموعه سلول‌های هم‌نوع"""
    
    def __init__(self, tissue_id: str, tissue_type: str, function: str):
        self.tissue_id = tissue_id
        self.tissue_type = tissue_type
        self.function = function
        
        self.cells: List[Cell] = []
        self.health = 100.0
        self.is_active = True
    
    def add_cell(self, cell: Cell):
        """اضافه کردن سلول به بافت"""
        self.cells.append(cell)
    
    async def coordinate_cells(self):
        """هماهنگی فعالیت سلول‌ها"""
        if not self.is_active:
            return
        
        # همه سلول‌ها متابولیسم می‌کنن
        for cell in self.cells:
            await cell.metabolize()
        
        # محاسبه سلامت کلی بافت
        if self.cells:
            self.health = sum(c.health for c in self.cells) / len(self.cells)
    
    async def send_nutrients_to_cells(self):
        """ارسال مواد مغذی به سلول‌ها"""
        for cell in self.cells:
            if cell.energy < 50:
                await cell.receive_signal({
                    'type': 'nutrient',
                    'data': 'glucose'
                })
    
    async def remove_dead_cells(self):
        """حذف سلول‌های مرده"""
        self.cells = [c for c in self.cells if c.health > 0]
    
    def get_status(self) -> Dict:
        """وضعیت بافت"""
        return {
            'id': self.tissue_id,
            'type': self.tissue_type,
            'cells_count': len(self.cells),
            'health': round(self.health, 2),
            'avg_energy': round(sum(c.energy for c in self.cells) / len(self.cells), 2) if self.cells else 0,
            'active': self.is_active
        }


class Organ:
    """اندام - مجموعه بافت‌های مختلف"""
    
    def __init__(self, organ_id: str, organ_type: str, function: str):
        self.organ_id = organ_id
        self.organ_type = organ_type
        self.function = function
        
        self.tissues: Dict[str, Tissue] = {}
        self.health = 100.0
        self.efficiency = 1.0
        self.is_active = True
    
    def add_tissue(self, tissue: Tissue):
        """اضافه کردن بافت به اندام"""
        self.tissues[tissue.tissue_id] = tissue
    
    async def perform_function(self) -> Any:
        """انجام وظیفه اختصاصی اندام"""
        if not self.is_active:
            return None
        
        # هماهنگی بافت‌ها
        for tissue in self.tissues.values():
            await tissue.coordinate_cells()
        
        # محاسبه سلامت اندام
        if self.tissues:
            tissue_healths = [t.health for t in self.tissues.values()]
            self.health = sum(tissue_healths) / len(tissue_healths)
            self.efficiency = self.health / 100
        
        # انجام وظیفه خاص
        return await self._specific_function()
    
    async def _specific_function(self) -> Any:
        """وظیفه خاص هر اندام (override می‌شه)"""
        return {'status': 'functioning'}
    
    def get_status(self) -> Dict:
        """وضعیت اندام"""
        return {
            'id': self.organ_id,
            'type': self.organ_type,
            'function': self.function,
            'tissues_count': len(self.tissues),
            'health': round(self.health, 2),
            'efficiency': round(self.efficiency, 2),
            'active': self.is_active
        }


class Brain(Organ):
    """مغز - اندام کنترل و تصمیم‌گیری"""
    
    def __init__(self):
        super().__init__('brain_001', 'brain', 'thinking_decision_making')
        
        # بخش‌های مغز
        self.cortex = {}  # قشر مغز - تفکر
        self.limbic_system = {}  # سیستم لیمبیک - احساسات
        self.cerebellum = {}  # مخچه - هماهنگی
        self.brainstem = {}  # ساقه مغز - کارهای اساسی
        
        # حافظه
        self.short_term_memory = []
        self.long_term_memory = []
        self.working_memory = {}
    
    async def _specific_function(self) -> Any:
        """تفکر و تصمیم‌گیری"""
        # پردازش اطلاعات
        thoughts = await self.think()
        decisions = await self.decide()
        
        return {
            'thoughts': thoughts,
            'decisions': decisions,
            'memory_items': len(self.long_term_memory)
        }
    
    async def think(self) -> List[str]:
        """فرآیند تفکر"""
        thoughts = []
        
        # پردازش حافظه کوتاه‌مدت
        for item in self.short_term_memory[-5:]:
            thought = f"Processing: {item}"
            thoughts.append(thought)
        
        return thoughts
    
    async def decide(self) -> Dict:
        """تصمیم‌گیری"""
        return {
            'action': 'continue',
            'confidence': self.efficiency
        }


class Heart(Organ):
    """قلب - پمپاژ انرژی"""
    
    def __init__(self):
        super().__init__('heart_001', 'heart', 'circulate_energy')
        self.beat_rate = 72  # ضربان
        self.blood_flow = 100  # جریان خون (انرژی)
    
    async def _specific_function(self) -> Any:
        """پمپاژ انرژی به سیستم"""
        # ضربان قلب
        self.beat_rate = int(60 + (40 * self.efficiency))
        self.blood_flow = 100 * self.efficiency
        
        return {
            'beat_rate': self.beat_rate,
            'blood_flow': round(self.blood_flow, 2),
            'pumping': True
        }


class Lungs(Organ):
    """ریه - دریافت اکسیژن (اطلاعات)"""
    
    def __init__(self):
        super().__init__('lungs_001', 'lungs', 'oxygen_exchange')
        self.oxygen_level = 100
    
    async def _specific_function(self) -> Any:
        """تبادل اکسیژن"""
        # دریافت اکسیژن (اطلاعات جدید)
        self.oxygen_level = 95 + (5 * self.efficiency)
        
        return {
            'oxygen_level': round(self.oxygen_level, 2),
            'breathing': True
        }


# سلول‌های تخصصی

class NeuronCell(Cell):
    """سلول عصبی - انتقال اطلاعات"""
    
    def __init__(self, cell_id: str):
        super().__init__(cell_id, 'neuron', 'signal_transmission')
        self.connections = []  # اتصالات به نورون‌های دیگه
        self.synapses = []  # سیناپس‌ها
    
    async def fire(self, signal: Any):
        """شلیک سیگنال عصبی"""
        if self.energy > 5:
            self.energy -= 5
            # ارسال به تمام اتصالات
            for connection in self.connections:
                await connection.receive_signal({
                    'type': 'neural',
                    'data': signal,
                    'from': self.cell_id
                })


class MemoryCell(Cell):
    """سلول حافظه - ذخیره اطلاعات"""
    
    def __init__(self, cell_id: str):
        super().__init__(cell_id, 'memory', 'data_storage')
        self.stored_data = []
        self.capacity = 1000
    
    async def store(self, data: Any):
        """ذخیره داده"""
        if len(self.stored_data) < self.capacity:
            self.stored_data.append({
                'data': data,
                'timestamp': datetime.now().isoformat(),
                'access_count': 0
            })
    
    async def retrieve(self, query: str) -> List[Any]:
        """بازیابی داده"""
        results = []
        for item in self.stored_data:
            if query in str(item['data']):
                item['access_count'] += 1
                results.append(item['data'])
        return results


# Usage Example
if __name__ == '__main__':
    async def main():
        # ساخت سلول
        cell = Cell('cell_001', 'generic', 'metabolism')
        cell.nucleus['dna'] = {'protein_a': 'ATCG...'}
        
        # متابولیسم
        await cell.receive_signal({'type': 'nutrient', 'data': 'glucose'})
        await cell.metabolize()
        
        print("Cell Status:", cell.get_status())
        
        # ساخت بافت
        tissue = Tissue('tissue_001', 'epithelial', 'protection')
        for i in range(10):
            c = Cell(f'cell_{i}', 'epithelial', 'protect')
            tissue.add_cell(c)
        
        await tissue.coordinate_cells()
        print("Tissue Status:", tissue.get_status())
        
        # ساخت مغز
        brain = Brain()
        brain.short_term_memory = ['thought1', 'thought2', 'thought3']
        result = await brain.perform_function()
        print("Brain Function:", result)
        print("Brain Status:", brain.get_status())
    
    asyncio.run(main())
