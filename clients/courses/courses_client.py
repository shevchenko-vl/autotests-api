from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.files.files_schema import FileSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.users_schema import UserSchema


class Course(TypedDict):
    """
    Описание структуры курса.
    """
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: FileSchema
    estimatedTime: str
    createdByUser: UserSchema


class GetCoursesQueryDict(TypedDict):
    """
    Описание параметра запроса на получение списка курсов.
    """
    userId: str


class CreateCourseRequestDict(TypedDict):
    """
    Описание параметра запроса на создание курса.
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str


class CreateCourseResponseDict(TypedDict):
    """
    Описание структуры ответа создания курса.
    """
    course: Course


class UpdateCourseRequestDict(TypedDict):
    """
    Описание параметры запроса на обновление курса.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None


class CoursesClient(APIClient):
    """
    Клиент для /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Получает список курсов.

        :param query: Словарь с userId.
        :return: Объект Response с данными ответа.
        """
        return self.get('/api/v1/courses', params=query)

    def get_course_api(self, course_id: str) -> Response:
        """
        Получает курс.

        :param course_id: Идентификатор курса.
        :return: Объект Response с данными ответа.
        """
        return self.get(f'/api/v1/courses/{course_id}')

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Создает курс.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Объект Response с данными ответа.
        """
        return self.post('/api/v1/courses', json=request)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """
        Обновляет курс.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Объект Response с данными ответа.
        """
        return self.patch(f'/api/v1/courses/{course_id}', json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Удаляет курс.

        :param course_id: Идентификатор курса.
        :return: Объект Response с данными ответа.
        """
        return self.delete(f'/api/v1/courses/{course_id}')

    def create_course(self, request: CreateCourseRequestDict) -> CreateCourseResponseDict:
        response = self.create_course_api(request)
        return response.json()


def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))
