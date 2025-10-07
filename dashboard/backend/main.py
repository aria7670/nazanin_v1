"""
Nazanin Dashboard - FastAPI Backend
نازنین - بک‌اند داشبورد

یک API کامل برای مدیریت تمام جنبه‌های نازنین
"""

from fastapi import FastAPI, WebSocket, HTTPException, Depends, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
import asyncio
import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
import logging

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from nazanin.app_v5_complete import NazaninV5Complete
from nazanin.sheets_system import get_summary as get_sheets_summary

# ═══════════════════════════════════════════════════════════
# LOGGING
# ═══════════════════════════════════════════════════════════

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ═══════════════════════════════════════════════════════════
# APP INITIALIZATION
# ═══════════════════════════════════════════════════════════

app = FastAPI(
    title="Nazanin Dashboard API",
    description="Complete Dashboard API for Nazanin AI System",
    version="5.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Templates
templates = Jinja2Templates(directory="dashboard/frontend/templates")

# Static files
app.mount("/static", StaticFiles(directory="dashboard/frontend/static"), name="static")

# Security
security = HTTPBearer()

# Global Nazanin instance
nazanin: Optional[NazaninV5Complete] = None

# Active WebSocket connections
active_connections: List[WebSocket] = []

# ═══════════════════════════════════════════════════════════
# MODELS
# ═══════════════════════════════════════════════════════════

class LoginRequest(BaseModel):
    username: str
    password: str

class ConfigUpdate(BaseModel):
    section: str
    key: str
    value: Any

class APIKeyUpdate(BaseModel):
    provider: str
    keys: List[str]

class PersonalityUpdate(BaseModel):
    trait: str
    value: float

class ContentRequest(BaseModel):
    type: str  # "idea", "script", "title", etc.
    topic: str
    platform: str = "youtube"
    details: Optional[Dict] = {}

class TelegramMessage(BaseModel):
    chat_id: int
    message: str

class SheetOperation(BaseModel):
    spreadsheet: str
    sheet: str
    operation: str  # "get", "append", "update"
    data: Optional[Dict] = {}

class TaskCreate(BaseModel):
    title: str
    description: str
    priority: str = "medium"
    deadline: Optional[str] = None

# ═══════════════════════════════════════════════════════════
# AUTHENTICATION
# ═══════════════════════════════════════════════════════════

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Verify JWT token"""
    token = credentials.credentials
    # Simple token verification (در پروژه واقعی از JWT استفاده کنید)
    if token != "nazanin-dashboard-token-2024":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )
    return token

# ═══════════════════════════════════════════════════════════
# WEBSOCKET
# ═══════════════════════════════════════════════════════════

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket for real-time updates"""
    await websocket.accept()
    active_connections.append(websocket)
    
    try:
        while True:
            # Keep connection alive
            await asyncio.sleep(1)
            
            # Send updates
            if nazanin and nazanin.initialization_complete:
                stats = {
                    "timestamp": datetime.now().isoformat(),
                    "organism_age": nazanin.organism.age if nazanin.organism else 0,
                    "energy": nazanin.organism.get_vital_signs()['energy'] if nazanin.organism else 0,
                    "active": nazanin.is_running
                }
                await websocket.send_json(stats)
                
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
    finally:
        active_connections.remove(websocket)

async def broadcast_update(message: dict):
    """Broadcast update to all connected clients"""
    for connection in active_connections:
        try:
            await connection.send_json(message)
        except:
            pass

# ═══════════════════════════════════════════════════════════
# HTML PAGES
# ═══════════════════════════════════════════════════════════

@app.get("/", response_class=HTMLResponse)
async def dashboard_home(request: Request):
    """Main dashboard page"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/sheets", response_class=HTMLResponse)
async def sheets_page(request: Request):
    """Google Sheets management page"""
    return templates.TemplateResponse("sheets.html", {"request": request})

@app.get("/config", response_class=HTMLResponse)
async def config_page(request: Request):
    """Configuration page"""
    return templates.TemplateResponse("config.html", {"request": request})

@app.get("/telegram", response_class=HTMLResponse)
async def telegram_page(request: Request):
    """Telegram management page"""
    return templates.TemplateResponse("telegram.html", {"request": request})

@app.get("/content", response_class=HTMLResponse)
async def content_page(request: Request):
    """Content management page"""
    return templates.TemplateResponse("content.html", {"request": request})

@app.get("/analytics", response_class=HTMLResponse)
async def analytics_page(request: Request):
    """Analytics page"""
    return templates.TemplateResponse("analytics.html", {"request": request})

@app.get("/personality", response_class=HTMLResponse)
async def personality_page(request: Request):
    """Personality & Behavior page"""
    return templates.TemplateResponse("personality.html", {"request": request})

@app.get("/tasks", response_class=HTMLResponse)
async def tasks_page(request: Request):
    """Tasks & Automation page"""
    return templates.TemplateResponse("tasks.html", {"request": request})

@app.get("/logs", response_class=HTMLResponse)
async def logs_page(request: Request):
    """Logs & Security page"""
    return templates.TemplateResponse("logs.html", {"request": request})

@app.get("/youtube", response_class=HTMLResponse)
async def youtube_page(request: Request):
    """YouTube management page"""
    return templates.TemplateResponse("youtube.html", {"request": request})

# ═══════════════════════════════════════════════════════════
# API ENDPOINTS - SYSTEM
# ═══════════════════════════════════════════════════════════

@app.post("/api/auth/login")
async def login(request: LoginRequest):
    """Login endpoint"""
    # Simple authentication (در پروژه واقعی باید بهتر باشه)
    if request.username == "admin" and request.password == "nazanin2024":
        return {
            "success": True,
            "token": "nazanin-dashboard-token-2024",
            "user": {
                "username": "admin",
                "role": "admin"
            }
        }
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/api/status")
async def get_status(token: str = Depends(verify_token)):
    """Get system status"""
    global nazanin
    
    if not nazanin:
        return {
            "initialized": False,
            "running": False,
            "message": "Nazanin not initialized"
        }
    
    return {
        "initialized": nazanin.initialization_complete,
        "running": nazanin.is_running,
        "version": nazanin.version,
        "sheets_enabled": nazanin.sheets_initialized,
        "uptime": nazanin.organism.age if nazanin.organism else 0
    }

@app.post("/api/system/initialize")
async def initialize_system(token: str = Depends(verify_token)):
    """Initialize Nazanin"""
    global nazanin
    
    try:
        if not nazanin:
            nazanin = NazaninV5Complete()
        
        await nazanin.initialize(auto_init_sheets=False)
        
        await broadcast_update({
            "type": "system_initialized",
            "timestamp": datetime.now().isoformat()
        })
        
        return {
            "success": True,
            "message": "Nazanin initialized successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/system/start")
async def start_system(token: str = Depends(verify_token)):
    """Start Nazanin"""
    global nazanin
    
    if not nazanin or not nazanin.initialization_complete:
        raise HTTPException(status_code=400, detail="System not initialized")
    
    # Start in background
    asyncio.create_task(nazanin.run())
    
    return {"success": True, "message": "Nazanin started"}

@app.post("/api/system/stop")
async def stop_system(token: str = Depends(verify_token)):
    """Stop Nazanin"""
    global nazanin
    
    if nazanin:
        await nazanin.shutdown()
    
    return {"success": True, "message": "Nazanin stopped"}

@app.get("/api/stats")
async def get_stats(token: str = Depends(verify_token)):
    """Get complete stats"""
    global nazanin
    
    if not nazanin:
        raise HTTPException(status_code=400, detail="System not initialized")
    
    return nazanin.get_full_stats()

# ═══════════════════════════════════════════════════════════
# API ENDPOINTS - GOOGLE SHEETS
# ═══════════════════════════════════════════════════════════

@app.get("/api/sheets/summary")
async def sheets_summary(token: str = Depends(verify_token)):
    """Get Google Sheets structure summary"""
    return get_sheets_summary()

@app.get("/api/sheets/list")
async def list_spreadsheets(token: str = Depends(verify_token)):
    """List all spreadsheets"""
    global nazanin
    
    if not nazanin or not nazanin.sheets_manager:
        raise HTTPException(status_code=400, detail="Sheets not initialized")
    
    # بازگرداندن لیست spreadsheet ها
    return {
        "spreadsheets": list(nazanin.sheets_manager.spreadsheets.keys())
    }

@app.post("/api/sheets/get")
async def get_sheet_data(operation: SheetOperation, token: str = Depends(verify_token)):
    """Get data from a sheet"""
    global nazanin
    
    if not nazanin or not nazanin.sheets_manager:
        raise HTTPException(status_code=400, detail="Sheets not initialized")
    
    try:
        data = await nazanin.sheets_manager.get_sheet_data(
            operation.spreadsheet,
            operation.sheet
        )
        return {"success": True, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/sheets/append")
async def append_sheet_row(operation: SheetOperation, token: str = Depends(verify_token)):
    """Append row to sheet"""
    global nazanin
    
    if not nazanin or not nazanin.sheets_manager:
        raise HTTPException(status_code=400, detail="Sheets not initialized")
    
    try:
        await nazanin.sheets_manager.append_row(
            operation.spreadsheet,
            operation.sheet,
            operation.data.get('row', [])
        )
        
        await broadcast_update({
            "type": "sheet_updated",
            "spreadsheet": operation.spreadsheet,
            "sheet": operation.sheet
        })
        
        return {"success": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ═══════════════════════════════════════════════════════════
# API ENDPOINTS - CONFIGURATION
# ═══════════════════════════════════════════════════════════

@app.get("/api/config")
async def get_config(token: str = Depends(verify_token)):
    """Get current configuration"""
    global nazanin
    
    if not nazanin:
        # Load from file
        try:
            with open('config/config.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    
    return nazanin.config

@app.post("/api/config/update")
async def update_config(update: ConfigUpdate, token: str = Depends(verify_token)):
    """Update configuration"""
    global nazanin
    
    try:
        # Load config
        with open('config/config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # Update
        if update.section not in config:
            config[update.section] = {}
        config[update.section][update.key] = update.value
        
        # Save
        with open('config/config.json', 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        
        # Reload Nazanin config
        if nazanin:
            nazanin.config = config
        
        await broadcast_update({
            "type": "config_updated",
            "section": update.section,
            "key": update.key
        })
        
        return {"success": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/config/api-keys")
async def update_api_keys(update: APIKeyUpdate, token: str = Depends(verify_token)):
    """Update API keys"""
    try:
        with open('config/config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        if 'ai_apis' not in config:
            config['ai_apis'] = {}
        
        if update.provider not in config['ai_apis']:
            config['ai_apis'][update.provider] = {}
        
        config['ai_apis'][update.provider]['keys'] = update.keys
        
        with open('config/config.json', 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        
        # Reload API manager
        if nazanin and nazanin.api_manager:
            await nazanin.api_manager.reload_keys_from_sheets()
        
        return {"success": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ═══════════════════════════════════════════════════════════
# API ENDPOINTS - CONTENT GENERATION
# ═══════════════════════════════════════════════════════════

@app.post("/api/content/generate")
async def generate_content(request: ContentRequest, token: str = Depends(verify_token)):
    """Generate content"""
    global nazanin
    
    if not nazanin:
        raise HTTPException(status_code=400, detail="System not initialized")
    
    prompt = f"Generate {request.type} for {request.platform} about: {request.topic}"
    
    result = await nazanin.process_complete(
        prompt,
        context={'platform': request.platform, 'type': request.type}
    )
    
    return {
        "success": True,
        "content": result['response'],
        "processing_time": result['processing_time']
    }

@app.get("/api/content/ideas")
async def get_content_ideas(platform: str = "youtube", count: int = 10, token: str = Depends(verify_token)):
    """Get content ideas"""
    global nazanin
    
    if not nazanin:
        raise HTTPException(status_code=400, detail="System not initialized")
    
    prompt = f"Give me {count} content ideas for {platform}"
    
    result = await nazanin.process_complete(prompt, context={'platform': platform})
    
    return {
        "success": True,
        "ideas": result['response']
    }

# ═══════════════════════════════════════════════════════════
# API ENDPOINTS - TELEGRAM
# ═══════════════════════════════════════════════════════════

@app.post("/api/telegram/send")
async def send_telegram_message(message: TelegramMessage, token: str = Depends(verify_token)):
    """Send Telegram message"""
    global nazanin
    
    if not nazanin or not hasattr(nazanin, 'telegram_system'):
        raise HTTPException(status_code=400, detail="Telegram not initialized")
    
    # Send message (این بستگی به implementation داره)
    # await nazanin.telegram_system.send_message(message.chat_id, message.message)
    
    return {"success": True}

@app.get("/api/telegram/channels")
async def get_telegram_channels(token: str = Depends(verify_token)):
    """Get Telegram channels"""
    global nazanin
    
    if not nazanin or not nazanin.sheets_manager:
        return {"channels": []}
    
    channels = await nazanin.sheets_manager.get_telegram_channels()
    return {"channels": channels}

# ═══════════════════════════════════════════════════════════
# API ENDPOINTS - PERSONALITY
# ═══════════════════════════════════════════════════════════

@app.get("/api/personality")
async def get_personality(token: str = Depends(verify_token)):
    """Get current personality"""
    global nazanin
    
    if not nazanin or not nazanin.persona:
        return {}
    
    return nazanin.persona.get_current_state()

@app.post("/api/personality/update")
async def update_personality(update: PersonalityUpdate, token: str = Depends(verify_token)):
    """Update personality trait"""
    global nazanin
    
    if not nazanin or not nazanin.persona:
        raise HTTPException(status_code=400, detail="Persona not initialized")
    
    # Update trait
    if hasattr(nazanin.persona, 'personality_traits'):
        nazanin.persona.personality_traits[update.trait] = update.value
    
    return {"success": True}

# ═══════════════════════════════════════════════════════════
# API ENDPOINTS - ANALYTICS
# ═══════════════════════════════════════════════════════════

@app.get("/api/analytics/overview")
async def analytics_overview(token: str = Depends(verify_token)):
    """Get analytics overview"""
    global nazanin
    
    if not nazanin or not nazanin.sheets_modules:
        return {
            "total_messages": 0,
            "total_users": 0,
            "total_responses": 0,
            "avg_satisfaction": 0
        }
    
    # Get from analytics module
    summary = await nazanin.sheets_modules.analytics.get_stats_summary(days=30)
    
    return summary

@app.get("/api/analytics/performance")
async def analytics_performance(days: int = 7, token: str = Depends(verify_token)):
    """Get performance analytics"""
    # Mock data for now
    return {
        "daily_stats": [
            {"date": "2024-01-01", "messages": 150, "users": 45, "satisfaction": 0.92},
            {"date": "2024-01-02", "messages": 180, "users": 52, "satisfaction": 0.94},
            # ... more data
        ]
    }

# ═══════════════════════════════════════════════════════════
# API ENDPOINTS - TASKS
# ═══════════════════════════════════════════════════════════

@app.get("/api/tasks")
async def get_tasks(token: str = Depends(verify_token)):
    """Get all tasks"""
    global nazanin
    
    if not nazanin or not nazanin.sheets_manager:
        return {"tasks": []}
    
    # Get from sheets
    tasks = await nazanin.sheets_manager.get_sheet_data("TASK_MANAGEMENT", "Tasks")
    
    return {"tasks": tasks}

@app.post("/api/tasks/create")
async def create_task(task: TaskCreate, token: str = Depends(verify_token)):
    """Create new task"""
    global nazanin
    
    if not nazanin or not nazanin.sheets_manager:
        raise HTTPException(status_code=400, detail="System not initialized")
    
    # Add to sheets
    await nazanin.sheets_manager.append_row(
        "TASK_MANAGEMENT",
        "Tasks",
        [
            datetime.now().isoformat(),
            task.title,
            task.description,
            task.priority,
            "pending",
            task.deadline or ""
        ]
    )
    
    return {"success": True}

# ═══════════════════════════════════════════════════════════
# API ENDPOINTS - LOGS
# ═══════════════════════════════════════════════════════════

@app.get("/api/logs")
async def get_logs(limit: int = 100, token: str = Depends(verify_token)):
    """Get system logs"""
    try:
        with open('nazanin_v5.log', 'r', encoding='utf-8') as f:
            lines = f.readlines()[-limit:]
        return {"logs": lines}
    except:
        return {"logs": []}

@app.get("/api/security/logs")
async def get_security_logs(token: str = Depends(verify_token)):
    """Get security logs"""
    global nazanin
    
    if not nazanin or not nazanin.sheets_manager:
        return {"logs": []}
    
    logs = await nazanin.sheets_manager.get_sheet_data("SECURITY_LOGS", "Access_Logs")
    
    return {"logs": logs}

# ═══════════════════════════════════════════════════════════
# STARTUP
# ═══════════════════════════════════════════════════════════

@app.on_event("startup")
async def startup_event():
    """Initialize on startup"""
    logger.info("🚀 Nazanin Dashboard starting...")
    logger.info("📊 Dashboard available at: http://localhost:8000")
    logger.info("📚 API docs at: http://localhost:8000/api/docs")

@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    global nazanin
    if nazanin:
        await nazanin.shutdown()
    logger.info("👋 Dashboard stopped")

# ═══════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
