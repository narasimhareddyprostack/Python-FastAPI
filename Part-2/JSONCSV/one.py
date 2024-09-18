import json 
emp_json='''{
    "eid":"101",
    "ename":"Rahul",
    "avail":true,
    "loc":"undefined",
    "esal":null
}'''
print(emp_json)
emp_dict=json.loads(emp_json)
print(type(emp_dict))  #<class,dict>
print(emp_dict)      #{}