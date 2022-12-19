class Birthday:
    def __init__(self, d, m,y, *person):

        self.p=person
        self.day = d
        self.month = m
        self.year = y
    @classmethod
    def set_date(cls, data, persons):
        dat_mass = data.split('-')
        day, month, year  = dat_mass
        return cls(int(day), int(month), int(year), persons)
    @staticmethod
    def check_date(obj):
        if float(obj.day) > 31:
            print('не корректная дата - число дней не может превосходить 31 день')
        else:
            if float(obj.month) > 12:
                print('не корректная дата - месяцев всего 12')
            else:
                if float(obj.year)>2022:
                    print('дата ещё не наступила')
                else:
                    print('дата корректна')
        return f'дата {obj.day} / {obj.month} / {obj.year} прошла валидацию, результат проверки выше'


data_st = '26-04-1992'
person_list = ['Иванов, Петров, Климов']


Obj_1 = Birthday.set_date(data_st, person_list)
print(Obj_1.day)
print(Obj_1.month)
print(Obj_1.year)
print(Obj_1.p)
print(Birthday.check_date(Obj_1))