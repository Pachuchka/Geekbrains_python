def new_func(a,b):
    print(int(a)/int(b))
_a = input ('введите целое число: ')

try:
    _a = int(_a)
except ValueError:
    _a = input("Не корректный ввод. Попробуйте снова: ")

_b = input ('введите ещё одно целое число: ')
try:
    _b = int(_b)
except ValueError:
    _b = input("Не корректный ввод. Попробуйте снова:  ")

try:
    new_func(_a,_b)
except ZeroDivisionError:
    _b = input("На ноль делить нельзя, измените знаменатель: ")
    new_func(_a, _b)