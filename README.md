# Aether OS

Aether OS is being rebuilt as a **custom web application**.

This repository now focuses on a single product direction:
- Custom frontend web app (not Open WebUI, Streamlit, or Gradio)
- FastAPI backend API
- One cohesive UX and architecture built specifically for Aether OS

---

## Current Status

The project is in early foundation stage.

Implemented today:
- FastAPI app scaffold in `/core/main.py`
- Health endpoint: `GET /health`
- Vercel runtime entrypoint in `/api/index.py`
- Vercel rewrite configuration in `/vercel.json`

---

## Project Direction

Aether OS will be delivered as a fully custom web app with:
- Dedicated frontend application for dashboard, chat, and workflows
- Backend APIs for agents, tasks, memory, and integrations
- Shared data model and modular internal services
- Deployment-first architecture for web environments

---

## Repository Structure

```text
aether-os/
├── api/              # Deployment runtime entrypoints (Vercel)
├── core/             # FastAPI core backend
├── agents/           # Agent modules and orchestration logic
├── integrations/     # Third-party connectors
├── ui/               # Custom web app frontend (in-progress)
├── data/             # Local/dev data assets
├── requirements.txt
├── vercel.json
└── plan.md
```

---

## Quick Start (Local API)

```bash
# 1) Clone
git clone https://github.com/teephopdisawas/aether-os.git
cd aether-os

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run the API
uvicorn core.main:app --reload
```

Open:
- `http://localhost:8000/health`
- `http://localhost:8000/docs`

---

## Deployment (Vercel)

The repository is configured for Vercel with `api/index.py` as the app entrypoint.

```bash
vercel
```

---

## Contributing

Contributions should align with the custom web app direction.

Priority contributions:
- Frontend app foundation in `ui/`
- API surface design in `core/`
- Agent and integration modules that support the web product

---

## License

MIT
