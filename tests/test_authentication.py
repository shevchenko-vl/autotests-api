from http import HTTPStatus

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


def test_login():
    create_user_request = CreateUserRequestSchema()
    get_public_users_client().create_user(create_user_request)

    request = LoginRequestSchema(email=create_user_request.email, password=create_user_request.password)
    response = get_authentication_client().login_api(request)
    response_data = LoginResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_login_response(response_data)
    validate_json_schema(response.json(), response_data.model_json_schema())
