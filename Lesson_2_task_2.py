_user_number =int(input('введите количество элементов'))
while _user_number<0:
    _user_number = int(input('введите положительное целое число'))
n=0
_user_list=[]
while n <_user_number:
    _user_list.append(input('введите элемент списка'))
    n=n+1
k=0
print(_user_list)
print(_user_number)
print(n)
while k+1<len(_user_list):
    _new_list = [_user_list[k],_user_list[k+1]]
    _new_list.reverse()
    _user_list[k] = _new_list[0]
    _user_list[k+1] = _new_list[1]
    print(_user_list)
    k=k+2

