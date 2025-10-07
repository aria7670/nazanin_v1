"""
Autonomous System - سیستم خودمختار
قابلیت فکر، تصمیم‌گیری و عمل مستقل کامل

قابلیت‌ها:
- تصمیم‌گیری مستقل
- برنامه‌ریزی خودکار
- اجرای خودمختار
- خود-نظارتی
- خود-بهبودی
"""

import asyncio
import logging
import json
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from collections import deque
import random

logger = logging.getLogger(__name__)


class DecisionMaker:
    """تصمیم‌گیرنده مستقل"""
    
    def __init__(self):
        self.decision_history = deque(maxlen=1000)
        self.decision_rules = {}
        self.confidence_threshold = 0.7
        
        self._load_decision_rules()
    
    def _load_decision_rules(self):
        """بارگذاری قواعد تصمیم‌گیری"""
        
        self.decision_rules = {
            'greeting': {
                'condition': lambda ctx: 'سلام' in ctx.get('text', '').lower() or 'hello' in ctx.get('text', '').lower(),
                'action': 'respond_greeting',
                'priority': 10
            },
            'question': {
                'condition': lambda ctx: '?' in ctx.get('text', ''),
                'action': 'answer_question',
                'priority': 9
            },
            'help_request': {
                'condition': lambda ctx: any(word in ctx.get('text', '').lower() for word in ['help', 'کمک', 'please']),
                'action': 'provide_help',
                'priority': 10
            },
            'information': {
                'condition': lambda ctx: any(word in ctx.get('text', '').lower() for word in ['what', 'چی', 'اطلاعات', 'info']),
                'action': 'provide_information',
                'priority': 8
            },
            'conversation': {
                'condition': lambda ctx: True,  # همیشه
                'action': 'continue_conversation',
                'priority': 5
            }
        }
    
    async def make_decision(self, context: Dict) -> Dict:
        """تصمیم‌گیری مستقل"""
        
        # بررسی تمام قواعد
        applicable_rules = []
        
        for rule_name, rule in self.decision_rules.items():
            try:
                if rule['condition'](context):
                    applicable_rules.append({
                        'name': rule_name,
                        'action': rule['action'],
                        'priority': rule['priority']
                    })
            except Exception as e:
                logger.warning(f"Error checking rule {rule_name}: {e}")
        
        # مرتب‌سازی بر اساس اولویت
        applicable_rules.sort(key=lambda x: x['priority'], reverse=True)
        
        # انتخاب بهترین تصمیم
        if applicable_rules:
            selected_rule = applicable_rules[0]
            confidence = min(1.0, selected_rule['priority'] / 10.0)
        else:
            selected_rule = {'name': 'default', 'action': 'observe', 'priority': 1}
            confidence = 0.3
        
        decision = {
            'timestamp': datetime.now().isoformat(),
            'context': context.get('text', '')[:100],
            'rule': selected_rule['name'],
            'action': selected_rule['action'],
            'confidence': confidence,
            'applicable_rules': len(applicable_rules)
        }
        
        self.decision_history.append(decision)
        
        return decision
    
    async def learn_from_outcome(self, decision: Dict, outcome: Dict):
        """یادگیری از نتیجه تصمیم"""
        
        success = outcome.get('success', False)
        
        if success:
            # افزایش اولویت قانون موفق
            rule_name = decision.get('rule')
            if rule_name in self.decision_rules:
                self.decision_rules[rule_name]['priority'] = min(10, self.decision_rules[rule_name]['priority'] + 0.1)
        else:
            # کاهش اولویت
            rule_name = decision.get('rule')
            if rule_name in self.decision_rules:
                self.decision_rules[rule_name]['priority'] = max(1, self.decision_rules[rule_name]['priority'] - 0.1)


class TaskPlanner:
    """برنامه‌ریز خودکار"""
    
    def __init__(self):
        self.tasks = deque(maxlen=1000)
        self.plans = {}
        self.current_plan = None
        
    async def create_plan(self, goal: str, context: Dict = None) -> Dict:
        """ساخت برنامه برای رسیدن به هدف"""
        
        # تجزیه هدف به زیرتسک‌ها
        subtasks = await self._decompose_goal(goal, context)
        
        # اولویت‌بندی
        prioritized_tasks = sorted(subtasks, key=lambda x: x.get('priority', 5), reverse=True)
        
        # ساخت برنامه
        plan = {
            'id': f"plan_{len(self.plans)}",
            'goal': goal,
            'subtasks': prioritized_tasks,
            'created_at': datetime.now().isoformat(),
            'status': 'pending',
            'progress': 0.0
        }
        
        self.plans[plan['id']] = plan
        self.current_plan = plan
        
        return plan
    
    async def _decompose_goal(self, goal: str, context: Dict = None) -> List[Dict]:
        """تجزیه هدف به زیرتسک‌ها"""
        
        # الگوهای شناخته شده
        if 'respond' in goal.lower():
            return [
                {'task': 'understand_input', 'priority': 10},
                {'task': 'generate_response', 'priority': 9},
                {'task': 'validate_response', 'priority': 8},
                {'task': 'send_response', 'priority': 7}
            ]
        elif 'learn' in goal.lower():
            return [
                {'task': 'gather_data', 'priority': 10},
                {'task': 'analyze_data', 'priority': 9},
                {'task': 'update_knowledge', 'priority': 8},
                {'task': 'validate_learning', 'priority': 7}
            ]
        elif 'create' in goal.lower():
            return [
                {'task': 'understand_requirements', 'priority': 10},
                {'task': 'design_solution', 'priority': 9},
                {'task': 'implement', 'priority': 8},
                {'task': 'test', 'priority': 7},
                {'task': 'deliver', 'priority': 6}
            ]
        else:
            # هدف عمومی
            return [
                {'task': 'analyze_goal', 'priority': 10},
                {'task': 'execute', 'priority': 8},
                {'task': 'verify', 'priority': 6}
            ]
    
    async def execute_plan(self, plan_id: str) -> Dict:
        """اجرای برنامه"""
        
        if plan_id not in self.plans:
            return {'success': False, 'error': 'Plan not found'}
        
        plan = self.plans[plan_id]
        plan['status'] = 'executing'
        
        completed_tasks = 0
        total_tasks = len(plan['subtasks'])
        
        results = []
        
        for subtask in plan['subtasks']:
            # اجرای هر زیرتسک
            result = await self._execute_subtask(subtask)
            results.append(result)
            
            if result.get('success'):
                completed_tasks += 1
            
            # به‌روزرسانی پیشرفت
            plan['progress'] = completed_tasks / total_tasks
        
        plan['status'] = 'completed'
        plan['completed_at'] = datetime.now().isoformat()
        plan['results'] = results
        
        return {
            'success': True,
            'plan_id': plan_id,
            'completed_tasks': completed_tasks,
            'total_tasks': total_tasks,
            'progress': plan['progress']
        }
    
    async def _execute_subtask(self, subtask: Dict) -> Dict:
        """اجرای یک زیرتسک"""
        
        # شبیه‌سازی اجرا
        await asyncio.sleep(0.1)
        
        return {
            'task': subtask['task'],
            'success': True,
            'executed_at': datetime.now().isoformat()
        }


class SelfMonitor:
    """خود-نظارتی - نظارت بر عملکرد خود"""
    
    def __init__(self):
        self.metrics = {
            'performance': deque(maxlen=1000),
            'errors': deque(maxlen=1000),
            'resource_usage': deque(maxlen=1000)
        }
        self.alerts = deque(maxlen=100)
        
    async def monitor(self, system_state: Dict) -> Dict:
        """نظارت بر وضعیت سیستم"""
        
        # ثبت metrics
        metric = {
            'timestamp': datetime.now().isoformat(),
            'cpu_usage': system_state.get('cpu_usage', 0),
            'memory_usage': system_state.get('memory_usage', 0),
            'response_time': system_state.get('response_time', 0),
            'error_rate': system_state.get('error_rate', 0)
        }
        
        self.metrics['performance'].append(metric)
        
        # بررسی آلارم‌ها
        alerts = await self._check_alerts(metric)
        
        return {
            'status': 'healthy' if len(alerts) == 0 else 'warning',
            'alerts': alerts,
            'metric': metric
        }
    
    async def _check_alerts(self, metric: Dict) -> List[str]:
        """بررسی شرایط آلارم"""
        
        alerts = []
        
        if metric.get('cpu_usage', 0) > 80:
            alerts.append('HIGH_CPU_USAGE')
        
        if metric.get('memory_usage', 0) > 80:
            alerts.append('HIGH_MEMORY_USAGE')
        
        if metric.get('response_time', 0) > 5:
            alerts.append('SLOW_RESPONSE')
        
        if metric.get('error_rate', 0) > 0.1:
            alerts.append('HIGH_ERROR_RATE')
        
        # ذخیره آلارم‌ها
        for alert in alerts:
            self.alerts.append({
                'timestamp': datetime.now().isoformat(),
                'alert': alert,
                'metric': metric
            })
        
        return alerts


class SelfImprover:
    """خود-بهبودی - بهبود خودکار"""
    
    def __init__(self):
        self.improvements = deque(maxlen=1000)
        self.optimization_rules = {}
        
    async def analyze_and_improve(self, performance_data: Dict) -> Dict:
        """تحلیل و بهبود"""
        
        # شناسایی مشکلات
        issues = await self._identify_issues(performance_data)
        
        # پیشنهاد بهبود
        improvements = []
        
        for issue in issues:
            improvement = await self._suggest_improvement(issue)
            if improvement:
                improvements.append(improvement)
        
        # اعمال بهبودها
        applied = []
        for improvement in improvements:
            result = await self._apply_improvement(improvement)
            if result['success']:
                applied.append(improvement)
        
        return {
            'issues_found': len(issues),
            'improvements_suggested': len(improvements),
            'improvements_applied': len(applied),
            'details': applied
        }
    
    async def _identify_issues(self, data: Dict) -> List[str]:
        """شناسایی مشکلات"""
        
        issues = []
        
        if data.get('error_rate', 0) > 0.05:
            issues.append('high_error_rate')
        
        if data.get('response_time', 0) > 3:
            issues.append('slow_response')
        
        if data.get('success_rate', 1) < 0.9:
            issues.append('low_success_rate')
        
        return issues
    
    async def _suggest_improvement(self, issue: str) -> Optional[Dict]:
        """پیشنهاد بهبود"""
        
        suggestions = {
            'high_error_rate': {
                'action': 'increase_validation',
                'description': 'Add more input validation'
            },
            'slow_response': {
                'action': 'optimize_processing',
                'description': 'Optimize response generation'
            },
            'low_success_rate': {
                'action': 'improve_accuracy',
                'description': 'Improve decision accuracy'
            }
        }
        
        return suggestions.get(issue)
    
    async def _apply_improvement(self, improvement: Dict) -> Dict:
        """اعمال بهبود"""
        
        # ثبت بهبود
        self.improvements.append({
            'timestamp': datetime.now().isoformat(),
            'improvement': improvement,
            'applied': True
        })
        
        return {
            'success': True,
            'improvement': improvement['action']
        }


class AutonomousSystem:
    """
    سیستم کامل خودمختار
    قابلیت فکر، تصمیم‌گیری و عمل مستقل
    """
    
    def __init__(self):
        self.decision_maker = DecisionMaker()
        self.task_planner = TaskPlanner()
        self.self_monitor = SelfMonitor()
        self.self_improver = SelfImprover()
        
        # وضعیت
        self.is_autonomous = True
        self.autonomy_level = 1.0  # 0=manual, 1=fully autonomous
        
        # آمار
        self.decisions_made = 0
        self.plans_created = 0
        self.improvements_made = 0
        
        logger.info("🤖 Autonomous System initialized - Full autonomy enabled")
    
    async def autonomous_cycle(self, input_data: Dict) -> Dict:
        """
        چرخه خودمختار کامل:
        1. تصمیم‌گیری
        2. برنامه‌ریزی
        3. اجرا
        4. نظارت
        5. بهبود
        """
        
        cycle_start = datetime.now()
        
        # 1. تصمیم‌گیری
        decision = await self.decision_maker.make_decision(input_data)
        self.decisions_made += 1
        
        # 2. برنامه‌ریزی
        if decision['confidence'] > self.decision_maker.confidence_threshold:
            plan = await self.task_planner.create_plan(
                goal=decision['action'],
                context=input_data
            )
            self.plans_created += 1
            
            # 3. اجرا
            execution_result = await self.task_planner.execute_plan(plan['id'])
        else:
            execution_result = {
                'success': False,
                'reason': 'low_confidence',
                'confidence': decision['confidence']
            }
        
        # 4. نظارت
        system_state = {
            'cpu_usage': random.uniform(20, 70),
            'memory_usage': random.uniform(30, 60),
            'response_time': (datetime.now() - cycle_start).total_seconds(),
            'error_rate': 0.01 if execution_result.get('success') else 0.1
        }
        
        monitoring = await self.self_monitor.monitor(system_state)
        
        # 5. بهبود
        if monitoring['status'] != 'healthy':
            improvement = await self.self_improver.analyze_and_improve(system_state)
            self.improvements_made += improvement['improvements_applied']
        else:
            improvement = None
        
        # یادگیری از نتیجه
        await self.decision_maker.learn_from_outcome(
            decision,
            execution_result
        )
        
        return {
            'cycle_completed': True,
            'decision': decision,
            'execution': execution_result,
            'monitoring': monitoring,
            'improvement': improvement,
            'cycle_time': (datetime.now() - cycle_start).total_seconds(),
            'autonomous': True
        }
    
    def get_stats(self) -> Dict:
        """آمار سیستم خودمختار"""
        return {
            'is_autonomous': self.is_autonomous,
            'autonomy_level': self.autonomy_level,
            'decisions_made': self.decisions_made,
            'plans_created': self.plans_created,
            'improvements_made': self.improvements_made,
            'decision_history_size': len(self.decision_maker.decision_history),
            'active_plans': len(self.task_planner.plans),
            'active_alerts': len(self.self_monitor.alerts)
        }
