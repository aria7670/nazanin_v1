"""
Basic Tests - تست‌های پایه
تست‌های اولیه برای ربات
"""

import pytest
import asyncio
from nazanin_bot import NazaninBot
from nazanin_bot.config import Settings


@pytest.fixture
def bot():
    """ایجاد نمونه ربات برای تست"""
    settings = Settings(log_level="ERROR")  # کاهش لاگ در تست‌ها
    return NazaninBot(settings=settings)


@pytest.mark.asyncio
async def test_bot_initialization(bot):
    """تست مقداردهی اولیه"""
    assert bot is not None
    assert bot.settings.bot_name == "Nazanin"
    assert not bot.is_running
    assert not bot.is_sleeping


@pytest.mark.asyncio
async def test_bot_awaken(bot):
    """تست بیداری ربات"""
    await bot.awaken()
    
    assert bot.is_running
    assert bot.cognitive_core.is_active
    assert bot.consciousness.is_conscious
    
    await bot.shutdown()


@pytest.mark.asyncio
async def test_process_input(bot):
    """تست پردازش ورودی"""
    await bot.awaken()
    
    response = await bot.process_input("Hello!", user_id="test_user")
    
    assert response is not None
    assert isinstance(response, str)
    assert len(response) > 0
    
    await bot.shutdown()


@pytest.mark.asyncio
async def test_memory_storage(bot):
    """تست ذخیره در حافظه"""
    await bot.awaken()
    
    # ذخیره در STM
    success = bot.short_term_memory.store(
        item_id="test_item",
        content="test content",
        importance=0.8
    )
    
    assert success
    
    # بازیابی
    content = bot.short_term_memory.recall("test_item")
    assert content == "test content"
    
    await bot.shutdown()


@pytest.mark.asyncio
async def test_goal_management(bot):
    """تست مدیریت اهداف"""
    from nazanin_bot.decision.goal_manager import GoalPriority
    
    goal = bot.goal_manager.add_goal(
        goal_id="test_goal",
        description="Test goal",
        priority=GoalPriority.HIGH
    )
    
    assert goal is not None
    assert goal.goal_id == "test_goal"
    assert goal.priority == GoalPriority.HIGH


@pytest.mark.asyncio
async def test_emotional_response(bot):
    """تست پاسخ عاطفی"""
    await bot.awaken()
    
    # تشخیص احساس
    emotions = bot.emotion_detector.detect_from_text("I'm so happy!")
    
    assert emotions is not None
    assert 'emotions' in emotions
    
    await bot.shutdown()


@pytest.mark.asyncio
async def test_learning(bot):
    """تست یادگیری"""
    lessons = bot.adaptive_learning.learn_from_experience(
        context={'type': 'test'},
        action='test_action',
        outcome={'success': True},
        success=True,
        reward=0.8
    )
    
    assert lessons is not None
    assert len(lessons) > 0


@pytest.mark.asyncio
async def test_status_report(bot):
    """تست گزارش وضعیت"""
    await bot.awaken()
    
    status = bot.get_status()
    
    assert status is not None
    assert 'name' in status
    assert 'cognitive_state' in status
    assert 'emotional_state' in status
    assert 'memory' in status
    
    await bot.shutdown()


def test_personality():
    """تست شخصیت"""
    bot = NazaninBot()
    
    personality = bot.personality.get_profile()
    
    assert personality is not None
    assert 'name' in personality
    assert 'traits' in personality
    assert 'summary' in personality


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
