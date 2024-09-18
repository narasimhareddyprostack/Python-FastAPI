#read data.json, and create male.json file and female.json
import json 

fp1 = open('data.json','r')
users=json.load(fp1)
print(type(users))
print(len(users))