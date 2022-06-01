revenue = int(input("Введите сумму выручки: "))
costs = int(input("Введите сумму издержек: "))
profit = revenue - costs

if revenue > costs:
    print(f"Прибыль равна {profit} рублей")
    print(f"Рентабельность выручки составляет {100 * profit / revenue:.1f}%")
    personel = int(input("Введите число сотрудников: "))
    print(f"Прибыль фирмы в расчете на одного сотрудника: {profit / personel:.1f} рублей")
else:
    print("Убыток")
