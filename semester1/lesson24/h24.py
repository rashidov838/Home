class Data:
    def __init__(self,value,lol):
        self.value=value
        self.lol=lol
    def __mul__(self,other):
        return Data(self.value * other.value,self.lol*other.lol)
a=Data(12,78)
b=Data(90,67)
c=a*b
d=a*b
print(c.value,d.lol)

class Point:
    def __init__(self,value,lol):
        self.value=value
        self.lol=lol
    def __sub__(self,other):
        return Point(self.value-other.value,self.lol-other.lol)

p1=Point(200,999)
p2=Point(190,888)
c=p1-p2
d=p1-p2
print(c.lol,d.value)

class Point1:
    def __init__(self,x) :
        self.x=x
    def __floordiv__(self,other):                 #__floordiv__
        return Point1(self.x//other.x)
    def __truediv__(self,other):                 #__truediv__
        return Point1(self.x/other.x)
    def __str__(self) :
        return "Number " + str(self.x)
a=Point1(200)
b=Point1(100)
print(a//b)
print(a/b)

class Character:
    def __init__(self,name,surname,age) :
        self.name=name
        self.surname=surname
        self.age=age
    def __eq__(self,other):
        return Character(self.name==other.name,self.surname==other.surname,self.age==other.age)
    def __str__(self):
         return "NAme: " +  str(self.name) + "Surname: " + str(self.surname) + "Age: " +str(self.age)
per1=Character("Bekzod",'Rashidov',90)
per2=Character('Jony','Muminov',90)
print(per1==per2)


# class Animal:
#     def __init__(self,name):
#         self.name=name

# class Bird(Animal):
#     def __init__(self, name,color,wings,place,food):
#         super().__init__(name)
#         self.color=color
#         self.wings=wings
#         self.place=place
#         self.food=food

# orel=Bird("Whitehead eagle ", 'Black', 2,'USA','chicken')


class Figure:
    def __init__(self,name):
        self.name=name

class Triangle(Figure):
    def __init__(self, name,a,b,c):
        super().__init__(name)
        self.a=a
        self.b=b
        self.c=c
    def p(self):
        return self.a+self.b+self.c

    def s(self):
        per=self.p()/2
        return (per*(per-self.a)*(per-self.b)*(per-self.c))**0.5
tr=Triangle('10',2,3,4)
print(tr.p())
print(tr.s())
class Computer:
    def __init__(self,CPU,RAM,ROM,user) :
        self.CPU=CPU
        self.RAM=RAM
        self.ROM=ROM
        self.user=user
        self.say_user()
    def say_user(self):
        print(f'Владелец этого компьютера явдяется{self.user}')

    def __eq__(self, other):
        return self.RAM==other.RAM

c1=Computer('15',16,1000,' Bekzod')
c2=Computer('201',116,71000,' Sher')
print(c1==c2)



