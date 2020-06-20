# Задание 1 Напишите функцию, создающую словарь из 9 случайных строковых ключей и значений.
# Воспользуйтесь модулями random и string.

# Задание 2 Напишите или дополните существующую функцию,
# которая бы по случайному с один из случайных ключей записывала значение другого сгенерированного словаря
# из 9 случайных пар ключ-значение.
# уровень вложенности - 3
# { "a" : "b", "b" : "c", "c" : { "d" : "e", "f" : "g", "h" : { "k": "l", "m" : "n", "o" : "p" }

import random
import string
from pprint import pprint

alph = string.ascii_letters


def gen_random_string() -> str:
    random_string = ''
    for i in range(random.randint(1, 10)):
        random_string += random.choice(alph)
    return random_string


def gen_dict() -> dict:
    some_dict = dict()
    for i in range(9):
        some_dict[gen_random_string()] = gen_random_string()
    return some_dict


def add_dict_to_dict(some_dict: dict) -> dict:
    dict_keys = list(some_dict.keys())
    random_key = dict_keys[random.randint(0, len(some_dict) - 1)]
    some_dict[random_key] = gen_dict()
    return some_dict


somehow_dict = gen_dict()
pprint(somehow_dict)
print('\n')
pprint(add_dict_to_dict(somehow_dict))


# реализовать вложенность 3