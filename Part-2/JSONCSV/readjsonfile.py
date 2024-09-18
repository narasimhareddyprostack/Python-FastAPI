import json 

fp = open('data.json','r')

data=json.load(fp)
print(type(data))
print(len(data))
print(data)