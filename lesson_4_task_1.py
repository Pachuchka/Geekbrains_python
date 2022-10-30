from sys import argv

name, hours, price, bonus = argv

def new_func(a,b,c):
    print(float(a)*float(b)+float(c))


flag = False
while flag == False:
    try:
        _a = float(hours)
    except ValueError:
        hours = input("Не корректный ввод. Введите корректное число часов: ")
    else:
        try:
            _b = float(price)
        except ValueError:
            price = input(("Не корректный ввод. Введите корректную ставку: "))
        else:
            try:
                _c = float(bonus)
            except ValueError:
                bonus = input(("Не корректный ввод. Введите корректный бонус: "))
            else:

                #new_func(hours,price,bonus)
                flag = True
new_func(hours, price, bonus)

#if flag == True:
 #   print(argv)
  #  new_func(hours,price,bonus)
