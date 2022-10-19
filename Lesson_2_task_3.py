_user_num = int(input('Введите порядковый номер месяца '))
while _user_num < 1 or _user_num>12:
    _user_num = int(input('Введите порядковый номер в диапазоне от 1 до 12'))
_mounth_list = [['winter', 'january'],['winter', 'february'],['spring', 'march'],['spring', 'april'],['spring', 'may'],['summer', 'june'],['summer', 'jule'],['summer','august'],['autumn','september'],['autumn','october'],['autumn','november'],['winter','december']]
print(_mounth_list[_user_num-1][0])
_mounth_dict = {1:'winter',2:'winter', 3:'spring', 4:'spring', 5:'spring',6:'summer',7:'summer',8:'summer',9:'autumn',10:'autumn',11:'autumn',12:'winter'}
print(_mounth_dict[_user_num])
_mounth_dict = {2:'winter', 5:'spring', 8:'summer',11:'autumn',12:'winter'}
_key_list = list(_mounth_dict.keys())
n=0
while _user_num > int(_key_list[n]):
    n=n+1

print(_mounth_dict[_key_list[n]])