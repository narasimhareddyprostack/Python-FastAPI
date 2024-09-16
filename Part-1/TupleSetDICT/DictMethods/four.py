emp={'name': 'Rahul Gandhi'}
#emp.update('eid',101)
print(emp) 
#TypeError: update expected at most 1 argument, got 2
emp.update({'eid':101})
print(emp)