a, b, c = 3, 6, 9
a, b, c = c, a, b
print(a, b, c)

for (letter) in "Hello":
    print(letter)

x = int(input("insert any integer from 0 to 10 "))
while x <= 10:
    x += 1
    if x > 10:
        break
    print(x)
    if x % 2 == 0:
        print("even")
    else:
        print("odd")