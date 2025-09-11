from pydantic import BaseModel, Field


class TokenSchema(BaseModel):
    """
    Описание структуры аутентификационных токенов.
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class LoginRequestSchema(BaseModel):
    """
    Описание парамтера запроса на аутентификацию.
    """
    email: str
    password: str


class LoginResponseSchema(BaseModel):
    """
    Описание структуры ответа аутентификации.
    """
    token: TokenSchema


class RefreshRequestSchema(BaseModel):
    """
    Описание параметра запроса для обновления токена.
    """
    refresh_token: str = Field(alias="refreshToken")
