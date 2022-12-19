class My_Complex():
    def __init__(self,a,b):
        self.a = float(a)
        self.b = float(b)
    def __str__(self):
        return(f'{self.a} + {self.b}* i')
    def __add__(self, other):
        a_res = self.a + other.a
        b_res = self.b + other.b
        return(f'{a_res} + {b_res}*i')
    def __sub__(self, other):
        a_res = self.a - other.a
        b_res = self.b - other.b
        return (f'{a_res} + {b_res}*i')
    def __mul__(self, other):
        a_res = (self.a * other.a)-(self.b*other.b)
        b_res = (self.b * other.a) +(self.a*other.b)
        return (f'{a_res} + {b_res}*i')

first = My_Complex(1,2)
second = My_Complex(3,4)
print(first+second)
print(first-second)
print(first*second)