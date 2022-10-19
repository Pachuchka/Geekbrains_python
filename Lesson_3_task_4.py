def my_func(a,b):
    n = 1
    _result = a
    while n>int(b):
        _result = _result /a
        n=n-1
    print(_result)
_a = input("Введите положительное действительное число")
try:
    _a = float(_a)
except ValueError:
    _a = input("Не корректный ввод. Попробуйте снова: ")
else:
    while float(_a < 0):
        _a= input("Введите положительное число")

_b = input ('целое отрицательное число: ')
try:
    _b = int(_b)
except ValueError:
    _b = input("Не корректный ввод. Попробуйте снова:  ")
else:
    while int(_b)>0:
        _b = int(input('Введите отрицательное целое число'))
if float(_a) == 0:
    print('вы ввели ноль, ответ: ноль')
else:
    my_func(_a,_b)