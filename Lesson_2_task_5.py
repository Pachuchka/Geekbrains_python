_rate_list = [7,5,3,3,2]
print(_rate_list)
n = True
while n == True:
    _user_element = input('введите натурально чеисло, или если вы закончили, введите "-" : ')
    if _user_element != '-':
        try:
            input_data = int(_user_element)
        except ValueError:
                _user_element=input("Вы ввели не натуральное число. Попробуйте снова: ")
        else:
            try:
                _example = input_data / (input_data + abs(input_data))
            except ZeroDivisionError:
                    _user_element = input("Вы ввели не натуральное число. Попробуйте снова: ")
            else:
                if int(_user_element) in _rate_list:
                    _rate_list.append(int(_user_element))
                    _is_sort = False
                    while _is_sort == False:
                        k=len(_rate_list)-1
                        print(_rate_list)
                        while k > 0:
                            if int(_rate_list[k-1])<int(_rate_list[k]):
                                _a = _rate_list[k]
                                _b = _rate_list[k-1]
                                _rate_list[k] = _b
                                _rate_list[k-1] = _a
                                _is_sort = False
                                k=k-1
                                print(k)
                                print(_rate_list)
                            else:
                                _is_sort = True
                                k=k-1


                else:
                    _rate_list.append(int(_user_element))
                    print(_rate_list)
                    _rate_list.sort()
                    print(_rate_list)
                    _rate_list.reverse()
                    print(_rate_list)
    else:
        n = False