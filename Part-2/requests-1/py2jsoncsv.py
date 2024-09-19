import json
#import csv 
customers=[{'id':101,'name':'Rahul','avail':True},
           {'id':102,'name':'Sonia','avail':True},
           {'id':103,'name':'Priya','avail':False},
           {'id':104,'name':'Modi','avail':True},
           ]
fp1 = open('emp.json','w')
#fp1 = open('emp.csv','w')
json.dump(customers,fp1)
print("New JSON file Created!")
fp1.close()