max_num = 0
num = int(input("insert any integer "))
while num > 0:
    new_num = num % 10
    if new_num > max_num:
        max_num = new_num
    if max_num == 9:
        break
    num = num // 10
print(f"max digit in your number is {max_num}")
