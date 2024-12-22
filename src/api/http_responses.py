from fastapi import status
from pydantic import BaseModel


class HTTPErrorResponse(BaseModel):
    http_status_code: int
    error_code: int
    detail: str


class NotFoundErrorResponse(HTTPErrorResponse):
    http_status_code: int = status.HTTP_404_NOT_FOUND


class BadRequestErrorResponse(HTTPErrorResponse):
    http_status_code: int = status.HTTP_400_BAD_REQUEST

class UnauthorizedErrorResponse(HTTPErrorResponse):
    http_status_code: int = status.HTTP_401_UNAUTHORIZED


class ForbiddenErrorResponse(HTTPErrorResponse):
    http_status_code: int = status.HTTP_403_FORBIDDEN


class InternalServerErrorResponse(HTTPErrorResponse):
    http_status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
