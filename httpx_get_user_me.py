import httpx


login_payload = {
    'email': 'vsh@test.org',
    'password': 'password'
}
login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
assert login_response.status_code == 200

login_response_data = login_response.json()
assert login_response_data.get('token', {}).get('accessToken') is not None
assert login_response_data.get('token', {}).get('refreshToken') is not None

# "/api/v1/users/me" part:
headers = {'Authorization': f"Bearer {login_response_data['token']['accessToken']}"}
me_response = httpx.get('http://localhost:8000/api/v1/users/me', headers=headers)
assert me_response.status_code == 200

me_response_data = me_response.json()
assert me_response_data.get('user', {}).get('email') == login_payload['email']

print(f'{me_response.url} response:\n{me_response_data}\nstatus code: {me_response.status_code}')
