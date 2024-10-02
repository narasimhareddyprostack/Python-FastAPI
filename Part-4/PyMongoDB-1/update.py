import pymongo

client=pymongo.MongoClient()
db=client['11am']
user_col=db['user']

user_col.update_one({'id':1},{'name':"Rahul Gandhi"})

client.close()