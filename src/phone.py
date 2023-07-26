from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, num):
        self._number_of_sim = num
        if num <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self._number_of_sim})"

    def __add__(self, other):
        if isinstance(self, Phone) and isinstance(other, Phone):
            return int(self.quantity) + int(other.quantity)
        else:
            raise Exception
