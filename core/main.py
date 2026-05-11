from fastapi import FastAPI

from core.config import AI_CONFIG

app = FastAPI(title="Aether OS Core API", version="0.1.0")


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/config/ai")
async def get_ai_config() -> dict[str, str | bool | None]:
    return {
        "provider": AI_CONFIG.provider,
        "puter_js_enabled": AI_CONFIG.puter_js_enabled,
        "puter_app_id": AI_CONFIG.puter_app_id,
    }
