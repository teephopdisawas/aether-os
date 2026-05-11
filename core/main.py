from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from core.api.v1.router import router as v1_router
from core.config import AI_CONFIG, AI_PROVIDER
from core.schemas.common import ErrorResponse

app = FastAPI(title="Aether OS Core API", version="0.1.0")
app.include_router(v1_router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_, exc: RequestValidationError) -> JSONResponse:
    payload = ErrorResponse(
        error={"code": "validation_error", "message": str(exc.errors())}
    ).model_dump()
    return JSONResponse(status_code=422, content=payload)


@app.exception_handler(ValueError)
async def value_error_exception_handler(_, exc: ValueError) -> JSONResponse:
    payload = ErrorResponse(error={"code": "config_error", "message": str(exc)}).model_dump()
    return JSONResponse(status_code=400, content=payload)


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/config/ai")
async def get_ai_config() -> dict[str, str | bool | None]:
    return {
        "provider": AI_PROVIDER,
        "puter_js_enabled": AI_CONFIG.puter_js_enabled,
        "puter_app_id": AI_CONFIG.puter_app_id,
    }
