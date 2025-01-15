import doctest


class Window:
    def __init__(self, window_amount: float, window_handle: float):
        """
        Создание и подготовка к работе объекта "Окно"

        :param window_amount: количество окон
        :param window_handle: число оконных ручек

        Примеры:
        >>> window = Window(1, 2)  # инициализация экземпляра класса
        """
        if not isinstance(window_amount, (int, float)):
            raise TypeError("Количество окон быть типа int или float")
        if window_amount <= 0:
            raise ValueError("Количество окон должно быть положительным числом")
        self.window_amount = window_amount

        if not isinstance(window_handle, (int, float)):
            raise TypeError("Количество оконных ручек должно быть int или float")
        if window_handle < 1:
            raise ValueError("Количество оконных ручек не может быть оменьше одного, тк не открыть/закрыть окно")
        self.window_handle = window_handle

    def is_window_installed(self) -> bool:
        """
        Функция которая проверяет есть ли окно

        :return: Окна нет

        Примеры:
        >>> window = Window(1, 2)
        >>> window.is_window_installed()
        """
        ...

    def add_curtains_to_window(self, curtains: float) -> None:
        """
        Добавление штор.
        :param curtains: Количество добавляемых штор

        :raise ValueError: Если количество добавляемых штор превышает свободное место на карнизе, то вызываем ошибку

        Примеры:
        >>> window = Window(1, 2)
        >>> window.add_curtains_to_window(1)
        """
        if not isinstance(curtains, (int, float)):
            raise TypeError("Шторы должны быть типа int или float")
        if curtains < 0:
            raise ValueError("Количество штор должно быть больше 0, чтобы не было светло")
        if curtains > 2:
            raise ValueError("Количество штор должно быть меньше 2, тк это максимальное количество штор, помещающихся на карниз")
        ...

    def remove_curtain_from_window(self, curtain: float) -> None:
        """
        Убрать шторы с карниза спустя месяц.

        :param curtain: количество убираемых штор
        :raise ValueError: Если убрать шторы больше, чем висит, то возвращается ошибка.

        :return: количесвто убранных штор

        Примеры:
        >>> window = Window(1, 2)
        >>> window.remove_curtain_from_window(2)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
