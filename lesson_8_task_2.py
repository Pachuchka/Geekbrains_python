num_1 = float(input('n1: '))
num_2 = float(input('n2: '))
class Zero_num(Exception):
    def __init__(self, txt,n):
        self.txt = txt
        self.new = int(n)+1
try:

    if float(num_2) == 0:
        raise Zero_num('знаменатель не должен быть равен нулю. Знаменатель был увеличен на 1')

except (TypeError,Zero_num) as err:
    print(err)
    num_2 = err.new
else:
    print('всё ок')
finally:
    res = num_1 / num_2
    print(res)
