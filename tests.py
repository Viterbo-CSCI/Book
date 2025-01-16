import unittest
from book import Book
from library import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment. 
        Create a Library instance and add some initial Book objects.
        """
        self.library = Library()
        self.book1 = Book("9780747532699", "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997)
        self.book2 = Book("9780743273565", "The Great Gatsby", "F. Scott Fitzgerald", 1925)

        # Add the books to the library
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    # TODO 1: Test adding a book
    def test_add_book(self):
        """
        Write a test to add a new book to the library.
        Use self.assertIn to check if the book was added successfully.
        """
        # Example:
        # book3 = Book("9780451524935", "1984", "George Orwell", 1949)
        # Add the book to the library
        # self.library.add_book(book3)
        # Assert that the book is now in the library
        # self.assertIn(book3, self.library)
        pass  # Replace with implementation

    # TODO 2: Test adding a duplicate book
    def test_add_duplicate_book(self):
        """
        Write a test to verify that adding a duplicate book raises a ValueError.
        Use self.assertRaises to check for the exception.
        """
        pass  # Replace with implementation

    # TODO 3: Test removing a book
    def test_remove_book(self):
        """
        Write a test to remove an existing book from the library.
        Use self.assertNotIn to ensure the book is removed.
        """
        pass  # Replace with implementation

    # TODO 4: Test removing a book that does not exist
    def test_remove_nonexistent_book(self):
        """
        Write a test to ensure that removing a non-existent book raises a ValueError.
        Use self.assertRaises to check for the exception.
        """
        pass  # Replace with implementation

    # TODO 5: Test the length of the library
    def test_length(self):
        """
        Write a test to check the number of books in the library using len().
        """
        pass  # Replace with implementation

    # TODO 6: Test iteration over the library
    def test_iteration(self):
        """
        Write a test to verify that iteration works as expected.
        Use a list comprehension to collect books from the library and compare them.
        """
        pass  # Replace with implementation

    # TODO 7: Test searching for books
    def test_search_books(self):
        """
        Write a test to search for books by a keyword.
        Verify that the correct books are returned as a list.
        """
        pass  # Replace with implementation

if __name__ == '__main__':
    unittest.main()
