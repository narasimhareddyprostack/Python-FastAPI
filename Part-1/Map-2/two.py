numbers=[10,20,30,40,50]
def squreIt(num):
    return num*num

map_obj=map(squreIt,numbers)
print(map_obj)
print(type(map_obj))
print(list(map_obj))
