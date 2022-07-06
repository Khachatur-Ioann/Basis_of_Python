with open('subject.txt', 'r', encoding='utf8') as subject:
    list_subjects = subject.readlines()
    for el in list_subjects:  # el = 'Информатика: 100(л) 50(пр) 20(лаб).'
        new_str = ''.join((i if i in '1234567890' else ' ') for i in el)  # new_str: '             100    50     20      '
        new_2 = [int(i) for i in new_str.split()]
        print(f'{el.split()[0]} {sum(new_2)}')