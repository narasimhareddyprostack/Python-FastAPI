emp={
    'eid':101,
    'ename':"Rahul",
    'esal':45000
}
#print all keys - for loop
for key in emp.keys():
    print(key)

print("********")
#print all values- using for loop
for value in emp.values():
    print(value)

print("********")
for key,value in emp.items():
    print(key,":",value)