from httpx import Response

from clients.api_client import APIClient
from clients.courses.courses_schema import (
    GetCoursesQuerySchema,
    CreateCourseRequestSchema,
    CreateCourseResponseSchema,
    UpdateCourseRequestSchema,
)
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema


class CoursesClient(APIClient):
    """
    Клиент для /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Получает список курсов.

        :param query: Словарь с userId.
        :return: Объект Response с данными ответа.
        """
        return self.get('/api/v1/courses', params=query.model_dump(by_alias=True))

    def get_course_api(self, course_id: str) -> Response:
        """
        Получает курс.

        :param course_id: Идентификатор курса.
        :return: Объект Response с данными ответа.
        """
        return self.get(f'/api/v1/courses/{course_id}')

    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Создает курс.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Объект Response с данными ответа.
        """
        return self.post('/api/v1/courses', json=request.model_dump(by_alias=True))

    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Обновляет курс.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Объект Response с данными ответа.
        """
        return self.patch(f'/api/v1/courses/{course_id}', json=request.model_dump(by_alias=True))

    def delete_course_api(self, course_id: str) -> Response:
        """
        Удаляет курс.

        :param course_id: Идентификатор курса.
        :return: Объект Response с данными ответа.
        """
        return self.delete(f'/api/v1/courses/{course_id}')

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)


def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))
