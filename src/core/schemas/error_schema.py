from pydantic import BaseModel


class HTTPException(Exception):
    def __init__(self, error_code: str):
        self.error_code = error_code


class HTTPExceptionSchema(BaseModel):
    error_code: str
    detail: str

    class Config:
        schema_extra = {
            "example": {
                "error_code": "ERR_404",
                "detail": "Object not found"
            },
        }


class FieldErrorSchema(BaseModel):
    name: str
    detail: str

    class Config:
        schema_extra = {
            "example": {
                "field": "field1",
                "detail": "value is not a valid email address"
            },
        }


class RequestValidationErrorSchema(BaseModel):
    error_code: str
    detail: str = 'Request validation error'
    errors: list[FieldErrorSchema] = []

    class Config:
        schema_extra = {
            "example": {
                "error_code": "ERR_422",
                "detail": "Request validation error",
                "errors": [
                    {
                        "field": "email",
                        "detail": "value is not a valid email address"
                    },
                    {
                        "field": "password",
                        "detail": "field required"
                    }
                ]
            },
        }
