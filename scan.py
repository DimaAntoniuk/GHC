import numpy as np


class Library:
    def __init__(self, _id, book_num, books, books_per_day, singup):
        self._id = _id
        self.book_num = book_num
        self.books = books
        self.books_per_day = books_per_day
        self.singup = singup

class Book:
    def __init__(self, score):
        self.score = score

class AnsLib:
    def __init__(self, _id, book_num, books, books_per_day, singup):
        self._id = _id
        self.book_num = book_num
        self.books = books
        self.books_per_day = books_per_day
        self.singup = singup

all_libs = []
all_books_dict = {}
all_books = []

with open('input.txt', 'r') as input:
    book_num, lib_num, deadline = list(map(int, input.readline().split()))
    books_scores = sorted(list(map(int, input.readline().split())))
    for _ in range(lib_num):
        _book_num, _singup, _books_per_day = list(map(int, input.readline().split()))
        _books = list(map(int, input.readline().split()))
        lib = Library(_, _book_num, sorted(_books), _books_per_day, _singup)
        all_libs.append(lib)
        for b in _books:
            if b not in all_books:
                all_books.append(b)
        for _book in _books:
            if not str(_book) in all_books_dict or (str(_book) in all_books_dict and all_books_dict.get(str(_book)).singup<=lib.singup):
                all_books_dict.update({str(_book): lib})

all_books.sort()
res_all_libs = []
for book in all_books:
    if(str(book) in all_books_dict and deadline-all_books_dict.get(str(book)).singup>=0):
        lib = all_books_dict.get(str(book))
        deadline -= lib.singup
        cur_books = []
        for _ in lib.books[:min(len(lib.books), deadline*lib.books_per_day)]:
            if _ in all_books_dict:
                cur_books.append(_)
                del all_books_dict[_]
        res_all_libs.append(AnsLib(lib._id, deadline*lib.books_per_day, cur_books, lib.books_per_day, lib.singup))
        



with open('output.txt', 'w+') as output:
    output.write(str(len(res_all_libs)) + '\n')
    for res_lib in res_all_libs:
        output.write(str(res_lib._id) + ' ' + str(res_lib.book_num)+'\n')
        for book in res_lib.books:
            output.write(str(book)+' ')
        output.write('\n')