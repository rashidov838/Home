class Me:
    def __init__(self,name,lastname,age):
        self.name=name
        self.lastname=lastname
        self.age=age
    # def __str__(self) :
    #     return f'{self.name}  {self.lastname} {self.age}'
    def introduction(self,swim,jump,walk):
        self.swim=swim
        self.jump=jump
        self.walk=walk
        return f'Меня зовут {self.name} {self.lastname}.Мне  {self.age} лет. Я люблю {self.swim} и {self.jump} и {self.walk}'
    
me=Me("Bekzod","Rashidov",19)
# print(me.name,me.lastname,me.age)
# print(me) 
print(me.introduction("плавать","прыгать","гулять"))


class  Car:
    v=int(input("V: "))
    t=int(input("T: "))
    a=v//t
    def __init__(self,model,color,price,country,engine) :
        self.model=model
        self.color=color
        self.price=price
        self.country=country
        self.engine=engine
    def method(self):
        return f'Модель={self.model}, цвет={self.color}, цена={self.price}, страна={self.country}, двигатель={self.engine}, ускорение за секунду={self.a}'
    def rashod_topliva(self):
        self.L=int(input("L: "))
        self.S=int(input("S: "))
        self.R=(self.L/self.S)*100
        return f'Модель={self.model}, цвет={self.color}, цена={self.price}, страна={self.country}, двигатель={self.engine}, ускорение за секунду={self.a}, расход топлива={self.R}'
car=Car("Kia","red",25.00,'China',1.6)
print(car.method())
print(car.rashod_topliva())
