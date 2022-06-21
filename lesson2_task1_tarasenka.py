new_list = ['apple', 2, 13.5, False, (1, 2, 3), [20, 30, 40], 1, {"key_1": 'q', "key_2": 'w', "key_3": 'e'}]
for number, el in enumerate(new_list, 1):
    print(f"{number}. {type(el)}")
