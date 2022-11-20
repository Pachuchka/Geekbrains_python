from random import choices
class Car:
    def __init__(self, s,c,n,p):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = p
    def go(self):
        print(f"машина {self.name} поехала")
    def stop(self):
        print(f"машина {self.name} остановилась")
    def turn(self, direction):
        print(f"машина {self.name} повернула {direction}")

    def rnd_turn(self):
        directions = ['Налево', 'Направо','На север','На восток']
        print(f"машина {self.name} повернула {choices(directions,k=1)}")
    def show_speed(self):
        return self.speed
class TownCar(Car):
    def __init__(self,s,c,n,p):
        super().__init__( s,c,n,p)
        if self.is_police == True:
            self.is_police = False
            print('Теперь это гражданский автомобиль')
    def show_speed(self):
        if float(self.speed) > 60:
            print('Автомобиль движется с превышением установленной скорости!')
        return  self.speed
class SportCar(Car):
    def __init__(self,s,c,n,p):
        super().__init__( s,c,n,p)
        if self.is_police == True:
            self.is_police = False
            print('Теперь это гоночный автомобиль')
class WorkCar(Car):
    def __init__(self,s,c,n,p):
        super().__init__( s,c,n,p)
        if self.is_police == True:
            self.is_police = False
            print('Теперь это рабочий автомобиль')
    def show_speed(self):
        if float(self.speed) > 40:
            print('Автомобиль движется с превышением установленной скорости!')
        return  self.speed
class PoliceCar(Car):
    def __init__(self,s,c,n,p):
        super().__init__( s,c,n,p)
        if self.is_police == False:
            self.is_police = True
            print('Автомобиль стал полицейским')
        self.color = 'Black'


car_1 = Car(70,'red','viper',False)
car_1.go()
car_1.turn('Налево')
car_1.rnd_turn()
car_2 = TownCar(70,'red','viper',True)

print(car_2.show_speed())
print(car_2.is_police)
car_3 = PoliceCar(70,'red','viper',True)
print(car_3.color)
print(car_3.is_police)
print(car_3.show_speed())
car_4 = WorkCar(40,'white','opel',True)

print(car_4.show_speed())
print(car_4.is_police)