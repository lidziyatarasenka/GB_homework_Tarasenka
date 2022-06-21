rating = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

new_item = input("insert your result ")


def check_user_input(new_item):  # хочу проверить, корректно ли введены данные, но что-то пошло не так. Хэлп
    try:
        new_item = float(new_item)
        print("Input is a number")
    except ValueError:
        print("Input is not a number")
        return


check_user_input(new_item)

new_item = float(new_item)
if rating[-1] >= new_item:
    rating.append(new_item)
else:
    for index, el in enumerate(rating):
        if new_item > el:
            rating.insert(index, new_item)
            break

print(rating)
