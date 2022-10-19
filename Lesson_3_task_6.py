def _action():
    global _user_str
    _user_str = input('введите слово ')
    _int_func(_user_str)
def _int_func(txt):
    new_txt = txt.title()
    print(str(new_txt))
    _action()
_action()