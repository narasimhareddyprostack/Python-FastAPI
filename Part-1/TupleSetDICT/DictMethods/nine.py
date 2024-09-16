users=[
    {'eid':101,'ename':'Rahul','email':'Rahul@gmail.com','gender':'Male'},
    {'eid':102,'ename':'Sonia','email':'Sonia@gmail.com','gender':'Female'},
    {'eid':103,'ename':'Priyanka','email':'priya@gmail.com','gender':'Female'},
]
print(type(users))
#print all user names
for user in users:
    print(user['ename'])