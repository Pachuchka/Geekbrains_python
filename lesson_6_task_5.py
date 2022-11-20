class Stationery:
    def __init__(self,t):
        self.title = t
    def draw(self):
        return f"Если канцелярская принадлежность может рисовать, она рисует"
pen = Stationery("карандаш")
print(pen.draw())
class Pen(Stationery):
    def __init__(self,t,c):
        super().__init__(t)
        self.color = c
    def draw(self):
        return f"Это ручка, она рисует чернилами цвета: {self.color} "
pen_2 = Pen('Гелиевая ручка', 'Синий')
print(pen_2.draw())
class Pencil(Stationery):
    def __init__(self,t,c,cr):
        super().__init__(t)
        self.color = c
        self.crushed = cr
    def sharpen(self):
        if self.crushed == True:
            self.crushed = False
            print('карандаш заточен')
        return self.crushed
    def draw(self):
        if self.crushed == True:
            return f"Этот карандаш не заточен, он скребёт по листу оставляя кривой след"
        else:
            return f"Этот карандаш рисует чернилами цвета: {self.color} "
pencil = Pencil('Жёлтый карандаш', 'Жёлтый', True)
print(pencil.draw())
pencil.sharpen()
print(pencil.draw())
class Handle(Stationery):
    def __init__(self,t,c,w):
        super().__init__(t)
        self.color = c
        self.width = w
    def draw(self):
        return f"Это маркер, он рисует чернилами цвета: {self.color}, ширина следа: {self.width} "
handle = Handle('Красный маркер', 'Красный', 10)
print(handle.draw())