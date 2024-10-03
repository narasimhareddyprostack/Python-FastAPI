import pymongo
client = pymongo.MongoClient()
db=client['11am']
user_col=db['user']

query = {'id':6}

user_col.delete_many(query)
print("Deleted successfully")

client.close()