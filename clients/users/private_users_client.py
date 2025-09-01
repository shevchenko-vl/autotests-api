from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


class User(TypedDict):
    """
    Описание структуры пользователя.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


class GetUserResponseDict(TypedDict):
    """
    Описание структуры ответа получения пользователя.
    """
    user: User


class UpdateUserRequestDict(TypedDict):
    """
    Описание параметра запроса на обновление пользователя.
    """
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None


class PrivateUsersClient(APIClient):
    """
    Клиент для "/api/v1/users" запросов с аутентификацией.
    """

    def get_user_me_api(self) -> Response:
        """
        Получает текущего пользователя.

        :return: Объект Response с данными ответа.
        """
        return self.get('/api/v1/users/me')

    def get_user_api(self, user_id: str) -> Response:
        """
        Получает пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Объект Response с данными ответа.
        """
        return self.get(f'/api/v1/users/{user_id}')

    def update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        """
        Обновляет пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :param request: Словарь с email, lastName, firstName, middleName.
        :return: Объект Response с данными ответа.
        """
        return self.patch(f'/api/v1/users/{user_id}', json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Удаляет пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/api/v1/users/{user_id}')

    def get_user(self, user_id: str) -> GetUserResponseDict:
        response = self.get_user_api(user_id)
        return response.json()


def get_private_users_client(user: AuthenticationUserDict) -> PrivateUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))
