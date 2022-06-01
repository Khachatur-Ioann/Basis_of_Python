while True:
    days = 1
    start_km = float(input("Стартовый результат: "))
    last_km = float(input("Финальный результат: "))
    if start_km <= 0 or last_km < 0:
        print("Результаты должны быть больше нуля. Стартовое значение != 0.")
    else:
        while start_km < last_km:
            start_km += start_km * 0.1
            days += 1
        print(f"Спортсмен добьется результат за {days} дней")
        break

# first_result = int(input("Введите результат первого дня: "))
# last_result = int(input("Введите результат последнего дня: "))
# everyday_result = first_result
# days = 1
#
# while True:
#     if everyday_result > last_result:
#         break
#     everyday_result = everyday_result * 1.1
#     days += 1
#
# print(f"На {days} день спортсмен достиг результата - не менее {everyday_result} км")


# days = 1
# a = 2
# b = 3
# c = a
#
# while True:
#     if c > b:
#         break
#     c = c * 1.1
#     days += 1
#
# print(f"На {days} день спортсмен достиг результата - не менее {b} км")


# a = int(input("Введите сколько км пробежал спортсмен в первый день: "))
# b = int(input("Результат спортсмена, км: "))
# c = int(1)
#
# while a <= b:
#     c += 1
#     a = a * 1.1
#
# print("На", c, "день спортсмен достиг результата — не менее", b, "км")
#
#
# # Функция с рекурсией
# def km(res_min, res_max, days):
#     if res_min > res_max:
#         return days
#     else:
#         return km(res_min * 1.1, res_max, days + 1)
#
#
# print(km(int(input("Enter first param ")), int(input("Enter second param ")), 1))
