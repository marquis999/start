# """инкапсуляция"""

# class PublicExample:
#     def __init__(self, value):
#         self.value = value #публичный атрибут 

    # def info(self):
    #     print(self.value) #публичный метот

# public = PublicExample(42)
# public.info() #вызов публичного метода 

#     def info(self):
#     return self.value #публичный метот

# public = PublicExample(42)
# print (public.info())
# print (public.value)

#зашищенный 
# class ProtectedExample:
#     def __init__(self, value):
#         self._value = value #зашишенный атрибут

#     def _info(self):
#         return self._value #зашищенный метод 

# protected = ProtectedExample(50)
# print(protected._info()) #это работает но это противоречит принципам инкапсуляции 
# print(protected._value) #можно получить значение напрямую но это не рекомендуется 

#приватный 
# class PrivateExample:
#     def __init__(self, value):
#         self.__value = value #приватный атрибут

#     def __info(self):
#         return self.__value #приватный метод
    
#     def accesss_private(self):
#         return self.__info() #публичный метод где мы получаем доступ к приватному атрибуту 
     
# private = PrivateExample(300)
#прямой вызов приватного метода вызовит ошибку
# print(private.__info())
#прямой вызов приватного атрибута вызовит ошибку
# private(private.__value)
#доступ через публичный метод
# print(private.accesss_private())

#доступ к приватному атрибуту через (name mangling)
# print(private._PrivateExample__value)

class MobileLegends:
    def __init__(self, person, rang, item, history):
        self.person = person 
        self.rang = rang 
        self._item = item 
        self.__history = history

    def player_info(self):
        print(f'Персонаж - {self.person}, Ранг - {self.rang}')

    def _item(self):
        bag = input("Введите предметы: ")
        self._item = bag

    def __history_player(self):
        print(self.__history)

    def accesss_history_player(self):
        return self.__history_player()
    
mobale = MobileLegends('нана', 'легенда', 'облик', '-6 звезд')
mobale.player_info()