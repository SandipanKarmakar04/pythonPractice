'''Define a class Book with a constructor that takes title and author as arguments, where author defaults to 
"Unknown". A method display that prints the book details. Create an object with and without providing the author.'''

class Book:
    def __init__(self, title, author="unknown"):
        self.title = title
        self.author = author
    def display(self):
        print(self.title,"written by",self.author)

b = Book("Power of Money","Sandipan")
b.display()
