from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class LoginRequestDict(TypedDict):
    """
    Описание парамтера запроса на аутентификацию.
    """
    email: str
    password: str


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
