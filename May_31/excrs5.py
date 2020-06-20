# Задание 5
# Напишите рекурсивную функцию, проходящую по списку с неизвестными заранее
# элементами в поиске всех слов, начинающихся на А и выводом их на экран.
# Пример входных данных


my_data = ['Аниме', [0, 0, 0, 0, 0, [], [],
                     ['Аист', [1, 0, 0, 0, 1], 1, 1, 1, 1, 1, ["Арбуз"]]],
           'Астроном', {"1": [{'sdfg': 'Апостроф', 'Алхимия': 'Аргумент'}]}]

list_of_big_a = []


def finder_big_a_words(data):
    for el in data:
        if isinstance(el, dict):
            finder_big_a_words(list(el.items()))
        elif isinstance(el, list) or isinstance(el, tuple):
            finder_big_a_words(el)
        elif isinstance(el, str):
            if el[0] == 'А':
                list_of_big_a.append(el)
    return list_of_big_a


print(finder_big_a_words(my_data))
