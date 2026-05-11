# ✨ Aether OS — Feature Plan

> Tracks what has been implemented, what is in progress, and what is planned.  
> Status key: ✅ Done | 🔄 In Progress | 📋 Planned

---

## Phase 1 — MVP (Core Foundation)

### 🧩 Infrastructure & Setup
- [x] ✅ Docker Compose base setup (`docker-compose.yml`)
- [x] ✅ Environment variable scaffolding (`.env.example`)
- [x] ✅ Repository directory structure (`agents/`, `core/`, `ui/`, `integrations/`, `data/`)
- [x] ✅ `requirements.txt` with all Python dependencies
- [x] ✅ FastAPI backend skeleton (`core/`)

### 🤖 Multi-LLM Gateway
- [ ] 🔄 LiteLLM integration (unified API for Claude, GPT, Grok, local models)
- [ ] 📋 LiteLLM master key auth & config
- [ ] 📋 Support for OpenAI, Anthropic, Groq providers
- [ ] 📋 Support for additional providers (Cohere, Mistral, etc.)

### 💬 Chat Interface
- [ ] 🔄 Open WebUI fork / integration (ChatGPT-like interface on port 8080)
- [ ] 📋 Custom widget layer on top of Open WebUI
- [ ] 📋 Streamlit/Gradio custom dashboard (port 8501)

### 🌅 Daily Intelligence Agent (`agents/daily_intelligence/`)
- [ ] 📋 Morning briefing: summarise calendar, tasks, weather, news
- [ ] 📋 Priority suggestions based on context
- [ ] 📋 End-of-day wrap-up & reflection prompt
- [ ] 📋 Scheduled trigger (cron / Watchtower)

### 🏃 Habit & Mood Tracker (`agents/habit_coach/`)
- [ ] 📋 Habit logging API (check-in endpoint)
- [ ] 📋 Mood logging (daily score + free text)
- [ ] 📋 AI insight engine ("you're 40% more productive on days you run")
- [ ] 📋 Dashboard widget for streaks & trends

### 🧠 Smart Second Brain (`agents/knowledge_agent/`)
- [ ] 📋 Markdown vault ingestion (Obsidian-compatible)
- [ ] 📋 Vector embeddings for notes & tasks (local or API-based)
- [ ] 📋 Chat-with-notes interface (RAG pipeline)
- [ ] 📋 Memory persistence across sessions

### 🖥️ Unified Dashboard (`ui/`)
- [ ] 📋 Beautiful self-hosted UI shell
- [ ] 📋 Widget system (habits, tasks, agent outputs)
- [ ] 📋 Dark/light theme
- [ ] 📋 Mobile-responsive layout

---

## Phase 2 — Expanding Capabilities

### 📧 Email & Calendar Agent (`integrations/`)
- [ ] 📋 Gmail / IMAP read & summarise
- [ ] 📋 Auto-reply drafts with AI
- [ ] 📋 Google / Apple Calendar read & scheduling
- [ ] 📋 Smart meeting prep briefings

### 💰 Finance & Expense Tracker
- [ ] 📋 Manual expense logging
- [ ] 📋 Bank/card import (CSV or open-banking API)
- [ ] 📋 AI budgeting advice & anomaly detection
- [ ] 📋 Monthly financial summary report

### 🏋️ Health & Fitness Integration
- [ ] 📋 Whoop API integration
- [ ] 📋 Oura Ring API integration
- [ ] 📋 Apple Health import (export XML parser)
- [ ] 📋 Health trend insights linked to habit/mood data

### 🎯 Project & Goal Management
- [ ] 📋 Goal definition & milestone tracking
- [ ] 📋 Automatic progress tracking from linked tasks
- [ ] 📋 Weekly/monthly review agent
- [ ] 📋 Notion sync (bidirectional)

### 🎙️ Voice Interface
- [ ] 📋 Local Whisper STT integration
- [ ] 📋 TTS output (Coqui / Piper / ElevenLabs)
- [ ] 📋 Voice-activated agent commands
- [ ] 📋 Wake-word detection (optional)

---

## Phase 3 — Polish & Scale

### 🔒 Privacy & Security
- [ ] 📋 All data stored locally by default
- [ ] 📋 Optional encrypted vault for secrets
- [ ] 📋 Auth layer for multi-user or remote access (OAuth / passkey)

### ⚙️ DevOps & Self-Hosting
- [ ] 📋 Watchtower auto-update pipeline
- [ ] 📋 One-command install script
- [ ] 📋 Backup & restore tooling for `data/` vault
- [ ] 📋 Helm chart / k8s manifest (power users)

### 📖 Documentation
- [ ] 📋 Agent development guide (how to write a new agent)
- [ ] 📋 Integration guide (adding new LLM providers)
- [ ] 📋 Self-hosting walkthrough (Raspberry Pi, VPS, NAS)
- [ ] 📋 API reference (FastAPI auto-docs)

---

## Backlog / Ideas
- [ ] 📋 iOS / Android companion app (PWA or native)
- [ ] 📋 Browser extension for one-click capture
- [ ] 📋 Telegram / Discord bot interface
- [ ] 📋 Multi-agent workflow designer (visual canvas)
- [ ] 📋 Marketplace for community agents

---

*Last updated: May 2026*
