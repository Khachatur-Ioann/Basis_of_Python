time = int(input("Введите время в секундах:"))
hours = time // 3600
minutes = time // 60 - 60 * hours
seconds = time % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")


in_put = int(input("Введите время в секундах: "))

hours = in_put // 3600
minutes = in_put % 3600 // 60
seconds = in_put % 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")