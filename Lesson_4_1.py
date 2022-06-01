from sys import argv

name, hours, rub, bonus = argv
print(argv)
print(f'Расчет заработной платы: {(int(hours) * int(rub)) + int(bonus)}')