import csv 

fp = open('emp.csv','r')
rows=csv.reader(fp)

print(type(rows))
for row in rows:
    print(row[1])