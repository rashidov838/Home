#Люой обьект 
# name='bekhruz' #global

# def get_name():
#     name='George' #Local
#     print(name)

# get_name()

from threading import local


name='Dave'
def spam():
    name='Guido'

spam() 
print(name)


name='Dave'
def spam():
    global name
    name='Guido'

spam()
print(name)


def foo(items):
    items.append(42)
a=[1,2,3]
foo(a)
print(a)


# Создаем переменную вызывем ее потом меняется items на b и выводит 
def bar(items):
   items=[4,2,3,4]
b=[1,2,3]
bar(b)
print('b не поменялось= ',b)

# Мы не можем приравнять две переменные если переменные имеют свои аргументы
a=[1,2,3,4]
a=b
b=[6,8,9,23]
print(a,b)
 

def parent():
    a=5
    return a
print("Не вложенные",parent())
 

def parent():
    a=5
    def answer():
        return a
    return answer()
print('Вложенные', parent())
# ////////////////////////////////////////////////////////////////////////////////////////////////////
a=20
def parent():
    # enclosed
    a=5
    def answer():
        # local
        a=10
        def get():
            return a
        return get()
    return answer()
print('Вложенные =', parent()) 
# /////////////////////////////////////////////////////////////////////////////////////////////////////
# Nonlocal
def outer():
    # enclosed
    x='local'
    def inner():
        # local
        nonlocal x
        x='non local'
        print("inner", x)
    inner()
    print('outer:',x)
outer()    

#Modifying Global variables
name='Dave'
def spam():
    global name #Импортируем глобальную переменную
    name='Guido' #Change the global name above

spam()
print(name)