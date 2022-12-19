from abc import ABC,abstractmethod

class Сlothes(ABC):
    @abstractmethod
    def tissue_consumption(self):
        pass

class Coat(Сlothes):
    def __init__(self,s):
        self.__size = s
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, s):
        if s>60:
            self.__size = 60
        elif s<20:
            self.__size = 20
    def tissue_consumption(self):
        return float(self.size)/6.5 +0.5

class Costume(Сlothes):
    def __init__(self, h):
        self.hight = h
    def tissue_consumption(self):
        return float(self.hight)*2+0.3

class Skirt(Сlothes):
    def __init__(self, h):
        self.__hight = h
    @property
    def size(self):
        return self.__hight
    @size.setter
    def size(self,s):
        if s > 5:
            self.__hight = 5
        elif s < 2:
            self.__hight = 2
    def tissue_consumption(self):
        return (float(self.size)**2)/2

A = Coat(56)
B = Costume(44)
C = Skirt(12)
C.size = 16
Clot = [A,B,C]
_sum = 0
for _ in Clot:
    _sum = _sum + _.tissue_consumption()
print(A.tissue_consumption())
print(B.tissue_consumption())
print(C.tissue_consumption())
print(_sum)