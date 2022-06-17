x = int(input("insert any number of seconds "))
h = x // 3600
m = (x % 3600) // 60
s = x % 60
print(f"{h:02}:{m:02}:{s:02}")