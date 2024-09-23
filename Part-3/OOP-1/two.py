class Employee:
    loc="B101"

e1=Employee()
e2=Employee()
e3=Employee()
print(e1)
print(e2)
print(e3)
print(id(e1))
print(id(e2))
print(id(e3))
print(e1.__dict__)
print(e2.__dict__)
print(e3.__dict__)
print(Employee.__dict__)