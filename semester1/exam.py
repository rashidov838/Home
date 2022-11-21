# 1.
# Роль виртуальной машины Python (PVM) заключается в преобразовании инструкций байтового кода в машинный код, понятный компьютерам. Для этого у PVM есть интерпретатор. Интерпретатор отвечает за преобразование байт-кода в машинно-ориентированные коды.
# 2.  int- целое
#     float 
#     str строка 
#     list -список 
#     bool-True False
# 3.  Immutable-неизменяемые типы которых нельзя изменить к ним относятся целые числа, строки,  кортежи.
#     Mutable-изменяемые типы которых можно изменить к ним относятся списки, словари.
# 4. 
# from unicodedata import name
name='Bekzod'
surname='Rashidov'
age=19
a='My name is {},surname is {},and  age  is {} '.format(name,surname,age) 
print(a)
a='My name is {1},surname is {0},and  age  is {2} '.format(name,surname,age) 
print(a)
a=f'My name is {name},surname is {surname},and  age  is {age} '
print(a)
a=f'My name is {name:<10},surname is {surname:<10},and  age  is {age:<10} '
# print(a)
# 5. is Сравнивает id в двух значениях
#     == Сравнивает значения
#     in Помогает работать с for i in rangee()
# 6. 1)Local
#    2) Nonlocal
#    3)Global
# 7. None 
# Practice
1.
a=' '
print(len(a))
# 2. Написать функцию, которая принимает число (функция должна работать для чисел от 0 до 99) и возвращает её как строку на английском 
Example:2.1
def qwer():
    for i in range(1,100):
        if i==4:
            return "four"
            continue  
        elif i==19:
            return "nineteen"
            continue
        elif  i==99:
            return "ninety nine"
            continue
    return 
print(qwer())
Example:2.2
def qwer():
    for i in range(1,100):
        if i==4:
            print ("four")
            continue
        elif i==19:
            print("nineteen")
            continue
        elif  i==99:
            print("ninety nine")
            continue
    return 
print(qwer())
# 3.
a = "You've got that fire (fire).The flavor, the style (style)"
b = a.split('.')
print(b)
#  4.
names = [] 
for i in range(10): 
    names.append(i + 4) 
if i == 7: 
    names.pop(0)
    print(names)
else:
    del names[1]
    print(names)
# 5.
a=["bekzod",'John','qweqwrwqeqwe','zxczxczxc']
for i in a:
    if 'John' in a:
        print('John')
    else:
        print(-1)
# 6.
def asd():
    a={
    'Race':None,
    'age':20
    }
    for i in  a:
        if 'age' in i:
            return i[1]
        else:
            return "human"

    return i
print(asd())





