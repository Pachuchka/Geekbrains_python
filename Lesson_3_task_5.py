def _summary(s,e):
    global _summ
    _summ = s + e
def _action():
    global _user_str
    _user_str = input('введите набор чисел, разделённых промелами. Если вы введёте знак "-", это приведёт к завершению работы функции в этом месте: ')
    _calc()
def _calc():
    _number_list = _user_str.split()
    n = 0
    _l = len(_number_list)
    while n < _l:
        if _number_list[n] != '-':

            _element = float(_number_list[n])
            _summary(_summ, _element)
            n = n + 1

        else:
            print(_summ)
            break
    print(_summ)
    _action()

_summ = 0
_action()

