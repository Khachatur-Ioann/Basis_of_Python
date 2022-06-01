from itertools import count, cycle, islice
for n in count(3):
    if n > 10:
        break
    else:
        print(n)

lst_num = [n for n in range(3, 11)]
print(list(islice(lst_num, 8)))

c = 0
for el in cycle(['data', 123, True]):
    if c > 10:
        break
    else:
        print(el)
        c += 1

lst = ['data', 123, True]
isle_list = [el for el in islice(cycle(lst), 10)]
print(isle_list)

