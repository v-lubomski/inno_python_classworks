# ​ Задание 2
# Создать класс, расширяющий функционал словаря
# через множественное наследование.

# У словаря должен быть метод,
# проверяющий все его ключи на соответствие регулярному выражению.
# Ожидаемый результат:
# >>> regular_expression = "^[a-z]{3}[0-9]+$"
# >>> d1 = DictWithVerifier({"abc1" : "some value", "asdf" : "121321"})
# >>> d1.check_keys_against_regex(regular_expression)
# Exception: Ключ asdf не подходит по условию
# Ожидается, что класс DictWithVerifier наследуется от двух классов.
# Один из этих классов — слов


class Checker:
    pass


class Child(dict, Checker):
    pass

