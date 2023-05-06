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


    """Декоратор @property (геттер) делает атрибут __name доступным извне"""
    @property
    def name(self):
        return self.__name

    """В сеттере @name.setter проверяем, что длина наименования товара не больше 10 символов"""
    @name.setter
    def name(self, value):
        self.__name = value
        if len(value) <= 10:
            self.__name = value
        else:
            raise ValueError("Длина наименования товара превышает 10 символов.")
            #print("Ошибка! Длина наименования товара больше 10 символов")


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

