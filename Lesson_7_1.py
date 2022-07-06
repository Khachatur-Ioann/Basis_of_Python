a = [[5, 3, 1, 6], [4, 4, 4, 5], [9, 0, 5, 0]]
b = [[1, 1, 1, 2], [2, 2, 2, 2], [3, 3, 3, 1]]


class Matrix:
    def __init__(self, lists):  # передаем переменные a и b
        self.lists = lists  # атрибут объекта

    def __str__(self):
        return '\n'.join(map(str, self.lists))  # map() применяет str() к каждому значению в self.lists

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])  # lists[i][j] - j элемент i-го элемента
        return '\n'.join(map(str, c))

# создается объект класса Matrix, ссылка на который связывается с переменной a
matrix_1 = Matrix(a)  # передача данных, а именно передаем значение a в lists
matrix_2 = Matrix(b)  # передача данных, а именно передаем значение b в lists
print(f"Matrix 1\n"
      f"{matrix_1}\n"
      f"{'-' * 20}")
print(f"Matrix 2\n"
      f"{matrix_2}\n"
      f"{'-' * 20}")
print(f"matrix 1 + matrix 2\n"
      f"{matrix_1 + matrix_2}")