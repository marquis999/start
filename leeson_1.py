# """ объектно ореинтированное программирования """

# Full_name = 'Амир'  #змеийный регистр

# FullName = 'Амир'  #верблюжий регистр

# class Car: #шаблон или же чертеж 
#     def __init__(self, marka, model, color): #__init__ (магический метод) контруктор 
#          #атрибут объекта
#          self.model = model #self (ссылка на текуший объект)
#          self.marka = marka 
#          self.color = color 
#         #атрибут класса
#          self.bak = 10
#          self.is_start = False

#     def info(self):
#          print(f"Марка машины - {self.marka}, модель - {self.model}, цвет - {self.color}")

#     def start(self)
#         if self.bak > 0:
#            self.is_start = True
#            print(f"Машина {self.marka} - {self.model} заведина")
#         else:
#             print("Машина {self.marka} - {self.model} нет топлива")

#     def stop(self):
#         self.is_start = False
#         print(f'машина {self.marka} - {self.model} заглушено')

#     def drive(self, city):
#         if self.is_start == True:
#             print(f"Машина {self.marka} - {self.model} едет в {city}"")

#         else:
#              print(f"Машина {self.marka} - {self.model} не заведина ")

# bmw = Car('bmw', 'm5 f90', 'black')
# bmw.info()
# bmw.start()
# bmw.stop()
# bmw.drive("Дубай")





# class Book:
#     def __init__(self, avtor, book_name, year):
#         self.avtor = avtor
#         self.book_name = book_name
#         self.year = year

#     def info(self):
#         print(f"Автор книги - {self.avtor}, название книги - {self.book_name}, год - {self.year} ") 

# book = Book('Пушкин', 'золушка', '20')
# book.info()

# доп зд
# class Book:
#     def init(self, title, author, pages, stock):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.stock = stock

#     def check_pages(self):
#         if self.pages < 100:
#             print(f"Книга '{self.title}' автор {self.author} тонкая.")
#         elif 100 <= self.pages <= 300:
#             print(f"Книга '{self.title}' автор  {self.author} средняя.")
#         else:
#             print(f"Книга '{self.title}' автор  {self.author} тонкая.")

#     def sell(self, quantity):
#         if self.stock >= quantity:
#             self.stock -= quantity
#             print(f"Продано {quantity} копий '{self.title}'. {self.stock} На складу осталось копий.")
#         else:
#             print(f"Недостаточно запасов для продажи {quantity} копий '{self.title}'. Осталось только {self.stock} копий.")

#     def buy(self, quantity):
#         self.stock += quantity
#         print(f"Куплено {quantity} копий '{self.title}'. {self.stock} копий теперь есть в наличии.")

# # Пример использования:
# book1 = Book("Пиковая дама", "Пушкин", 95, 10)
# book2 = Book("Дубровский", "Пушкин", 250, 5)
# book3 = Book("С новым годом", "Пушкин", 450, 2)

# book1.check_pages()  
# book2.check_pages()  
# book3.check_pages()  
# book1.sell(3)  
# book2.buy(10)  
# book3.sell(5)  


