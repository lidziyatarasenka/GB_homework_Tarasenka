v = float(input('insert your income '))
s = float(input('insert your spendings '))
if v > s:
    print(f"congrats, you have {v - s:.3f} money ")
    print(f"your profitability is {((v - s) / v):.3f}")
    no_of_workers = int(input("how many workers do you have? "))
    print(f"you can pay {((v - s) / no_of_workers):.3f} each of your workers")
elif v == s:
    print("not so bad, you broke even ")
elif v < s:
    print('well, maybe next time you\'ll succeed')