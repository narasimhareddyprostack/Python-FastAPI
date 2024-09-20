import requests
import json 
import csv 

api_url='https://jsonplaceholder.typicode.com/users11111'
user_Data = None
users=None
try:
    user_Data=requests.get(api_url)
    #print(user_Data.status_code)
    users=user_Data.json()
    user_Data.raise_for_status()
    
except requests.exceptions.RequestException as e:
    fp = open('user.json','r')
    users = json.load(fp)


print(type(users))
print(users)