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
- Health endpoint: `GET /health` and `GET /api/v1/system/health`
- AI config endpoint: `GET /config/ai` and `GET /api/v1/system/config/ai` (Puter.js-only backend mode)
- Vercel runtime entrypoint in `/api/index.py`
- Vercel rewrite configuration in `/vercel.json`
- React + TypeScript frontend scaffold in `/ui`

---

## Project Direction

Aether OS will be delivered as a fully custom web app with:
- Dedicated frontend application for dashboard, chat, and workflows
- Backend APIs for agents, tasks, memory, and integrations
- Puter.js-based AI integration for chat and agent intelligence
- Shared data model and modular internal services
- Deployment-first architecture for web environments

---

## Phase 1 API Contract (Frontend ↔ Backend)

Versioned routes are grouped under `/api/v1`.

Core Phase 1 endpoints:

| Route | Method | Purpose | Response shape |
|---|---|---|---|
| `/api/v1/system/health` | `GET` | Backend liveness/status | `{ "success": true, "data": { "status": "ok" } }` |
| `/api/v1/system/config/ai` | `GET` | Frontend-safe AI runtime config | `{ "success": true, "data": { "provider": "puter_js", "puter_js_enabled": true, "puter_app_id": "..." } }` |

Shared error shape:

```json
{
  "success": false,
  "error": {
    "code": "validation_error",
    "message": "..."
  }
}
```

---

## Module Boundaries

- `core/`: API surface, shared schemas, and runtime configuration.
- `agents/`: agent logic and orchestration modules (kept isolated from HTTP layer).
- `integrations/`: third-party connectors and provider adapters.
- `ui/`: frontend app shell and UX.
- `api/`: deployment runtime entrypoints only.

---

## Environment Strategy

- `APP_ENV=local`: local development defaults.
- `APP_ENV=preview`: preview deployment behavior.
- `APP_ENV=production`: strict production mode (requires `PUTER_APP_ID` when Puter.js is enabled).

See `.env.example` for all variables.

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
- `http://localhost:8000/config/ai`
- `http://localhost:8000/api/v1/system/health`
- `http://localhost:8000/api/v1/system/config/ai`
- `http://localhost:8000/docs`

---

## Quick Start (Frontend)

```bash
cd ui
npm install
npm run dev
```

Default local frontend uses Vite `/api` proxy to `http://localhost:8000`.

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
