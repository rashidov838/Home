# Дз
# 1. написать код, который реализует то, что делает функция isinstance и сделать проверку на то, является ли перменная строкой или числом.
# 2. Принять через Input 3 значения: xp (int), damage (int), mp (int). Сравнить эти числа и если 
# xp<=100 damage<=10 mp<=50 -> "Уровень 1"
# xp<=300 damage<=20 mp<=100 -> "Уровень 10"
# xp<=500 damage<=100 mp<=200 -> "Уровень 15" 
# Если больше этого -> "Вы герой"





#Exercise 2
# from asyncore import write

# xp=int(input('Writeb xp: '))
# damage=int(input("Write dam: ")) 
# mp=int(input("write mp: "))

# if xp<=100 and  damage<=10 and mp<=50:
#     print("Уровень 1")
# elif xp<=300 and damage<=20 and mp<=100:
#     print("Уровень 10")
# elif  xp<=500 and damage<=100 and mp<=200:
#     print("Уровень 15")
# else:
#     print("Вы герой")

# Exercise 1
# from re import I
# from turtle import home


# a=input()
# if type(a) is str:
#     print('it is str')
# else type(a) is int:
#     print('it is int')
# input('Write')
# if input is float:
#     print('it is float')
# elif input is int:
#     print('it is int')
# else:
#     print('it is str')

# print( True if a == type(str) else  False)


# a='qwertyu'
# b=12
# print(type(a),type(b))
# print(type(input))
q=input()
def a(q):
    if type(a) == int:
        return True
    else:
       return False
print(a(50))
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

a=int(input('write: '))
if isinstance(a,(str,int)):
    print('str')
else:
    print('int')