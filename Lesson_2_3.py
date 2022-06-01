while True:
    month = input("Введите номер месяца от 1 до 12: ")
    if month.isdigit() and 0 < int(month) <= 12:
        season_1 = ["зима", "весна", "лето", "осень", "зима"]
        season_2 = {0: "зима", 1: "весна", 2: "лето", 3: "осень", 4: "зима"}
        print(f"Список сезонов - {season_1[int(month) // 3]}\nСловарь сезонов - {season_2[int(month) // 3]}")
        break
    else:
        print('Нет такого номера месяца')

# while True:
#     user_month = input('Введите номер месяца от 1 до 12: ')
#     if user_month.isdigit() and 0 < int(user_month) <= 12:
#         season_1 = ['зима', 'весна', 'лето', 'осень', 'зима']
#         season_2 = {0:'зима', 1:'весна', 2:'лето', 3:'осень', 4:'зима'}
#         print(f'Список сезонов - {season_1[int(user_month)//3]}\nСловарь сезонов - {season_2[int(user_month)//3]}')
#         break
#     else:
#         print('Ошибка')








# season_1 = ["зима", "весна", "лето", "осень", "зима"]
# season_2 = {0: "зима", 1: "весна", 2: "лето", 3: "осень", 4: "зима"}
#
# number = int(input("Введите номер месяца от 1 до 12: "))
# print(f"Список сезонов - {season_1[number//3]}\nСловарь сезонов - {season_2[number//3]}")


# while True:
#     user_month = input('Введите номер месяца от 1 до 12: ')
#     if user_month.isdigit() and 0 < int(user_month) <= 12:
#         season_2 = {0:'зима', 1:'весна', 2:'лето', 3:'осень', 4:'зима'}
#         print(f'Словарь сезонов - {season_2[int(user_month)//3]}')
#         break
#     else:
#         print('Ошибка')