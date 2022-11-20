class Road:

    def __init__(self,l,w):
        self.__lenght = l
        self.__wight = w
        self.__hight = 5
        self.__norma = 25
        self.calculate()

    def calculate(self):
        _mass = self.__hight*self.__lenght*self.__norma*self.__wight
        print(_mass)


E_95 = Road(1000,25)
