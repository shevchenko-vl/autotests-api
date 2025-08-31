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

    def login_api(self, payload: LoginRequestDict) -> Response:
        """
        Аутентифицирует пользователя.

        :param payload: Словарь с email и password.
        :return: Объект Response с данными ответа.
        """
        return self.post("/api/v1/authentication/login", json=payload)

    def refresh_api(self, payload: RefreshRequestDict) -> Response:
        """
        Обновляет токен доступа.

        :param payload: Словарь с refreshToken.
        :return: Объект Response с данными ответа.
        """
        return self.post("/api/v1/authentication/refresh", json=payload)
