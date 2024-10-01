from abc import *

class Bank:
    
    @abstractmethod
    def cal_tax(self):
        pass 

b = Bank()
print(b)
print(id(b))
