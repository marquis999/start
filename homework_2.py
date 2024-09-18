# 1
class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
        self.name = "Амир"
        self.school = "Ошту"
        self.city = "Кара-Суу"

    def info(self):
        print(f"Полное имя - {self.fullname}, возраст - {self.age}, женат - {self.is_married}")

    def introduce_myself(self):
        print(f"Имя - {self.name}, учюсь в - {self.school}, живу в - {self.city}")

person = Person("Матазимов Амир",17,"нет")
person.info()
person.introduce_myself()

class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def info(self):
        print(f"Имя - {self.fullname}, возраст - {self.age}, женат - {self.is_married}, опыт работы - {self.experience}")

tescher = Teacher("Амир", 17, "нет", 0)
tescher.info()