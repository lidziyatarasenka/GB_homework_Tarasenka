var = (input("write down a sentence ")).split()

for num, el in enumerate(var, 1):
    print(f"{num}. {el[:10]}")
