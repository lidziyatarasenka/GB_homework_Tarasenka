rating = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

new_item = input("insert your result ")


def check_user_input(new_item):
    try:
        print("Input is a number")
        return float(new_item)
    except ValueError:
        print("Input is not a number")
        return 0


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
