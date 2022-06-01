from random import randint
numbers = [randint(0, 20) for i in range(10)]
print(numbers)
numbers = [number for number in numbers if numbers.count(number) == 1]
print(numbers)

numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
numbers = [number for number in numbers if numbers.count(number) == 1]
print(numbers)

numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []
for number in numbers:
    if numbers.count(number) == 1:
        result.append(number)
print(result)