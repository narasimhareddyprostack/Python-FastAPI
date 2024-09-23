class Employee:
    pass

e1=Employee()
e2=Employee()
e3=Employee()
print(id(e1))
print(id(e2))
print(id(e3))
print(e1.__dict__)
print(e2.__dict__)
print(e3.__dict__)