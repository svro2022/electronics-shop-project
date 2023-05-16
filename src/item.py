import csv


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
        self.all.append(self)

    def __repr__(self):
        """Магический метод __repr__ для отображения названия класса и объекте класса в режиме отладки"""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Магический метод __str__ для отображения информации об объекте класса для пользователей"""
        return f"{self.__name}"

    def __add__(self, other):
        """Магический метод __add__ для сложения экземпляров класса.
        isinstance(other, Item) - проверяет принадлежность объекта к классу Item"""
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise AssertionError("Сложение возможно только для экземпляров Item и Phone")

    @property
    def name(self):
        """Декоратор @property (геттер) делает атрибут __name доступным извне"""
        return self.__name

    @name.setter
    def name(self, value):
        """В сеттере @name.setter проверяем, что длина наименования товара не больше 10 символов"""
        self.__name = value
        if len(value) <= 10:
            self.__name = value
        else:
            raise ValueError("Длина наименования товара превышает 10 символов.")
            # print("Ошибка! Длина наименования товара больше 10 символов")

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
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_path='../src/items.csv'):
        """
        Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv
        """
        cls.all.clear()
        with open(file_path, 'r', encoding='windows-1251') as file:
            file_reader = csv.DictReader(file, delimiter=',')

            for value in file_reader:
                name, price, quantity = value.values()
                cls(name, cls.string_to_number(price), cls.string_to_number(quantity))

    @staticmethod
    def string_to_number(number):
        """
        Статический метод, возвращающий число из числа-строки
        """
        return int(float(number))
