class Book: 

    def __init__(self, book_id, book_title, author, pages):

        self.book_id = book_id
        self.book_title = book_title
        self.author = author 
        self.pages = pages

    def get_total_pages(self):
        return self.pages

class ReadingProcess:

    def __init__(self, book, current_page=1):
        
        self.book = book
        self.current_page = current_page
    
    def update_page(self, page):

        if page < 1 or page > self.book.get_total_pages():
            raise ValueError("Invalid page number.")

        self.current_page = page

class Library:

    def __init__(self):

        self.books = {}

    def add_book(self, book):
        
        self.books[book.book_id] = book
    
    def get_book(self, book_id):

        return self.books.get(book_id)

class User:

    def __init__(self, user_id, name):

        self.user_id = user_id
        self.name = name
        self.progress = {}

    def start_reading(self, book):

        if book.book_id not in self.progress:
            self.progress[book.book_id] = ReadingProcess(book)
    
    def update_progress(self, book_id, page):

        progress = self.progress.get(book_id)

        if progress is None:
            raise ValueError("User has not started this book.")
        
        progress.update_page(page)

    def get_active_books(self):
        return self.progress.values()

    def open_book(self, book_id):

        progress = self.progress.get(book_id)

        if progress is None:
            raise ValueError("Book is not active")

        return progress.current_page



def main():

    library = Library()

    book1 = Book(1, "1984", "George Orwel", 328)
    book2= Book(2, "The Hobbit", "J.R.R. Tolkien", 310)

    library.add_book(book1)
    library.add_book(book2)

    user = User(1, "Filip")

    while True:

        print("\n===Book Library===")
        print("1. List Books")
        print("2. Start reading")
        print("3. Update progress")
        print("4. Open book")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            
            for book in library.books.values():
                print(book.book_id, book.book_title, book.author)
        
        elif choice == "2":

            book_id = int(input("Book ID: "))
            book = library.get_book(book_id)

            if book is None:
                print("Book not found!")
            else:
                user.start_reading(book)
                print(f"Started reading: {book.book_title}")

        elif choice == "3":

            book_id= int(input("Book ID: "))
            page = int(input("Page: "))

            try:

                user.update_progress(book_id, page)
                print("Progress updated!")
            
            except ValueError as e:
                
                print(e)
        
        elif choice == "4":

            book_id = int(input("Book ID: "))

            try:

                page = user.open_book(book_id)

                print(f"Continue reading from page {page}")

            except ValueError as e:
                print(e)
        
        elif choice == "5":

            break

        else:

            print("Invalid Choice!")


if __name__ == "__main__":
    main()
