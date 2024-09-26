class InsuffientBalError(Exception):
    def __init__(self,msg):
        self.msg=msg

def withdrawl():
    amount = int(input("Enter Amout to withdrawl"))
    acc_bal  = 5000
    if acc_bal > amount:
        print("Withdrawl and enjoy")
    else:
        raise InsuffientBalError("Low Bal")
withdrawl()
print("Good Morning")