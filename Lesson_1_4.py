number = int(input("Введите целое положительне число: "))
maximum = 0
number_rest = number

while number_rest > 0:
    rest = number_rest % 10
    if rest > maximum:
        maximum = rest
        if maximum == 9:
            break
    number_rest = number_rest // 10
print(f"Максимальная цифра в числе {number} равна {maximum}")


# Функция с рекурсией

def num_max(num):
    if num < 10:
        return num
    else:
        m = num_max(num // 10)
        return m if m > num % 10 else num % 10

print(f"The largest number is: {num_max(int(input('Enter the number: ')))}")



