import json 
emp_dict={'eid': '101', 'ename': 'Rahul', 'avail': True, 'loc': 'undefined', 'esal': None}

emp_json=json.dumps(emp_dict)

print(type(emp_dict))
print(type(emp_json))
print(emp_dict)
print(emp_json)