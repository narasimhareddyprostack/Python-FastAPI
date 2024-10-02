import pymongo

client=pymongo.MongoClient('mongodb://localhost:27017')
db=client['11am']
user_col=db['user']

user_col.insert_one({'id':6,'name':'Rajni','gender':"Male"})
client.close()