class Bicycle:
    """
    Базовый класс для велосипеда
    """

    def __init__(self, type: str, material: str, year: int):
        """
        Инициализация велосипеда:
        :param type:     Название и тип велосипеда: "названи" + Городской/Горный/Шоссейный
        :param material: Материал рамы: Сталь/Карбон/Алюминий
        :param year:     Год выпуска
        """
        self._type = type  # Защищенный атрибут, доступен внутри класса и подклассов
        self.material = material
        self.year = year

    def __str__(self) -> str:
        """
        Возвращает строковое представление т/с
        """
        return f"{self.year} {self._type} {self.material}"

    def __repr__(self) -> str:
        """
        Возвращает строку, представляющую объект для разработчиков.
        """
        return f"Bicycle(type='{self._type}', material='{self.material}', year={self.year})"

    def turnon_lights(self) -> str:
        """
        Метод включения заднего фонарика
        """
        return "Задний фонарик включен"


class Kiddobike(Bicycle):
    """
    Дочерний класс для детских велосипедов
    """

    def __init__(self, type: str, material: str, year: int, wheels: int):
        """
        Расширенный конструктор для класса Kiddobike

        :param type:     Тип велосипеда: городской/горный/шоссейный
        :param material: Материал: сталь/карбон
        :param year:     Год выпуска
        :param wheels:   Количество колес
        """
        super().__init__(type, material, year)
        self.wheels = wheels

    def __str__(self) -> str:
        """
        Перегруженный метод __str__ для более детализированного описания.
        """
        return f"{self.year} {self._type} {self.material} ({self.wheels} колеса)"

    def __repr__(self) -> str:
        """
        Перегруженный метод __repr__.
        """
        return f"Car(type='{self._type}', material='{self.material}', year={self.year}, wheels={self.wheels})"

    def turnon_lights(self) -> str:
        """
        Перегруженный метод по добавлению дополнительного фонарика спереди помимо заднего.
        Причина перегрузки: необходимость обусловлена минимизацией риска того, что ребенок что-либо не заметит на дороге
        """
        return "Включен задний и передний фонарики"

    def bottle_holder(self) -> str:
        """
        Метод наличия крепления для бутылки с водой или иной жидкостью
        """
        return "Крепление для бутылки есть"


if __name__ == "__main__":
    bicycle = Bicycle("Canyon Grizl CF SL 7 Шоссейный", "Карбон", 2021)
    print(bicycle)  # Вывод: 2021 Canyon Grizl CF SL 7 Карбон 2021
    print(bicycle.turnon_lights())  # Вывод: Задний фонарик включен

    kiddobike = Kiddobike("Cube Acid 200 Горный", "Алюминий", 2025, 4)
    print(kiddobike)  # Вывод: 2022 Honda Civic (4 двери)
    print(kiddobike.turnon_lights())  # Вывод: Помимо заднего есть и передний фонарик
    print(kiddobike.bottle_holder())  # Вывод: Крепление для бутылки есть
