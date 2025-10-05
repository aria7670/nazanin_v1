"""
Autonomous Decision Maker - تصمیم‌گیر خودمختار
سیستم تصمیم‌گیری مستقل و هوشمند
"""

import logging
import asyncio
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
import random

logger = logging.getLogger(__name__)


class DecisionType(Enum):
    """انواع تصمیم"""
    IMMEDIATE = "immediate"  # تصمیم فوری
    DELIBERATE = "deliberate"  # تصمیم سنجیده
    INTUITIVE = "intuitive"  # تصمیم شهودی


@dataclass
class Decision:
    """یک تصمیم"""
    decision_id: str
    action: str
    confidence: float
    reasoning: str
    type: DecisionType
    expected_outcome: Dict[str, Any]
    timestamp: datetime


class AutonomousDecisionMaker:
    """
    تصمیم‌گیر خودمختار
    
    این کلاس قادر به تصمیم‌گیری مستقل بر اساس:
    - اطلاعات موجود
    - اهداف فعلی
    - تجربیات گذشته
    - وضعیت عاطفی
    """
    
    def __init__(self):
        self.decision_history: List[Decision] = []
        self.decision_style = "balanced"  # balanced, cautious, bold
        self.autonomy_level = 0.8  # سطح خودمختاری (0-1)
        self.is_active = False
        
        logger.info("🤖 Autonomous Decision Maker initialized")
    
    async def make_decision(self, context: Dict[str, Any], 
                           options: List[Dict[str, Any]],
                           urgency: float = 0.5) -> Decision:
        """
        اتخاذ تصمیم
        
        Args:
            context: متن و اطلاعات موقعیت
            options: گزینه‌های ممکن
            urgency: فوریت تصمیم (0-1)
            
        Returns:
            تصمیم اتخاذ شده
        """
        logger.info(f"🤔 Making decision (urgency: {urgency})...")
        
        # تعیین نوع تصمیم بر اساس فوریت
        decision_type = self._determine_decision_type(urgency)
        
        # ارزیابی گزینه‌ها
        evaluated_options = await self._evaluate_options(options, context)
        
        # انتخاب بهترین گزینه
        best_option = self._select_best_option(evaluated_options, decision_type)
        
        # ایجاد تصمیم
        decision = Decision(
            decision_id=f"decision_{datetime.now().timestamp()}",
            action=best_option['action'],
            confidence=best_option['score'],
            reasoning=best_option['reasoning'],
            type=decision_type,
            expected_outcome=best_option.get('expected_outcome', {}),
            timestamp=datetime.now()
        )
        
        # ذخیره در تاریخچه
        self.decision_history.append(decision)
        if len(self.decision_history) > 100:
            self.decision_history.pop(0)
        
        logger.info(f"✅ Decision made: {decision.action} (confidence: {decision.confidence:.2f})")
        
        return decision
    
    def _determine_decision_type(self, urgency: float) -> DecisionType:
        """تعیین نوع تصمیم بر اساس فوریت"""
        if urgency > 0.8:
            return DecisionType.IMMEDIATE
        elif urgency < 0.3:
            return DecisionType.DELIBERATE
        else:
            return DecisionType.INTUITIVE
    
    async def _evaluate_options(self, options: List[Dict[str, Any]], 
                                context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """ارزیابی گزینه‌ها"""
        evaluated = []
        
        for option in options:
            # شبیه‌سازی زمان تفکر
            await asyncio.sleep(0.1)
            
            # محاسبه امتیاز
            score = self._calculate_option_score(option, context)
            
            # تولید استدلال
            reasoning = self._generate_reasoning(option, score, context)
            
            evaluated.append({
                'action': option.get('action', 'unknown'),
                'score': score,
                'reasoning': reasoning,
                'expected_outcome': option.get('expected_outcome', {}),
                'original': option
            })
        
        return evaluated
    
    def _calculate_option_score(self, option: Dict[str, Any], 
                                context: Dict[str, Any]) -> float:
        """محاسبه امتیاز یک گزینه"""
        score = 0.5  # امتیاز پایه
        
        # عوامل مختلف در امتیازدهی
        
        # 1. سودمندی
        utility = option.get('utility', 0.5)
        score += utility * 0.3
        
        # 2. امکان‌پذیری
        feasibility = option.get('feasibility', 0.5)
        score += feasibility * 0.2
        
        # 3. ریسک (ریسک کمتر = امتیاز بیشتر)
        risk = option.get('risk', 0.5)
        score += (1 - risk) * 0.2
        
        # 4. همخوانی با اهداف
        goal_alignment = option.get('goal_alignment', 0.5)
        score += goal_alignment * 0.3
        
        # تنظیم بر اساس سبک تصمیم‌گیری
        if self.decision_style == "cautious":
            score -= risk * 0.2
        elif self.decision_style == "bold":
            score += utility * 0.1
        
        return max(0.0, min(1.0, score))
    
    def _generate_reasoning(self, option: Dict[str, Any], 
                           score: float, context: Dict[str, Any]) -> str:
        """تولید استدلال برای تصمیم"""
        reasons = []
        
        if score > 0.7:
            reasons.append("This option shows strong potential")
        elif score < 0.3:
            reasons.append("This option has significant limitations")
        
        if option.get('risk', 0.5) > 0.7:
            reasons.append("with considerable risk")
        elif option.get('risk', 0.5) < 0.3:
            reasons.append("with minimal risk")
        
        if option.get('utility', 0.5) > 0.7:
            reasons.append("and high utility")
        
        return " ".join(reasons) if reasons else "Standard option"
    
    def _select_best_option(self, evaluated_options: List[Dict[str, Any]], 
                           decision_type: DecisionType) -> Dict[str, Any]:
        """انتخاب بهترین گزینه"""
        if not evaluated_options:
            return {
                'action': 'no_action',
                'score': 0.0,
                'reasoning': 'No options available'
            }
        
        # مرتب‌سازی بر اساس امتیاز
        sorted_options = sorted(evaluated_options, key=lambda x: x['score'], reverse=True)
        
        if decision_type == DecisionType.IMMEDIATE:
            # در تصمیم فوری، اولین گزینه خوب را انتخاب کن
            for option in sorted_options:
                if option['score'] > 0.5:
                    return option
            return sorted_options[0]
        
        elif decision_type == DecisionType.DELIBERATE:
            # در تصمیم سنجیده، بهترین گزینه را انتخاب کن
            return sorted_options[0]
        
        else:  # INTUITIVE
            # در تصمیم شهودی، با احتمال بیشتر گزینه‌های بهتر را انتخاب کن
            weights = [opt['score'] for opt in sorted_options]
            return random.choices(sorted_options, weights=weights)[0]
    
    async def reconsider_decision(self, decision: Decision, 
                                  new_information: Dict[str, Any]) -> Optional[Decision]:
        """
        بازنگری تصمیم با اطلاعات جدید
        
        Args:
            decision: تصمیم قبلی
            new_information: اطلاعات جدید
            
        Returns:
            تصمیم جدید یا None
        """
        logger.info(f"🔄 Reconsidering decision: {decision.action}")
        
        # تحلیل اطلاعات جدید
        impact = new_information.get('impact', 0.5)
        
        # اگر تأثیر بالا باشد، تصمیم جدید بگیر
        if impact > 0.7:
            logger.info("⚠️ Significant new information, making new decision")
            return await self.make_decision(
                context=new_information,
                options=[{'action': 'revise', 'utility': 0.8}],
                urgency=0.7
            )
        
        return None
    
    def learn_from_outcome(self, decision: Decision, outcome: Dict[str, Any]):
        """
        یادگیری از نتیجه تصمیم
        
        Args:
            decision: تصمیم اتخاذ شده
            outcome: نتیجه واقعی
        """
        success = outcome.get('success', False)
        
        if success:
            logger.info(f"✅ Decision '{decision.action}' was successful")
            # افزایش اعتماد به نفس در تصمیم‌گیری مشابه
            if self.decision_style == "cautious":
                self.autonomy_level = min(1.0, self.autonomy_level + 0.05)
        else:
            logger.info(f"❌ Decision '{decision.action}' was unsuccessful")
            # کاهش اعتماد و محتاط‌تر شدن
            if self.decision_style == "bold":
                self.decision_style = "balanced"
    
    def set_decision_style(self, style: str):
        """
        تنظیم سبک تصمیم‌گیری
        
        Args:
            style: balanced, cautious, bold
        """
        if style in ["balanced", "cautious", "bold"]:
            self.decision_style = style
            logger.info(f"⚙️ Decision style set to: {style}")
    
    def get_decision_stats(self) -> Dict[str, Any]:
        """دریافت آمار تصمیم‌گیری"""
        if not self.decision_history:
            return {'total_decisions': 0}
        
        return {
            'total_decisions': len(self.decision_history),
            'average_confidence': sum(d.confidence for d in self.decision_history) / len(self.decision_history),
            'decision_style': self.decision_style,
            'autonomy_level': self.autonomy_level,
            'decision_types': {
                'immediate': sum(1 for d in self.decision_history if d.type == DecisionType.IMMEDIATE),
                'deliberate': sum(1 for d in self.decision_history if d.type == DecisionType.DELIBERATE),
                'intuitive': sum(1 for d in self.decision_history if d.type == DecisionType.INTUITIVE)
            }
        }
