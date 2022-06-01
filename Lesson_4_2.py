from random import randint
lst = [randint(0, 1000) for i in range(10)]
max2_lst = [lst[i] for i in range(1, len(lst)) if lst[i] > lst[i-1]]
print(lst)  # привел для наглядности, чтобы проверить
print(f'{max2_lst} - элементы исходного списка, значения которых\n '
      f'больше предыдущего элемента')