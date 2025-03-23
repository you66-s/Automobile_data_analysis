class Library:
    def __init__(self, books):
        self.__books = books

    def add_book(self, book):
        self.__books.append(book)
    def display_books(self):
        for book in self.__books:
            print(book.get_details())