with open('my_file.txt', 'r', encoding='utf-8') as my_file:
    my_file = {line.split()[0]: float(line.split()[1]) for line in my_file}
    # привели ко множеству, чтобы можно было работать с файлом
    # {'Иванов': 23543.12, 'Петров': 13749.32, 'Сидоров': 14986.99, 'Мовсесян': 30009.87,
    # 'Христов': 45987.09, 'Агапкин': 34000.78, 'Сладков': 66005.11,
    # 'Кудаков': 15098.23, 'Жданов': 19876.78, 'Невзоров': 12004.45}

    print(f'Кто из сотрудников имеет оклад менее 20 тысяч - \n'
          f'{[line[0] for line in my_file.items() if line[1] < 20000]}')
    print(f'Средняя величина дохода сотрудников = '
          f'{round(sum(my_file.values()) / len(my_file), 3)}\n')


# with open('text_3.txt', 'r', encoding='utf-8') as f:
#     employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
#     print(f'Average salary = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
#           f'Employees with salary less than 20k {[e[0] for e in employees_dict.items() if e[1] < 20000]}')