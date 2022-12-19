class Not_num(Exception):
    def __init__(self, txt):
        self.txt = txt
        print(self.txt)

user_data = []
data_mass = []
n=True
while n == True:
    input_data = input('введите чеисло, или если вы закончили, введите "stop" : ')
    if input_data != 'stop':
        if input_data[0] == "-":
            new_data = input_data.replace('-','',1)
        else:
            new_data = input_data
        try:
            point_mass = new_data.split('.')
            if len(point_mass)>2:
                raise Not_num('в записи числа не может быть больше одной точки')
            else:
                new_data = new_data.replace('.','')
                check = True
                for j in new_data:
                    try:
                        if j.isdigit()==False:
                            check = False
                            raise Not_num('в записи числа допустимы только цифровые символы, 1 точка для дробей и знак - для отрицательных чисел')
                    except (Not_num) as err:
                        pass
                if check == True:
                    data_mass.append(input_data)
                       # print(err)
        except (Not_num) as err:
            pass
        print (data_mass)
    else:
        n = False