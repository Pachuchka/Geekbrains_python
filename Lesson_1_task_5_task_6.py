print('задача 5')
_proceeds = int(input('Введите выручку фирмы '))
_cost= int(input('Введите издержки '))
if _proceeds > _cost:
    print('компания работает с прибылью')
    _profitability = True
else:
    print('компания несёт убытки')
    _profitability = False
print('задача 6')
if _profitability == True and _proceeds!=0:
   _profit = (_proceeds-_cost)/_proceeds
   print('показатель рентабельности составил: ', _profit)
   _number_of_staff = int(input('Введите численность персонала '))
   _profit_per_person = (_proceeds-_cost)/_number_of_staff
   print('выручка на одного сотрудника составляет: ', _profit_per_person)