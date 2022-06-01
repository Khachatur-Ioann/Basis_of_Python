number = 0
try:
    while number != '#':
        for i in map(int, input("Для выхода наберите '#'\nВведите числа, используя пробел.\n").split()):
            number += i
        print(number)
except ValueError:
    print(number)

#  ------------------------------------------- вариант решения ---------------------------------------------------------
# моя попытка выполнить задание
# while True:
#     number1 = input(('Введите строку чисел, разделённых пробелом\n'))  # 4 4 44
#     if '#' in number1:  # если number1 содержит #, то завершить программу
#         break
#     if ' ' in number1:
#         number2 = number1.split()
#         number2 = [int(n) for n in number2]
#         print(sum(number2))
#     else:
#         print('r')

#  ------------------------------------------- вариант решения ---------------------------------------------------------

# def sum_num():
#     s = 0
#     while True:
#         in_list = input("Enter a number, input 'q' to exit: ").split()
#         for num in in_list:
#             if num == "q":
#                 return s
#             else:
#                 try:
#                     s += int(num)
#                 except (ValueError, SyntaxError):
#                     print("To exit the program, enter - 'q'.")
#         print(f"Sum of numbers = {s}")
#
# print(sum_num())

#  ------------------------------------------- вариант решения ---------------------------------------------------------

# def summary():
#     result = 0
#     while True:
#         print(f"Текущая сумма = {result}")
#         input_s = input("Введите строку чисел, разделенных пробелом для подсчета суммы (# - символ для завершения): ").split()
#         for value in input_s:
#             if value == "#":
#                 print(f"Окончательная сумма = {result}")
#                 break
#             try:
#                 result += float(value)
#             except ValueError:
#                 print(f"Значение {value} не было учтено при подсчете суммы - неверный тип")
#         else:
#             # если символа завершения программы не были то продолжаем ввод данных
#             continue
#         # сюда мы дойдем только если встретим символ завершения программы
#         break
#     return f"\nОкончательная сумма = {result}"
#
# summary()