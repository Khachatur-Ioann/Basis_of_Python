def my_func():
    try:
        num_1 = int(input())
        num_2 = int(input())
        return num_1 / num_2
    except ZeroDivisionError as err:
        return err

print(my_func())

# Вариант решения 2

# def my_func():
#     try:
#         num_1 = int(input())
#         num_2 = int(input())
#         return num_1 / num_2
#     except ZeroDivisionError:
#         return 'err'
#
# print(my_func())

# Вариант решения 3
# def my_func():
#
#         num_1 = int(input())
#         num_2 = int(input())
#         return num_1 / num_2
#
# try:
#     print(my_func())
# except ZeroDivisionError as err:
#     print(err)
