from dataclasses import dataclass
import os


@dataclass(frozen=True)
class AIConfig:
    provider: str
    puter_js_enabled: bool
    puter_app_id: str | None


def _is_truthy(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "on"}


def load_ai_config() -> AIConfig:
    enabled = _is_truthy(os.getenv("PUTER_JS_ENABLED", "true"))
    app_id = os.getenv("PUTER_APP_ID") or None
    return AIConfig(
        provider="puter_js",
        puter_js_enabled=enabled,
        puter_app_id=app_id,
    )


AI_CONFIG = load_ai_config()
