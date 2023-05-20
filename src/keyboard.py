from src.item import Item


class MixinLog:
    """
    Mixin-класс для метода change_lang
    """

    def __init__(self, language="EN"):
        self.__language = language

    @property
    def language(self):
        """Декоратор @property (геттер) делает атрибут __language доступным извне"""
        return self.__language

    @language.setter
    def language(self, data):
        """В сеттере @language.setter проверяем, что язык может быть только EN или RU"""
        self.__language = data
        if self.__language != "EN" or self.__language != "RU":
            raise AttributeError("AttributeError: property 'language' of 'Keyboard' object has no setter")

    def change_lang(self):
        """
        Метод изменения языка с EN на RU
        """
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self


class Keyboard(Item, MixinLog):
    """
    Класс Keyboard (наследование от Item, MixinLog)
    """
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Метод инициализации объекта класса Keyboard
        name: имя
        price: цена
        quantity: количество товара в магазине
        language: язык клавиатуры, по умолчанию EN
        """
        super().__init__(name, price, quantity)
        MixinLog.__init__(self)
