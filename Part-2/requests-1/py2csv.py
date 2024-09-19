import csv 
customers=[{'id':101,'name':'Rahul','avail':True},
           {'id':102,'name':'Sonia','avail':True},
           {'id':103,'name':'Priya','avail':False},
           {'id':104,'name':'Modi','avail':True},
           ]

fp1 = open('emp.csv','w',newline="")
wr=csv.writer(fp1)
wr.writerow(['id','name','avail'])
for cust in customers:
    wr.writerow([cust['id'],cust['name'],cust['avail']])


print("New CSV File Created")
fp1.close()