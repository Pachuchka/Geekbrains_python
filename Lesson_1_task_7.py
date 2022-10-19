print('задача 7')
_start = int(input('Введите начальную дистанцию '))
_finish = int(input('Введите конечную дистанцию '))
n=0
while float(_start) < float(_finish):
    n=n+1
    print(n,'-й день результат ', _start)
    _start = _start * 1.1
print('на ', n, '-й день спортсмен достиг результата не менее', _finish, ' км., а именно', _start, ' км.')