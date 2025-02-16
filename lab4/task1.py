# -*- coding: utf-8 -*-
class Food:
    """
    Базовый класс для еды.
    """
    name: str
    _calories: int
    price: float

    def __init__(self, name: str, calories: int, price: float) -> None:
        """
        Инициализация продукта.
        :param name: Название продукта
        :param calories: Количество калорий
        :param price: Цена продукта
        """
        self.name = name
        self._calories = calories
        self.price = price

    @property
    def calories(self) -> int:
        return self._calories

    def __str__(self) -> str:
        return f"{self.name} (Калории: {self._calories}, Цена: {self.price} руб.)"

    def __repr__(self) -> str:
        return f"Food(name={self.name!r}, calories={self._calories!r}, price={self.price!r})"

    def consume(self) -> str:
        """
        Абстрактный метод, должен быть переопределен в дочерних классах.
        """
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе")


class Fruit(Food):
    """
    Класс для фруктов.
    """
    is_citrus: bool

    def __init__(self, name: str, calories: int, price: float, is_citrus: bool) -> None:
        """
        Инициализация фрукта.
        :param is_citrus: Является ли цитрусовым
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
        return f"{self.name} можно съесть в свежем виде."


class Meat(Food):
    """
    Класс для мяса.
    """
    is_cooked: bool

    def __init__(self, name: str, calories: int, price: float, is_cooked: bool) -> None:
        """
        Инициализация мяса.
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
        return f"{self.name} можно съесть в зависимости от способа приготовления."


if __name__ == "__main__":
    apple = Fruit("Яблоко", 52, 100.0, False)
    steak = Meat("Стейк", 250, 500.0, True)
