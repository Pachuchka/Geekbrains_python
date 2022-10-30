user_list = input("введите список чисел, разделённых пробелом: ").split()
print(user_list)
def proverka(el):
    flag = False
    while flag == False:
        try:
            el = float(el)
        except ValueError:
            _el = input(f'Не корректный элемент ' +el+ ' введите корректный новый элемент')
        else:
            flag = True
            _el = float(el)
        return _el

_i=0
while _i < len(user_list):
    prov = proverka(user_list[_i])
    user_list[_i] = prov
    _i=_i+1

new_list = [user_list[n] for n in range(1,len(user_list)) if int(user_list[n])> int(user_list[n-1])]
print(new_list)