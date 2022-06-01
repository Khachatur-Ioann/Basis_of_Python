from functools import reduce

def my_func(n_1, n_2):
    return n_1 * n_2

even_numbers = [n for n in range(100, 1001, 2)]
print(reduce(my_func, even_numbers))