try:
    a= int(input("Enter First No:"))
    b= int(input("Enter Secon No:"))
    print(a/b)
except ZeroDivisionError as e:
    print("cont divibe zero")
except ValueError as e:
    print('Cant convert str to int') 
