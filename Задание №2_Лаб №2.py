BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages


# TODO написать класс Library
class Library:
    def __init__(self, books=None):
        if books is None:   #если при создании объекта класса аргумент букс не будет передан, то у него будет значение нон
            books = []      #проверка: если букс = нон, то создается пустой список
        self.books = books

    def get_next_book_id(self):
        if not self.books:                             #проверка пуст ли список
            return 1
        return max(book.id for book in self.books) + 1 #создается последовательность индентификаторов всех книг, находится наибольшее значение в списке, когда находим наибольшее значение, то прибавляем единицу, чтобы получить новый номер и добавить в библиотеку

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")




if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
