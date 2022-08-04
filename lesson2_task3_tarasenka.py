month = int(input("insert number of a month "))

my_list = [0, "january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
           "november", "december"]
month_in_a_list = my_list[month]  # connects input with indexes in a list

if 0 < month < 3:
    print(month_in_a_list, "-", "winter")
elif month > 11:
    print(month_in_a_list, "-", "winter")
elif 2 < month < 6:
    print(month_in_a_list, "-", "spring")
elif 5 < month < 9:
    print(month_in_a_list, "-", "summer")
else:
    print(month_in_a_list, "-", "autumn")

my_dict = {
    0: "0", 1: "january - winter", 2: "february - winter", 3: "march - spring", 4: "april - spring", 5: "may - spring",
    6: "june - summer", 7: "july - summer", 8: "august - summer", 9: "september - autumn", 10: "october - autumn",
    11: "november - autumn", 12: "december - winter"}
print(my_dict.get(month))
