from pydantic import BaseModel, Field


class ApiError(BaseModel):
    code: str = Field(..., examples=["validation_error"])
    message: str = Field(..., examples=["Invalid request payload."])


class ErrorResponse(BaseModel):
    success: bool = False
    error: ApiError
