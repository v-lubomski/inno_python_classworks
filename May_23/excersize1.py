# Функция принимает слово из букв ABCDEF (кажд буква не более 2 раз)
# Я тестировщик. Нужно сгенерировать все возможные входные тестовые данные

# Задание1
# Поставлена задача подготовить тестовые случаи для программы,
# Программа находится в разработке и должна будет принимать слово составленное из букв A,B,C,D,E,F.
# Каждая буква может повторяться не более 2ух раз.
# Сгенерировать все возможные позитивные тестовые входные данные.
# Дополнить негативными тестовыми данными.
# Записать результат в файл.

from itertools import combinations_with_replacement

char_list = list('ABCDEF')
filename = 'test.txt'
data = []

for j in range(0, len(char_list) * 2 + 1):
    for i in list(combinations_with_replacement(char_list, j)):
        data.append(''.join(i))


def filter_func(lst):
    for k in lst:
        for p in char_list:
            if k.count(p) > 2:
                return False
            else:
                return True


data1 = list(filter(filter_func, data))


# with open(filename, 'w') as my_file:
#     my_file.write(data)
# print(data)

print(data1)
