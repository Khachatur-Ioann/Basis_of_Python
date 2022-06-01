def my_func(x, y):
    try:
        number = x ** y
    except (ValueError, TypeError):
        return 'Введите действительное положительное число и целое отрицательное число y'
    return f'{number: .30f}'

print(my_func(5.0, -5))


def my_func(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return 'x должен быть больше 0, y должен быть меньше 0'
        else:
            x_1 = 1 / x
            y_1 = abs(y)
            x_2 = x_1
            iteracia = 1
            while iteracia < y_1:
                x_2 *= x_1
                iteracia += 1
            return f'{x_2:.5f}'
    except (ValueError, TypeError):
        return 'Введите числа'

num_1 = input('Введите действительное положительное число: ')
num_2 = input('Введите целое отрицательное число: ')
print(my_func(num_1, num_2))