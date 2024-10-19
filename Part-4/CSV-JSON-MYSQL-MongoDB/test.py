import requests
import csv
import json 
import mysql.connector
import pymongo 
users = None 
users_data=requests.get('https://jsonplaceholder.typicode.com/users')
users=users_data.json()

print(users)