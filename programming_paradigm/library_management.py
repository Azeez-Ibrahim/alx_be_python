class Book:
    def __init__(self, title, author):
        """
        Initialize a Book object with a title, author, and a checked-out status.

        Parameters:
        title (str): The title of the book.
        author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False


class Library:
    def __init__(self):
        """Initialize a Library object with an empty list of books."""
        self._books = []

    def add_book(self,book):
        """
        Add a Book object to the library's collection.

        Parameters:
        book (Book): The book to be added.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Attempt to check out a book by its title.

        Parameters:
        title (str): The title of the book to be checked out.

        Returns:
        bool: True if the book was successfully checked out, False otherwise.
        """
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                return True
        return False

    def return_book(self):
        """
        Attempt to return a book by its title.

        Returns:
        bool: True if the book was successfully returned, False otherwise.
        """
        for book in self._books:
            if book._is_checked_out:
                book._is_checked_out = False
                return True
        return False

    def list_available_books(self):
        """List all books that are currently available (not checked out)."""
        if self._books:
            for book in self._books:
                if not book._is_checked_out:
                    print(f"{book.title} by {book.author}")
