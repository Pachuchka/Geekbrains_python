def my_func(a,b,c):
    user_list = [a,b,c]
    _first = max(user_list, key = lambda  i:int(i))

    user_list.remove(_first)
    _second = max(user_list, key = lambda  i:int(i))
    _result = _first + _second
    print(_result)


_a = int( input('введите первое число'))
_b = int( input('введите второе число'))
_с = int( input('введите второе число'))
my_func(_a,_b,_с)