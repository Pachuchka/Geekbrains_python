flag = False
_content = ""
while flag == False:
    _user_str = input ('Введите данные для записи в файл, по окончании введите enter. Пустая строка остановит ввод. ')
    if _user_str=="":
        flag = True
    else:
        _content = _content +_user_str+ "\n"
_my_f = open("user_content.txt","x",encoding="utf-8")
_my_f.write(_content)
_my_f.close()