name='Bekzod'
surname='Rashidov'
age=20
skil='D2'
#1
if name=='Bekzod' and skil=='D2':
    print(name,skil)
else:
    print('And') 

if name=='Sardor' and skil=='D2':
    print(name,skil)
else:
    print('And') 

#2
if name=='QWERTY' or skil=='D2':
    print(name,skil)
else:
    print('OR') 

# #3
if not age:
    print(age)
else:
    print('Age is false')    

if age:
    print(age)
else:
    print('Age is false')    
          
if (name=='Bekzod' and age>18) or skil =='D2':
    print(name,age,skil)
else:
    print('Invalid name,skil,age')

if name=='Bekzod' or age>18 and skil =='D2':
    print(name,age,skil)
else:
    print('Invalid name,skil,age')

if name=='Bekzod' or age>22 or skil =='D2':
    print(name,age,skil)
else:
    print('Invalid name,skil,age')
# //////////////////////////////////////////////////////////////////
# is ==
# is -Сравнивает  id  Двух значений
#id()
# a=1
# b=1
# print(id(a),id(b))
# #Tuple
# t_1=()
# t_2=()
# print(id(t_1),id(t_2))
# print(t_1==t_2)
# print('Tuple', t_1 is t_2 )
# # Изменяемые типы данных
#[] [] List
l_1=[1,2]
l_2=[1,2]
print(l_1==l_2)
print(l_1 is l_2)
print(l_1,id(l_1),l_2,id(l_2))
# #Dictionary
d_1={1:1}
d_2={1:1}
print('Dict',d_1==d_2)
print('Dict',d_1 is d_2)
# #

# if elif else 



#isinstance
# import this


# name='Bekzod'
# print(isinstance(name,str))
# print(isinstance(name,(str,int)))
# name= 12
# print(isinstance(name,str))
# print(isinstance(name,int))
# print(isinstance(name,(str,int)))



#Bool True False
# from operator import truediv
# from traceback import print_tb

# #first type
# x=10
# y=20
# if x>y:
#     print('Good')
# else:
#     print('Bad')

# #Second type
# print('Good' if y>x else 'Bad')  # a if condition else b 

# 'qwerty asdfghj'.split() #['qwerty', 'asdfghj']
#True=1   False=0
#

#== != > >= < <= is , is not , and, or, not
#[] {} () ''   Если они пустые то будет всегда 0    иначе все будет работать
if []:
    print(True)
if -19:
    print(True,-19)

if 45678:
    print(True,45678)
# ///////////////////////////////////////////////////
print('in =', 1 in [2,3,4,1])
print('in =', 'Hi' in 'Hi my name is SMth')
print('in =', [1,2] in [2,3,4,[1,2]])
print('in =', {1,2} in [2,3,4,{1,2}])

if 1:
    print(True)
else: 
    print(False)

if 0:
    print(True)
elif 2==2:
    print('elif 1')
elif 2==2:
    print('elif 1')
elif 2==2:
    print('elif 1')
else:
    print(False)

x=('key','key2','key3')
y=0
thisdict=dict.fromkeys(x,y)
print(thisdict)
# thisdict=list.fromkeys(x,y)
# print(thisdict) #eror

