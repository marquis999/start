""" Объектно ориентированное программирование """

" Наследование и множественное наследование "

class Game:
    def __init__(self, game_name, graphics, game_year, company):
        self.game_name = game_name
        self.graphics = graphics
        self.game_year = game_year
        self.company = company
        
    def info(self):
        print(f"Название игры - {self.game_name}, максимальная графика - {self.graphics},
 дата релиза - {self.game_year}, создатели - {self.company}")
        
game = Game('CsGO', 'FULL HD 4K', 2013, 'Valve')
# game.info()

class Roblox(Game):
    def __init__(self, game_name, graphics, game_year, company, multiplayer):
        super().__init__(game_name, graphics, game_year, company)
        # Game.__init__(game_name, graphics, game_year, company)
        self.multiplayer = multiplayer
        self.name = 'player'
        self.gender = 'man'
        self.skin = 'VIP'
        self.hp = 100
        
    def info(self):
        print(f"Название игры - {self.game_name}, максимальная графика - {self.graphics},
     дата релиза - {self.game_year}, создатели - {self.company}, мультиплеер - {self.multiplayer}")
    
    def info_player(self):
        print(f"Игрок - {self.name}, Пол - {self.gender}, Облик - {self.skin}, Здоровье - {self.hp}")
        print('=========================\nROBLOX - запустился и готов к игре!')
    
    
roblox = Roblox("Roblox", 'ULTRA', '2006', 'Roblox Corporation', "Да")
roblox.info()
roblox.info_player()

# 1
class Animal:
    def __init__(self, name, eat, sleep):
        self.name = name
        self.eat = eat
        self.sleep = sleep
    def info(self):
        print(f"Имя животного - {self.name}, что ест - {self.eat}, когда спит - {self.sleep}")


class Walker:
    def __init__(self, name, eat, walk):
        self.name = name
        self.eat = eat
        self.walk = walk

    def info(self):
        print(f"")
