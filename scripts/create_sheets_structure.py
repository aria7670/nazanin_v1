"""
اسکریپت ساخت خودکار ساختار Google Sheets
"""

import gspread
from google.oauth2.service_account import Credentials
import json
import time

# تنظیمات
CREDENTIALS_FILE = '../credentials.json'

# ساختار کامل شیت‌ها
SHEETS_STRUCTURE = {
    'Nazanin_Bot_Configuration': [
        'Personality',
        'Rules',
        'Prompts',
        'Responses',
        'Settings'
    ],
    'Nazanin_AI_Data': [
        'API_Keys',
        'Model_Performance',
        'AI_Responses',
        'Training_Data',
        'Embeddings'
    ],
    'Nazanin_Telegram_Data': [
        'Messages_Log',
        'Channels',
        'Groups',
        'Files_Storage',
        'Media_Archive',
        'Conversations',
        'Channel_Posts',
        'Saved_Messages'
    ],
    'Nazanin_Users_Database': [
        'User_Profiles',
        'User_Behavior',
        'User_Preferences',
        'User_Interactions',
        'VIP_Users',
        'Blocked_Users'
    ],
    'Nazanin_Content_Management': [
        'Tweet_Log',
        'Content_Ideas',
        'Templates',
        'Scheduled_Posts',
        'Content_Archive',
        'Hashtags'
    ],
    'Nazanin_News_Channels': [
        'News_Sources',
        'Collected_News',
        'Trends',
        'RSS_Feeds',
        'Scraped_Data'
    ],
    'Nazanin_Analytics_Performance': [
        'Daily_Stats',
        'Emotions_History',
        'Performance_Metrics',
        'User_Analytics',
        'Content_Performance'
    ],
    'Nazanin_Tasks_Automation': [
        'Active_Tasks',
        'Completed_Tasks',
        'Recurring_Tasks',
        'Failed_Tasks',
        'Workflows'
    ],
    'Nazanin_Cloud_Storage': [
        'Files_Index',
        'Backups',
        'Cache_Data',
        'Temporary_Storage',
        'Media_Storage'
    ],
    'Nazanin_Security_Logs': [
        'Access_Logs',
        'Error_Logs',
        'Security_Events',
        'API_Usage',
        'Suspicious_Activity',
        'Admin_Actions'
    ]
}

# هدرهای هر شیت
SHEET_HEADERS = {
    # Bot Configuration
    'Personality': ['Key', 'Value', 'Description', 'Last_Updated'],
    'Rules': ['Rule_ID', 'Category', 'Rule', 'Priority', 'Active', 'Examples', 'Created_Date'],
    'Prompts': ['Prompt_ID', 'Type', 'Template', 'Variables', 'Usage_Count'],
    'Responses': ['Response_ID', 'Trigger', 'Response', 'Condition', 'Priority'],
    'Settings': ['Setting_Key', 'Setting_Value', 'Type', 'Description'],
    
    # AI Data
    'API_Keys': ['Provider', 'API_Key', 'Status', 'Usage_Count', 'Daily_Limit', 'Last_Used', 'Cost', 'Notes'],
    'Model_Performance': ['Model_Name', 'Provider', 'Avg_Response_Time', 'Success_Rate', 'Cost_Per_Call', 'Total_Calls'],
    'AI_Responses': ['Timestamp', 'Model_Used', 'Input_Tokens', 'Output_Tokens', 'Cost', 'Quality_Score'],
    'Training_Data': ['Data_ID', 'Input', 'Expected_Output', 'Actual_Output', 'Feedback', 'Used_For_Training'],
    'Embeddings': ['Text_ID', 'Text', 'Embedding_Vector', 'Model', 'Created_Date'],
    
    # Telegram Data
    'Messages_Log': ['Message_ID', 'Timestamp', 'Chat_ID', 'User_ID', 'Username', 'Message_Type', 'Content', 'Response', 'Response_Time'],
    'Channels': ['Channel_ID', 'Channel_Name', 'Channel_Username', 'Type', 'Members_Count', 'Description', 'Joined_Date', 'Active'],
    'Groups': ['Group_ID', 'Group_Name', 'Type', 'Members_Count', 'Admin_Rights', 'Joined_Date', 'Active', 'Purpose'],
    'Files_Storage': ['File_ID', 'File_Name', 'File_Type', 'Size', 'Telegram_File_ID', 'Upload_Date', 'Description', 'Tags'],
    'Media_Archive': ['Media_ID', 'Media_Type', 'Telegram_ID', 'Caption', 'Uploaded_By', 'Upload_Date', 'Download_Link'],
    'Conversations': ['Conversation_ID', 'User_ID', 'Start_Time', 'End_Time', 'Message_Count', 'Topic', 'Summary', 'Sentiment'],
    'Channel_Posts': ['Post_ID', 'Channel_ID', 'Timestamp', 'Content', 'Media', 'Views', 'Forwards', 'Reactions'],
    'Saved_Messages': ['Message_ID', 'Timestamp', 'From_Chat', 'Content', 'Tags', 'Importance', 'Notes'],
    
    # Users Database
    'User_Profiles': ['User_ID', 'Username', 'First_Name', 'Last_Name', 'Phone', 'Join_Date', 'Last_Seen', 'Status', 'VIP'],
    'User_Behavior': ['User_ID', 'Total_Messages', 'Avg_Sentiment', 'Favorite_Topics', 'Active_Hours', 'Response_Rate', 'Engagement_Score'],
    'User_Preferences': ['User_ID', 'Language', 'Preferred_Length', 'Tone_Preference', 'Notification_Settings', 'Tags'],
    'User_Interactions': ['Interaction_ID', 'User_ID', 'Timestamp', 'Type', 'Content', 'Platform', 'Outcome'],
    'VIP_Users': ['User_ID', 'VIP_Level', 'Benefits', 'Joined_VIP', 'Subscription_Status', 'Notes'],
    'Blocked_Users': ['User_ID', 'Block_Date', 'Reason', 'Blocked_By', 'Unblock_Date', 'Notes'],
    
    # Content Management
    'Tweet_Log': ['Tweet_ID', 'Timestamp', 'Content', 'Type', 'Category', 'Engagement', 'Impressions', 'AI_Used', 'Status'],
    'Content_Ideas': ['Idea_ID', 'Topic', 'Type', 'Priority', 'Status', 'Scheduled_For', 'Created_Date', 'Notes'],
    'Templates': ['Template_ID', 'Name', 'Content', 'Variables', 'Category', 'Usage_Count', 'Success_Rate'],
    'Scheduled_Posts': ['Post_ID', 'Platform', 'Content', 'Media', 'Scheduled_Time', 'Status', 'Created_By'],
    'Content_Archive': ['Archive_ID', 'Content', 'Platform', 'Published_Date', 'Performance', 'Tags', 'Archived_Date'],
    'Hashtags': ['Hashtag', 'Usage_Count', 'Avg_Engagement', 'Category', 'Trending_Score', 'Last_Used'],
    
    # News Channels
    'News_Sources': ['Source_ID', 'Source_Name', 'Type', 'Channel_ID', 'URL', 'Category', 'Language', 'Active', 'Reliability_Score'],
    'Collected_News': ['News_ID', 'Source_ID', 'Timestamp', 'Title', 'Summary', 'Full_Text', 'Link', 'Category', 'Relevance_Score'],
    'Trends': ['Trend_ID', 'Keyword', 'Category', 'Volume', 'Growth_Rate', 'First_Seen', 'Peak_Time', 'Status'],
    'RSS_Feeds': ['Feed_ID', 'Feed_URL', 'Name', 'Category', 'Last_Checked', 'Items_Count', 'Active'],
    'Scraped_Data': ['Scrape_ID', 'Source', 'Timestamp', 'Data_Type', 'Content', 'Processed', 'Stored_Location'],
    
    # Analytics Performance
    'Daily_Stats': ['Date', 'Platform', 'Posts_Count', 'Engagement', 'New_Followers', 'Reach', 'Impressions'],
    'Emotions_History': ['Timestamp', 'Joy', 'Trust', 'Fear', 'Surprise', 'Sadness', 'Disgust', 'Anger', 'Anticipation', 'Curiosity', 'Confidence'],
    'Performance_Metrics': ['Date', 'Response_Time', 'Uptime_Percent', 'API_Calls', 'Errors', 'Success_Rate', 'Cost'],
    'User_Analytics': ['Date', 'Active_Users', 'New_Users', 'Returning_Users', 'Avg_Session_Time', 'Bounce_Rate'],
    'Content_Performance': ['Content_ID', 'Type', 'Engagement_Rate', 'Viral_Score', 'Best_Time', 'Audience_Segment'],
    
    # Tasks Automation
    'Active_Tasks': ['Task_ID', 'Type', 'Description', 'Priority', 'Status', 'Assigned_Agent', 'Created', 'Deadline'],
    'Completed_Tasks': ['Task_ID', 'Type', 'Description', 'Completed_At', 'Result', 'Duration', 'Agent_Used'],
    'Recurring_Tasks': ['Task_ID', 'Type', 'Schedule', 'Frequency', 'Last_Run', 'Next_Run', 'Active', 'Configuration'],
    'Failed_Tasks': ['Task_ID', 'Type', 'Failed_At', 'Error_Message', 'Retry_Count', 'Status', 'Notes'],
    'Workflows': ['Workflow_ID', 'Name', 'Steps', 'Trigger', 'Condition', 'Active', 'Success_Rate'],
    
    # Cloud Storage
    'Files_Index': ['File_ID', 'File_Name', 'Storage_Location', 'Size', 'Type', 'Upload_Date', 'Last_Access', 'Tags'],
    'Backups': ['Backup_ID', 'Backup_Type', 'Timestamp', 'Size', 'Location', 'Status', 'Restore_Point'],
    'Cache_Data': ['Cache_Key', 'Data', 'Created_At', 'Expires_At', 'Hit_Count', 'Size'],
    'Temporary_Storage': ['Temp_ID', 'Data', 'Created_At', 'Expires_At', 'Purpose', 'Auto_Delete'],
    'Media_Storage': ['Media_ID', 'Type', 'URL', 'Telegram_File_ID', 'Size', 'Upload_Date', 'Description'],
    
    # Security Logs
    'Access_Logs': ['Log_ID', 'Timestamp', 'User_ID', 'Action', 'IP_Address', 'Status', 'Details'],
    'Error_Logs': ['Error_ID', 'Timestamp', 'Error_Type', 'Message', 'Stack_Trace', 'Severity', 'Resolved'],
    'Security_Events': ['Event_ID', 'Timestamp', 'Type', 'Severity', 'Description', 'Action_Taken', 'Status'],
    'API_Usage': ['Timestamp', 'API_Name', 'Endpoint', 'User', 'Response_Time', 'Status_Code', 'Cost'],
    'Suspicious_Activity': ['Activity_ID', 'Timestamp', 'User_ID', 'Type', 'Description', 'Risk_Level', 'Investigated'],
    'Admin_Actions': ['Action_ID', 'Timestamp', 'Admin_ID', 'Action', 'Target', 'Reason', 'Result'],
}


def create_sheets_structure():
    """ساخت خودکار تمام ساختار شیت‌ها"""
    
    print("🚀 شروع ساخت ساختار Google Sheets...")
    print()
    
    # اتصال به Google
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=scope)
    client = gspread.authorize(creds)
    
    service_account_email = creds.service_account_email
    print(f"✅ متصل شد با: {service_account_email}")
    print()
    
    spreadsheet_ids = {}
    
    # ساخت هر Spreadsheet
    for spreadsheet_name, sheet_names in SHEETS_STRUCTURE.items():
        print(f"📊 در حال ساخت: {spreadsheet_name}")
        
        try:
            # ساخت Spreadsheet جدید
            spreadsheet = client.create(spreadsheet_name)
            spreadsheet_id = spreadsheet.id
            
            print(f"   ✅ Spreadsheet ساخته شد: {spreadsheet_id}")
            
            # حذف Sheet پیش‌فرض
            default_sheet = spreadsheet.sheet1
            
            # ساخت Sheet های مورد نیاز
            for i, sheet_name in enumerate(sheet_names):
                if i == 0:
                    # Sheet اول رو rename می‌کنیم
                    default_sheet.update_title(sheet_name)
                    worksheet = default_sheet
                else:
                    # بقیه رو جدید می‌سازیم
                    worksheet = spreadsheet.add_worksheet(title=sheet_name, rows=1000, cols=20)
                
                # اضافه کردن هدرها
                if sheet_name in SHEET_HEADERS:
                    headers = SHEET_HEADERS[sheet_name]
                    worksheet.append_row(headers)
                    print(f"      ✅ {sheet_name} (با {len(headers)} ستون)")
                
                time.sleep(0.5)  # جلوگیری از rate limit
            
            # ذخیره ID
            key = spreadsheet_name.replace('Nazanin_', '').lower()
            spreadsheet_ids[key] = spreadsheet_id
            
            print(f"   🔗 Share این لینک رو با Service Account:")
            print(f"      {service_account_email}")
            print()
            
            time.sleep(1)  # جلوگیری از rate limit
            
        except Exception as e:
            print(f"   ❌ خطا: {e}")
            print()
    
    # ذخیره IDها در فایل
    config_output = {
        "google_sheets": {
            "credentials_file": "credentials.json",
            "spreadsheets": spreadsheet_ids
        }
    }
    
    with open('spreadsheet_ids.json', 'w', encoding='utf-8') as f:
        json.dump(config_output, f, indent=2, ensure_ascii=False)
    
    print("=" * 60)
    print("✅ تمام Spreadsheet ها ساخته شدند!")
    print()
    print("📝 Spreadsheet IDs ذخیره شد در: spreadsheet_ids.json")
    print()
    print("⚠️  مهم: همه Spreadsheet ها رو با Service Account share کن:")
    print(f"   {service_account_email}")
    print("   دسترسی: Editor")
    print("=" * 60)
    
    # نمایش IDها
    print()
    print("📋 Spreadsheet IDs:")
    print()
    for key, sid in spreadsheet_ids.items():
        print(f"   {key}: {sid}")
    

if __name__ == '__main__':
    try:
        create_sheets_structure()
    except FileNotFoundError:
        print("❌ فایل credentials.json پیدا نشد!")
        print("💡 مطمئن شو فایل credentials.json کنار این اسکریپت هست")
    except Exception as e:
        print(f"❌ خطا: {e}")
