class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name  # Приватный атрибут, защищающий название книги от изменений
        self.author = author  # Приватный атрибут, защищающий имя автора от изменений

    @property
    def name(self) -> str:
        return self._name  # Геттер для name, запрещает его изменение

    @property
    def author(self) -> str:
        return self._author  # Геттер для author, запрещает его изменение

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)  # Вызов конструктора родительского класса для установки name и author
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages  # Геттер для pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")  # Валидация pages
        self._pages = value   # Присваиваем значение после проверки

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)  # Вызов конструктора родительского класса для установки name и author
        self.duration = duration  # Устанавливаем duration через свойство, чтобы сработала валидация

    @property
    def duration(self) -> float:
        return self._duration  # Геттер для duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")  # Валидация duration
        self._duration = float(value)

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

