while True:
    def my_func():
        try:
            var_1 = int(input())
            var_2 = int(input())
            var_3 = int(input())
            my_list = [var_1, var_2, var_3]
            my_list.remove(min(my_list))
            return sum(my_list)
        except ValueError:
            return 'Введите числа'
    print(my_func())