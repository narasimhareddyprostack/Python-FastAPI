import requests

data=requests.get('https://dummyjson.com/users')

user_data=data.json()
users=user_data['users']
print(type(users))
