import json

with open("my_ex7.json", "w", encoding="utf-8") as write_f, \
     open("text_7.txt", encoding="utf-8") as f_obj:
    # создание и запись в my_ex7.json, чтение файла text_7.txt
    profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_obj}
    # посчитали прибыль по каждой строке (фирме), profit = {'firm_1': 5000, 'firm_2': 15000, 'firm_3': 3000}
    f_up = [i for i in profit.values() if i > 0]  # f_up = [5000, 15000, 3000]
    # profit.values() == dict_values([5000, 15000, 3000]), при условии что элемент больше 0, записывать его в f_up
    result = [profit, {"average_profit": round(sum(f_up) / len(f_up))}]
    # записываем в result собственно то что будет в файле

    json.dump(result, write_f, ensure_ascii=False, indent=4)
    # result - что отправляем, write_f - куда отправляем
