from httpx import Response

from clients.api_client import APIClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema, RefreshRequestSchema
from clients.public_http_builder import get_public_http_client


class AuthenticationClient(APIClient):
    """
    Клиент для /api/v1/authentication
    """

    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Аутентифицирует пользователя.

        :param request: Словарь с email и password.
        :return: Объект Response с данными ответа.
        """
        return self.post('/api/v1/authentication/login', json=request.model_dump(by_alias=True))

    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        Обновляет токен доступа.

        :param request: Словарь с refreshToken.
        :return: Объект Response с данными ответа.
        """
        return self.post('/api/v1/authentication/refresh', json=request)

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(response.text)


def get_authentication_client() -> AuthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())
