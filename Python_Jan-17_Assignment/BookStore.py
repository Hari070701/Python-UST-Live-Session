class BookStore:
    NoofBooks = 0
    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoofBooks += 1
    def Display(self):
        print(self.Name, self.Author, BookStore.NoofBooks,sep = ", ")


Obj1 = BookStore("Linux System Programming","Robert Love")
Obj1.Display()

Obj2 = BookStore("C Programming","Robert Love")
Obj2.Display()