class Book:
    """
    A class representing a book.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
    """

    def __init__(self, title, author):
        """
        Initializes a new instance of the Book class.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """Returns a string representation of the Book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    A class representing an electronic book, inheriting from Book.

    Attributes:
        file_size (int): The file size of the eBook in KB.
    """

    def __init__(self, title, author, file_size):
        """
        Initializes a new instance of the EBook class.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            file_size (int): The file size of the eBook in KB.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Returns a string representation of the EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    A class representing a printed book, inheriting from Book.

    Attributes:
        page_count (int): The number of pages in the printed book.
    """

    def __init__(self, title, author, page_count):
        """
        Initializes a new instance of the PrintBook class.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            page_count (int): The number of pages in the printed book.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Returns a string representation of the PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    A class representing a library, which manages a collection of books.

    Attributes:
        books (list): A list to store instances of Book, EBook, and PrintBook.
    """

    def __init__(self):
        """Initializes a new instance of the Library class."""
        self.books = []

    def add_book(self, book):
        """
        Adds a Book, EBook, or PrintBook instance to the library.

        Args:
            book (Book): An instance of Book, EBook, or PrintBook.
        """
        self.books.append(book)

    def list_books(self):
        """Prints details of each book in the library."""
        for book in self.books:
            print(book)
