import requests
import csv
import json 
import mysql.connector
import pymongo 
users = None 

try:
    users_data=requests.get('https://jsonplaceholder.typicode.com/users')
    users=users_data.json()
except Exception as e:
    print(e)

fp1 = None
try:
    fp1 = open('user.json','w')
    json.dump(users,fp1)
    print("User Data - write into json file successfully")
except Exception as e:
    print(e)
finally:
    fp1.close()

new_users=[]
for user in users:
    new_users.append((user['id'],user['name'],
                      user['email'],user['address']['city'],
                      user['website'],user['phone']))
print(new_users)

try:
    dbcon=mysql.connector.connect(host='localhost',user='root',
                                  password='root', database='dasara')
    cursor = dbcon.cursor()
    sql_st = '''insert into user(uid,uname,email,city,website,phone) 
              values(%s,%s,%s,%s,%s,%s)'''
    cursor.executemany(sql_st,new_users)
    dbcon.commit()
    print("Data Inserted successfully mysql table")
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()




try:
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['api_data']
    users_col = db['users']
    users_col.insert_many(users)
    print("Inserted Successfully!")
except Exception as err:
    print(err)


fp2 = None 
try:
    fp2=open('user.csv','w',newline='\n')
    csvwriter=csv.writer(fp2)
    csvwriter.writerow(['UId','UName','Email'])
    for user in users:
        csvwriter.writerow([user['id'],user['name'],user['email']])
    print("Write in CSV File")
except Exception as err:
    print(err)
finally:
    fp2.close()