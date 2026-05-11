from fastapi import APIRouter

from core.config import AI_CONFIG, AI_PROVIDER
from core.schemas.system import AIConfigData, AIConfigResponse, HealthData, HealthResponse

router = APIRouter(prefix="/system", tags=["system"])


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="Health check",
    response_description="API health status",
)
async def health_check() -> HealthResponse:
    return HealthResponse(data=HealthData(status="ok"))


@router.get(
    "/config/ai",
    response_model=AIConfigResponse,
    summary="AI configuration",
    response_description="Server-side AI integration configuration",
)
async def get_ai_config() -> AIConfigResponse:
    return AIConfigResponse(
        data=AIConfigData(
            provider=AI_PROVIDER,
            puter_js_enabled=AI_CONFIG.puter_js_enabled,
            puter_app_id=AI_CONFIG.puter_app_id,
        )
    )
