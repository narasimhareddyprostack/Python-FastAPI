import requests
import csv
import json 
import mysql.connector
import pymongo 
users = None 
users_data=requests.get('https://jsonplaceholder.typicode.com/users')
users=users_data.json()

fp1 = open('user.json','w')
json.dump(users,fp1)
print("User Data - write into json file successfully")
fp1.close()

new_users=[]
for user in users:
    new_users.append((user['id'],user['name'],user['email'],user['address']['city'],user['website'],user['phone']))


print(new_users)

con=mysql.connector.connect(host='localhost',user='root',password='root', database='dasara')
cursor = con.cursor()
sql_st = 'insert into user(uid,uname,email,city,website,phone) values(%s,%s,%s,%s,%s,%s)'
cursor.executemany(sql_st,new_users)
con.commit()

print("Data Inserted successfully mysql table")


client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['api_data']
users_col = db['users']
users_col.insert_many(users)
print("Inserted Successfully!")

