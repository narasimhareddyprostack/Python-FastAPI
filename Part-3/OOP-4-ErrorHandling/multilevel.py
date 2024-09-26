class GP:
    def m1(self):
        print("GP- class m1 method")
        
    def m2(self):
        print("GP- class m2 method")
class Parent(GP):
    
    def m3(self):
        print("Parent- class m3 method")
class Child(Parent):
    
    def m4(self):
        print("Child- class m4 method")

obj=Child()
obj.m1()
obj.m2()
obj.m3()
obj.m4()