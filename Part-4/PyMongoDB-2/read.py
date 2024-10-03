import pymongo

client= pymongo.MongoClient('mongodb://localhost:27017/')
db=client['11am']
user_col=db['user']

#print user id and name
users_list = user_col.find()

for user in users_list:
    print("User Id",user['id'],"and Name", user['username'])

client.close()