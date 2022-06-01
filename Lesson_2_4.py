string = input('Введите несколько слов: ').split()
for ind, el in enumerate(string, start=1):
    print(f'{ind}) {el[:10]}')
