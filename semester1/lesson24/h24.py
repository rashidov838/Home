# class BankAcount:
#     def __init__(self,name,balance) :
#         self.name=name
#         self.balance=balance
#     def __add__(self,other):
#         if isinstance(other,BankAcount):
#             return self.balance+other.balance
#         if isinstance(other,(int,float)):
#             return self.balance+other
#         raise NotImplemented

# person=BankAcount('Bekzod',200)
# person2=BankAcount('Ikrpom',900)
# a=

# class Data:
#     def __init__(self,value,lol):
#         self.value=value
#         self.lol=lol
#     def __mul__(self,other):
#         return Data(self.value * other.value,self.lol*other.lol)
# a=Data(12,78)
# b=Data(90,67)
# c=a*b
# d=a*b
# print(c.value,d.lol)

# class Point:
#     def __init__(self,value,lol):
#         self.value=value
#         self.lol=lol
#     def __sub__(self,other):
#         return Point(self.value-other.value,self.lol-other.lol)

# p1=Point(200,999)
# p2=Point(190,888)
# c=p1-p2
# d=p1-p2
# print(c.lol,d.value)

class Point1:
    def __init__(self,x) :
        self.x=x
    def __floordiv__(self,other):
        return Point1(self.x//other.x)
    def __truediv__(self,other):
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
