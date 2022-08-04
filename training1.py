def optional_greeter(name):
  if name.startswith('X'):
#  We don\'t greet people with weird names :p
       return print("name")

print('Hi there, ', name)
optional_greeter('Xander')


def greeting(name="organizm", location="somewhere"):
    print("welcome", name, "to", location)

# greeting("Lida", "tut")

# def xueta(first=1, second=2):
#    print("welcome", first, "but", second)

# xueta("a", "b")

my_list = ["xueta", "i", "serost"]
my_list.reverse()
print(my_list)

result_list = [2, 'text', 456, 45.3, None])

# a = input("insert name ")
# b = input("insert surname ")
# def funct(name=a, surname=b):
#   print("listen", name, surname)
# funct("qwerty", "uiop")

# def funct(name="ivan", surname="govnov"):
#   print("and here again", name, surname)
# funct(surname="sergej")


my_str = "xueta nesusvetnaja"
print(len(my_str))
print(my_str[3:10:1])


my_list = ['i', 'k', 'y', 'v', 'z', ' ', 'i', ' ', 'a', 'v', 'o', 'l', 's']
print(my_list)

for i, v in enumerate(my_list):
    print(f"{i}) {v}")

a = input("insert any integer")
print("good" if a.isdigit() else "the number should be integer")

my_list = [[10, 20, 30], [40, 50], [60], [70, 80, 90]]
import intertools
my_list_n=[[10, 20, 30], [40, 50], [60], [70, 80, 90]]
print(list(intertools.chain(*my_list)))

users = {'u_1': 'active', 'u_2': 'inactive', 'u_3': 'active', 'u_4': 'inactive', 'u_5': 'active'}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print(users.copy())

# global r_val, h_val
r_val = float(input("Укажите радиус: "))
h_val = float(input("Укажите высоту: "))


def full_s_calc():
    # s_side, s_circle
    s_side = 2 * 3.14 * r_val * h_val
    s_circle = 3.14 * r_val ** 2
    s_full = s_side + 2 * s_circle
    # return s_full
    print(s_full)


def add_numbers(x, y):
    return float(x + y)


x = float(input('insert first number '))
y = float(input('insert second number '))
print(add_numbers(x, y))


def greet(name):
    print('Hi', name)
name = input('tell me your name ')
greet(name)

my_str = '123abv123gdejz123iklmnopr123stuf'
my_list = list(my_str)
print(my_list.pop(0))
print(my_list)

my_list.remove("2")
print(my_list)
my_list.count("2")

# print(my_str)
# print(type(my_str))
# print(my_str[1:6:1])
# print(my_str[::-1])
# for elements in my_str:
#     print(elements)
print(my_str.find('abv'))

for kolbasa in "hello":
    print(kolbasa)

my_dict = {'k_1': 'a', 'k_2': 'b', 'k_3': 'c', 'k_4': 'd', 'k_5': 'e'}
print(my_dict)

my_dict.items()
my_dict.keys()
my_dict.values()
my_dict.get("k_1")
my_dict.popitem()
my_dict.setdefault('k_6')

my_list = [[10, 20, 30], [40, 50, 10], [60, 50], [70, 80, 90, 10]]
new_list = sum(my_list, [])

list(set(new_list))

a, b, c = 3, 5, 7
a, b, c = c, a, b

old_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
new_list = zip(*old_list)
print(list(new_list))

for nom, el in enumerate(['a', 'b', 'c', 'd', 'e'], 1):
    print(nom, el)

my_list = [1, 3, 3, 4, 4, 6, 8, 0, 4]
new_list = []
for el in my_list:
    new_list.append(el / 2)
print(new_list)

my_list = ['1', '3', '3', '4', '4', '6', '8', '0', '4']
new_var = ''.join(my_list)
print(new_var)

one_more_list = [1, 2, 3, 4, 5, 6, 7]
one_more_new_var = ''.join(str(el) for el in one_more_list)
print(one_more_new_var)

list = ['1', 'abv', True, 'next']
new_list = ''.join([str(el) for el in list])
print(new_list)

one_more_list = [1, 2, 3, 4, 5, 6, 7]
one_more_new_var = ''.join(map(str, one_more_list))
print(one_more_new_var)

my_str = '1 2 3 4'
my_list = '1 2 3 4'.split()
print(my_list)
summ = sum(int(el) for el in my_list)
print(summ)

my_list = list(range(9))
print(my_list)

my_list = list('qwerty')
for i in range(len(my_list)):
    my_list[i] *= 2
print(my_list)my_list = list('qwerty')
new_list = []
for el in my_list:
    el *= 2
    new_list.append(el)
print(new_list)

timeit(sum(range(10000000)))

my_list = ["ab", "ra", "kada", "bra"]
#for el in ["ab", "ra", "kada", "bra"]:
#print(el, end='')
new_list = ''.join(my_list)
print(new_list)

month = int(input('insert No of a month '))
season_dict = {'winter': [12, 1, 2], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
if month in sum(season_dict.values(), []):
    for item in season_dict.items():
        if month in item[1]:
            print(item[0])
            break

rating = [7, 5, 3]
new_el = ''
while True:
    new_el = input("insert next element of your rating or 'q' to quit")
    if new_el.isdigit():
        rating.append(int(new_el))
        rating.sort()
        rating.reverse()
    else:
        new_el == 'q'
        break
    print(rating)

uni_list = []
def testfunct1(str):
    for i in str:
        uni_list.append(ord(i))
    print(uni_list)
    return uni_list

def testfunct2(my_list):
    new_str = ''
    for i in my_list:
        new_str += chr(i)
    print(new_str)

testfunct2(testfunct1('python is amazing'))




uni_list = []
def funct(my_str):
    for i in my_str:
        uni_list.append(ord(i))
    print(uni_list)
    return uni_list

def funct2(my_list):
    my_str = ''
    for i in my_list:
        my_str += chr(i)
    print(my_str)

funct2(funct('piesta'))
"""
# what we can do with list[]

list_1 = [10, 20, True, 20.15, "apple", 10, 20, 30, [50, 70, 30]]
list_2 = [10, 10, 10, 30, 50, [1, 2, 3], 60, [4, 5, 6]]
list_2[0]  # returns el with 0 index
list_2[5][0]  # returns el with o index in sublist wthich is in the position with 5th index
list_2[5], [0]  # creates a tuple ([1, 2, 3], [0])
list_1[1] * 2  # returns 40
list_1 + list_2  # concatenates lists
list_2[5].append(3)  # returns [10, 10, 10, 30, 50, [1, 2, 3, 3], 60, [4, 5, 6]]

for i in range(len(list_2)):
    print(i)
# takes length, then ranges it, iterates every object in range

for i in range(len(list_2)):
    list_2[i] = list_2[i] * 2
print(list_2)
# takes length, then ranges it, iterates every object in range > takes every object in list according to its index
# and multoplies by 2
#
for i, val in enumerate(list_2, 1):
    print(f"{i} {val}")

print(max(set(my_list), key=my_list.count))

find
sum
of
an
elements in a
string / list
my_list.extend(["1", "2", "3"])
print(my_list)

my_list = "1 2 3 4 5".split()
sum = int(0)
for el in my_list:
    sum = sum + int(el)
print(sum)


def sum_of_list(l):
    total = 0
    for val in l:
        total = total + val
    return total


print(sum_of_list([1, 3, 5, 2, 4]))

num = input("insert any integer")
print(True if num.replace("-", "").isdigit() else False)

"d" in {"f": 15, "n": 16, "c": "d"}
# returns False

"d" in {"f": 15, "n": 16, "c": "d"}.values()
# returns True

# to find intersection in lists
# method N1
lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


print(intersection(lst1, lst2))


# method N2
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


# Driver Code
lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
print(intersection(lst1, lst2))


##
# Method 3
def Intersection(lst1, lst2):
    return set(lst1).intersection(lst2)


# Driver Code
def Intersection(lst1, lst2):
    return set(lst1).intersection(lst2)


lst1 = [4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91]
lst2 = [9, 9, 74, 21, 45, 11, 63]
print(Intersection(lst1, lst2))
#
# # Method 4
lst1 = [4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91]
lst2 = [9, 9, 74, 21, 45, 11, 63]
list(set(lst1).intersection(lst2))  # returns list
set(lst1).intesection(lst2)  # returns set

#
seasons_dict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

month_num = int(input('Введи номер месяца(только цифра): '))

if month_num in sum(seasons_dict.values(), []):
    for i in seasons_dict.items():
        if month_num in i[1]:
            print(i[0])
            break

#
a = [3, 4, 5, 2, 7, 8]
b = [7, 9, 2, 4, 5, 1]
c = [5, 7, 3, 4, 5, 9]

print(list(map(lambda x, y, z: x + y + z, a, b, c)))
print(list(map(lambda x, y, z: 2 * x + 2.5 * y + z, a, b, c)))

print(list(filter(lambda x: x > 5, c)))
print(list(filter(lambda x: x % 2 == 0, a)))

names = ["Abram", "Arib", "Bob", "Shawn",
         "Aria", "Cicilia", "John", "Reema",
         "Alice", "Craig", "Aaron", "Simi"]
print(list(filter(lambda x: x[0] != "A", names)))
print(sorted(names, key=lambda x: x.endswith("ia")))


def s_calc():
    try:
        r_val = float(input("Укажите радиус: "))
        h_val = float(input("Укажите высоту: "))
    except ValueError:
        return
    s_side = 2 * 3.14 * r_val * h_val
    s_circle = 3.14 * r_val ** 2
    s_full = s_side + 2 * s_circle
    return s_side, s_full


s_side_val, s_full_val = s_calc()

# перечисление значений через запятую формирует объект типа кортеж (tuple).
# Присваивая кортеж сразу набору переменных, его элементы сопоставляются переменным.
# Происходит своего рода распаковка.

listsame = [1, 1, 1]
listdiff = [1, 3, 5]
samplestr = "qwerdfbfgf"
print(all([x == 1 for x in listsame]))
print(all([x == 10 for x in listsame]))
print(any([x == 1 for x in listdiff]))
print(any(x == "q" for x in samplestr))

bin(14)  # returns '0b1110'
format(14, 'b')  # returns '1110'
format(14, '#b')  # returns '0b1110'
f'{14:#b}', f'{14:b}'  # returns ('0b1110', '1110')

x = 'ertyuiop'
y = bytearray(x, 'UTF-8')
print(y)
z = list(x)
print(z)

# callable - an instance of a class with a __call__ method; - is of a type that has a non null tp_call member which
# indicates callability

hasattr({1: "a", 2: "b"}, '__call__')
False
hasattr(type({1: "a", 2: "b"}), '__call__')
True


######
def ord_out_of_str(my_str):
    my_ord = []
    for characters in my_str:
        my_ord.append(ord(characters))
    return my_ord
    print(my_ord)


ord_out_of_str("mama_myla_ramy")
######

#####
def my_func(num_1, num_2, num_3):
    try:
        my_list = list(map(int, [num_1, num_2, num_3]))
        my_list.remove(min(my_list))
        return sum(my_list)
    except (TypeError, ValueError):
        return "Enter only a numbers!"


print(my_func(input(), input(), input()))


new_list = (i ** 5 for i in range(1, 100000001))
print(new_list)

for i in new_list:
    print(i) #

print(next(new_list))


from itertools import islice

new_list = (i ** 5 for i in range(1, 11))
print(new_list)

# for i in new_list:
#     print(i)

print(next(new_list))
print(next(new_list))
print(next(new_list))

print(*islice(new_list, 10))
print(list(islice(new_list, 10)))
new_list = (i ** 5 for i in range(1, 11))
print(list(islice(new_list, 10)))


my_file = open(r"C:\Users\Lida\PycharmProjects\pythonProject\testfile.txt", "r", encoding="utf-8")

new_func = ((lambda *args: sum(args))(67, 11, 14, 6))
print(new_func)



a = [1, 3, 5, 4, 8, 9]
b = [3, 5, 0, 5, 2, 8]
c = [4, 9, 3, 1, 3, 9]
d = ["Anna", "Alex", "Sonja", "Asja", "Boris", "Katy", "Craig", "Denis", "Phillip"]

print(list(map(lambda x, y, z: x + y + z, a, b, c)))
print(list(filter(lambda x: x > 5, c)))
print(list(filter(lambda x: x % 2 == 0, c)))
print(list(filter(lambda x: x[0] != "A", d)))
print(sorted(d))
print(sorted(d, key=lambda x: x.endswith("a")))

