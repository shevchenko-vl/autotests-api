from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


class Token(TypedDict):
    """
    Описание структуры аутентификационных токенов.
    """
    tokenType: str
    accessToken: str
    refreshToken: str


class LoginRequestDict(TypedDict):
    """
    Описание парамтера запроса на аутентификацию.
    """
    email: str
    password: str


class LoginResponseDict(TypedDict):
    """
    Описание структуры ответа аутентификации.
    """
    token: Token


class RefreshRequestDict(TypedDict):
    """
    Описание параметра запроса для обновления токена.
    """
    refreshToken: str


class AuthenticationClient(APIClient):
    """
    Клиент для /api/v1/authentication
    """

    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Аутентифицирует пользователя.

        :param request: Словарь с email и password.
        :return: Объект Response с данными ответа.
        """
        return self.post('/api/v1/authentication/login', json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Обновляет токен доступа.

        :param request: Словарь с refreshToken.
        :return: Объект Response с данными ответа.
        """
        return self.post('/api/v1/authentication/refresh', json=request)

    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        response = self.login_api(request)
        return response.json()


def get_authentication_client() -> AuthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())
