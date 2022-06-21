my_list = (input("insert any number of items divided by ' '")).split()


for el in my_list[:-1:2]:
    index = my_list.index(el)
    my_list[index], my_list[index+1] = my_list[index+1], my_list[index]
print(my_list)

