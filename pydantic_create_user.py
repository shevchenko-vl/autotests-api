import uuid
from typing import Annotated

from pydantic import AfterValidator, BaseModel, ConfigDict, EmailStr, Field, StringConstraints


def is_uuid4(value: str) -> str:
    uuid.UUID(value, version=4)
    return value


UserNameConstraints = StringConstraints(min_length=1, max_length=50)


class UserDetailsSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    email: Annotated[EmailStr, StringConstraints(min_length=1, max_length=250)]  # noqa
    last_name: Annotated[str, UserNameConstraints, Field(alias='lastName')]
    first_name: Annotated[str, UserNameConstraints, Field(alias='firstName')]
    middle_name: Annotated[str, UserNameConstraints, Field(alias='middleName')]


class UserSchema(UserDetailsSchema):
    id: Annotated[str, AfterValidator(is_uuid4)]


class CreateUserRequestSchema(UserDetailsSchema):
    password: Annotated[str, StringConstraints(min_length=1, max_length=250)]  # noqa


class CreateUserResponseSchema(BaseModel):
    user: UserSchema
