class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def book_info(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"


book1 = Book(title="Harry Potter",author="J.K. Rowling",price="499")
book2 = Book(title="Atomic Habits",author="James Clear",price="350")
print(book1.book_info())
print(book2.book_info())