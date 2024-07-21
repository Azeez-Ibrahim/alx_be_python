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
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")