my_list = [int(10), 1.2, (5+6j), 'string', [list], {1},
           tuple('tuple'), {'key_1': 'val_1'}, True, b'text',
           bytearray(b"some text"), None]
for el in my_list:
    print(type(el))

# второй вариант решения
for ind, el in enumerate(my_list, 1):
    print(f'{ind} {el} - {type(el)}')
