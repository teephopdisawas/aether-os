from pydantic import BaseModel


class HealthData(BaseModel):
    status: str


class HealthResponse(BaseModel):
    success: bool = True
    data: HealthData


class AIConfigData(BaseModel):
    provider: str
    puter_js_enabled: bool
    puter_app_id: str | None


class AIConfigResponse(BaseModel):
    success: bool = True
    data: AIConfigData
