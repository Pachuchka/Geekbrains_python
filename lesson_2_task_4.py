_user_string = str(input('Введите строку: '))
_text_list = _user_string.split()
n=0
while len(_text_list) - n >0:
    if len(_text_list[n])> 10:
        _text_list[n] = _text_list[n][0:10]
    print(n+1, '-ая строка',_text_list[n])
    n=n+1
