import csv 

fp = open('emp.csv','r')
rows=csv.reader(fp)
users=list(rows)


for user_data in users[1:]:
    print(user_data[1])