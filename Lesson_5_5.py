from random import randint

with open("sum_numbers.txt", "w", encoding="utf-8") as sn:
    list_n = [randint(1, 100) for _ in range(100)]
    sn.write(" ".join(map(str, list_n)))

print(sum(list_n))