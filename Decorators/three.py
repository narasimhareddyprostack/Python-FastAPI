def outer():
    print("outer function")
    
    def inner():
        print("inner function")

    print(id(inner))
    return inner
    

x=outer()
print(id(x))
#inner()  #how to execute inner function  - from outside