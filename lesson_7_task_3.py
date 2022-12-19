class Cell:
    def __init__(self,n,s):
        self.name = n
        self.size = s
    def __add__(self, other):
        if int(self.size) >= int(other.size):
            self.size = int(self.size) + int(other.size)
            print(f'клетка {other.name} была поглощена клеткой {self.name}')
            other.size = 0
            return self.size
        else:
            other.size = int(self.size) + int(other.size)
            print(f'клетка {self.name} была поглощена клеткой {other.name}')
            self.size = 0
            return other.size
    def __sub__(self, other):
        if int(self.size) - int(other.size)>0:
            self.size = self.size - other.size
            return self.size
        else:
            print(f'нельзя выполнять операцию с клеткой большего размера. Клетка {other.name} превосходит клетку {self.name}')
    def __mul__(self, other):
        self.size = self.size*other.size
        other.size = 0
        return self.size
    def __truediv__(self, other):
        self.size = self.size / other.size
        other.size = 0
        return self.size
    def make_order(self, l):
        if self.size>l:
            remain = self.size-l
            result_str = str(('*' * l + '\n'))
            while remain >l:
                result_str = result_str + str(('*'*l+'\n'))
                remain = remain -l
        k =  self.size%l
        result_str = result_str + str(('*' * k + '\n'))
        return result_str




A=Cell('A',8)
B=Cell('B',2)
print(A.size)
print(B.size)
print(A*B)
print(A.size)
print(B.size)
print(A.make_order(5))