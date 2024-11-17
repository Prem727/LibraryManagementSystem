class Library:
    def __init__(self):
        # Dictionary to store books with status (True if available)
        self.books = {}

    def add_book(self, book_name):
        """Adds a book to the library."""
        if book_name in self.books:
            print(f"'{book_name}' already exists in the library.")
        else:
            self.books[book_name] = True
            print(f"'{book_name}' has been added to the library.")

    def view_books(self):
        """Displays all the books in the library with their status."""
        if not self.books:
            print("The library is empty.")
            return

        print("\nBooks in the library:")
        for book, available in self.books.items():
            status = "Available" if available else "Borrowed"
            print(f" - {book} ({status})")

    def borrow_book(self, book_name):
        """Allows a user to borrow a book if it is available."""
        if book_name not in self.books:
            print(f"'{book_name}' is not available in the library.")
        elif not self.books[book_name]:
            print(f"'{book_name}' is currently borrowed.")
        else:
            self.books[book_name] = False
            print(f"You have borrowed '{book_name}'.")

    def return_book(self, book_name):
        """Allows a user to return a borrowed book."""
        if book_name not in self.books:
            print(f"'{book_name}' does not belong to this library.")
        elif self.books[book_name]:
            print(f"'{book_name}' was not borrowed.")
        else:
            self.books[book_name] = True
            print(f"Thank you for returning '{book_name}'.")
