my_library = ["JAVA", "C", "C++", "Python", "Ruby", "Perl", "PHP", "HTML", "CSS", "JavaScript"] #Library books
print("Our Library books:", my_library)

new_book = input("Enter the name of the book to add:\n") #User to add a book
my_library.add(new_book)
print("After adding:", my_library)
if new_book in my_library:
    print(new_book,"Book added to library")
else:
    print("Book not added to library")

remove_book = input("Enter the name of the book to remove:\n") #User to remove a book
if remove_book in my_library:
    my_library.remove(remove_book)
    print(remove_book, "has been removed from the library.")
else:
    print("Book not found in the library.")
print("After removing:", my_library)

search_book = input("Enter the name of the book to search:\n") #User to search a book
if search_book in my_library:
    print(search_book,"Book found in the library")
else:
    print("Book not found")

print("Books available in the library:\n", my_library) #Show all books are in the library