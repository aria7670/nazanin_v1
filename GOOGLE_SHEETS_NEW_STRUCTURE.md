# 📊 ساختار جدید Google Sheets - سازماندهی شده

ساختار کاملاً طبقه‌بندی شده با 10 شیت اصلی و زیرشیت‌ها

---

## 🎯 نگاه کلی

به جای 11 شیت جدا، حالا داریم:
- **10 Spreadsheet اصلی** (هر کدوم یه فایل Google Sheets جداگانه)
- هر Spreadsheet شامل **چندین Sheet** (زیرشیت)

**مزایا:**
✅ سازماندهی بهتر
✅ دسترسی آسان‌تر
✅ مدیریت راحت‌تر
✅ Backup آسان‌تر
✅ Performance بهتر

---

## 📁 ساختار کامل

### 1️⃣ **Bot_Configuration** (تنظیمات ربات)

**Spreadsheet ID**: `config_spreadsheet_id`

**Sheets داخلش:**

#### Sheet 1.1: Personality
```
ستون‌ها: Key | Value | Description | Last_Updated
```

#### Sheet 1.2: Rules
```
ستون‌ها: Rule_ID | Category | Rule | Priority | Active | Examples | Created_Date
```

#### Sheet 1.3: Prompts
```
ستون‌ها: Prompt_ID | Type | Template | Variables | Usage_Count
```

#### Sheet 1.4: Responses
```
ستون‌ها: Response_ID | Trigger | Response | Condition | Priority
```

#### Sheet 1.5: Settings
```
ستون‌ها: Setting_Key | Setting_Value | Type | Description
```

---

### 2️⃣ **AI_Data** (داده‌های هوش مصنوعی)

**Spreadsheet ID**: `ai_data_spreadsheet_id`

**Sheets داخلش:**

#### Sheet 2.1: API_Keys
```
ستون‌ها: Provider | API_Key | Status | Usage_Count | Daily_Limit | Last_Used | Cost | Notes
```

#### Sheet 2.2: Model_Performance
```
ستون‌ها: Model_Name | Provider | Avg_Response_Time | Success_Rate | Cost_Per_Call | Total_Calls
```

#### Sheet 2.3: AI_Responses
```
ستون‌ها: Timestamp | Model_Used | Input_Tokens | Output_Tokens | Cost | Quality_Score
```

#### Sheet 2.4: Training_Data
```
ستون‌ها: Data_ID | Input | Expected_Output | Actual_Output | Feedback | Used_For_Training
```

#### Sheet 2.5: Embeddings
```
ستون‌ها: Text_ID | Text | Embedding_Vector | Model | Created_Date
```

---

### 3️⃣ **Telegram_Data** (داده‌های تلگرام)

**Spreadsheet ID**: `telegram_data_spreadsheet_id`

**Sheets داخلش:**

#### Sheet 3.1: Messages_Log
```
ستون‌ها: Message_ID | Timestamp | Chat_ID | User_ID | Username | Message_Type | Content | Response | Response_Time
```

#### Sheet 3.2: Channels
```
ستون‌ها: Channel_ID | Channel_Name | Channel_Username | Type | Members_Count | Description | Joined_Date | Active
```

#### Sheet 3.3: Groups
```
ستون‌ها: Group_ID | Group_Name | Type | Members_Count | Admin_Rights | Joined_Date | Active | Purpose
```

#### Sheet 3.4: Files_Storage
```
ستون‌ها: File_ID | File_Name | File_Type | Size | Telegram_File_ID | Upload_Date | Description | Tags
```

#### Sheet 3.5: Media_Archive
```
ستون‌ها: Media_ID | Media_Type | Telegram_ID | Caption | Uploaded_By | Upload_Date | Download_Link
```

#### Sheet 3.6: Conversations
```
ستون‌ها: Conversation_ID | User_ID | Start_Time | End_Time | Message_Count | Topic | Summary | Sentiment
```

#### Sheet 3.7: Channel_Posts
```
ستون‌ها: Post_ID | Channel_ID | Timestamp | Content | Media | Views | Forwards | Reactions
```

#### Sheet 3.8: Saved_Messages
```
ستون‌ها: Message_ID | Timestamp | From_Chat | Content | Tags | Importance | Notes
```

---

### 4️⃣ **Users_Database** (پایگاه داده کاربران)

**Spreadsheet ID**: `users_database_spreadsheet_id`

**Sheets داخلش:**

#### Sheet 4.1: User_Profiles
```
ستون‌ها: User_ID | Username | First_Name | Last_Name | Phone | Join_Date | Last_Seen | Status | VIP
```

#### Sheet 4.2: User_Behavior
```
ستون‌ها: User_ID | Total_Messages | Avg_Sentiment | Favorite_Topics | Active_Hours | Response_Rate | Engagement_Score
```

#### Sheet 4.3: User_Preferences
```
ستون‌ها: User_ID | Language | Preferred_Length | Tone_Preference | Notification_Settings | Tags
```

#### Sheet 4.4: User_Interactions
```
ستون‌ها: Interaction_ID | User_ID | Timestamp | Type | Content | Platform | Outcome
```

#### Sheet 4.5: VIP_Users
```
ستون‌ها: User_ID | VIP_Level | Benefits | Joined_VIP | Subscription_Status | Notes
```

#### Sheet 4.6: Blocked_Users
```
ستون‌ها: User_ID | Block_Date | Reason | Blocked_By | Unblock_Date | Notes
```

---

### 5️⃣ **Content_Management** (مدیریت محتوا)

**Spreadsheet ID**: `content_management_spreadsheet_id`

**Sheets داخلش:**

#### Sheet 5.1: Tweet_Log
```
ستون‌ها: Tweet_ID | Timestamp | Content | Type | Category | Engagement | Impressions | AI_Used | Status
```

#### Sheet 5.2: Content_Ideas
```
ستون‌ها: Idea_ID | Topic | Type | Priority | Status | Scheduled_For | Created_Date | Notes
```

#### Sheet 5.3: Templates
```
ستون‌ها: Template_ID | Name | Content | Variables | Category | Usage_Count | Success_Rate
```

#### Sheet 5.4: Scheduled_Posts
```
ستون‌ها: Post_ID | Platform | Content | Media | Scheduled_Time | Status | Created_By
```

#### Sheet 5.5: Content_Archive
```
ستون‌ها: Archive_ID | Content | Platform | Published_Date | Performance | Tags | Archived_Date
```

#### Sheet 5.6: Hashtags
```
ستون‌ها: Hashtag | Usage_Count | Avg_Engagement | Category | Trending_Score | Last_Used
```

---

### 6️⃣ **News_Channels** (کانال‌های خبری)

**Spreadsheet ID**: `news_channels_spreadsheet_id`

**Sheets داخلش:**

#### Sheet 6.1: News_Sources
```
ستون‌ها: Source_ID | Source_Name | Type | Channel_ID | URL | Category | Language | Active | Reliability_Score
```

#### Sheet 6.2: Collected_News
```
ستون‌ها: News_ID | Source_ID | Timestamp | Title | Summary | Full_Text | Link | Category | Relevance_Score
```

#### Sheet 6.3: Trends
```
ستون‌ها: Trend_ID | Keyword | Category | Volume | Growth_Rate | First_Seen | Peak_Time | Status
```

#### Sheet 6.4: RSS_Feeds
```
ستون‌ها: Feed_ID | Feed_URL | Name | Category | Last_Checked | Items_Count | Active
```

#### Sheet 6.5: Scraped_Data
```
ستون‌ها: Scrape_ID | Source | Timestamp | Data_Type | Content | Processed | Stored_Location
```

---

### 7️⃣ **Analytics_Performance** (تحلیل و عملکرد)

**Spreadsheet ID**: `analytics_spreadsheet_id`

**Sheets داخلش:**

#### Sheet 7.1: Daily_Stats
```
ستون‌ها: Date | Platform | Posts_Count | Engagement | New_Followers | Reach | Impressions
```

#### Sheet 7.2: Emotions_History
```
ستون‌ها: Timestamp | Joy | Trust | Fear | Surprise | Sadness | Disgust | Anger | Anticipation | Curiosity | Confidence
```

#### Sheet 7.3: Performance_Metrics
```
ستون‌ها: Date | Response_Time | Uptime_Percent | API_Calls | Errors | Success_Rate | Cost
```

#### Sheet 7.4: User_Analytics
```
ستون‌ها: Date | Active_Users | New_Users | Returning_Users | Avg_Session_Time | Bounce_Rate
```

#### Sheet 7.5: Content_Performance
```
ستون‌ها: Content_ID | Type | Engagement_Rate | Viral_Score | Best_Time | Audience_Segment
```

---

### 8️⃣ **Tasks_Automation** (وظایف و اتوماسیون)

**Spreadsheet ID**: `tasks_spreadsheet_id`

**Sheets داخلش:**

#### Sheet 8.1: Active_Tasks
```
ستون‌ها: Task_ID | Type | Description | Priority | Status | Assigned_Agent | Created | Deadline
```

#### Sheet 8.2: Completed_Tasks
```
ستون‌ها: Task_ID | Type | Description | Completed_At | Result | Duration | Agent_Used
```

#### Sheet 8.3: Recurring_Tasks
```
ستون‌ها: Task_ID | Type | Schedule | Frequency | Last_Run | Next_Run | Active | Configuration
```

#### Sheet 8.4: Failed_Tasks
```
ستون‌ها: Task_ID | Type | Failed_At | Error_Message | Retry_Count | Status | Notes
```

#### Sheet 8.5: Workflows
```
ستون‌ها: Workflow_ID | Name | Steps | Trigger | Condition | Active | Success_Rate
```

---

### 9️⃣ **Cloud_Storage** (ذخیره‌سازی ابری)

**Spreadsheet ID**: `cloud_storage_spreadsheet_id`

**Sheets داخلش:**

#### Sheet 9.1: Files_Index
```
ستون‌ها: File_ID | File_Name | Storage_Location | Size | Type | Upload_Date | Last_Access | Tags
```

#### Sheet 9.2: Backups
```
ستون‌ها: Backup_ID | Backup_Type | Timestamp | Size | Location | Status | Restore_Point
```

#### Sheet 9.3: Cache_Data
```
ستون‌ها: Cache_Key | Data | Created_At | Expires_At | Hit_Count | Size
```

#### Sheet 9.4: Temporary_Storage
```
ستون‌ها: Temp_ID | Data | Created_At | Expires_At | Purpose | Auto_Delete
```

#### Sheet 9.5: Media_Storage
```
ستون‌ها: Media_ID | Type | URL | Telegram_File_ID | Size | Upload_Date | Description
```

---

### 🔟 **Security_Logs** (امنیت و لاگ‌ها)

**Spreadsheet ID**: `security_spreadsheet_id`

**Sheets داخلش:**

#### Sheet 10.1: Access_Logs
```
ستون‌ها: Log_ID | Timestamp | User_ID | Action | IP_Address | Status | Details
```

#### Sheet 10.2: Error_Logs
```
ستون‌ها: Error_ID | Timestamp | Error_Type | Message | Stack_Trace | Severity | Resolved
```

#### Sheet 10.3: Security_Events
```
ستون‌ها: Event_ID | Timestamp | Type | Severity | Description | Action_Taken | Status
```

#### Sheet 10.4: API_Usage
```
ستون‌ها: Timestamp | API_Name | Endpoint | User | Response_Time | Status_Code | Cost
```

#### Sheet 10.5: Suspicious_Activity
```
ستون‌ها: Activity_ID | Timestamp | User_ID | Type | Description | Risk_Level | Investigated
```

#### Sheet 10.6: Admin_Actions
```
ستون‌ها: Action_ID | Timestamp | Admin_ID | Action | Target | Reason | Result
```

---

## 🗂️ نحوه ساخت

### روش 1: دستی (توصیه می‌شه)

1. برای هر کدوم از 10 مورد بالا، یه Spreadsheet جدید بساز
2. اسم‌گذاری:
   - `Nazanin_Bot_Configuration`
   - `Nazanin_AI_Data`
   - `Nazanin_Telegram_Data`
   - `Nazanin_Users_Database`
   - `Nazanin_Content_Management`
   - `Nazanin_News_Channels`
   - `Nazanin_Analytics_Performance`
   - `Nazanin_Tasks_Automation`
   - `Nazanin_Cloud_Storage`
   - `Nazanin_Security_Logs`

3. در هر Spreadsheet، Sheet های مربوطه رو بساز

4. همه رو با Service Account share کن (Editor access)

5. Spreadsheet ID های همه رو کپی کن

### روش 2: با اسکریپت (سریع‌تر)

یه اسکریپت Python برات می‌نویسم که خودکار همه رو بسازه!

---

## 📝 Config جدید

```json
{
  "google_sheets": {
    "credentials_file": "credentials.json",
    "spreadsheets": {
      "bot_configuration": "SPREADSHEET_ID_1",
      "ai_data": "SPREADSHEET_ID_2",
      "telegram_data": "SPREADSHEET_ID_3",
      "users_database": "SPREADSHEET_ID_4",
      "content_management": "SPREADSHEET_ID_5",
      "news_channels": "SPREADSHEET_ID_6",
      "analytics_performance": "SPREADSHEET_ID_7",
      "tasks_automation": "SPREADSHEET_ID_8",
      "cloud_storage": "SPREADSHEET_ID_9",
      "security_logs": "SPREADSHEET_ID_10"
    }
  }
}
```

---

## ✅ مزایای ساختار جدید

1. **سازماندهی بهتر**: هر بخش جدا
2. **Performance بهتر**: شیت‌های کوچک‌تر
3. **Backup راحت‌تر**: هر بخش جداگانه
4. **دسترسی مدیریت‌شده**: می‌تونی برای هر بخش دسترسی جدا بدی
5. **Scale پذیری**: راحت می‌تونی گسترش بدی

---

**آماده برای پیاده‌سازی! 🚀**
