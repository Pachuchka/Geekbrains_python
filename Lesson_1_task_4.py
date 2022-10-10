print('задача 4')
_user_number = int(input('Введите ваше число '))
_depth = 10
list = []
_unins = _user_number % _depth

while _user_number//_depth>0:
    list.append(int(_user_number % _depth))
    _user_number = (_user_number-(_user_number % _depth))/10
list.append(int(_user_number%_depth))
print(list)
n=0
_max =  list[n]
for element in list:
    if element >=_max:
        _max = element

print(_max)

