class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        print('название книги:', self.title, ';', self.author, '; год издания:', self.year)

book1 = Book('Преступление и наказание', 'Ф. М. Достоевский', '1866')
book1.get_info()
