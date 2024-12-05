# 문제 1
# class Book(object):
#     def __init__(self, title, author, year: int):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.rental_status = True
    
#     def display_info(self):
#         status = "대여 가능" if self.rental_status else "대여중"
#         print(f"책 제목: {self.title}, 저자: {self.author}, 출판연도: {self.year}, 대여 상태: {status}")

#     def borrow(self):
#         if self.rental_status:
#             self.rental_status = False
#             print(f"{self.title} 대여가 완료되었습니다.")
#         else:
#             print(f"현재 다른 이용자가 대여중입니다.")
        
    
#     def return_book(self):
#         self.rental_status = True
#         print(f"{self.title} 반납이 완료되었습니다.")

# book1 = Book("Python Programming", "John Smith", 2023)
# book1.display_info()
# book1.borrow()
# book1.borrow()
# book1.return_book()
# book1.borrow()

# 문제 2
class Shape(object):
    def __init__(self, color):
        self.color = color

    def get_area(self):
        pass

    def display_info(self):
        print(f"도형의 색상은 {self.color} 이고, 면적은 {self.get_area()}입니다.")

class Rectangle(Shape):

    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height * 0.5

rect = Rectangle("빨강", 5, 3)
tri = Triangle("파랑", 4, 6)
rect.display_info()
tri.display_info()