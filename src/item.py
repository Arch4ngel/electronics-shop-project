import csv
import os
import math


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    def __add__(self, other):
        if isinstance(self, Item) and isinstance(other, Item):
            return int(self.quantity) + int(other.quantity)
        else:
            raise TypeError('Данные объекты невозможно сложить')

    @property
    def name(self):
        """
        Возвращает имя сотрудника
        """
        return self.__name

    @name.setter
    def name(self, data_string):
        """
        Метод срабатывает при операции присваивания
        """
        name = data_string[:10]
        self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        """
        Инициализация класса из CSV
        """
        cls.all = []
        with open(os.path.join(os.path.dirname(__file__),
                  'items.csv'), newline='', encoding='WINDOWS-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(num_string):
        """
        Возвращает число из строки
        """
        return math.floor(float(num_string))
