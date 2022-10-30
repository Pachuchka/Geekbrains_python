user_list = input("введите список чисел, разделённых пробелом").split()
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
def povtor(el,u_list):
    i=0
    flag = 0
    while i < len (user_list):
        if el == user_list[i]:
            flag = flag+1
        i = i+1
    return flag

_i=0
while _i < len(user_list):
    prov = float(proverka(user_list[_i]))
    user_list[_i] = prov
    _i=_i+1


new_list = [user_list[n] for n in range(0,len(user_list)) if povtor(user_list[n],user_list)<2]
print(new_list)