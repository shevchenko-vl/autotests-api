import httpx

from tools.fakers import fake


create_user_payload = {
    'email': fake.email(),
    'password': 'string',
    'lastName': 'string',
    'firstName': 'string',
    'middleName': 'string'
}
create_user_response = httpx.post('http://localhost:8000/api/v1/users', json=create_user_payload)
create_user_response.raise_for_status()
create_user_response_data = create_user_response.json()

login_payload = {
    'email': create_user_payload['email'],
    'password': create_user_payload['password']
}
login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response.raise_for_status()
login_response_data = login_response.json()

# Update part:
update_user_payload = {
    'email': fake.email(),
    'lastName': 'string',
    'firstName': 'string',
    'middleName': 'string'
}
auth_header = {'Authorization': f"Bearer {login_response_data['token']['accessToken']}"}
update_user_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
    json=update_user_payload,
    headers=auth_header
)
update_user_response.raise_for_status()
