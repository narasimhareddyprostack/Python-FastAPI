import json
fp1= open("users.json",'r')
users_list=json.load(fp1)

employees=[]
for user in users_list:
    employees.append({'eid':user['id'], "ename":user['name']})

fp2 = open('emp.json','w')
json.dump(employees,fp2)

fp1.close()
fp2.close()