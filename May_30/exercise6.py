#        Задание 6
# Для класса из задания 4 реализовать метод, который принимает коодринаты
# элемента матрицы и возвращает список координат.
# Если по указанным в параметре координатам находится единица —
# вeрнуть координаты всех единиц, которые находятся справа/слева/сверху/снизу
# от указанной.
# Пример.
# Исходная матрица [[0,1],[1,1]]
# Параметр для метода: (1,1)
# Метод при вызове вернёт [(1,0), (0,1)]


class Moon:

    matrix = []
    moon_tuple = []

    def __init__(self, data):
        self.matrix = data

    def input_in_tuple(self):
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                if self.matrix[row][col] == 1:
                    self.moon_tuple.append((row, col))

    def finder(self, coord: tuple) -> list:
        list_of_return_values = []
        if self.matrix[coord[0]][coord[1]] == 1:
            # вверх
            if coord[0] != 0:
                value = self.matrix[coord[0]-1][coord[1]]
                if value == 1:
                    list_of_return_values.append((coord[0]-1, coord[1]))
            # влево
            if coord[1] != 0:
                value = self.matrix[coord[0]][coord[1]-1]
                if value == 1:
                    list_of_return_values.append((coord[0], coord[1]-1))

        return list_of_return_values


if __name__ == '__main__':
    matrix = [[0, 1],
              [1, 1]]
    new_matrix = Moon(matrix)
    print(new_matrix.finder((1, 1)))
