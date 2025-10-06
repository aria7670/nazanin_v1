# Makefile for Nazanin AI Bot
# راهنمای دستورات مفید

.PHONY: help install test clean run docker lint format

# رنگ‌ها برای output
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[0;33m
RED := \033[0;31m
NC := \033[0m # No Color

help: ## نمایش این راهنما
	@echo "$(BLUE)Nazanin AI Bot - دستورات مفید$(NC)"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "$(GREEN)%-20s$(NC) %s\n", $$1, $$2}'

install: ## نصب dependencies
	@echo "$(BLUE)📦 Installing dependencies...$(NC)"
	pip install --upgrade pip
	pip install -r requirements.txt
	@echo "$(GREEN)✅ Installation complete!$(NC)"

install-dev: ## نصب dependencies برای توسعه
	@echo "$(BLUE)📦 Installing dev dependencies...$(NC)"
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install pytest pytest-asyncio black flake8 mypy isort
	@echo "$(GREEN)✅ Dev installation complete!$(NC)"

config: ## کپی کردن config نمونه
	@if [ ! -f config/config.json ]; then \
		cp config/config.example.json config/config.json; \
		echo "$(GREEN)✅ Config file created!$(NC)"; \
		echo "$(YELLOW)⚠️  Please edit config/config.json with your API keys$(NC)"; \
	else \
		echo "$(YELLOW)⚠️  config.json already exists$(NC)"; \
	fi

test: ## اجرای تست‌ها
	@echo "$(BLUE)🧪 Running tests...$(NC)"
	python tests/test_basic.py

test-imports: ## تست import ها
	@echo "$(BLUE)🧪 Testing imports...$(NC)"
	@python -c "from src.core import SheetsManager, APIManager; print('✅ Core imports OK')" && \
	python -c "from src.ai import BrainSimulation, QuantumAgent, NeuralAgent; print('✅ AI imports OK')" && \
	python -c "from src.agents import AgentOrchestrator; print('✅ Agents imports OK')" && \
	python -c "from src.utils import MessageClassifier; print('✅ Utils imports OK')"

lint: ## چک کردن کد با flake8
	@echo "$(BLUE)🔍 Linting code...$(NC)"
	flake8 src/ --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 src/ --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

format: ## فرمت کردن کد با black
	@echo "$(BLUE)✨ Formatting code...$(NC)"
	black src/ main.py main_advanced.py tests/
	isort src/ main.py main_advanced.py tests/
	@echo "$(GREEN)✅ Code formatted!$(NC)"

format-check: ## چک کردن فرمت بدون تغییر
	@echo "$(BLUE)🔍 Checking code format...$(NC)"
	black --check src/ main.py main_advanced.py tests/

clean: ## پاک کردن فایل‌های موقت
	@echo "$(BLUE)🧹 Cleaning temporary files...$(NC)"
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.log" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf build/ dist/ .pytest_cache/ .coverage htmlcov/
	@echo "$(GREEN)✅ Cleanup complete!$(NC)"

run: ## اجرای نسخه ساده
	@echo "$(BLUE)🚀 Starting Nazanin (simple version)...$(NC)"
	python main.py

run-advanced: ## اجرای نسخه پیشرفته
	@echo "$(BLUE)🚀 Starting Nazanin Advanced...$(NC)"
	python main_advanced.py

demo: ## اجرای demo
	@echo "$(BLUE)🎮 Running demo...$(NC)"
	python tests/demo_advanced.py

docker-build: ## ساخت Docker image
	@echo "$(BLUE)🐳 Building Docker image...$(NC)"
	docker build -t nazanin-ai-bot .
	@echo "$(GREEN)✅ Docker image built!$(NC)"

docker-run: ## اجرا با Docker
	@echo "$(BLUE)🐳 Starting Docker container...$(NC)"
	docker-compose up -d
	@echo "$(GREEN)✅ Docker container started!$(NC)"
	@echo "$(YELLOW)📋 View logs: make docker-logs$(NC)"

docker-stop: ## متوقف کردن Docker container
	@echo "$(BLUE)🐳 Stopping Docker container...$(NC)"
	docker-compose down
	@echo "$(GREEN)✅ Docker container stopped!$(NC)"

docker-logs: ## نمایش Docker logs
	docker-compose logs -f

docker-restart: ## ریستارت Docker container
	docker-compose restart

venv: ## ساخت virtual environment
	@echo "$(BLUE)📦 Creating virtual environment...$(NC)"
	python3 -m venv venv
	@echo "$(GREEN)✅ Virtual environment created!$(NC)"
	@echo "$(YELLOW)⚡ Activate with: source venv/bin/activate$(NC)"

setup: venv config install ## راه‌اندازی اولیه کامل
	@echo "$(GREEN)✅ Setup complete!$(NC)"
	@echo "$(YELLOW)Next steps:$(NC)"
	@echo "  1. Edit config/config.json"
	@echo "  2. Run: make run-advanced"

check: lint test-imports ## چک کردن کامل پروژه
	@echo "$(GREEN)✅ All checks passed!$(NC)"

git-status: ## نمایش وضعیت git
	@git status --short

git-push: ## push به GitHub
	@echo "$(BLUE)📤 Pushing to GitHub...$(NC)"
	git add -A
	@read -p "Commit message: " msg; \
	git commit -m "$$msg"
	git push origin main
	@echo "$(GREEN)✅ Pushed to GitHub!$(NC)"

docs: ## ساخت مستندات
	@echo "$(BLUE)📚 Building documentation...$(NC)"
	@echo "$(YELLOW)Documentation files are in docs/$(NC)"
	@ls -1 docs/*.md

tree: ## نمایش ساختار پروژه
	@echo "$(BLUE)📁 Project structure:$(NC)"
	@tree -I 'venv|__pycache__|*.pyc|.git' -L 3

stats: ## نمایش آمار پروژه
	@echo "$(BLUE)📊 Project Statistics:$(NC)"
	@echo "$(GREEN)Python files:$(NC) $$(find src -name '*.py' | wc -l)"
	@echo "$(GREEN)Lines of code:$(NC) $$(find src -name '*.py' -exec wc -l {} + | tail -1 | awk '{print $$1}')"
	@echo "$(GREEN)Documentation files:$(NC) $$(find docs -name '*.md' | wc -l)"
	@echo "$(GREEN)Total files:$(NC) $$(find . -type f ! -path './venv/*' ! -path './.git/*' ! -name '*.pyc' | wc -l)"

all: clean install config test ## انجام همه کارها

.DEFAULT_GOAL := help
