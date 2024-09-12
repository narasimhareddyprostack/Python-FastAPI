def outer():
    print("outer function")
    def inner():
        print("inner function")

    

outer()
inner()  #how to execute inner function  - from outside