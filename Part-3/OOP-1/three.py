class Account:
    min_ba=500

    def open_account(self):
        print("account opened succuessfully")
    @classmethod
    def m2(cls):
        pass
    @staticmethod
    def m3():
        pass

a1=Account()
a2=Account()
#what class contains: variables and Methods

print(a1.__dict__)
print(a2.__dict__)
print(Account.__dict__)