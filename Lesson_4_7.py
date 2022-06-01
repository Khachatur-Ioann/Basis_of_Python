def fact_gen(number):  # функция и его аргумент number
    f_num = 1  # счетчик чисел от 1! до number!
    for i in range(number + 1):
        # цикл с последовательностью чисел согласно
        # введенному факториалу числа
        yield f'{i}! = {f_num}'
        # возврат генерации чисел,
        # возвращение по частям
        f_num *= i + 1

for el in fact_gen(int(input('Factorial number: '))):
    # взаимодействие с результатом, работаем снаружи через цикл
    print(el)


