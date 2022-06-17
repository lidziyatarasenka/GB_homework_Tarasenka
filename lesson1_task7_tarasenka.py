a = float(input("insert initial distance in km "))
b = float(input("insert desired distance in km "))
d = 1
while a < b:
    d += 1
    a = a + 0.1 * a
    if a >= b:
        break
print(f"you\'ll make your desired distance on day {d}")
