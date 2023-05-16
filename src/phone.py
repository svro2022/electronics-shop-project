from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Создание экземпляра класса phone (наследует атрибуты name, price, quantity от класса item).
                :param name: Название товара.
                :param price: Цена за единицу товара.
                :param quantity: Количество товара в магазине.
                :number_of_sim: Количество поддерживаемых сим-карт.
                """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """Магический метод __repr__ для отображения названия класса и объекте класса в режиме отладки"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    @property
    def number_of_sim(self):
        """Декоратор @property (геттер) делает атрибут __number_of_sim доступным извне"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int):
        """В сеттере @number_of_sim.setter проверяем, что количество SIM-карт должно быть целым числом больше нуля"""
        if not isinstance(value, int) or value < 1:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.__number_of_sim = value
