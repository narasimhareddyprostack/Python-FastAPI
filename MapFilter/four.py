numbers=[10,20,30,40]
# add 1 to every element and create new list


map_obj=map(lambda num:num+1,numbers)

new_numbers=list(map_obj)
print(numbers)
print(new_numbers)