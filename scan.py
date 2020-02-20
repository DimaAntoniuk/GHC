class Library:
    def __init__(self, book_num, books, books_per_day, singup):
        self.book_num = book_num
        self.books = books
        self.books_per_day = books_per_day
        self.singup = singup

class Book:
    def __init__(self, score):
        self.score = score

all_libs = []

with open('input.txt', 'r') as input:
    book_num, lib_num, deadline = map(int, input.readline().split())
    books_scores = map(int, input.readline().split())
    for _ in range(lib_num):
        _book_num, _singup, _books_per_day = map(int, input.readline().split())
        _books = map(int, input.readline().split())
        lib = Library(_book_num, _books, _books_per_day, _singup)
        all_libs.append(lib)

with open('output.txt', 'w+') as output:
    output.write(str(deadline)+'\n')