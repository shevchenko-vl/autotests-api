from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateUserRequestDict(TypedDict):
    """
    Описание параметра запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для "/api/v1/users" запросов без аутентификации.
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Создает пользователя.

        :param request: Словарь соответствующий CreateUserRequestDict (note: казалось бы `payload`)
        :return: Объект Response с данными ответа.
        """
        return self.post('/api/v1/users', json=request)
