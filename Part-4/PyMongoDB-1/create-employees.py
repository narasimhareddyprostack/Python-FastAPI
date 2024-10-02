import pymongo

client = pymongo.MongoClient()
db=client['11am']
emp_col=db['emp']

emp_list=[{"eid":1,"ename":"Ronna","email":"rgilffillan0@360.cn","gender":"Female"},
{"eid":2,"ename":"Claude","email":"cpacheco1@guardian.co.uk","gender":"Female"},
{"eid":3,"ename":"Geoffrey","email":"gseldner2@slideshare.net","gender":"Male"},
{"eid":4,"ename":"Dennie","email":"dgoundrill3@google.com","gender":"Male"},
{"eid":5,"ename":"Marja","email":"mdoale4@buzzfeed.com","gender":"Female"}]

emp_col.insert_many(emp_list)
client.close()