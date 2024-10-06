# library_management.py

class Book:
    """Represents a book with a title, author, and its availability status."""
    
    def __init__(self, title, author):
        """Initialize a book with title, author, and availability."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track if the book is checked out

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available (not checked out)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is available for checkout."""
        return not self._is_checked_out

    def __str__(self):
        """Return a user-friendly string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """Represents a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title, if it is available."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"{title} has been checked out.")
                    return
                else:
                    print(f"{title} is already checked out.")
                    return
        print(f"{title} is not in the library.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"{title} has been returned.")
                    return
                else:
                    print(f"{title} was not checked out.")
                    return
        print(f"{title} is not in the library.")

    def list_available_books(self):
        """List all books that are available for checkout."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books are available.")
