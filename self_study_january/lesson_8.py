# name="Bekzod"
# usrname='Rashidov'
# age=21
# skill="D2"
# if name=='Bekzod' and skill=="D2":
#     print("It is correct")
# else:
#     print("It is incorrect")

# if name=='Sardor' and skill=='DA':
#     print("it is correct")
# else:
#     print('It is inccorect ')



# if name=='Sher' or skill=='D2':
#     print(" it is correct ")
# else:
#     print('It is not correct ')
# if not age:
#     print(age)
# else:
#     print('It is  not available')

# if (name=='Bekzod' and age==21) or skill=='C2':
#     print(f'Name: {name}, Age : {age}, Skill: {skill}')
# else:
#     print('Invalid name age and skill')

# id1=1
# id2=2
# print(id1 is id2)
# print(id1==id2)

# t1=[]
# t2=[]
# print(t1==t2)
# print(id(t1)==id(t2))
# print(id(t1),id(t2))


# name='Bekzod'

# print('Check: '+f'{isinstance(name,str)}')
# print('Check: '+ f'{isinstance(name,int)}')

# a=10
# b=20

# print(True if a==b else False)
# if -19:
#     print(True)
# else:
#     print(False)


print(2 not in [23,12,3,0,2])
print([2,3,4] in [5,6,7,2,0,[2,3,4]])

if 0:
    print(True)
elif 2==2:
    print('2 is equal 2')
elif 3==3:
    print('3 is equal 3')
else:
    print('What is goin on')

x=('k1','k2','k3','k4')
y=0
together=dict.fromkeys(x,y)
print(together)

name ='bekzod'
if(isinstance(name,str)):
    print('it is string ')
else:
    print('It is integer')



# xp=int(input('Write your xp: '))
# damage=int(input("Write your damage: "))
# mp=int(input('Write your mp: '))

# if(xp<=100 and  damage<=10 and mp<=50):
#     print("Уровень 1")
# elif(xp<=300 and  damage<=20 and  mp<=100 ):
#     print("Уровень 10")
# elif (xp<=500 and  damage<=100 and  mp<=200):
#     print("Уровень 15" )
# else:
#     print("Вы герой")

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

print(is_number("Bekzod"))
info=int(input('write: '))
if isinstance(info,(str,int)):
    print('Str')
else:
    print('Int')