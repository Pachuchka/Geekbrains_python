def user_list(name, age, phone, adress):
    print(f'hello, {name} !' )
    print(f'your age: {age}, your phone: {phone}, adress: {adress}')
_name = input('введите ваше имя: ')
_phone = input('Введиет ваш телефон: ')
_age = input('введите ваш возраст: ')
_adress = input('введите ваш адрес: ')
user_list(adress =_adress ,age = _age,name = _name,phone=_phone)