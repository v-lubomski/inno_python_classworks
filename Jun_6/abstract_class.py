# ​ Задание 3
# Напишите один абстрактный и один отнаследованный от него обычный класс
# для видов носимых мобильных устройств.


from abc import ABC


class Goods(ABC):
    price = 0
    shop_address = ''

    def __init__(self, price, shop):
        self.price = price
        self.shop_address = shop


class CellPhones(Goods):
    pass
