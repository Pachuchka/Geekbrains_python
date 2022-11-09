_my_f = open("оклады.txt","r",encoding="utf-8")
_content_list = _my_f.read().split("\n")
i =0
_sum = 0
k = 0
while i < len(_content_list):
    _elem_list = _content_list[i].split()
    if len(_elem_list)>2:
        print(f"Не корректный ввод {_elem_list}")
        i=i+1
        k=k+1

    else:
        try:
            _elem = _elem_list[1]
            _elem = float(_elem)
            if _elem < 20000:
                print(f"сотрудник {_elem_list[0]} получает меньше 20 000")
        except ValueError:
            try:
                _elem = _elem_list[0]
                _elem = float(_elem)
                if _elem < 20000:
                    print(f"сотрудник {_elem_list[1]} получает меньше 20 000")
            except ValueError:
                print(f"ошибка ввода {_elem_list}")
                k=k=1
                i=i+1
            else:
                _sum = _sum + _elem
                i=i+1
        else:
           _sum = _sum+_elem
           i=i+1
_sred = _sum/(i-k)
print(_sred)



