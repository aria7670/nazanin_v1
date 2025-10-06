"""
Advanced Algorithms & Pattern Recognition
الگوریتم‌های پیشرفته و تشخیص الگو
"""

import asyncio
import logging
from typing import Dict, List, Any, Optional, Tuple
import numpy as np
from collections import defaultdict, Counter
from datetime import datetime, timedelta
import json

logger = logging.getLogger(__name__)


class PatternRecognitionAlgorithm:
    """الگوریتم تشخیص الگو"""
    
    def __init__(self):
        self.patterns = {}
        self.pattern_history = []
        
    async def detect_patterns(self, data: List[Dict]) -> Dict[str, Any]:
        """تشخیص الگوها در داده"""
        
        patterns_found = {
            'time_patterns': await self._detect_time_patterns(data),
            'content_patterns': await self._detect_content_patterns(data),
            'engagement_patterns': await self._detect_engagement_patterns(data),
            'user_behavior_patterns': await self._detect_user_patterns(data)
        }
        
        return patterns_found
    
    async def _detect_time_patterns(self, data: List[Dict]) -> Dict:
        """الگوهای زمانی"""
        time_distribution = defaultdict(int)
        
        for item in data:
            if 'timestamp' in item:
                try:
                    dt = datetime.fromisoformat(item['timestamp'])
                    hour = dt.hour
                    time_distribution[hour] += 1
                except:
                    pass
        
        # یافتن ساعات پیک
        if time_distribution:
            sorted_hours = sorted(time_distribution.items(), key=lambda x: x[1], reverse=True)
            peak_hours = [hour for hour, count in sorted_hours[:3]]
        else:
            peak_hours = []
        
        return {
            'peak_hours': peak_hours,
            'distribution': dict(time_distribution),
            'most_active_hour': peak_hours[0] if peak_hours else None
        }
    
    async def _detect_content_patterns(self, data: List[Dict]) -> Dict:
        """الگوهای محتوایی"""
        topics = Counter()
        content_lengths = []
        
        for item in data:
            if 'topic' in item:
                topics[item['topic']] += 1
            if 'content' in item:
                content_lengths.append(len(item['content']))
        
        return {
            'top_topics': topics.most_common(5),
            'avg_content_length': np.mean(content_lengths) if content_lengths else 0,
            'content_length_std': np.std(content_lengths) if content_lengths else 0
        }
    
    async def _detect_engagement_patterns(self, data: List[Dict]) -> Dict:
        """الگوهای تعامل"""
        engagement_scores = []
        
        for item in data:
            if 'engagement' in item:
                engagement_scores.append(item['engagement'])
        
        if not engagement_scores:
            return {'avg_engagement': 0, 'trend': 'stable'}
        
        avg_engagement = np.mean(engagement_scores)
        
        # تشخیص ترند
        if len(engagement_scores) > 5:
            recent_avg = np.mean(engagement_scores[-5:])
            overall_avg = np.mean(engagement_scores[:-5])
            
            if recent_avg > overall_avg * 1.2:
                trend = 'growing'
            elif recent_avg < overall_avg * 0.8:
                trend = 'declining'
            else:
                trend = 'stable'
        else:
            trend = 'insufficient_data'
        
        return {
            'avg_engagement': avg_engagement,
            'trend': trend,
            'best_performing': max(engagement_scores) if engagement_scores else 0
        }
    
    async def _detect_user_patterns(self, data: List[Dict]) -> Dict:
        """الگوهای رفتار کاربر"""
        user_segments = {
            'power_users': 0,
            'regular_users': 0,
            'casual_users': 0
        }
        
        user_activity = defaultdict(int)
        
        for item in data:
            if 'user_id' in item:
                user_activity[item['user_id']] += 1
        
        for user_id, activity_count in user_activity.items():
            if activity_count > 20:
                user_segments['power_users'] += 1
            elif activity_count > 5:
                user_segments['regular_users'] += 1
            else:
                user_segments['casual_users'] += 1
        
        return user_segments


class ContentOptimizationAlgorithm:
    """الگوریتم بهینه‌سازی محتوا"""
    
    def __init__(self):
        self.optimization_history = []
        
    async def optimize(self, content: str, target_metrics: Dict) -> Dict[str, Any]:
        """بهینه‌سازی محتوا"""
        
        # تحلیل فعلی
        current_metrics = await self._analyze_content(content)
        
        # محاسبه gap
        gaps = self._calculate_gaps(current_metrics, target_metrics)
        
        # اعمال بهینه‌سازی‌ها
        optimized_content = content
        optimizations_applied = []
        
        for gap_type, gap_value in gaps.items():
            if abs(gap_value) > 0.1:  # آستانه معنی‌دار
                optimized_content, optimization = await self._apply_optimization(
                    optimized_content, gap_type, gap_value
                )
                optimizations_applied.append(optimization)
        
        # تحلیل نهایی
        final_metrics = await self._analyze_content(optimized_content)
        
        result = {
            'original_content': content,
            'optimized_content': optimized_content,
            'original_metrics': current_metrics,
            'final_metrics': final_metrics,
            'improvements': self._calculate_improvements(current_metrics, final_metrics),
            'optimizations_applied': optimizations_applied
        }
        
        self.optimization_history.append(result)
        
        return result
    
    async def _analyze_content(self, content: str) -> Dict:
        """تحلیل محتوا"""
        return {
            'length': len(content),
            'word_count': len(content.split()),
            'sentence_count': content.count('.') + 1,
            'readability_score': await self._calculate_readability(content),
            'engagement_potential': await self._estimate_engagement(content)
        }
    
    async def _calculate_readability(self, content: str) -> float:
        """محاسبه خوانایی (Flesch Reading Ease ساده شده)"""
        words = content.split()
        sentences = content.count('.') + 1
        
        if sentences == 0 or len(words) == 0:
            return 0.0
        
        avg_words_per_sentence = len(words) / sentences
        
        # ساده: هرچه جملات کوتاه‌تر، خوانایی بهتر
        score = 100 - (avg_words_per_sentence * 2)
        
        return max(0, min(100, score))
    
    async def _estimate_engagement(self, content: str) -> float:
        """تخمین پتانسیل engagement"""
        score = 50.0
        
        # عوامل مثبت
        if '?' in content:
            score += 10  # سوال engagement بیشتری دارد
        if any(word in content.lower() for word in ['new', 'breaking', 'amazing', 'جدید', 'فوری']):
            score += 15
        if 100 < len(content) < 250:
            score += 10  # طول بهینه
        
        # عوامل منفی
        if len(content) > 500:
            score -= 20  # خیلی طولانی
        
        return max(0, min(100, score))
    
    def _calculate_gaps(self, current: Dict, target: Dict) -> Dict:
        """محاسبه شکاف‌ها"""
        gaps = {}
        
        for key in target:
            if key in current:
                gaps[key] = target[key] - current[key]
        
        return gaps
    
    async def _apply_optimization(self, content: str, gap_type: str, 
                                  gap_value: float) -> Tuple[str, str]:
        """اعمال یک بهینه‌سازی"""
        
        if gap_type == 'length' and gap_value < 0:
            # کوتاه کردن
            optimized = content[:int(len(content) + gap_value)]
            return optimized, f"Shortened by {abs(gap_value)} characters"
        
        elif gap_type == 'readability_score' and gap_value > 0:
            # بهبود خوانایی
            # ساده: تبدیل جملات بلند به کوتاه
            sentences = content.split('.')
            if len(sentences) > 2:
                optimized = '. '.join(sentences[:2]) + '.'
                return optimized, "Improved readability by shortening sentences"
        
        return content, "No optimization applied"
    
    def _calculate_improvements(self, before: Dict, after: Dict) -> Dict:
        """محاسبه بهبودها"""
        improvements = {}
        
        for key in before:
            if key in after:
                change = after[key] - before[key]
                change_percent = (change / before[key] * 100) if before[key] != 0 else 0
                improvements[key] = {
                    'absolute_change': change,
                    'percent_change': change_percent
                }
        
        return improvements


class PredictiveAnalyticsAlgorithm:
    """الگوریتم تحلیل پیش‌بینی"""
    
    def __init__(self):
        self.models = {}
        self.prediction_history = []
        
    async def predict_engagement(self, content_features: Dict, 
                                historical_data: List[Dict]) -> Dict:
        """پیش‌بینی engagement"""
        
        # استخراج ویژگی‌ها از داده تاریخی
        X_train, y_train = self._prepare_training_data(historical_data)
        
        # آموزش مدل ساده (Linear Regression ساده شده)
        model = await self._train_simple_model(X_train, y_train)
        
        # پیش‌بینی
        X_test = self._extract_features_vector(content_features)
        prediction = await self._predict(model, X_test)
        
        # محاسبه فاصله اطمینان
        confidence_interval = await self._calculate_confidence(
            prediction, historical_data
        )
        
        result = {
            'predicted_engagement': prediction,
            'confidence_interval': confidence_interval,
            'confidence_level': 0.75,  # 75% confidence
            'factors': self._get_influential_factors(content_features, model)
        }
        
        self.prediction_history.append(result)
        
        return result
    
    def _prepare_training_data(self, data: List[Dict]) -> Tuple[List, List]:
        """آماده‌سازی داده آموزشی"""
        X = []
        y = []
        
        for item in data:
            if 'features' in item and 'engagement' in item:
                X.append(self._extract_features_vector(item['features']))
                y.append(item['engagement'])
        
        return X, y
    
    def _extract_features_vector(self, features: Dict) -> List[float]:
        """تبدیل features به vector"""
        vector = [
            features.get('length', 0) / 1000.0,  # نرمال‌سازی
            features.get('word_count', 0) / 100.0,
            1.0 if features.get('has_hashtag', False) else 0.0,
            1.0 if features.get('has_emoji', False) else 0.0,
            features.get('readability_score', 50) / 100.0,
            features.get('hour', 12) / 24.0
        ]
        
        return vector
    
    async def _train_simple_model(self, X: List, y: List) -> Dict:
        """آموزش مدل ساده"""
        if not X or not y:
            return {'weights': [1.0] * 6, 'bias': 0.0}
        
        # ساده‌سازی شده: وزن‌های ثابت
        model = {
            'weights': [10, 5, 15, 12, 8, 7],  # وزن هر ویژگی
            'bias': 20
        }
        
        return model
    
    async def _predict(self, model: Dict, X: List[float]) -> float:
        """پیش‌بینی"""
        weights = model['weights']
        bias = model['bias']
        
        prediction = bias
        for i, feature_value in enumerate(X):
            if i < len(weights):
                prediction += weights[i] * feature_value
        
        return max(0, prediction)  # حداقل 0
    
    async def _calculate_confidence(self, prediction: float, 
                                    historical_data: List[Dict]) -> Tuple[float, float]:
        """محاسبه فاصله اطمینان"""
        if not historical_data:
            return (prediction * 0.8, prediction * 1.2)
        
        # محاسبه انحراف معیار
        engagements = [item.get('engagement', 0) for item in historical_data]
        std = np.std(engagements) if engagements else 10
        
        # فاصله اطمینان 95%
        lower = prediction - 1.96 * std
        upper = prediction + 1.96 * std
        
        return (max(0, lower), upper)
    
    def _get_influential_factors(self, features: Dict, model: Dict) -> List[Dict]:
        """عوامل تاثیرگذار"""
        feature_names = ['length', 'word_count', 'has_hashtag', 
                        'has_emoji', 'readability', 'hour']
        weights = model['weights']
        
        influential = []
        
        for i, name in enumerate(feature_names):
            if i < len(weights):
                influential.append({
                    'feature': name,
                    'weight': weights[i],
                    'impact': 'high' if weights[i] > 10 else 'medium' if weights[i] > 5 else 'low'
                })
        
        return sorted(influential, key=lambda x: x['weight'], reverse=True)


class ClusteringAlgorithm:
    """الگوریتم خوشه‌بندی"""
    
    def __init__(self, n_clusters: int = 5):
        self.n_clusters = n_clusters
        self.clusters = {}
        
    async def cluster_content(self, contents: List[Dict]) -> Dict:
        """خوشه‌بندی محتوا"""
        
        # استخراج ویژگی‌ها
        features_matrix = [self._extract_features(c) for c in contents]
        
        # خوشه‌بندی ساده (K-means ساده شده)
        clusters = await self._simple_kmeans(features_matrix)
        
        # تحلیل خوشه‌ها
        cluster_analysis = await self._analyze_clusters(clusters, contents)
        
        return {
            'clusters': clusters,
            'analysis': cluster_analysis,
            'n_clusters': self.n_clusters
        }
    
    def _extract_features(self, content: Dict) -> List[float]:
        """استخراج ویژگی‌ها"""
        text = content.get('text', '')
        
        return [
            len(text) / 1000.0,
            len(text.split()) / 100.0,
            1.0 if '#' in text else 0.0,
            content.get('engagement', 0) / 100.0
        ]
    
    async def _simple_kmeans(self, features: List[List[float]]) -> Dict:
        """K-means ساده"""
        if not features:
            return {}
        
        # مراکز اولیه تصادفی
        n_features = len(features[0])
        centers = [
            [np.random.random() for _ in range(n_features)]
            for _ in range(self.n_clusters)
        ]
        
        # اختصاص نقاط به نزدیکترین مرکز
        clusters = defaultdict(list)
        
        for idx, feature_vec in enumerate(features):
            distances = [
                self._euclidean_distance(feature_vec, center)
                for center in centers
            ]
            closest_cluster = np.argmin(distances)
            clusters[closest_cluster].append(idx)
        
        return dict(clusters)
    
    def _euclidean_distance(self, vec1: List[float], vec2: List[float]) -> float:
        """فاصله اقلیدسی"""
        return np.sqrt(sum((a - b) ** 2 for a, b in zip(vec1, vec2)))
    
    async def _analyze_clusters(self, clusters: Dict, contents: List[Dict]) -> Dict:
        """تحلیل خوشه‌ها"""
        analysis = {}
        
        for cluster_id, content_indices in clusters.items():
            cluster_contents = [contents[i] for i in content_indices]
            
            avg_length = np.mean([len(c.get('text', '')) for c in cluster_contents])
            avg_engagement = np.mean([c.get('engagement', 0) for c in cluster_contents])
            
            analysis[f'cluster_{cluster_id}'] = {
                'size': len(content_indices),
                'avg_length': avg_length,
                'avg_engagement': avg_engagement,
                'characteristics': self._describe_cluster(cluster_contents)
            }
        
        return analysis
    
    def _describe_cluster(self, contents: List[Dict]) -> str:
        """توصیف خوشه"""
        avg_len = np.mean([len(c.get('text', '')) for c in contents])
        
        if avg_len < 100:
            return 'short_content'
        elif avg_len < 250:
            return 'medium_content'
        else:
            return 'long_content'


class AnomalyDetectionAlgorithm:
    """الگوریتم تشخیص ناهنجاری"""
    
    def __init__(self):
        self.baseline_metrics = {}
        
    async def detect_anomalies(self, data: List[Dict]) -> Dict:
        """تشخیص ناهنجاری‌ها"""
        
        # محاسبه baseline
        if not self.baseline_metrics:
            await self._calculate_baseline(data)
        
        # تشخیص ناهنجاری‌ها
        anomalies = []
        
        for item in data:
            is_anomaly, reason = await self._is_anomaly(item)
            if is_anomaly:
                anomalies.append({
                    'item': item,
                    'reason': reason,
                    'severity': self._calculate_severity(item)
                })
        
        return {
            'anomalies_found': len(anomalies),
            'anomalies': anomalies,
            'baseline': self.baseline_metrics
        }
    
    async def _calculate_baseline(self, data: List[Dict]):
        """محاسبه خط پایه"""
        engagements = [item.get('engagement', 0) for item in data]
        lengths = [len(item.get('content', '')) for item in data]
        
        self.baseline_metrics = {
            'avg_engagement': np.mean(engagements) if engagements else 0,
            'std_engagement': np.std(engagements) if engagements else 0,
            'avg_length': np.mean(lengths) if lengths else 0,
            'std_length': np.std(lengths) if lengths else 0
        }
    
    async def _is_anomaly(self, item: Dict) -> Tuple[bool, str]:
        """آیا ناهنجار است؟"""
        engagement = item.get('engagement', 0)
        content_length = len(item.get('content', ''))
        
        # engagement غیرعادی
        avg_eng = self.baseline_metrics['avg_engagement']
        std_eng = self.baseline_metrics['std_engagement']
        
        if engagement > avg_eng + 3 * std_eng:
            return True, 'Unusually high engagement'
        if engagement < avg_eng - 3 * std_eng and engagement < 10:
            return True, 'Unusually low engagement'
        
        # طول غیرعادی
        avg_len = self.baseline_metrics['avg_length']
        std_len = self.baseline_metrics['std_length']
        
        if content_length > avg_len + 3 * std_len:
            return True, 'Unusually long content'
        
        return False, ''
    
    def _calculate_severity(self, item: Dict) -> str:
        """محاسبه شدت ناهنجاری"""
        engagement = item.get('engagement', 0)
        avg_eng = self.baseline_metrics['avg_engagement']
        
        if engagement < avg_eng * 0.1:
            return 'critical'
        elif engagement < avg_eng * 0.5:
            return 'high'
        elif engagement > avg_eng * 5:
            return 'positive_anomaly'
        else:
            return 'moderate'


# ارکستراتور الگوریتم‌ها
class AlgorithmOrchestrator:
    """مدیریت تمام الگوریتم‌ها"""
    
    def __init__(self):
        self.pattern_recognition = PatternRecognitionAlgorithm()
        self.content_optimization = ContentOptimizationAlgorithm()
        self.predictive_analytics = PredictiveAnalyticsAlgorithm()
        self.clustering = ClusteringAlgorithm()
        self.anomaly_detection = AnomalyDetectionAlgorithm()
        
        logger.info("🧮 All algorithms initialized")
    
    async def run_full_analysis(self, data: List[Dict]) -> Dict[str, Any]:
        """اجرای تحلیل کامل"""
        
        results = {
            'patterns': await self.pattern_recognition.detect_patterns(data),
            'anomalies': await self.anomaly_detection.detect_anomalies(data),
            'clusters': await self.clustering.cluster_content(data),
            'timestamp': datetime.now().isoformat()
        }
        
        return results
