from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class GetExercisesQueryDict(TypedDict):
    """
    Описание параметра запроса на получение списка упражнений.
    """
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """
    Описание параметра запроса на создание задания.
    """
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str | None


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание параметра запроса на обновление задания.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
    Клиент для /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Получает список заданий.

        :param query: Словарь с courseId.
        :return: Объект Response с данными ответа.
        """
        return self.get('/api/v1/exercises', params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получает информацию задания.

        :param exercise_id: Идентификатор задания.
        :return: Объект Response с данными ответа.
        """
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Создает задание.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex,
        description, estimatedTime
        :return: Объект Response с данными ответа.
        """
        return self.post('/api/v1/exercises', json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Обновляет задание.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex,
        description, estimatedTime
        :return: Объект Response с данными ответа.
        """
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаляет задание.

        :param exercise_id: Идентификатор задания.
        :return: Объект Response с данными ответа.
        """
        return self.delete(f'/api/v1/exercises/{exercise_id}')
