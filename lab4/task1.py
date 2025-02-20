# -*- coding: utf-8 -*-
class Food:
    """
    Базовый класс для еды.
    Атрибуты:
        name (str): Название продукта.
        _calories (int): Количество калорий. Защищенный атрибут, так как калории
                     не должны изменяться напрямую без проверки.
        price (float): Цена продукта.
    """
    name: str
    _calories: int
    price: float

    def __init__(self, name: str, calories: int, price: float) -> None:
        """
        Инициализация продукта.
        :param name: Название продукта.
        :param calories: Количество калорий.
        :param price: Цена продукта.
        """
        self.name = name
        self._calories = calories
        self.price = price

    @property
    def calories(self) -> int:
        """
        Получение количества калорий.
        :return: Количество калорий.
        """
        return self._calories

    def __str__(self) -> str:
        return f"{self.name} (Калории: {self._calories}, Цена: {self.price} руб.)"

    def __repr__(self) -> str:
        return f"Food(name={self.name!r}, calories={self._calories!r}, price={self.price!r})"

    def prepare(self) -> str:
        """
        Метод для подготовки продукта к употреблению.
        :return: Сообщение о подготовке.
        """
        return f"{self.name} готов к употреблению."

    def consume(self) -> str:
        """
        Метод для употребления продукта.
        :return: Сообщение о том, как употреблять продукт.
        """
        return f"{self.name} можно съесть."


class Fruit(Food):
    """
    Класс для фруктов.
    Атрибуты:
        is_citrus (bool): Является ли фрукт цитрусовым.
    """
    is_citrus: bool

    def __init__(self, name: str, calories: int, price: float, is_citrus: bool) -> None:
        """
        Инициализация фрукта.
        :param name: Название фрукта.
        :param calories: Количество калорий.
        :param price: Цена фрукта.
        :param is_citrus: Является ли фрукт цитрусовым.
        """
        super().__init__(name, calories, price)
        self.is_citrus = is_citrus

    def __str__(self) -> str:
        citrus_info = "цитрусовый" if self.is_citrus else "не цитрусовый"
        return f"{self.name} (Калории: {self.calories}, Цена: {self.price} руб., {citrus_info})"

    def __repr__(self) -> str:
        return (f"Fruit(name={self.name!r}, calories={self.calories!r}, "
                f"price={self.price!r}, is_citrus={self.is_citrus!r})")

    def consume(self) -> str:
        """
        Перегрузка метода consume для фруктов
        :return: Сообщение , как есть фрукт
        """
        return f"{self.name} можно съесть в свежем виде."

    def peel(self) -> str:
        """
        Метод для очистки фрукта
        :return: Сообщение о том , что фрукт очищен
        """
        return f"{self.name} очищен."


class Meat(Food):
    """
    Класс для мяса.
    Атрибуты:
        is_cooked (bool): Приготовлено ли мясо.
    """
    is_cooked: bool

    def __init__(self, name: str, calories: int, price: float, is_cooked: bool) -> None:
        """
        Инициализация мяса
        :param name: Название
        :param calories: Калории
        :param price: Цена мяса
        :param is_cooked: Приготовлено ли мясо
        """
        super().__init__(name, calories, price)
        self.is_cooked = is_cooked

    def __str__(self) -> str:
        cooked_info = "приготовленное" if self.is_cooked else "сырое"
        return f"{self.name} (Калории: {self.calories}, Цена: {self.price} руб., {cooked_info})"

    def __repr__(self) -> str:
        return (f"Meat(name={self.name!r}, calories={self.calories!r}, "
                f"price={self.price!r}, is_cooked={self.is_cooked!r})")

    def consume(self) -> str:
        """
        Перегрузка метода consume для мяса
        :return: Сообщение о том, как употреблять мясо
        """
        if self.is_cooked:
            return f"{self.name} можно съесть, так как оно приготовлено."
        else:
            return f"{self.name} нельзя съесть, так как оно сырое."

    def cook(self) -> str:
        """
        Метод для приготовления мяса.
        :return:  cообщение о том, что мясо приготовлено
        """
        self.is_cooked = True
        return f"{self.name} приготовлено."


if __name__ == "__main__":
    apple = Fruit("Яблоко", 52, 100.0, False)
    steak = Meat("Стейк", 250, 500.0, True)
