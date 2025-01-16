class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author} ({self.year}) - ISBN: {self.isbn}"

    def __eq__(self, other):
        """Books are equal if their ISBNs match."""
        if isinstance(other, Book):
            return self.isbn == other.isbn
        return False

    def __hash__(self):
        """Enable books to be used in sets or dictionaries."""
        return hash(self.isbn)
