my_list = [7, 5, 3, 3, 2]
new_number = int(input('Введите натуральное число - '))
i = 0

for el in my_list:
    if new_number <= el:
        i += 1
    elif new_number > el:
        break

my_list.insert(i, new_number)
print(my_list)

# my_list = [4, 3, 3, 2, 1]
#
# while True:
#     print(f"Current rating: {my_list}")
#     number = input("Enter rating number or 111 to finish - ")
#     if number.lstrip('-').isdigit() and number != "111":
#         number = int(number)
#         if my_list.count(number):
#             my_list.insert(my_list.index(number) + my_list.count(number), float(number))
#         else:
#             param = 0
#             n_param = 0
#             for n, i in enumerate(my_list):
#                 if number > i:
#                     if param < i:
#                         param = i
#                         n_param = n
#                 else:
#                     n_param = n + 1
#             my_list.insert(n_param, number)
#     elif not number.isdigit():
#         print("Enter number please")
#     else:
#         break

#  ------------------------------------------- вариант решения ---------------------------------------------------------


# my_list = [9, 8, 7, 7, 7, 6, 5, 3, 3, 3, 2, 1]
# new_number = ""

# while new_number != "q":
#     i = 0
#     new_number = input("Enter a new rating element in the form of a natural number.\nTo exit - q\n")
#
#     if new_number.isdigit():
#         for n in my_list:
#             if int(new_number) <= n:
#                 i += 1
#             else:
#                 break
#         my_list.insert(i, int(new_number))
#     print(my_list)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


# my_list = [9, 8, 7, 7, 7, 6, 5, 3, 3, 3, 2, 1]
#
# while True:
#     new_number = input("Enter a new rating element in the form of a natural number.\n")
#     if new_number.isdigit():
#         my_list.append(float(new_number))
#         my_list.sort(reverse=True)
#         print(my_list)
#     elif new_number == "q":
#         break