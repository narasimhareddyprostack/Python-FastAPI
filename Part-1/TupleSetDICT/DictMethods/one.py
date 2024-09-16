emp={
    'eid':101,
    'enmae':"Rahul",
    'esal':45000
}
#how to read dict values
print(emp['eid'])
print(emp.get('eid'))
#print all keys
print(emp.keys())
print(type(emp.keys()))
#print all values
print(emp.values())
print(type(emp.values()))
#print all key and values
print(emp.items())