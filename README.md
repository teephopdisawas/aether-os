# ✨ Life OS

**Your Personal AI-Powered Life Operating System**  
*One clean interface to rule your entire existence.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Status](https://img.shields.io/badge/status-alpha-orange)
![Made with ❤️](https://img.shields.io/badge/made%20with-love-red)

---

## 🚀 What is Life OS?

Life OS is a **self-hosted, AI-first operating system for your life**.

Think of it as the ultimate personal productivity layer — but actually intelligent.

It combines:
- Multiple AI agents that actually *do* things for you
- A beautiful unified dashboard
- Your second brain (knowledge + tasks + habits)
- Smart automations that run 24/7

**Goal**: Turn your chaotic life into a smooth, well-oiled machine powered by AI.

---

## ✨ Core Features (Current + Planned)

### Phase 1 (MVP)
- **Daily Intelligence Agent** — wakes up with you, summarises your day, suggests priorities
- **Habit & Mood Tracker** with AI insights ("you’re 40% more productive on days you run")
- **Smart Second Brain** — chat with all your notes, tasks, and memories
- **Unified Dashboard** — beautiful self-hosted UI (Open WebUI + custom widgets)
- **Multi-LLM Support** via LiteLLM (Claude, GPT, Grok, local models, etc.)

### Phase 2 (Coming soon)
- Email + Calendar agent (read, summarise, auto-reply, schedule)
- Finance & expense tracker with AI budgeting
- Health & fitness integration (Whoop, Oura, Apple Health)
- Project & goal management with automatic progress tracking
- Voice interface (local Whisper + TTS)

---

## 🛠 Tech Stack

| Layer          | Tool                          | Why |
|----------------|-------------------------------|-----|
| **AI Gateway** | LiteLLM                       | One API to rule all LLMs |
| **Chat UI**    | Open WebUI (forked)           | Beautiful ChatGPT-like interface |
| **Backend**    | FastAPI + Python              | Fast, modern, async |
| **Database**   | SQLite (local dev) / Managed Postgres (Vercel prod) | Serverless-safe persistence |
| **Deployment** | Vercel | Fast serverless deployment |
| **Frontend**   | Streamlit / Gradio (planned)  | Quick beautiful dashboards |
| **Knowledge**  | Obsidian / Markdown vault     | Future-proof second brain |
| **Agents**     | Custom LangChain / CrewAI     | Multi-agent workflows |

---

## 📁 Repository Structure

```
life-os/
├── agents/                 # Individual AI agents
│   ├── daily_intelligence/
│   ├── habit_coach/
│   └── knowledge_agent/
├── core/                   # Main OS logic & orchestration
├── integrations/           # Notion, Gmail, Calendar, etc.
├── ui/                     # Custom dashboards & widgets
├── data/                   # Local databases & vaults
├── vercel.json
├── .env.example
├── README.md
└── requirements.txt
```

---

## ⚡ Quick Start (Local + Vercel)

```bash
# 1. Clone the repo
git clone https://github.com/tdisawas0github/aether-os.git
cd aether-os

# 2. Copy environment
cp .env.example .env
# Edit .env with your API keys (OpenAI, Anthropic, etc.)

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the API locally
uvicorn core.main:app --reload

# 5. Open the magic (while the uvicorn process is running)
# → Core API health: http://localhost:8000/health
# → API docs: http://localhost:8000/docs
```

To deploy on Vercel:

```bash
vercel
```

**That’s it.** Your personal life OS API is now running locally and ready for Vercel.

## 🔄 Migration from Docker Compose

- The default deployment target is now Vercel for the FastAPI core API.
- Open WebUI and LiteLLM are no longer shipped as default Compose services in this repo.
- If you keep using Open WebUI/LiteLLM, host them separately and point them to your deployed API (for example: set Open WebUI `LITELLM_PROXY_URL` and LiteLLM upstream/base URL values to your Vercel endpoint).
- If you are migrating existing Docker data, back up your old volumes first (`open-webui:/app/backend/data` and local `./data` SQLite files) before switching deployment.

### Production database on Vercel

- Do not rely on local SQLite files in production serverless environments.
- Use a managed Postgres instance and set `DATABASE_URL` in Vercel project environment variables.
- Keep SQLite only for local development runs.

---

## 🔑 Environment Variables (example)

```env
# === Life OS Environment Variables ===
# Copy this file to .env and fill in your keys

# AI Provider Keys (add the ones you use)
OPENAI_API_KEY=sk-your-openai-key-here
ANTHROPIC_API_KEY=sk-ant-your-anthropic-key-here
GROQ_API_KEY=gsk_your-groq-key-here

# LiteLLM Settings
LITELLM_MASTER_KEY=sk-1234-super-secret-change-me

# Optional: Add more providers later
# COHERE_API_KEY=...
# MISTRAL_API_KEY=...
```

---

## 🧠 Philosophy

- **Privacy first** — everything runs on *your* hardware
- **AI that actually helps** — not just chat, but agents that *act*
- **Simple > Complex** — beautiful defaults, power users can go deep
- **Future-proof** — markdown + local files everywhere

---

## 🤝 Contributing

This is very early stage (alpha). PRs, ideas, and agent contributions are super welcome!

Just open an issue with the tag `agent-idea` or `feature-request`.

---

## 📜 License

MIT — do whatever you want, just don’t be evil.

---

**Built with ❤️ by thomelab-codes + friends**  
*Making life actually manageable since 2026*

---

> “The best operating system for your life is the one that disappears into the background and just *works*."

---

**Star this repo if you want to see it become the ultimate life OS** ⭐

---

*Last updated: May 2026*
