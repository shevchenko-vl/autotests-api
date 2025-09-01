from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


class File(TypedDict):
    """
    Описание структуры файла.
    """
    id: str
    url: str
    filename: str
    directory: str


class CreateFileRequestDict(TypedDict):
    """
    Описание параметра запроса на создание файла.
    """
    filename: str
    directory: str
    upload_file: str


class CreateFileResponseDict(TypedDict):
    """
    Описание структуры ответа создания файла.
    """
    file: File


class FilesClient(APIClient):
    """
    Клиент для /api/v1/files
    """

    def get_file_api(self, file_id: str) -> Response:
        """
        Получает файл.

        :param file_id: Идентификатор файла.
        :return: Объект Response с данными ответа.
        """
        return self.get(f'/api/v1/files/{file_id}')

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Создает файл.

        :param request: Словарь с filename, directory, upload_file.
        :return: Объект Response с данными ответа.
        """
        return self.post(
            '/api/v1/files',
            data=request,
            files={'upload_file': open(request['upload_file'], 'rb')}
        )

    def delete_file_api(self, file_id: str) -> Response:
        """
        Удаляет файл.

        :param file_id: Идентификатор файла.
        :return: Объект Response с данными ответа.
        """
        return self.delete(f'/api/v1/files/{file_id}')

    def create_file(self, request: CreateFileRequestDict) -> CreateFileResponseDict:
        response = self.create_file_api(request)
        return response.json()


def get_files_client(user: AuthenticationUserDict) -> FilesClient:
    """
    Функция создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию FilesClient.
    """
    return FilesClient(client=get_private_http_client(user))
