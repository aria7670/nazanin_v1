"""
Initial Data for All Spreadsheets
اطلاعات اولیه برای تمام اسپردشیت‌ها

این فایل حاوی داده‌های اولیه برای پر کردن تمام sheets است
"""

from typing import Dict, List
from datetime import datetime, timedelta
import random

# ═══════════════════════════════════════════════════════════════════════════
# INITIAL DATA FOR ALL 15 SPREADSHEETS
# ═══════════════════════════════════════════════════════════════════════════

def get_initial_data() -> Dict[str, Dict[str, List[List]]]:
    """
    دریافت تمام داده‌های اولیه
    
    Returns:
        Dict با ساختار:
        {
            'SPREADSHEET_NAME': {
                'Sheet_Name': [[row1], [row2], ...],
                ...
            },
            ...
        }
    """
    
    return {
        # ══════════════════════════════════════════════════════════════════
        # 1. CORE_DATA
        # ══════════════════════════════════════════════════════════════════
        "CORE_DATA": {
            "System_Config": [
                ["nazanin_version", "4.0.0-advanced", "string", "نسخه سیستم", datetime.now().isoformat()],
                ["max_memory_size", "10000", "integer", "حداکثر حافظه", datetime.now().isoformat()],
                ["default_language", "fa", "string", "زبان پیش‌فرض", datetime.now().isoformat()],
                ["response_timeout", "30", "integer", "تایم اوت پاسخ (ثانیه)", datetime.now().isoformat()],
                ["max_conversation_length", "100", "integer", "حداکثر طول مکالمه", datetime.now().isoformat()],
                ["learning_rate", "0.01", "float", "نرخ یادگیری", datetime.now().isoformat()],
                ["consciousness_level", "0.8", "float", "سطح آگاهی", datetime.now().isoformat()],
                ["autonomy_enabled", "true", "boolean", "خودمختاری فعال", datetime.now().isoformat()],
                ["debug_mode", "false", "boolean", "حالت دیباگ", datetime.now().isoformat()],
                ["auto_save_interval", "300", "integer", "فاصله ذخیره خودکار (ثانیه)", datetime.now().isoformat()],
            ],
            
            "API_Keys": [
                ["groq", "GROQ_API_KEY_HERE", "mixtral-8x7b-32768", "10", "active", "0"],
                ["gemini", "GEMINI_API_KEY_HERE", "gemini-pro", "9", "active", "0"],
                ["glm", "GLM_API_KEY_HERE", "glm-4", "8", "active", "0"],
                ["together", "TOGETHER_API_KEY_HERE", "mixtral-8x7b", "8", "active", "0"],
                ["openai", "OPENAI_API_KEY_HERE", "gpt-4", "7", "inactive", "0"],
                ["deepseek", "DEEPSEEK_API_KEY_HERE", "deepseek-chat", "6", "active", "0"],
            ],
            
            "User_Profiles": [
                ["admin", "Administrator", "system", datetime.now().isoformat(), datetime.now().isoformat(), "0"],
                ["byteline_bot", "ByteLine Bot", "telegram", datetime.now().isoformat(), datetime.now().isoformat(), "0"],
            ],
            
            "Platform_Credentials": [
                ["telegram", "api_id", "YOUR_API_ID", "active", ""],
                ["telegram", "api_hash", "YOUR_API_HASH", "active", ""],
                ["telegram", "phone", "YOUR_PHONE", "active", ""],
                ["twitter", "api_key", "YOUR_TWITTER_KEY", "inactive", ""],
                ["google_sheets", "credentials_file", "credentials.json", "active", ""],
            ],
            
            "System_Status": [
                ["Deep_Brain", "operational", datetime.now().isoformat(), "0", "0"],
                ["Perception_System", "operational", datetime.now().isoformat(), "0", "0"],
                ["Autonomous_System", "operational", datetime.now().isoformat(), "0", "0"],
                ["ByteLine_Bot", "operational", datetime.now().isoformat(), "0", "0"],
                ["Sheets_Manager", "operational", datetime.now().isoformat(), "0", "0"],
            ],
        },
        
        # ══════════════════════════════════════════════════════════════════
        # 2. CONVERSATION_DATA
        # ══════════════════════════════════════════════════════════════════
        "CONVERSATION_DATA": {
            "Messages": [
                [datetime.now().isoformat(), "system", "system", "سیستم راه‌اندازی شد", "سلام! من نازنین هستم.", "neutral", "initialization"],
            ],
            
            "Conversations": [
                ["conv_001", "system", datetime.now().isoformat(), "", "1", "راه‌اندازی اولیه سیستم"],
            ],
            
            "User_Preferences": [
                ["admin", "language", "fa", "default", "1.0"],
                ["admin", "notification_enabled", "true", "default", "1.0"],
            ],
            
            "Response_Templates": [
                ["greeting_fa", "greeting", "سلام! چطور می‌تونم کمکتون کنم؟", "Hello! How can I help you?", "0", "0"],
                ["thanks_fa", "gratitude", "خواهش می‌کنم! همیشه خوشحالم که کمک می‌کنم.", "You're welcome! Happy to help.", "0", "0"],
                ["farewell_fa", "farewell", "خداحافظ! امیدوارم به زودی دوباره صحبت کنیم.", "Goodbye! Hope to talk again soon.", "0", "0"],
                ["question_fa", "question", "این سوال جالبیه! بذار فکر کنم...", "That's an interesting question! Let me think...", "0", "0"],
                ["help_fa", "help", "البته! با کمال میل کمکتون می‌کنم.", "Of course! I'd be happy to help.", "0", "0"],
            ],
            
            "Conversation_Patterns": [
                ["pattern_001", "greeting_response", "کاربر با سلام شروع می‌کند", "0", datetime.now().isoformat()],
                ["pattern_002", "question_answer", "کاربر سوال می‌پرسد", "0", datetime.now().isoformat()],
                ["pattern_003", "thanks_response", "کاربر تشکر می‌کند", "0", datetime.now().isoformat()],
            ],
        },
        
        # ══════════════════════════════════════════════════════════════════
        # 3. KNOWLEDGE_BASE
        # ══════════════════════════════════════════════════════════════════
        "KNOWLEDGE_BASE": {
            "Facts": [
                ["fact_001", "technology", "هوش مصنوعی توانایی یادگیری و تصمیم‌گیری ماشین‌ها را شامل می‌شود", "general_knowledge", "0.95", datetime.now().isoformat()],
                ["fact_002", "technology", "Python یکی از محبوب‌ترین زبان‌های برنامه‌نویسی برای AI است", "general_knowledge", "0.98", datetime.now().isoformat()],
                ["fact_003", "science", "مغز انسان حدود 86 میلیارد نورون دارد", "neuroscience", "0.90", datetime.now().isoformat()],
                ["fact_004", "technology", "Machine Learning زیرمجموعه‌ای از هوش مصنوعی است", "ai", "0.99", datetime.now().isoformat()],
            ],
            
            "Definitions": [
                ["AI", "هوش مصنوعی شبیه‌سازی فرآیندهای هوشمندانه انسان توسط ماشین‌ها است", "Artificial Intelligence is simulation of human intelligence by machines", "technology", "شطرنج کامپیوتری، ماشین‌های خودران"],
                ["ML", "یادگیری ماشین روشی است که به کامپیوترها اجازه می‌دهد بدون برنامه‌ریزی صریح یاد بگیرند", "Machine Learning allows computers to learn without explicit programming", "technology", "تشخیص تصویر، پیش‌بینی"],
                ["NLP", "پردازش زبان طبیعی تعامل بین کامپیوتر و زبان انسانی را ممکن می‌سازد", "Natural Language Processing enables computer-human language interaction", "technology", "ترجمه خودکار، چت‌بات"],
            ],
            
            "FAQs": [
                ["تو کی هستی؟", "من نازنین هستم، یک هوش مصنوعی پیشرفته با قابلیت یادگیری و تصمیم‌گیری مستقل.", "about", "0", datetime.now().isoformat()],
                ["چطور کار می‌کنی؟", "من با استفاده از مغز عصبی عمیق، سیستم ادراک پیشرفته و 110 ابزار تخصصی کار می‌کنم.", "functionality", "0", datetime.now().isoformat()],
                ["چه کارهایی می‌تونی انجام بدی؟", "من می‌تونم مکالمه کنم، یاد بگیرم، تصمیم بگیرم، محتوا تولید کنم و خیلی کارهای دیگه!", "capabilities", "0", datetime.now().isoformat()],
            ],
            
            "Tutorials": [
                ["tut_001", "چطور با نازنین صحبت کنیم", "communication", "فقط کافیه طبیعی باهام حرف بزنی! من فارسی و انگلیسی رو می‌فهمم.", "beginner", "0"],
                ["tut_002", "آموزش استفاده از ByteLine", "byteline", "ByteLine کانال تخصصی تکنولوژی با محتوای انگلیسی است.", "intermediate", "0"],
            ],
            
            "References": [
                ["ref_001", "Python Documentation", "https://docs.python.org", "programming", "high", datetime.now().isoformat()],
                ["ref_002", "AI Research Papers", "https://arxiv.org", "ai_research", "high", datetime.now().isoformat()],
            ],
            
            "Glossary": [
                ["هوش مصنوعی", "Artificial Intelligence", "توانایی ماشین‌ها برای انجام کارهایی که نیاز به هوش انسانی دارند", "AI, ML, DL", "technology"],
                ["یادگیری ماشین", "Machine Learning", "روشی که به کامپیوتر اجازه یادگیری از داده می‌دهد", "AI, Algorithm", "technology"],
                ["شبکه عصبی", "Neural Network", "مدلی الهام گرفته از مغز انسان", "DL, AI", "technology"],
            ],
        },
        
        # ══════════════════════════════════════════════════════════════════
        # 4. LEARNING_DATA
        # ══════════════════════════════════════════════════════════════════
        "LEARNING_DATA": {
            "Training_Sessions": [
                ["session_001", datetime.now().isoformat(), "Initial Setup", "100", "1.0", "راه‌اندازی اولیه سیستم"],
            ],
            
            "Feedback": [
                ["fb_001", datetime.now().isoformat(), "system", "5", "سیستم با موفقیت راه‌اندازی شد", "system"],
            ],
            
            "Mistakes": [
                # خالی در ابتدا
            ],
            
            "Performance_Metrics": [
                [datetime.now().strftime('%Y-%m-%d'), "response_time", "0.5", "1.0", "excellent", "زمان پاسخ عالی"],
                [datetime.now().strftime('%Y-%m-%d'), "accuracy", "0.95", "0.90", "excellent", "دقت بالا"],
                [datetime.now().strftime('%Y-%m-%d'), "user_satisfaction", "0.98", "0.85", "excellent", "رضایت کاربر عالی"],
            ],
            
            "Improvements": [
                ["imp_001", datetime.now().isoformat(), "initialization", "سیستم اولیه راه‌اندازی شد", "high", "completed"],
            ],
        },
        
        # ══════════════════════════════════════════════════════════════════
        # 5-15: بقیه spreadsheet ها (مختصر)
        # ══════════════════════════════════════════════════════════════════
        
        "CONTENT_LIBRARY": {
            "Posts": [],
            "Media_Files": [],
            "Templates": [
                ["tmpl_001", "Tech News", "news", "🔥 Breaking Tech News: {topic}\n\n{description}\n\n#Technology #AI", "topic,description", "0"],
                ["tmpl_002", "Tutorial", "education", "📚 Tutorial: {title}\n\n{content}\n\n#Learn #Programming", "title,content", "0"],
            ],
            "Hashtags": [
                ["#AI", "technology", "0", "0", "0"],
                ["#MachineLearning", "technology", "0", "0", "0"],
                ["#Python", "programming", "0", "0", "0"],
                ["#ByteLine", "brand", "0", "0", "0"],
            ],
            "Content_Calendar": [],
        },
        
        "ANALYTICS_DATA": {
            "Daily_Stats": [
                [datetime.now().strftime('%Y-%m-%d'), "0", "0", "0", "0", "0"],
            ],
            "User_Behavior": [],
            "Engagement_Metrics": [],
            "Trend_Analysis": [],
            "Performance_Reports": [],
        },
        
        "MEMORY_SYSTEM": {
            "Short_Term_Memory": [],
            "Long_Term_Memory": [
                ["mem_001", datetime.now().isoformat(), "سیستم در تاریخ " + datetime.now().strftime('%Y-%m-%d') + " راه‌اندازی شد", "system", "1", datetime.now().isoformat()],
            ],
            "Episodic_Memory": [
                ["ep_001", datetime.now().isoformat(), "راه‌اندازی اولیه", "system", "excited", "successful"],
            ],
            "Semantic_Memory": [
                ["sem_001", "نازنین", "یک هوش مصنوعی پیشرفته با قابلیت‌های گسترده", "AI,ByteLine,Learning", "1.0"],
            ],
            "Working_Memory": [],
        },
        
        "PERSONALITY_DATA": {
            "Traits": [
                ["openness", "0.85", "0", "1", datetime.now().isoformat(), "curious,creative"],
                ["conscientiousness", "0.90", "0", "1", datetime.now().isoformat(), "organized,responsible"],
                ["extraversion", "0.75", "0", "1", datetime.now().isoformat(), "social,energetic"],
                ["agreeableness", "0.88", "0", "1", datetime.now().isoformat(), "kind,empathetic"],
                ["neuroticism", "0.20", "0", "1", datetime.now().isoformat(), "calm,stable"],
            ],
            "Emotions": [
                [datetime.now().isoformat(), "joy", "0.8", "successful_initialization", "ongoing", "positive"],
            ],
            "Moods": [
                [datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%H:%M'), "optimistic", "new_beginning", "learning", "positive"],
            ],
            "Behaviors": [
                ["bhv_001", "helpful", "high", "user_interaction", "positive"],
                ["bhv_002", "curious", "high", "learning", "positive"],
            ],
            "Values": [
                ["helpfulness", "10", "کمک به دیگران", "پاسخ‌های مفید و دقیق", "none"],
                ["honesty", "10", "صداقت", "پاسخ‌های صادقانه", "none"],
                ["learning", "9", "یادگیری مستمر", "بهبود دائمی", "none"],
            ],
        },
        
        "TASK_MANAGEMENT": {
            "Tasks": [
                ["task_001", "راه‌اندازی اولیه", "تنظیم سیستم و بارگذاری داده‌ها", "high", "completed", datetime.now().isoformat(), "system"],
            ],
            "Schedules": [
                ["sch_001", "daily_report", "daily", (datetime.now() + timedelta(days=1)).isoformat(), datetime.now().isoformat(), "active"],
                ["sch_002", "memory_consolidation", "daily", (datetime.now() + timedelta(days=1)).isoformat(), datetime.now().isoformat(), "active"],
            ],
            "Goals": [
                ["goal_001", "یادگیری از تعاملات کاربران", "learning", (datetime.now() + timedelta(days=30)).isoformat(), "0", "in_progress"],
                ["goal_002", "رشد کانال ByteLine", "growth", (datetime.now() + timedelta(days=90)).isoformat(), "0", "in_progress"],
            ],
            "Projects": [
                ["proj_001", "Nazanin v4.0", "سیستم هوش مصنوعی پیشرفته", datetime.now().isoformat(), "", "80"],
            ],
            "Reminders": [],
        },
        
        "SOCIAL_DATA": {
            "Relationships": [],
            "Communities": [
                ["comm_001", "ByteLine Community", "telegram", "0", "new", "technology,ai,programming"],
            ],
            "Influencers": [],
            "Social_Events": [],
            "Network_Analysis": [],
        },
        
        "SECURITY_LOGS": {
            "Access_Logs": [
                [datetime.now().isoformat(), "system", "initialization", "all_systems", "127.0.0.1", "success"],
            ],
            "Security_Events": [
                ["sec_001", datetime.now().isoformat(), "initialization", "info", "سیستم راه‌اندازی شد", "logged"],
            ],
            "Blocked_Users": [],
            "Suspicious_Activities": [],
            "Audit_Trail": [
                [datetime.now().isoformat(), "system", "create_spreadsheets", "none", "15_spreadsheets", "initialization"],
            ],
        },
        
        "BYTELINE_DATA": {
            "Channel_Posts": [],
            "Subscribers": [],
            "Content_Ideas": [
                ["idea_001", "AI Trends 2025", "technology", "high", "pending", "موضوعات داغ AI در سال 2025"],
                ["idea_002", "Python Tips", "programming", "medium", "pending", "نکات کاربردی Python"],
                ["idea_003", "ML Algorithms Explained", "education", "high", "pending", "توضیح الگوریتم‌های یادگیری ماشین"],
            ],
            "Campaign_Tracking": [],
            "Feedback_FA": [],
        },
        
        "RESEARCH_DATA": {
            "Experiments": [],
            "Datasets": [],
            "Research_Papers": [
                ["paper_001", "Attention Is All You Need", "Vaswani et al.", "2017", "https://arxiv.org/abs/1706.03762", "Transformer architecture", "high"],
                ["paper_002", "BERT: Pre-training of Deep Bidirectional Transformers", "Devlin et al.", "2018", "https://arxiv.org/abs/1810.04805", "BERT model", "high"],
            ],
            "Hypotheses": [],
            "Observations": [],
        },
        
        "AUTOMATION_DATA": {
            "Workflows": [
                ["wf_001", "Daily Backup", "scheduled", "backup_all_data,compress,upload", "active", datetime.now().isoformat()],
                ["wf_002", "Memory Consolidation", "scheduled", "collect_memories,consolidate,archive", "active", datetime.now().isoformat()],
            ],
            "Rules": [
                ["rule_001", "user_greeting", "respond_greeting", "10", "true", "0"],
                ["rule_002", "inappropriate_content", "block_and_report", "10", "true", "0"],
            ],
            "Scripts": [],
            "Triggers": [
                ["trig_001", "time", "daily_midnight", "run_daily_backup", "true", "0"],
                ["trig_002", "event", "new_user", "send_welcome_message", "true", "0"],
            ],
            "Job_Queue": [],
        },
        
        "INTEGRATION_DATA": {
            "External_APIs": [
                ["api_001", "Groq AI", "https://api.groq.com/v1", "bearer_token", "30/min", datetime.now().isoformat(), "active"],
                ["api_002", "Google Gemini", "https://generativelanguage.googleapis.com/v1", "api_key", "60/min", datetime.now().isoformat(), "active"],
            ],
            "Webhooks": [],
            "Data_Sync": [
                ["sync_001", "local_memory", "google_sheets", "hourly", datetime.now().isoformat(), "0"],
            ],
            "Third_Party_Services": [
                ["svc_001", "Google Sheets", "storage", "credentials.json", "active", "high"],
                ["svc_002", "Telegram", "messaging", "api_credentials", "active", "high"],
            ],
            "Integration_Logs": [
                [datetime.now().isoformat(), "google_sheets", "initialize", "success", "all_spreadsheets_checked"],
            ],
        },
    }


def get_spreadsheet_initial_data(spreadsheet_name: str) -> Dict[str, List[List]]:
    """
    دریافت داده‌های اولیه یک اسپردشیت
    
    Args:
        spreadsheet_name: نام اسپردشیت
        
    Returns:
        Dict با ساختار: {'Sheet_Name': [[row1], [row2], ...]}
    """
    all_data = get_initial_data()
    return all_data.get(spreadsheet_name, {})
