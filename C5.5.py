class Publisher:
    def __init__(self):
        print("parent class")
class Book(Publisher):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display(self):
        print("the title of the book is : ", self.title)
        print("the author of the book is:", self.author)
class Python(Book):
    def __init__(self,price,pages):
        self.price = price
        self.pages = pages
    def display(self):
        print("the price of the book is :", self.price)
        print("the pages of the book is :", self.pages)


b = Book("learning python","khaled hussain")
b.display()
c = Python(560, 600)
c.display()

