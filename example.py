from book import Book
from library import Library

# Create a library instance
library = Library()

# Add books to the library
book1 = Book("9780747532699", "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997)
book2 = Book("9780743273565", "The Great Gatsby", "F. Scott Fitzgerald", 1925)

library.add_book(book1)
library.add_book(book2)

# Display books in the library
print(f"Number of books: {len(library)}")
print("Books in library:")
for book in library:
    print(book)

# Search for books by keyword
print("\nSearch results:")
for book in library.search_books("Harry"):
    print(book)

# Remove a book
library.remove_book("9780747532699")
print(f"\nAfter removing, number of books: {len(library)}")
