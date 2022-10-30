from math import factorial
_n = input("Введите целое число " )
flag = False
while flag == False:
    try:
        _n = int(_n)
    except ValueError:
        _n = input("Не корректный ввод. Введите корректное целое число: ")
    else:
        flag = True

def generator():
    for el in range(1,_n+1):
        yield factorial(el)


for i in generator():
    print(i)