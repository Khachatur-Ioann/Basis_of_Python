my_list = list(input('Введите числа без пробелов - '))

# для элемента(ов) i в my_list с 1 по конечный с шагом два выполнить:
for i in range(1, len(my_list), 2):
    # обмен значений соседних элементов, где нулевой элемент становится на место первого и наоборот
    # и так повторяется для каждого второго элемента, начиная с 1
    # соответственно последний нечетный элемент не будет обменен, поскольку мы задали шаг 2
    my_list[i-1], my_list[i] = my_list[i], my_list[i-1]  # 0, 1 = 1, 0
    # значению под индексом 0 присваиваем значение под индексом 1 и наоборот
print(my_list)

# a = input('Введите элементы для массива разделяя их пробелами: ').split()
# i = 0  # счетчик элементов
# print(f'Оригинальный список {a}')  # список из введенных элементов
# while i + 1 < len(a):  # цикл будет выполняться по каждому элементу, кроме последнего
#     if i % 2 == 0:  # если остаток номера элемента от деления на два равен нулю
#         a.insert(i, a.pop(i + 1))  # тогда меняем местами
#     i += 1
# print(f'Измененный список {a}')

# user_list = input('Введите числа с пробелами - ').split()
# for i in range(1, len(user_list), 2):
#     user_list.insert(i-1, user_list.pop(i))
# print(user_list)

# string = "abrakadabra"
# str_reverse = ''
# symbols = list(string)
# for el in range(len(string) // 2):
#     tmp = symbols[el]
#     symbols[el] = symbols[len(string) - el - 1]
#     symbols[len(string) - el - 1] = tmp
# str_reverse = ''.join(symbols)
# print(str_reverse)

# var_1, var_2 = 20, 30
# print(var_1, var_2)
# var_1, var_2 = var_2, var_1
# print(var_1, var_2)
