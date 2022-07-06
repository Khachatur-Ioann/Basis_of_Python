with open("out_file.txt", "r", encoding='utf-8') as out_f:
    useful = [f'{count}. {line.strip()} - {len(line.split())} слов'
              for count, line in enumerate(out_f, 1)]
    print(*useful, f"Всего строк - {len(useful)}.", sep="\n")  # * - распаковка итерируемых объектов в списке