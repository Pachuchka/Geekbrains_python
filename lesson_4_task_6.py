from sys import argv
from itertools import count
from itertools import cycle
from  math import ceil


name, _st = argv
flag = False
while flag == False:
    try:
        _a= float(_st)
    except ValueError:
         _st = input("Не корректный ввод. Введите действительное число: ")
    else:
        flag = True
sub_zero = list()
for _el in count(float(_st)):
    if _el>10:
        break
    else:
        _new_el = ceil(float(_st))
        if _new_el <0:
            sub_zero.append(_st)
        print(_new_el)
        _st = float(_st)+1
n=0
print("итератор отрицательных элементов ")
for i in cycle(sub_zero):
    if n>10:
        break
    else:
        print(i)
    n+=1