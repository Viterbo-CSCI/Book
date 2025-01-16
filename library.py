from collections.abc import Collection

class Library(Collection):
    def __init__(self):
        self._books = {}  # Dictionary to store books by ISBN

    def add_book(self, book):
        """Adds a Book object to the library using its ISBN as the key."""
        if book.isbn not in self._books:
            self._books[book.isbn] = book
        else:
            raise ValueError(f"Book with ISBN '{book.isbn}' already exists in the library.")

    def remove_book(self, isbn):
        """Removes a Book object from the library by its ISBN."""
        if isbn in self._books:
            del self._books[isbn]
        else:
            raise ValueError(f"No book with ISBN '{isbn}' found in the library.")

    def __iter__(self):
        """Allows iteration over the books."""
        return iter(self._books.values())

    def __len__(self):
        """Returns the number of books in the library."""
        return len(self._books)

    def __contains__(self, book):
        """Checks if a Book object is in the library by its ISBN."""
        return book.isbn in self._books

    def search_books(self, keyword):
        """Returns a list of books whose title or author contains the keyword."""
        return [
            book for book in self._books.values()
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()
        ]
