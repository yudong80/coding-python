from collections import namedtuple

#클래스 생성 가능
Book = namedtuple('Book', ['title', 'price'])
b = Book("파이썬을 이용한 비트코인 자동매매", 27000)
print(b.title, b.price)
print(b[0], b[1])