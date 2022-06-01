# nice Hdол Отл cool
# Nice Cool

def int_func():
    for word in input("Enter words with a space(lower latin script):\n").split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
        print(word.title() if chars == len(word) else f"{word} - only small English letters!")

int_func()


# int_func = lambda word: word.title() if word.islower() and ascii(word)[1:-1].isalpha() else ''
# print(' _ '.join(map(int_func, input("Enter phrase: ").split())))


# def int_func(word):
#     latin_char = 'qwertyuiopasdfghjklzxcvbnm'
#     return word.title() if not set(word).difference(latin_char) else False
#
# words = input('Введите строку из слов разделнных пробелом: ').split()
# for w in words:
#     result = int_func(w)
#     if result:
#         print(int_func(w), ' ')


# моя попытка решить
# def int_func():
#     latin = input('Введите слова: ')
#     # перевести каждый элемент в каждом слове в ord
#     new_latin = ""
#     for letter in latin:
#         letter = str(ord(letter))
#         new_latin = new_latin + letter + " "
#         print(new_latin)
#     # latin_2 = []
#     # return latin.title()
# int_func()
# # print(type(int_func()))

