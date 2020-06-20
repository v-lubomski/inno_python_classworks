#        Задание 5
# Создать класс, который хранит несколько аттрибутов:
# двуменрую матрицу из нулей и единиц
# список кортежей с координатами

# Реализовать метод который проходится по всем элементам матрицы
# и записывает в кортеж координаты с единицами


class Moon:

    matrix = []
    moon_tuple = []

    def __init__(self, matrix):
        self.matrix = matrix

    def input_in_tuple(self):
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                if self.matrix[row][col] == 1:
                    self.moon_tuple.append((row, col))


if __name__ == '__main__':
    matrix = [[1], [1], [0], [0], [1]]
    new_matrix = Moon(matrix)
    new_matrix.input_in_tuple()
    print(new_matrix.moon_tuple)
