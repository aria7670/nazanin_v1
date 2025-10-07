"""
Spreadsheet Structure Definition
ساختار 15 اسپردشیت اصلی با تمام زیرشیت‌ها

این فایل ساختار کامل 15 اسپردشیت را تعریف می‌کند
"""

from typing import Dict, List, Any

# ═══════════════════════════════════════════════════════════════════════════
# 15 MAIN SPREADSHEETS STRUCTURE
# ساختار 15 اسپردشیت اصلی
# ═══════════════════════════════════════════════════════════════════════════

SPREADSHEET_STRUCTURE = {
    
    # ══════════════════════════════════════════════════════════════════════
    # 1. CORE_DATA - داده‌های اصلی
    # ══════════════════════════════════════════════════════════════════════
    "CORE_DATA": {
        "description": "داده‌های اصلی و بنیادی سیستم",
        "sheets": {
            "System_Config": {
                "headers": ["key", "value", "type", "description", "last_updated"],
                "description": "تنظیمات سیستم"
            },
            "API_Keys": {
                "headers": ["provider", "key", "model", "priority", "status", "usage_count"],
                "description": "کلیدهای API"
            },
            "User_Profiles": {
                "headers": ["user_id", "name", "platform", "first_seen", "last_seen", "message_count"],
                "description": "پروفایل کاربران"
            },
            "Platform_Credentials": {
                "headers": ["platform", "credential_type", "value", "status", "expires_at"],
                "description": "اطلاعات احراز هویت پلتفرم‌ها"
            },
            "System_Status": {
                "headers": ["component", "status", "last_check", "uptime", "errors"],
                "description": "وضعیت اجزای سیستم"
            }
        }
    },
    
    # ══════════════════════════════════════════════════════════════════════
    # 2. CONVERSATION_DATA - داده‌های مکالمه
    # ══════════════════════════════════════════════════════════════════════
    "CONVERSATION_DATA": {
        "description": "ذخیره تمام مکالمات و تعاملات",
        "sheets": {
            "Messages": {
                "headers": ["timestamp", "user_id", "platform", "message", "response", "sentiment", "context"],
                "description": "تمام پیام‌ها"
            },
            "Conversations": {
                "headers": ["conversation_id", "user_id", "start_time", "end_time", "message_count", "summary"],
                "description": "مکالمات کامل"
            },
            "User_Preferences": {
                "headers": ["user_id", "preference_key", "preference_value", "learned_from", "confidence"],
                "description": "ترجیحات یادگرفته شده"
            },
            "Response_Templates": {
                "headers": ["template_id", "category", "template_fa", "template_en", "usage_count", "success_rate"],
                "description": "قالب‌های پاسخ"
            },
            "Conversation_Patterns": {
                "headers": ["pattern_id", "pattern_type", "description", "occurrences", "last_seen"],
                "description": "الگوهای مکالمه"
            }
        }
    },
    
    # ══════════════════════════════════════════════════════════════════════
    # 3. KNOWLEDGE_BASE - پایگاه دانش
    # ══════════════════════════════════════════════════════════════════════
    "KNOWLEDGE_BASE": {
        "description": "دانش عمومی و تخصصی",
        "sheets": {
            "Facts": {
                "headers": ["fact_id", "category", "fact", "source", "confidence", "last_verified"],
                "description": "حقایق و دانسته‌ها"
            },
            "Definitions": {
                "headers": ["term", "definition_fa", "definition_en", "category", "examples"],
                "description": "تعاریف"
            },
            "FAQs": {
                "headers": ["question", "answer", "category", "asked_count", "last_updated"],
                "description": "سوالات متداول"
            },
            "Tutorials": {
                "headers": ["tutorial_id", "title", "category", "content", "difficulty", "views"],
                "description": "آموزش‌ها"
            },
            "References": {
                "headers": ["reference_id", "title", "url", "category", "reliability", "added_date"],
                "description": "منابع و مراجع"
            },
            "Glossary": {
                "headers": ["term_fa", "term_en", "definition", "related_terms", "category"],
                "description": "واژه‌نامه"
            }
        }
    },
    
    # ══════════════════════════════════════════════════════════════════════
    # 4. LEARNING_DATA - داده‌های یادگیری
    # ══════════════════════════════════════════════════════════════════════
    "LEARNING_DATA": {
        "description": "یادگیری و بهبود مستمر",
        "sheets": {
            "Training_Sessions": {
                "headers": ["session_id", "date", "topic", "data_size", "accuracy", "notes"],
                "description": "جلسات آموزش"
            },
            "Feedback": {
                "headers": ["feedback_id", "timestamp", "user_id", "rating", "comment", "category"],
                "description": "بازخوردها"
            },
            "Mistakes": {
                "headers": ["mistake_id", "timestamp", "type", "description", "correction", "learned"],
                "description": "اشتباهات و یادگیری"
            },
            "Performance_Metrics": {
                "headers": ["date", "metric_name", "value", "target", "status", "notes"],
                "description": "معیارهای عملکرد"
            },
            "Improvements": {
                "headers": ["improvement_id", "date", "area", "change", "impact", "status"],
                "description": "بهبودها"
            }
        }
    },
    
    # ══════════════════════════════════════════════════════════════════════
    # 5. CONTENT_LIBRARY - کتابخانه محتوا
    # ══════════════════════════════════════════════════════════════════════
    "CONTENT_LIBRARY": {
        "description": "محتوای تولید شده و ذخیره شده",
        "sheets": {
            "Posts": {
                "headers": ["post_id", "platform", "content", "media_urls", "created_at", "published_at", "engagement"],
                "description": "پست‌ها"
            },
            "Media_Files": {
                "headers": ["file_id", "type", "url", "description", "tags", "uploaded_at"],
                "description": "فایل‌های رسانه‌ای"
            },
            "Templates": {
                "headers": ["template_id", "name", "category", "content", "variables", "usage_count"],
                "description": "قالب‌ها"
            },
            "Hashtags": {
                "headers": ["hashtag", "category", "usage_count", "engagement_rate", "trend_score"],
                "description": "هشتگ‌ها"
            },
            "Content_Calendar": {
                "headers": ["date", "time", "platform", "content_type", "topic", "status"],
                "description": "تقویم محتوا"
            }
        }
    },
    
    # ══════════════════════════════════════════════════════════════════════
    # 6. ANALYTICS_DATA - داده‌های تحلیلی
    # ══════════════════════════════════════════════════════════════════════
    "ANALYTICS_DATA": {
        "description": "تحلیل‌ها و آمار",
        "sheets": {
            "Daily_Stats": {
                "headers": ["date", "messages", "users", "responses", "avg_response_time", "satisfaction"],
                "description": "آمار روزانه"
            },
            "User_Behavior": {
                "headers": ["user_id", "activity_type", "frequency", "peak_hours", "preferences"],
                "description": "رفتار کاربران"
            },
            "Engagement_Metrics": {
                "headers": ["date", "platform", "likes", "comments", "shares", "reach", "impressions"],
                "description": "معیارهای تعامل"
            },
            "Trend_Analysis": {
                "headers": ["trend_id", "topic", "start_date", "peak_date", "volume", "sentiment"],
                "description": "تحلیل روندها"
            },
            "Performance_Reports": {
                "headers": ["report_id", "period", "metric", "value", "comparison", "insights"],
                "description": "گزارش‌های عملکرد"
            }
        }
    },
    
    # ══════════════════════════════════════════════════════════════════════
    # 7. MEMORY_SYSTEM - سیستم حافظه
    # ══════════════════════════════════════════════════════════════════════
    "MEMORY_SYSTEM": {
        "description": "حافظه کوتاه‌مدت و بلندمدت",
        "sheets": {
            "Short_Term_Memory": {
                "headers": ["memory_id", "timestamp", "content", "context", "importance", "expires_at"],
                "description": "حافظه کوتاه‌مدت"
            },
            "Long_Term_Memory": {
                "headers": ["memory_id", "date_stored", "content", "category", "access_count", "last_accessed"],
                "description": "حافظه بلندمدت"
            },
            "Episodic_Memory": {
                "headers": ["episode_id", "date", "event", "participants", "emotions", "outcome"],
                "description": "حافظه اپیزودیک"
            },
            "Semantic_Memory": {
                "headers": ["concept_id", "concept", "definition", "relations", "confidence"],
                "description": "حافظه معنایی"
            },
            "Working_Memory": {
                "headers": ["task_id", "current_task", "context", "variables", "status"],
                "description": "حافظه کاری"
            }
        }
    },
    
    # ══════════════════════════════════════════════════════════════════════
    # 8. PERSONALITY_DATA - داده‌های شخصیتی
    # ══════════════════════════════════════════════════════════════════════
    "PERSONALITY_DATA": {
        "description": "شخصیت و رفتار",
        "sheets": {
            "Traits": {
                "headers": ["trait_name", "value", "min", "max", "last_updated", "influencers"],
                "description": "صفات شخصیتی"
            },
            "Emotions": {
                "headers": ["timestamp", "emotion", "intensity", "trigger", "duration", "response"],
                "description": "احساسات"
            },
            "Moods": {
                "headers": ["date", "time", "mood", "factors", "activities", "social_interactions"],
                "description": "خلق و خو"
            },
            "Behaviors": {
                "headers": ["behavior_id", "behavior_type", "frequency", "context", "outcome"],
                "description": "رفتارها"
            },
            "Values": {
                "headers": ["value_name", "importance", "description", "manifestations", "conflicts"],
                "description": "ارزش‌ها"
            }
        }
    },
    
    # ══════════════════════════════════════════════════════════════════════
    # 9. TASK_MANAGEMENT - مدیریت وظایف
    # ══════════════════════════════════════════════════════════════════════
    "TASK_MANAGEMENT": {
        "description": "مدیریت تسک‌ها و برنامه‌ریزی",
        "sheets": {
            "Tasks": {
                "headers": ["task_id", "title", "description", "priority", "status", "deadline", "assigned_to"],
                "description": "وظایف"
            },
            "Schedules": {
                "headers": ["schedule_id", "task", "frequency", "next_run", "last_run", "status"],
                "description": "برنامه‌زمانی"
            },
            "Goals": {
                "headers": ["goal_id", "goal", "category", "target_date", "progress", "status"],
                "description": "اهداف"
            },
            "Projects": {
                "headers": ["project_id", "name", "description", "start_date", "end_date", "progress"],
                "description": "پروژه‌ها"
            },
            "Reminders": {
                "headers": ["reminder_id", "title", "datetime", "repeat", "sent", "user_id"],
                "description": "یادآوری‌ها"
            }
        }
    },
    
    # ══════════════════════════════════════════════════════════════════════
    # 10. SOCIAL_DATA - داده‌های اجتماعی
    # ══════════════════════════════════════════════════════════════════════
    "SOCIAL_DATA": {
        "description": "شبکه اجتماعی و روابط",
        "sheets": {
            "Relationships": {
                "headers": ["user1_id", "user2_id", "relationship_type", "strength", "interactions", "last_contact"],
                "description": "روابط"
            },
            "Communities": {
                "headers": ["community_id", "name", "platform", "members", "activity_level", "topics"],
                "description": "جوامع"
            },
            "Influencers": {
                "headers": ["influencer_id", "name", "platform", "followers", "engagement_rate", "niche"],
                "description": "تاثیرگذاران"
            },
            "Social_Events": {
                "headers": ["event_id", "title", "date", "participants", "outcome", "insights"],
                "description": "رویدادهای اجتماعی"
            },
            "Network_Analysis": {
                "headers": ["date", "metric", "value", "change", "insights"],
                "description": "تحلیل شبکه"
            }
        }
    },
    
    # ══════════════════════════════════════════════════════════════════════
    # 11. SECURITY_LOGS - لاگ‌های امنیتی
    # ══════════════════════════════════════════════════════════════════════
    "SECURITY_LOGS": {
        "description": "امنیت و ممیزی",
        "sheets": {
            "Access_Logs": {
                "headers": ["timestamp", "user_id", "action", "resource", "ip_address", "result"],
                "description": "لاگ دسترسی"
            },
            "Security_Events": {
                "headers": ["event_id", "timestamp", "type", "severity", "description", "action_taken"],
                "description": "رویدادهای امنیتی"
            },
            "Blocked_Users": {
                "headers": ["user_id", "reason", "blocked_at", "blocked_until", "severity"],
                "description": "کاربران مسدود شده"
            },
            "Suspicious_Activities": {
                "headers": ["activity_id", "timestamp", "user_id", "activity", "risk_score", "investigated"],
                "description": "فعالیت‌های مشکوک"
            },
            "Audit_Trail": {
                "headers": ["timestamp", "user", "action", "before", "after", "reason"],
                "description": "رد ممیزی"
            }
        }
    },
    
    # ══════════════════════════════════════════════════════════════════════
    # 12. BYTELINE_DATA - داده‌های ByteLine
    # ══════════════════════════════════════════════════════════════════════
    "BYTELINE_DATA": {
        "description": "داده‌های کانال ByteLine",
        "sheets": {
            "Channel_Posts": {
                "headers": ["post_id", "date", "content_en", "media", "views", "reactions", "comments"],
                "description": "پست‌های کانال"
            },
            "Subscribers": {
                "headers": ["user_id", "join_date", "activity_level", "interests", "engagement_score"],
                "description": "مشترکین"
            },
            "Content_Ideas": {
                "headers": ["idea_id", "topic", "category", "priority", "status", "notes"],
                "description": "ایده‌های محتوا"
            },
            "Campaign_Tracking": {
                "headers": ["campaign_id", "name", "start_date", "end_date", "goal", "results"],
                "description": "پیگیری کمپین‌ها"
            },
            "Feedback_FA": {
                "headers": ["feedback_id", "date", "user", "feedback_fa", "category", "action_taken"],
                "description": "بازخورد فارسی"
            }
        }
    },
    
    # ══════════════════════════════════════════════════════════════════════
    # 13. RESEARCH_DATA - داده‌های تحقیقاتی
    # ══════════════════════════════════════════════════════════════════════
    "RESEARCH_DATA": {
        "description": "تحقیقات و آزمایش‌ها",
        "sheets": {
            "Experiments": {
                "headers": ["experiment_id", "name", "hypothesis", "method", "results", "conclusion"],
                "description": "آزمایش‌ها"
            },
            "Datasets": {
                "headers": ["dataset_id", "name", "source", "size", "format", "last_updated"],
                "description": "مجموعه داده‌ها"
            },
            "Research_Papers": {
                "headers": ["paper_id", "title", "authors", "year", "url", "summary", "relevance"],
                "description": "مقالات تحقیقاتی"
            },
            "Hypotheses": {
                "headers": ["hypothesis_id", "statement", "status", "evidence", "confidence"],
                "description": "فرضیه‌ها"
            },
            "Observations": {
                "headers": ["observation_id", "date", "context", "observation", "implications"],
                "description": "مشاهدات"
            }
        }
    },
    
    # ══════════════════════════════════════════════════════════════════════
    # 14. AUTOMATION_DATA - داده‌های اتوماسیون
    # ══════════════════════════════════════════════════════════════════════
    "AUTOMATION_DATA": {
        "description": "اتوماسیون و فرآیندها",
        "sheets": {
            "Workflows": {
                "headers": ["workflow_id", "name", "trigger", "steps", "status", "last_run"],
                "description": "گردش کارها"
            },
            "Rules": {
                "headers": ["rule_id", "condition", "action", "priority", "active", "execution_count"],
                "description": "قوانین خودکار"
            },
            "Scripts": {
                "headers": ["script_id", "name", "language", "code", "purpose", "last_modified"],
                "description": "اسکریپت‌ها"
            },
            "Triggers": {
                "headers": ["trigger_id", "type", "condition", "action", "enabled", "fire_count"],
                "description": "ماشه‌ها"
            },
            "Job_Queue": {
                "headers": ["job_id", "type", "priority", "status", "created_at", "completed_at"],
                "description": "صف کارها"
            }
        }
    },
    
    # ══════════════════════════════════════════════════════════════════════
    # 15. INTEGRATION_DATA - داده‌های یکپارچه‌سازی
    # ══════════════════════════════════════════════════════════════════════
    "INTEGRATION_DATA": {
        "description": "یکپارچه‌سازی با سیستم‌های خارجی",
        "sheets": {
            "External_APIs": {
                "headers": ["api_id", "name", "endpoint", "auth_type", "rate_limit", "last_call", "status"],
                "description": "API های خارجی"
            },
            "Webhooks": {
                "headers": ["webhook_id", "url", "event_type", "secret", "active", "last_triggered"],
                "description": "وب‌هوک‌ها"
            },
            "Data_Sync": {
                "headers": ["sync_id", "source", "destination", "frequency", "last_sync", "records_synced"],
                "description": "همگام‌سازی داده"
            },
            "Third_Party_Services": {
                "headers": ["service_id", "name", "type", "credentials", "status", "usage"],
                "description": "سرویس‌های شخص ثالث"
            },
            "Integration_Logs": {
                "headers": ["log_id", "timestamp", "service", "action", "status", "details"],
                "description": "لاگ یکپارچه‌سازی"
            }
        }
    }
}


def get_all_spreadsheet_names() -> List[str]:
    """دریافت نام تمام اسپردشیت‌ها"""
    return list(SPREADSHEET_STRUCTURE.keys())


def get_spreadsheet_info(spreadsheet_name: str) -> Dict:
    """دریافت اطلاعات یک اسپردشیت"""
    return SPREADSHEET_STRUCTURE.get(spreadsheet_name, {})


def get_total_sheets_count() -> int:
    """تعداد کل زیرشیت‌ها"""
    total = 0
    for spreadsheet in SPREADSHEET_STRUCTURE.values():
        total += len(spreadsheet.get('sheets', {}))
    return total


def get_summary() -> Dict:
    """خلاصه ساختار"""
    return {
        'total_spreadsheets': len(SPREADSHEET_STRUCTURE),
        'total_sheets': get_total_sheets_count(),
        'spreadsheet_names': get_all_spreadsheet_names()
    }
