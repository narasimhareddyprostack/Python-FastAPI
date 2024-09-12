def outer():
    print("outer function")
    
    def inner():
        print("inner function")

    return inner

inner=outer()
#print(id(x))
inner()  #how to execute inner function  - from outside
inner()  #how to execute inner function  - from outside
inner()  #how to execute inner function  - from outside
inner()  #how to execute inner function  - from outside
inner()  #how to execute inner function  - from outside