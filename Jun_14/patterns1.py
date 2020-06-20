# ПО для конвейера по сборке БПЛА

from abc import ABC, abstractmethod


class Uav(ABC):

    @abstractmethod
    def speed(self):
        pass


class UavFactory(ABC):
    def create_uav(self):
        pass
