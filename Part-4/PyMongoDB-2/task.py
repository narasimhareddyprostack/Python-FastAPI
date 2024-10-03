import requests
import pymongo
user_data=requests.get('https://jsonplaceholder.typicode.com/users')
print(user_data)
user_list = user_data.json()
print(type(user_list))

new_user_list=[]
for user in user_list:
    new_user_list.append({'id':user['id'],
                         'username':user['username'],
                         'city':user['address']['city'],
                         'website':user['website']
                         })
print(new_user_list)
client= pymongo.MongoClient('mongodb://localhost:27017/')
db=client['11am']
user_col=db['user']
user_col.insert_many(new_user_list)
print("New Users Added!")
client.close()