from pydantic import BaseModel, ConfigDict, Field


class GetExercisesQuerySchema(BaseModel):
    """
    Описание параметра запроса на получение списка упражнений.
    """
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias='courseId')


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание параметра запроса на создание задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias='courseId')
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str | None = Field(alias='estimatedTime')


class ExerciseSchema(BaseModel):
    """
    Описание структуры упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str | None = Field(alias='estimatedTime')


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание параметра запроса на обновление задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    order_index: int | None = Field(alias='orderIndex')
    description: str | None
    estimated_time: str | None = Field(alias='estimatedTime')


class GetExercisesResponseSchema(BaseModel):
    exercises: list[ExerciseSchema]


class ExerciseResponseSchema(BaseModel):
    exercise: ExerciseSchema
