numbers=[10,20,30,40]
# add 1 to every element and create new list
def addplus(num):
    return num+1

map_obj=map(addplus,numbers)

new_numbers=list(map_obj)
print(numbers)
print(new_numbers)