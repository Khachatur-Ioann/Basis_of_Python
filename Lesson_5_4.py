rus_words = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("rus.txt", "w", encoding='utf-8') as rus:
    with open("out_file.txt", encoding='utf-8') as eng:
        rus.writelines([line.replace(line.split()[0],
                                     rus_words.get(line.split()[0]))
                        for line in eng])