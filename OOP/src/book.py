class Book:
    NBR_OF_BOOKS = 0
    def __init__(self, title, author, isbn, is_borrowed):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_borrowed = is_borrowed
        Book.NBR_OF_BOOKS += 1
    def get_details(self):
        print(f"Title: {self.__title}\nAuthor: {self.__author}\nISBN: {self.__isbn}\nBorrowed: {self.__is_borrowed}")
    def borrow_book(self):
        self.__is_borrowed = True
    def return_book(self):
        self.__is_borrowed = False