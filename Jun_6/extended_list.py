# Задание 1 Реализовать операцию деления списка на число.
# Создайте класс, наследующий от list,
# в котором будет реализован метод деления списка на целое число частей.
# Ожидаемый результат:
# >>> my_list = BetterList([1,2,3,4,5,6,7,8,9,10,11,12])
# >>> my_list / 4
# ([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12])
# >>> my_list / 5
# ([1, 2], [3, 4], [5, 6], [7, 8], [9, 10, 11, 12])


class ExtendedList(list):

    def __truediv__(self, other):
        list_len = len(self)

        if isinstance(other, int) and list_len >= other > 0:

            piece_len = list_len // other
            last_piece = list_len % other
            start_index = 0
            end_index = piece_len
            output = list()

            for i in range(other):
                output.append(self[start_index:end_index])
                start_index = end_index
                end_index += piece_len

            if last_piece != 0:
                output[-1] = output[-1] + self[-last_piece:]

            return output

        else:
            raise Exception('Число, на которое делим, должно быть натуральным'
                            'числом не больше длины списка.')


ex_list = ExtendedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# print(ex_list / 14)
# print(ex_list / 0)
# print(ex_list / -2)
# print(ex_list / 'dsfsdf')
# print(ex_list / 234.32)
# print(ex_list / [3,3,4,])
