class My_error(Exception):
    def __init__(self, txt):
        self.txt = txt
        print(self.txt)

class Stock:
    def __init__(self,adr,s,f,b):
        self.adr = adr
        try:
            if float(s)<0:
                s = float(abs(s))
                raise My_error('площадь склада не может быть отрицательной, площадь была изменена')

        except:
            pass
        self.space = s
        self.free = f
        self.balance = b

    def get_for_storage(self,obj):
        gabarite = float(obj.width) * float(obj.long)
        if float(self.space) > gabarite:
            self.balance.append(obj)
            self.space -= gabarite
            return True
        else:
            print('отказано, на складе не хватает места')
            if self.space<5:
                self.free = False
            return False
    def give_technic(self, obj, company):
        if obj in self.balance:
            company.balance.append(obj)
            self.space = self.space + float(obj.long)*float(obj.width)
            self.balance.remove(obj)
            company.inventarization()
        else:
            print('предмет не найден')
class Rack(Stock):
    def __init__(self,adr,s,f,b,t):
        Stock.__init__(self,adr,s,f,b)
        self.tiers = t
    def set_tiers(self,n):
        Rack_1.adr.space -= self.space
        self.space = int(self.space)/int(self.tiers)
        #self.tiers = int(input('введите число полок: '))
        self.tiers = int(n)
        self.space = int(self.space)*int(self.tiers)
        Rack_1.adr.space += self.space

class Technice:
    def __init__(self,a,b,n):
        self.width=a
        self.long=b
        self.name = n
class Appliances(Technice):
    def __init__(self,a,b,n,built_in,br):
        Technice.__init__(self,a,b,n)
        self.built_in = built_in
        self.brand = br
class Computers(Technice):
    def __init__(self, a, b, n, br):
        Technice.__init__(self, a, b, n)
        self.brand = br
class Mobile(Technice):
    def __init__(self, a, b, n, br,sup):
        Technice.__init__(self, a, b, n)
        self.brand = br
        self.support = sup
class Company():
    def __init__(self,n,b,d):
        self.name = n
        self.balance = b
        self.departments = d
    def assing_dep(self, dep):
        self.departments.append(dep)
        return self.departments
    def return_to_stock(self,obj,stock):
        if obj in self.balance:
            if stock.get_for_storage(obj)==True:
                self.balance.remove(obj)
                self.inventarization()
            else:
                print('нельзя передать на этот склад')
        else:
            print('нельзя передать то чего нет')
    def check_balance(self):
        if self.departments ==0:
            return self.balance
        else:
            for i in self.departments:
                if i.balance !=[]:
                    self.balance.append(i.balance)
            return self.balance
    def inventarization(self):
        self.check_balance()

class Departments(Company):
    def __init__(self,n,b,c):
        self.name = n
        self.balance = b
        self.company = c
        self.company.departments.append(self)
        if self.balance!=[]:
            self.company.check_balance()
    def inventarization(self):
        self.company.check_balance()

ABB = Stock('Irkutsk',-1000,True,[]) #Создаём склад
Rack_1 = Rack(ABB,15,True,[],1) #Площадь склада можно увеличивать добавляя стойки с полками
Rack_1.set_tiers(4) #Добавим в стойку полки, доведя их число до четырёх

INK = Company('Irkoil',[],[]) #создадим компанию
srv = Departments('Irk_Service',[],INK) #создадим департамент
ink_logistic = Departments('Irk_Logistic',[],INK) #создадим департамент
microvave = Appliances(1,2,'Микроволновка',False,'Bosh') # добавим технику
comp_1 = Computers(1,1,'ноутбук асус','Asus')
phone_1 = Mobile(0.5,0.2,'смартфон сяоми', 'xiaomi', '02-02-2025')

ABB.get_for_storage(microvave) #получим техник на склад
ABB.get_for_storage(comp_1)
print(f' на складе {ABB.adr} хранится {len(ABB.balance)} единиц техники, а именно {ABB.balance}')
print('выдадим технику')
ABB.give_technic(microvave,INK)# выдадим технику
print(INK.balance)
ABB.give_technic(comp_1,srv)
print(INK.balance)
print(f' на складе {ABB.adr} хранится {len(ABB.balance)} единиц техники') # проверим остаток, должно быть равно нулю
print('на складе должно быть пусто')
ABB.give_technic(phone_1,ink_logistic) # попробуем выдать то чего нет

srv.return_to_stock(comp_1,ABB)# вернём технику из департамента назад на склад
print(f' на складе {ABB.adr} хранится {len(ABB.balance)} единиц техники') # проверим остаток, должен вернуться 1 объект
print(srv.balance)# проверим баланс департамента, должно быть пусто
print('баланс выше должен быть пустым')
print(f'в компании {INK.name} хранится {len(INK.balance)} объекта')# проверим баланс компании не актуализированный
print('баланс компании должен включать 2 объекта до актуализации')
INK.check_balance()
print(f'в компании {INK.name} хранится {len(INK.balance)} объекта')# проверим баланс компании, актуализированный
print('баланс компании должен включать 1 объект после актуализации')
print(f' на складе {ABB.adr} хранится {len(ABB.balance)} единиц техники')
INK.return_to_stock(comp_1,ABB)
INK.check_balance()
print(INK.balance)
print(f' на складе {ABB.adr} хранится {len(ABB.balance)} единиц техники')
print((ABB.space))