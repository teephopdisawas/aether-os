import os
from dataclasses import dataclass
from enum import StrEnum


class AppEnvironment(StrEnum):
    LOCAL = "local"
    PREVIEW = "preview"
    PRODUCTION = "production"


@dataclass(frozen=True)
class AIConfig:
    puter_js_enabled: bool
    puter_app_id: str | None


@dataclass(frozen=True)
class AppConfig:
    environment: AppEnvironment
    ai: AIConfig


TRUTHY_VALUES = {"1", "true", "yes", "on"}
FALSY_VALUES = {"0", "false", "no", "off"}


def _parse_bool(name: str, default: str) -> bool:
    raw = os.getenv(name, default).strip().lower()
    if raw in TRUTHY_VALUES:
        return True
    if raw in FALSY_VALUES:
        return False
    raise ValueError(
        f"Invalid boolean for {name!r}: {raw!r}. "
        f"Expected one of {sorted(TRUTHY_VALUES | FALSY_VALUES)}."
    )


def _load_environment() -> AppEnvironment:
    raw = os.getenv("APP_ENV", AppEnvironment.LOCAL.value).strip().lower()
    try:
        return AppEnvironment(raw)
    except ValueError as exc:
        allowed = ", ".join(env.value for env in AppEnvironment)
        raise ValueError(f"Invalid APP_ENV {raw!r}. Allowed values: {allowed}.") from exc


def load_ai_config(environment: AppEnvironment) -> AIConfig:
    enabled = _parse_bool("PUTER_JS_ENABLED", "true")
    app_id = os.getenv("PUTER_APP_ID") or None
    if environment == AppEnvironment.PRODUCTION and enabled and not app_id:
        raise ValueError("PUTER_APP_ID is required when APP_ENV=production.")
    return AIConfig(
        puter_js_enabled=enabled,
        puter_app_id=app_id,
    )


AI_PROVIDER = "puter_js"


def load_app_config() -> AppConfig:
    environment = _load_environment()
    return AppConfig(environment=environment, ai=load_ai_config(environment))


APP_CONFIG = load_app_config()
AI_CONFIG = APP_CONFIG.ai
