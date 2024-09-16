
a=100
update=lambda name:name.lower()

print(type(a))  #<class, int>
print(type(update))  #<class, function>

name = update("RAHUL")
print(name)