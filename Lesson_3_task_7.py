def _action():
    global _user_str
    _user_str = input('введите строку ')
    _int_func(_user_str)
def _int_func(txt):
    txt_list = txt.split()
    n=0
    new_txt = ""
    while n<len(txt_list):
        new_txt =new_txt + txt_list[n].title() + ' '
        n=n+1
    print(str(new_txt))

_action()