# решение 1
out_f = open("out_file.txt", "w", encoding='utf-8')
user_input = out_f.write(input(f'Введите данные: '))
out_f.write(f'{user_input}\n')
out_f.close()

# решение 2
out_f = open("out_file.txt", "w", encoding='utf-8')
user_input = input(f'Введите данные: ')
print(user_input, file=out_f)
out_f.close()

# решение 3
with open("out_file.txt", "w", encoding='utf-8') as out_f:
    user_input = input(f'Введите данные: ')
    print(user_input, file=out_f)

# решение 4
with open("out_file.txt", "w", encoding='utf-8') as out_f:
    print('One — 1\nTwo — 2\nThree — 3\nFour — 4\n', file=out_f)



