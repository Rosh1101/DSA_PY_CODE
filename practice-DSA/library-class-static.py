class Library:
    book_count = 0
    def __init__(self, name,  author):
        self.name = name
        self.author = author
        print(f"Initializing the title of the book as: {self.name} \n by {self.author}")

        Library.book_count+=1
    
    def remove(self):
        print(f"Book being removed is titled: {self.name} by {self.author}")
        Library.book_count-= 1

        if(Library.book_count<=0):
            print(f"No books can be removed as the library has {Library.book_count} books")
        else:
            print(f"The total books in the library is: {Library.book_count}")

data_books = []
n = int(input("Number of books to create: "))
for i in range(n):
    book_name = input("Enter the name of the book: ")
    book_author = input(f"Enter  the author of the book {book_name}")
    data_books.append(book_name)
    data_books.append(book_author)

    final_reading = Library(data_books.append(book_name), da)
print(data_books)