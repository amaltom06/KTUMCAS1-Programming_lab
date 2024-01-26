# Create a class Publisher (name). Derive class Book from Publisher with attributes 
# title and author. Derive class Python from Book with attributes price and 
# no_of_pages. Write a program that displays information about a Python book. 
# Use base class constructor invocation and method overriding.

class Publisher:
 def __init__(self, name):
    self.name = name
class Book(Publisher):
 def __init__(self, name, title, author):
    super().__init__(name)
    self.title = title
    self.author = author
 def display_info(self):
    print("Publisher:", self.name)
    print("Title:", self.title)
    print("Author:", self.author)
class Python(Book):
 def __init__(self, name, title, author, price, no_of_pages):
    super().__init__(name, title, author)
    self.price = price
    self.no_of_pages = no_of_pages
 def display_info(self):
    super().display_info()
    print("Price:", self.price)
    print("Number of Pages:", self.no_of_pages)
publisher=input("Enter the name of publisher:")
book_name=input("Enter the name of book:")
author=input("Enter the name of author:")
book_price=input("Enter the price of book:")
book_pages=input("Enter the number of pages of the book:")
python_book = Python(publisher, book_name, author, book_price, book_pages)
python_book.display_info()