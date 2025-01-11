import sys 
class Project: #Create the class 
    def __init__(self):
        self.books = ["Python","Java","C","C#","C++","JavaScript","HTML","CSS","PHP","SQL"] #Books Are available in our library.

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
        else:
            print("Book already exists")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print("Book not found")

    def list_books(self, *args):
        if len(args) == 0:
            return self.books
        else:
            return args

    def search_book(self, book):
        if book in self.books:
            return f"'{book}' is available in the library."
        else:
            return f"'{book}' is not available in the library."

my_library = Project()#Create a class

print("Our Library books:", my_library.list_books())#List the books

new_book = input("Enter the name of the book to add:\n")#User add a book
my_library.add_book(new_book)
print("After adding:", my_library.list_books())

remove_book = input("Enter the name of the book to remove:\n")#User to remove a book
my_library.remove_book(remove_book)
print("After removing:", my_library.list_books())

search_book = input("Enter the name of the book to search:\n")#User to search a book
print(my_library.search_book(search_book))

print("Books available in the library:\n", my_library.list_books())#Show all books are in the library

print("Do You Wants More Books?")#Do you Want more Books.
if input("Enter 'y' to add more books or 'n' to exit:\n") == "y":
    new_book = input("Enter the name of the book to add:\n")
    my_library.add_book(new_book)
    print("After adding:", my_library.list_books())

