"""
Auto Setup Google Sheets
ساخت خودکار تمام شیت‌ها در اولین اجرا
"""

import gspread
from google.oauth2.service_account import Credentials
import logging
import time
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)


class SheetsAutoSetup:
    """ساخت و مدیریت خودکار Google Sheets"""
    
    # تعریف کامل ساختار شیت‌ها
    SPREADSHEET_STRUCTURE = {
        'Bot_Configuration': {
            'sheets': {
                'Personality': ['Key', 'Value', 'Description', 'Last_Updated'],
                'Rules': ['Rule_ID', 'Category', 'Rule', 'Priority', 'Active', 'Examples', 'Created_Date'],
                'Prompts': ['Prompt_ID', 'Type', 'Template', 'Variables', 'Usage_Count'],
                'Responses': ['Response_ID', 'Trigger', 'Response', 'Condition', 'Priority'],
                'Settings': ['Setting_Key', 'Setting_Value', 'Type', 'Description']
            },
            'initial_data': {
                'Personality': [
                    ['name', 'نازنین', 'نام ربات', '2025-10-06'],
                    ['tone', 'friendly', 'لحن گفتگو', '2025-10-06'],
                    ['personality_type', 'ENFP', 'تیپ شخصیتی', '2025-10-06']
                ],
                'Settings': [
                    ['auto_backup', 'true', 'boolean', 'بک‌آپ خودکار'],
                    ['cache_enabled', 'true', 'boolean', 'فعال بودن کش']
                ]
            }
        },
        
        'AI_Data': {
            'sheets': {
                'API_Keys': ['Provider', 'API_Key', 'Status', 'Usage_Count', 'Daily_Limit', 'Last_Used', 'Cost', 'Notes'],
                'Model_Performance': ['Model_Name', 'Provider', 'Avg_Response_Time', 'Success_Rate', 'Cost_Per_Call', 'Total_Calls'],
                'AI_Responses': ['Timestamp', 'Model_Used', 'Input_Tokens', 'Output_Tokens', 'Cost', 'Quality_Score'],
                'Training_Data': ['Data_ID', 'Input', 'Expected_Output', 'Actual_Output', 'Feedback', 'Used_For_Training'],
                'Embeddings': ['Text_ID', 'Text', 'Embedding_Vector', 'Model', 'Created_Date']
            }
        },
        
        'Telegram_Data': {
            'sheets': {
                'Messages_Log': ['Message_ID', 'Timestamp', 'Chat_ID', 'User_ID', 'Username', 'Message_Type', 'Content', 'Response', 'Response_Time'],
                'Channels': ['Channel_ID', 'Channel_Name', 'Channel_Username', 'Type', 'Members_Count', 'Description', 'Joined_Date', 'Active'],
                'Groups': ['Group_ID', 'Group_Name', 'Type', 'Members_Count', 'Admin_Rights', 'Joined_Date', 'Active', 'Purpose'],
                'Files_Storage': ['File_ID', 'File_Name', 'File_Type', 'Size', 'Telegram_File_ID', 'Upload_Date', 'Description', 'Tags'],
                'Media_Archive': ['Media_ID', 'Media_Type', 'Telegram_ID', 'Caption', 'Uploaded_By', 'Upload_Date', 'Download_Link'],
                'Conversations': ['Conversation_ID', 'User_ID', 'Start_Time', 'End_Time', 'Message_Count', 'Topic', 'Summary', 'Sentiment'],
                'Channel_Posts': ['Post_ID', 'Channel_ID', 'Timestamp', 'Content', 'Media', 'Views', 'Forwards', 'Reactions'],
                'Saved_Messages': ['Message_ID', 'Timestamp', 'From_Chat', 'Content', 'Tags', 'Importance', 'Notes']
            }
        },
        
        'Users_Database': {
            'sheets': {
                'User_Profiles': ['User_ID', 'Username', 'First_Name', 'Last_Name', 'Phone', 'Join_Date', 'Last_Seen', 'Status', 'VIP'],
                'User_Behavior': ['User_ID', 'Total_Messages', 'Avg_Sentiment', 'Favorite_Topics', 'Active_Hours', 'Response_Rate', 'Engagement_Score'],
                'User_Preferences': ['User_ID', 'Language', 'Preferred_Length', 'Tone_Preference', 'Notification_Settings', 'Tags'],
                'User_Interactions': ['Interaction_ID', 'User_ID', 'Timestamp', 'Type', 'Content', 'Platform', 'Outcome'],
                'VIP_Users': ['User_ID', 'VIP_Level', 'Benefits', 'Joined_VIP', 'Subscription_Status', 'Notes'],
                'Blocked_Users': ['User_ID', 'Block_Date', 'Reason', 'Blocked_By', 'Unblock_Date', 'Notes']
            }
        },
        
        'Content_Management': {
            'sheets': {
                'Tweet_Log': ['Tweet_ID', 'Timestamp', 'Content', 'Type', 'Category', 'Engagement', 'Impressions', 'AI_Used', 'Status'],
                'Content_Ideas': ['Idea_ID', 'Topic', 'Type', 'Priority', 'Status', 'Scheduled_For', 'Created_Date', 'Notes'],
                'Templates': ['Template_ID', 'Name', 'Content', 'Variables', 'Category', 'Usage_Count', 'Success_Rate'],
                'Scheduled_Posts': ['Post_ID', 'Platform', 'Content', 'Media', 'Scheduled_Time', 'Status', 'Created_By'],
                'Content_Archive': ['Archive_ID', 'Content', 'Platform', 'Published_Date', 'Performance', 'Tags', 'Archived_Date'],
                'Hashtags': ['Hashtag', 'Usage_Count', 'Avg_Engagement', 'Category', 'Trending_Score', 'Last_Used']
            }
        },
        
        'News_Channels': {
            'sheets': {
                'News_Sources': ['Source_ID', 'Source_Name', 'Type', 'Channel_ID', 'URL', 'Category', 'Language', 'Active', 'Reliability_Score'],
                'Collected_News': ['News_ID', 'Source_ID', 'Timestamp', 'Title', 'Summary', 'Full_Text', 'Link', 'Category', 'Relevance_Score'],
                'Trends': ['Trend_ID', 'Keyword', 'Category', 'Volume', 'Growth_Rate', 'First_Seen', 'Peak_Time', 'Status'],
                'RSS_Feeds': ['Feed_ID', 'Feed_URL', 'Name', 'Category', 'Last_Checked', 'Items_Count', 'Active'],
                'Scraped_Data': ['Scrape_ID', 'Source', 'Timestamp', 'Data_Type', 'Content', 'Processed', 'Stored_Location']
            }
        },
        
        'Analytics_Performance': {
            'sheets': {
                'Daily_Stats': ['Date', 'Platform', 'Posts_Count', 'Engagement', 'New_Followers', 'Reach', 'Impressions'],
                'Emotions_History': ['Timestamp', 'Joy', 'Trust', 'Fear', 'Surprise', 'Sadness', 'Disgust', 'Anger', 'Anticipation', 'Curiosity', 'Confidence'],
                'Performance_Metrics': ['Date', 'Response_Time', 'Uptime_Percent', 'API_Calls', 'Errors', 'Success_Rate', 'Cost'],
                'User_Analytics': ['Date', 'Active_Users', 'New_Users', 'Returning_Users', 'Avg_Session_Time', 'Bounce_Rate'],
                'Content_Performance': ['Content_ID', 'Type', 'Engagement_Rate', 'Viral_Score', 'Best_Time', 'Audience_Segment']
            }
        },
        
        'Tasks_Automation': {
            'sheets': {
                'Active_Tasks': ['Task_ID', 'Type', 'Description', 'Priority', 'Status', 'Assigned_Agent', 'Created', 'Deadline'],
                'Completed_Tasks': ['Task_ID', 'Type', 'Description', 'Completed_At', 'Result', 'Duration', 'Agent_Used'],
                'Recurring_Tasks': ['Task_ID', 'Type', 'Schedule', 'Frequency', 'Last_Run', 'Next_Run', 'Active', 'Configuration'],
                'Failed_Tasks': ['Task_ID', 'Type', 'Failed_At', 'Error_Message', 'Retry_Count', 'Status', 'Notes'],
                'Workflows': ['Workflow_ID', 'Name', 'Steps', 'Trigger', 'Condition', 'Active', 'Success_Rate']
            }
        },
        
        'Cloud_Storage': {
            'sheets': {
                'Files_Index': ['File_ID', 'File_Name', 'Storage_Location', 'Size', 'Type', 'Upload_Date', 'Last_Access', 'Tags'],
                'Backups': ['Backup_ID', 'Backup_Type', 'Timestamp', 'Size', 'Location', 'Status', 'Restore_Point'],
                'Cache_Data': ['Cache_Key', 'Data', 'Created_At', 'Expires_At', 'Hit_Count', 'Size'],
                'Temporary_Storage': ['Temp_ID', 'Data', 'Created_At', 'Expires_At', 'Purpose', 'Auto_Delete'],
                'Media_Storage': ['Media_ID', 'Type', 'URL', 'Telegram_File_ID', 'Size', 'Upload_Date', 'Description']
            }
        },
        
        'Security_Logs': {
            'sheets': {
                'Access_Logs': ['Log_ID', 'Timestamp', 'User_ID', 'Action', 'IP_Address', 'Status', 'Details'],
                'Error_Logs': ['Error_ID', 'Timestamp', 'Error_Type', 'Message', 'Stack_Trace', 'Severity', 'Resolved'],
                'Security_Events': ['Event_ID', 'Timestamp', 'Type', 'Severity', 'Description', 'Action_Taken', 'Status'],
                'API_Usage': ['Timestamp', 'API_Name', 'Endpoint', 'User', 'Response_Time', 'Status_Code', 'Cost'],
                'Suspicious_Activity': ['Activity_ID', 'Timestamp', 'User_ID', 'Type', 'Description', 'Risk_Level', 'Investigated'],
                'Admin_Actions': ['Action_ID', 'Timestamp', 'Admin_ID', 'Action', 'Target', 'Reason', 'Result']
            }
        }
    }
    
    def __init__(self, credentials_file: str):
        self.credentials_file = credentials_file
        self.client = None
        self.spreadsheets = {}
        
    async def initialize(self):
        """راه‌اندازی اولیه"""
        logger.info("🚀 Starting Auto Setup...")
        
        # اتصال به Google
        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
        creds = Credentials.from_service_account_file(
            self.credentials_file,
            scopes=scope
        )
        self.client = gspread.authorize(creds)
        
        logger.info(f"✅ Connected to Google Sheets")
        logger.info(f"📧 Service Account: {creds.service_account_email}")
        
        # ساخت یا بارگذاری تمام spreadsheets
        await self._setup_all_spreadsheets()
        
        logger.info("✅ Auto Setup Complete!")
        
        return self.spreadsheets
    
    async def _setup_all_spreadsheets(self):
        """ساخت یا بارگذاری تمام spreadsheet ها"""
        
        for spreadsheet_name, structure in self.SPREADSHEET_STRUCTURE.items():
            full_name = f"Nazanin_{spreadsheet_name}"
            
            logger.info(f"📊 Processing: {full_name}")
            
            # چک کردن وجود spreadsheet
            existing_ss = await self._find_spreadsheet(full_name)
            
            if existing_ss:
                logger.info(f"   ✅ Found existing spreadsheet")
                spreadsheet = existing_ss
            else:
                logger.info(f"   🔨 Creating new spreadsheet...")
                spreadsheet = self.client.create(full_name)
                logger.info(f"   ✅ Created: {spreadsheet.id}")
            
            # ذخیره ID
            self.spreadsheets[spreadsheet_name.lower()] = spreadsheet.id
            
            # ساخت sheets داخل spreadsheet
            await self._setup_sheets_in_spreadsheet(
                spreadsheet,
                structure['sheets'],
                structure.get('initial_data', {})
            )
            
            time.sleep(1)  # جلوگیری از rate limit
    
    async def _find_spreadsheet(self, name: str):
        """پیدا کردن spreadsheet با نام مشخص"""
        try:
            spreadsheets = self.client.openall()
            for ss in spreadsheets:
                if ss.title == name:
                    return ss
            return None
        except Exception as e:
            logger.debug(f"Error finding spreadsheet: {e}")
            return None
    
    async def _setup_sheets_in_spreadsheet(
        self,
        spreadsheet,
        sheets_structure: Dict,
        initial_data: Dict
    ):
        """ساخت sheets داخل یک spreadsheet"""
        
        # دریافت لیست sheets موجود
        existing_sheets = {ws.title: ws for ws in spreadsheet.worksheets()}
        
        # حذف Sheet1 پیش‌فرض اگه وجود داره
        if 'Sheet1' in existing_sheets and len(sheets_structure) > 0:
            try:
                first_sheet_name = list(sheets_structure.keys())[0]
                existing_sheets['Sheet1'].update_title(first_sheet_name)
                existing_sheets[first_sheet_name] = existing_sheets.pop('Sheet1')
                logger.info(f"      ♻️ Renamed Sheet1 to {first_sheet_name}")
            except:
                pass
        
        # ساخت یا به‌روزرسانی هر sheet
        for sheet_name, headers in sheets_structure.items():
            if sheet_name in existing_sheets:
                logger.info(f"      ✅ Sheet exists: {sheet_name}")
                worksheet = existing_sheets[sheet_name]
            else:
                logger.info(f"      🔨 Creating sheet: {sheet_name}")
                worksheet = spreadsheet.add_worksheet(
                    title=sheet_name,
                    rows=1000,
                    cols=len(headers)
                )
            
            # چک کردن و اضافه کردن headers
            try:
                current_headers = worksheet.row_values(1)
                if not current_headers or current_headers != headers:
                    worksheet.clear()
                    worksheet.append_row(headers)
                    logger.info(f"         📝 Added headers ({len(headers)} columns)")
                    
                    # اضافه کردن داده‌های اولیه
                    if sheet_name in initial_data:
                        for row in initial_data[sheet_name]:
                            worksheet.append_row(row)
                        logger.info(f"         📥 Added {len(initial_data[sheet_name])} initial rows")
            except Exception as e:
                logger.error(f"         ❌ Error setting up {sheet_name}: {e}")
            
            time.sleep(0.5)  # جلوگیری از rate limit
    
    def get_spreadsheet_ids(self) -> Dict[str, str]:
        """دریافت تمام spreadsheet IDs"""
        return self.spreadsheets
    
    def save_config(self, config_path: str = 'config/spreadsheet_ids.json'):
        """ذخیره IDs در فایل config"""
        import json
        
        config = {
            "google_sheets": {
                "credentials_file": "credentials.json",
                "spreadsheets": self.spreadsheets
            }
        }
        
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        
        logger.info(f"💾 Config saved to: {config_path}")


# استفاده نمونه
if __name__ == '__main__':
    import asyncio
    
    async def main():
        setup = SheetsAutoSetup('credentials.json')
        spreadsheet_ids = await setup.initialize()
        setup.save_config()
        
        print("\n✅ Setup Complete!")
        print("\n📋 Spreadsheet IDs:")
        for name, sid in spreadsheet_ids.items():
            print(f"   {name}: {sid}")
    
    asyncio.run(main())
