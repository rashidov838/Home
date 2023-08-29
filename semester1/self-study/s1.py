#  Set classwork
#  numbers={2,3,4,'Hello',2.3,5,6}
# print(numbers)
# numbers={}
# print(type(numbers))
# numbers=set()
# print(type(numbers))
# remove_duplicate=[1,2,3,4,5,6,1,2,3,4,'AA','VV','AA']
# print(set(remove_duplicate))
# print(list(set(remove_duplicate)))
# print(tuple(set(remove_duplicate)))
# User_data={
#     'Color':'Black',
#     2:24,
#     3:9.4,
#     4:['qwe','das',1230],
#     5:(12,343,5,6),
#     4:['qwe','das',1230],
#     5:(12,343,5,6),
#     4:['qwe','das',1230],
#     5:(12,343,5,6),
#     4:['qwe','das',1230],
#     5:(12,343,5,6),
#     6:{'model':'Uzauto'},
#     'Country':'Turkey'
# }
# print(type(User_data),User_data['Color'])
# print(User_data[4][2])
# print(User_data.keys())
# print(User_data.values())
# print(User_data.items())
# User_data['Black']='Made in'
# print(User_data)
# print(User_data.get('Country'),User_data.get('Color'))
# User_info=[
#     {
#     'name':'Bekzod',
#     'Surname':'Rashidov',
#     'Age':45,
#     5:'Car',
#     }   ,
#     {
#         'Name':'Shax',
#         'Surname':'Karimov',
#         'Age':90,
#         10:'Car',

#     }

# ]
# print(User_info[0]['name'])
# print(User_info[1]['Age'])
# Set homework
# a={ 'Shelf Expert',"Woods & Screws",'SofaSoGood'
#    }
# b={'Kitchen','Magic','Clever', 'Machines'
# }
# a.update(b)
# print(a)
# b.add('Lola')
# print(b)
# a.pop()
# print(a)
# b.remove('Magic')
# print(b)
# c=a.copy()
# print(c)
# print(a.clear())
# print(a.clear())
# print(b.difference(a))
# print(a.difference(b))
# 2 exe/Прочитать и попробовать методы словарей (dict).
# user={
#     'name':'bekzod',
#     'password':'1234567',
#     'age':89
# }
# user2={
#     'name':'Sancho',
#     'password':'098765',
#     'age':78
# }
# print(user.pop('password'))
# print(user.items())
# print(user.setdefault('age')) #Пишим ключ получаем значение
# user.update({'weight':23}) # Тоже добавление
# print(user)
# del user2['password']
# print(user2)
# lesson-8
# name="Bekzod"
# last='Rashidov'
# age=34
# skill='wrestling'
# if name=='Bekzod' and age==34:
#     print(f'Welcome')
# elif name=='Bekzod' or age==90:
#     print(f'Hi baby')
# else:
#     print(f'Buy ')

# if not age:
#     print(age)
# else:
#     print('age is False')
# a=2
# b=2
# print(a is b)
# print(id(a),id(b))
# print(a==b)
# c=[2]
# d=[2]
# print(c is d)
# print(id(c),id(d))
# print(c==d)
# e={3}
# t={3}
# print(id(e),id(t))
# print(e is t)
# print(e==t)
# d_1={1:1}
# d_2={1:1}
# print('Dict',d_1==d_2)
# print('Dict',d_1 is d_2)
# print(id(d_1),id(d_2))
# name="Bekzod"
# last='Rashidov'
# age=34
# skill='wrestling'
# print(isinstance(last,str))
# print(isinstance(age,int))
# print(isinstance(skill,float))
# x=8
# y=10
# print("good" if x>y else "Bad")
# a='My project is aabout family'.split(' is ')
# print(a)
# if []:
#     print(True)
# if -19:
#     print(True, -19)
# print({1,2} in [2,3,400,{1,2}])
# x=('COl1','COl2','COl3')
# y=1
# print(dict.fromkeys(x,y)).
# a=int(input("Write your code "))
# b=input('Write your code ')
# if type(a) is int:
#     print(f'it is int {a}')
# else:
#     print(f'It is str  {a}')
# xp=int(input('XP: '))
# damage=int(input('Damage:  '))
# mp=int(input('Mp: '))
# if xp<=100 and  damage<=10 and mp<=50:
#     print("Уровень 1")
# elif xp<=300  and damage<=20 and  mp<=100: 
#     print("Уровень 10")
# elif xp<=500  and damage<=100 and  mp<=200:
#     print("Уровень 15" )
# w=input()
# def a(w):
#     if type(w) == int:
#         return True 
#     else:
#         return False
# print(a(123))
# str=int(input('Wrute: '))
# def id_numbers(str):
#     try:
#         float(str)
#         return True
#     except ValueError:
#         return False
# print(id_numbers('FFFF'))
# import copy
# a=[2,3,4,5]
# w=a.copy()
# print(w)
# w.append(123)
# print(w)
# e=copy.deepcopy(w)
# e.append([2,3,33,3,3,9])
# print(e)
# value='hi'
# print(e)
# value='hi'
# print(e)
# value='hi'
# print(e)
# value='hi'
# if not type(value)==int:
#     print(True)
# else:
#     print(False)
# w=[1,2,3,4,5,6,7]
# for i in w:
#     print(i)
# user={
#     'name':'Gearge',
#     'age':23,
#     'skill':'swim',
# }   
# for key,val in user.items():
#     print({key,val})
# for key in user.keys():
#     print(key)
# print('-----------------')
# for value in user.values():
#     print(value)
# print('-----------------')
# for val in [1, 2, 3, 4, 5, [6, 7, 8, 5, 6], (4, 5, 6)]:
#     if isinstance(val,(list,tuple,set)):
#         for i in val:
#             print(i)
# w=[1, 2, 3, 4, 5, 6, 7]
# for i in range(len(w)):
#     print(w[i]*4)
# a=[1, 2, "hello", 4, 5, 6, 7]
# a.pop(2)
# print(a)
# a=input('name: ')
# b=int(input('Age: '))

# info=[]
# i=0
# while i<10:    
#     info.append({
#     'name': a,
#     'age': b,
# })
#     i+=1
# print(info)
# keys =['a',' b', 'c']
# values =[1, 2, 3] 
# list_dict={k:v for k,v in zip(keys,values)}
# print(list_dict)
# numbers=[1,2,3,4,5,6,7]

# for i in numbers:
#     if i==6 or 3==i:
#         print('Go ahead')
#         break
#     print(i)
# for i in numbers:
#     if 4==i:
#         continue
#     print(i)
# if 12==12:
#     pass
# info_stuff=[]
# for i in range(5):
#     name=input('Name')
#     age=int(input('Age '))
#     info_stuff.append({
#         'Name': name,
#         'Age': age
#     })
#     print(info_stuff)
# faranheits=[4444,19,67,78]
# cel1=(faranheits[0]-32)*5/9
# cel2=(faranheits[1]-32)*5/9
# cel3=(faranheits[2]-32)*5/9
# cel4=(faranheits[3]-32)*5/9
# value=[cel1,cel2,cel3,cel4]
# for i in value:    
#     if i>=50:
#         print(f'Слишком горячо {i}')
#     else:
#         print(f'Жить можно {i}')

# square_line=4
# star='*'
# star_width=star * square_line
# for i in range(square_line):
#     if i>0 and i<(square_line-1):
#         empty_space=' ' *(square_line-2)
#         print(f'{star }{empty_space}{star}')
#     else:
#         print(star*square_line)
# i=0
# while True:
#     print(i)
#     i+=1
#     if i==10:
#         break 

# numbers=[1,2,3,90,6,8]
# i=0
# while i<len (numbers):
#     print(numbers[i])
#     i+=1
# w='monika'
# for i in range(len(w)):
#     print(w[i])
# for i,val in enumerate(w):
#     print(i,val)
# a={3:1, 2:2, 1:3}
# for key,val in a.items():
#     b=[]
#     b.append((key,val))
#     print(sorted((b),reverse=False))
# print(list(tuple(sorted((a),reverse=True))))
# print(sorted(a.items()))
# b=[2,3,4,5,6]
# for i in b:
#     even=[]
#     odd=[]
#     if i%2==0:
#         even.append(i)
#         print(f'Even {even}')
#     else:
#         odd.append(i)
#         print(f'Odd {odd}')
# faranheits = [200, 190, 240, 45] 
# celsius1= (faranheits[0] - 32) * 5 / 9
# celsius2 = (faranheits[1] - 32) * 5 / 9
# celsius3 = (faranheits[2] - 32) * 5 / 9
# celsius4= (faranheits[3] - 32) * 5 / 9
# box=[celsius1,celsius2,celsius3,celsius4]
# i=0
# while i <len(faranheits):
#     for f in box:
#         if f>50.0:
#             print(f'Too hot {f}')
#         else:
#             print(f'Able to live {f}')
#     i+=1
# def great():
#     print(f'Hello')
# great()

# def great():
#     return "Hello Babby"
# print(great())

# def name(n):
#     print(f' Name {n}')
# name(input('Name: '))

# def great():
#     return "Hello Babby"
# a=great()
# print(a)
# def make_upper_case():
#     a=input()
#     i=a.upper()
#     return i
# print(make_upper_case())
# def number_pow():
#     return 3**4
# print(number_pow())
# def multiplication_numbers(a,c):
#     i=0    
#     while i<10:
#         for key,val in a,c:

#             b=key*val
#             w=[]
#             w.append(b)
#             print(w)
#         i+=1
# multiplication_numbers(int(input('First '),int(input('Second '))))
# def factorial(n):
#     pr=1
#     a=[]
#     for i in range(2,n+1):
#         pr=pr*i
#         a.append(pr)
#     return a
# print(factorial(10))
# def shades_of_grey(n):
#     shades=[]
#     hex='123456789abcdef'
#     counter=0
#     for i in range(n):
#         if counter==15:
#             counter=0
#         gray=f'#0{hex[counter]}0{hex[counter]}0{hex[counter]}'
#         if i>=15:
#             gray=f'#1{hex[counter]}1{hex[counter]}1{hex[counter]}'
#         shades.append(gray)
#         counter+=1
#     return shades
# print(shades_of_grey(50))
# n=[]
# def mul(num):
#     for i in  range(5,10):
#         a=num*i
#         n.append(a)

#     return n
# print(mul(10))

# def fuction(a,b,default='Hi'):
#     return a,b, default
# print(fuction(123,'Hllll'))

# Args
# def func(a,b,default='NONO',*args):
#         print(a,b,default,args)
# func('DODO',123.34,'sdfghj','rtyuio')
# def any(*args):
#     print(args)
#     for arg in args:
#         print(arg)
# any(2,3,4,'goooooo','biiiiiiii',{3,2,2,},(4,4,4),[1,2,3])
# def fibonacci(n):
#     if n in (1,2):
#         return 1
#     return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(10))
# def connection():
#     a=['name']
#     b={}
#     return b.fromkeys(a)
# print(connection())
# def num_mul():
#     a=[12,23,34,45,56]
#     result=[]
#     for i in range(len(a)):
#         b=a[i]*4
#         result.append(b)
#     return result
# print(*num_mul())
# for i in range(10,80,4):
    # print(i)
    # print(list(range(i)))
# def order_of_args(name,default='Go',*args,sep='Seperator',username,end='\n',**kwargs):
#     print(name,default,args,sep,username,end,kwargs)
# order_of_args('Bekhruz',123,4,5,6,username='Bekzod',end='END',sep='SEP',emal='e@mail.com',address=['123asd'])
# def func(*args,**kwargs):
#     return args, kwargs
# print(func(2,3,4,{243},username={'name':'Bekzod'},last='Baby'))
# name='Dave'
# def spam():
#     global name
#     name='Bekzod'
#     print(name)
# spam()
# def foo(items):
#     items.append(42)
# a=[12,32,34]
# foo(a)
# print(a)
# def father():
#     a='Bekzod'
#     def son():
#         return a
#     return son()
# print(father())
# def father():
#     a='Bekzod'
#     def son():
#         # a='Rashidov'
#         def little_child():
#             return a
#         return little_child()
#     return son()
# print(father())
# def outer():
#     x='local'
#     def inner():
#         nonlocal x
#         x='HHIIHIHIHIHI'
#         print(x)
#     return inner()
#     print(x)
# print(outer())
# def factorial(n):
#     if n==0:
#         return 1
#     return factorial(n-1)*n
# print(factorial(5))
# n=int(input())
# c=0
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(c+j,end=' ')
#     print(i+j,end=' ')
#     c=c+1
#     print(c)
# from itertools import permutations   #Combination
# input='monika'
# letter=[x.upper() for x in input ]
# for i in list(permutations(letter)):
#     print(''.join(i))

# def fibonaci(n):
#     cur=1
#     if n>2:
#         cur==fibonaci(n-1)+fibonaci(n+2)
#     return cur

# element = input('Введите номер искомого элемента : ')
# element = int(element)
# value=fibonaci(element)
# print(str(element)+ 'элемент последовательности равен' +str(value))
# names = [
#     "Adam",
#     [
#         "Bob",
#         [
#             "Chet",
#             "Cat",
#         ],
#         "Barb",
#         "Bert"
#     ],
#     "Alex",
#     [
#         "Bea",
#         "Bill"
#     ],
#     "Ann"
# ]
# print(isinstance(names[0],str))
# for a,b in enumerate(names):
#     print(a,b)
# def count_leaf_items(items_list):
#     count=0
#     for item in items_list:
#         if isinstance(item,list):
#             count+=count_leaf_items(item)
#         else:
#             count+=1
#     return count
# print(count_leaf_items([5,6,7]))
# def palindrom(word):
#     return word==word[::-1]
# # print(palindrom('qweewq'))
# import random
# def random_get(length,min=1,max=100):
#     numbers=[]
#     for i in range(length):
#         numbers.append(random.randint(min,max))
#     return numbers
# print(random_get(50))
# obj={
#     'RACE':"oGRE",
#     'age':100,
#     'skill':['Roar'],
# }
# if 'RACE' in obj and 'age' in obj and isinstance(obj['age'],int):
#     print(obj['RACE'],obj['age'])
# else:
#     print('human')
# def short_word(names):
#     if names:
#         length=len(names[0])
#     else:
#         return False
#     for name in names[1:]:
#         name_len=len(name)
#         if name_len<length:
#             length=name_len
#         return length
# name=['Bekzod','JOhn','Gabriel']
# result=short_word(name)
# print(result)
# def encode(s:str)->str:
#     s=list(s)
#     total=''
#     for i in range(len(s)):
#         if i%2==0:
#             total+=s[0]
#             s.pop(0)
#         else:
#             total+=s[-1]
#             s.pop(-1)
#     return total
# print(encode('codewars'))
# def number_to_words(n):
#     f={1:'one', 2:'two',3:'three',4:'four',5:'five',6:"six",7:'seven', 8:"eight",9:'nine', 
#     }
#     l={10:'ten', 20:"twenty",30:'thirty', 40:"fourthy",50:'fifty', 60:"sixty",70:'seventy', 80:"eight",90:'ninety', 
#     }
#     s={11:'eleven', 12:"twelve",13:'thirteen', 14:"fourteen",15:'fivteen', 16:"sixteen",17:'seventeen', 18:"eighteen",19:'nineteen', 
#     }
#     n1=n%10
#     n2=n-n1
#     if n<10:
#         return f.get(n)
#     elif 20>n>10:
#         return s.get(n)
#     elif n>=10 and n2==0:
#         return l.get(n)
#     elif n>20:
#         return str(l.get(n2))+' '+str(f.get(n1))
# print(number_to_words(30))
# def call(text):
#     tl=text.split(' ')
#     store=[]
#     for i in tl:
#         if i.isalpha():
#             i=i[1:]+i[0]+'ay'
#             store.append(i)
#             return ' '.join(store)
#         else:
#             return ' '.join(store)
# print(call('Nomika'))
# x='Bekzod Rashidov'
# a=x.split(' ')
# print(set(a))


# class Marker:
#     size=15
#     health=10
#     a=[]
#     def __init__(self,company,color,price):
#         self.company=company
#         self.color=color
#         self.price=price
#     def draw(self,line_length):
#         if self.health<=0:
#             return 'Маркер истощен'
#         self.health=self.health-line_length
# marker1=Marker('Kola inc','Black',20003)
# marker2=Marker('Al nasr inc','Yellow',20003)
# marker3=Marker('PSJ inc','Blue',20003)

# print(marker1.health)   
# marker1.draw(5)
# print(marker1.health)    
# 
#  
# class Information_about_Me:
#     def __init__(self,name,lastname,age,gender):
#         self.name=name
#         self.lastname=lastname
#         self.age=age
#         self.gender=gender
#     def introduction(self,swim,jump,reading,speaking):
#         self.swim=swim
#         self.jump=jump
#         self.reading=reading
#         self.speaking=speaking
#         return f' My name  is {self.name} {self.lastname}, age is {self.age} and gender is {self.gender}. I really love {self.jump},{self.reading},{self.swim}'
# me=Information_about_Me('Bekzod','Rashidov',90,'Man')
# print(me.introduction('Swimming in  pools','Jump in balls','reading books','speaking so a lot'))
# class Car:
#     v=int(input('V: ' ))
#     t=int(input('T'))
#     a=v//t
#     def __init__(self,model,color,price,country,engine):
#         self.model=model
#         self.color=color
#         self.price=price
#         self.country=country
#         self.engine=engine
#     def __str__(self) -> str:
#         return f'Model = {self.model}, Color = {self.color}, Price = {self.price}, Country = {self.country}, Engine = {self.engine}' 
#     def rashod_topliva(self):
#         self.l=int(input('L: '))
#         self.s=int(input('S: '))
#         self.r=(self.l/self.s)*100
#         return f'Model = {self.model}, Color = {self.color}, Price = {self.price}, Country = {self.country}, Engine = {self.engine}, ускорение за секунду={self.a}, расход топлива={self.r}'
           
# car1=Car('Gentra','White',18800,'Uzbekistan',1.6)
# print(car1)
# print(car1.rashod_topliva())
# class PlayerCharacter:
#     membership=True
#     def __init__(self,name='Bekzod',age=19):
#         self.name=name
#         self.age=age
#     # def __str__(self):
#     #     return f'Name is {self.name} and age is {self.age}'

#     @classmethod
#     def addition(cls,num1,num2,num3,num4):
#         return cls(num2+num3)


# player1=PlayerCharacter('Muhammad',20)
# # print(player1)

# player2=PlayerCharacter.addition(40,56,90,89)
# print(player2.name)
# class Point():
#     color='red'
#     circle=2
#     def set(self,x,y):
#         self.x=x
#         self.y=y
# pt=Point()
# pt2=Point()
# pt.set(19,90)
# pt2.set(12,89)
# print(pt.__dict__)
# print(pt2.__dict__)
# def count(x,n):
#     a=[]
#     for i in range(n):
#         a.append(x*(i+1))
#     return a
# print(count(90,78))
# class Point:
#     color='red'
#     circle=2
#     def __init__(self,a,b) :
#         self.a=a
#         self.b=b
#     def __del__(self):
#         print('It was deleted ' +str(self))
# p=Point(30,50)
# print(p.__dict__)
# print(p.__dict__)
# class Point():
#     def __new__(cls,*args,**kwargs):
#         print(' New ' + str(cls) + str(args)+ str(kwargs))
#     def __init__(self,x=0,y=0):
#         self.x=x
#         self.y=y
#         print('Init' +str(self))
# pt=Point.__new__(45,90,'qwertyu',767676, code=' asdsas')
# print(pt)
# class Father:
#     house=True
#     def __init__(self,name,job,hobby,bank_account):
#         self.name=name
#         self.job=job
#         self.hobby=hobby
#         self.bank_account=bank_account
#     def spend_money(self,amount):
#         self.bank_account-=amount
#     def income_money(self,amount):
#         self.bank_account+=amount 
    
# class Mother:
#     cooked=' '
#     def cook(self,product):
#         if 'tomato' in product and 'eggplant' in product and 'onion' in product:
#             print(f'Mother has  cooked and used all {product}')
#         else:
#             print(f' Sister has cooked a food') 

# class Child(Father,Mother):
#     def __init__(self, name, job, hobby, bank_account,age):
#         super().__init__(name, job, hobby, bank_account)
#         self.age=age
#     def __str__(self) -> str:
#         super().__str__()
#         return f' My name is {self.name},job = {self.job}, hobby = {self.hobby}, bank_account= {self.bank_account},age= {self.age}'
#     def cook(self, product):
#         super().cook(product)
#         if 'mushroom' in product and 'dough' in product:
#             self.cooked_food='fired_eggplant'
#             return self.cooked_food
#     def income_money(self, amount,hours):
#         super().income_money(amount)
#         self.hours=hours
#         self.bank_account+=amount
#         self.bank_account/=hours
#     def __str__(self) -> str:
#         super().__str__()
#         return self.bank_account
# me=Child('Bekzod','Programmer','Talking',20000,19)

# print(me.cook(['mushroom','dough']))
# me.income_money(4800,89)
# print(me.bank_account)


# me.spend_money(100)
# print(me.bank_account)
# class Personage():
#     def __init__(self,health,mana,damage,type,skill,name):
#         self.health=health
#         self.mana=mana
#         self.damage=damage
#         self.type=type
#         self.skill=skill
#         self.name=name
#     def attack(self):
#         self.attacks=self.health-self.damage
#         return self.attacks

#     def heals(self):
#         self.heal=self.health-self.attacks
#         return self.heal

#     def level_up(self):
#         self.level=0
#         if self.attacks<1000:
#             return self.level-10
#         else:
#             return self.level+10


# class Archer(Personage):
#     def __init__(self, health, mana, damage, type, skill, name):
#         super().__init__(health, mana, damage, type, skill, name)
#     def attack(self):
#         return super().attack()
#     def heals(self):
#         return super().heals()
#     def level_up(self):
#         return super().level_up()


# class Paladin(Personage):
#     def __init__(self, health, mana, damage, type, skill, name):
#         super().__init__(health, mana, damage, type, skill, name)
    
#     def attack(self):
#         return super().attack()

#     def heals(self):
#         return super().heals()
    
#     def  level_up(self):
#          return super().level_up()

# class Mushtariy(Personage):
#     def __init__(self, health, mana, damage, type, skill, name):
#         super().__init__(health, mana, damage, type, skill, name)
    
#     def attack(self):
#          return super().attack()
#     def heals(self):
#         return super().heals()
#     def level_up(self):
#         return super().level_up()

# hero=Personage(2000,100,150,"Protagonist","Shoot","Persogage")
# hero_2=Archer(1000,200,150,'Warrior','Beat',"Archer")
# hero_3=Paladin(9000,300,150,'Ranger','Kill',"PAladin")
# hero_4=Mushtariy(800,400,150,'Mage','Destroy',"Wizard")

# print(hero_3.attack(),hero_3.level_up(),hero_3.heals())
# print(hero_2.attack(),hero_2.level_up(),hero_2.heals())
# print(hero_4.attack(),hero_4.level_up(),hero_4.heals())

# class Person():
#     def __init__(self,name='Bekzod',age=19):
#         self.name=name
#         self.age=age
#     # def __str__(self):
#     #     return f' Name is {self.name} and age is {self.age}'
#     def __repr__(self):
#         return f' Name  is {self.name} and age is {self.age}'
# per=Person('Monika',1000)
# per2=Person('Monika',400)
# print(per)
# print(per2)
# class Point():
#     def __init__(self,x=0,y=0):
#         self.x=x
#         self.y=y
#     def __str__(self):
#         return f'Fisrt = {self.x}, second= {self.y}'.format(self.x,self.y)
#     def __add__(self,other):
#         x=self.x+other.x
#         y=self.y+other.y
#         return Point(x,y)

# p1=Point(20,50)
# p2=Point(30,78)

# result=p1+p2
# print(result)

# print(p2)
# print(p1)
# print(p2.x,p1.x)

# a=input('Write your answer ')
# b=[]
# question_1='Where do you study: a) Amity b) Inha c) Turin d) MDIS'
# if  a in question_1:
#     b.append('Amity')
#     print(b)
# elif a in question_1:
#     b.append('Inha')
#     print(b)
# elif a is question_1:
#     b.append('Turin')
#     print(b)
# elif a is question_1:
#     b.append('MDIS')
#     print(b)

# right_answer=[]
# wrong_answer=[]
# point_skip=[]
# right=0
# wrong=0
# point=0
# question_1=int(input('100+50= (zero can be used for skipping).Answer: '))
# if question_1==150:
#     right_answer.append(question_1)
#     right+=1
# elif question_1==0:
#     point+=1
#     point_skip.append(question_1)
# elif question_1!=150:
#     wrong_answer.append(question_1)
#     wrong-=0.25


# question_2=int(input('100+90= '))
# if question_2==190:
#     right_answer.append(question_2)
#     right+=1
# elif question_2==0:
#     point+=1
#     point_skip.append(question_2)
# elif question_2!=190:
#     wrong_answer.append(question_2)
#     wrong-=0.25

# question_3=int(input('10+90= '))
# if question_3==100:
#     right_answer.append(question_3)
#     right+=1
# elif question_3==0:
#     point+=1
#     point_skip.append(question_3)
# elif question_3!=190:
#     wrong_answer.append(question_3)
#     wrong-=0.25


# print(f'Right answer {right} list is {right_answer}')
# print(f'Wrong answer {wrong} list is {wrong_answer}')
# print(f'Point is {point} skipping was {point_skip}')

# percentage=right*100/3
# if percentage>86:
#     print(f'Your score: A. Percentage {percentage}%')
# elif 75 < percentage < 86:
#     print(f'Your score: B. Percentage {percentage}%')
# elif 65 < percentage < 75:
#     print(f'Your score: C. Percentage {percentage}%')
# elif percentage <65:
#     print(f'Your score: F. Percentage {percentage}%')
# class Data:
#     def __init__(self,number_1,number_2):
#         self.number_1=number_1
#         self.number_2=number_2

#     def __mul__(self,other):
#         return Data(self.number_1* other.number_1,self.number_2*other.number_2)

# a=Data(56,90)
# b=Data(23,98)
# c=a*b
# d=a*b
# print(c.number_1,d.number_2)

# class Point:
#     def __init__(self,first,second):
#         self.first=first
#         self.second=second

#     def __sub__(self,other):
#         return Point(self.first-other.first,self.second-other.second)

# a=Point(345,987)
# b=Point(666,999)
# c=a-b
# d=a-b
# print(c.first,d.second)

# class Point:
#     def __init__(self,x):
#         self.x=x
#     def __floordiv__(self,other):
#         return Point(self.x//other.x)
#     def __truediv__(self,other):
#         return Point(self.x/other.x)
# a=Point(90)
# b=Point(45)
# c=a//b
# d=a/b
# print(d.x)
# print(c.x)

# class Character:
#     def __init__(self,name,surname,age):
#         self.name=name
#         self.surname=surname
#         self.age=age
#     def __eq__(self,other):
#         return Character(self.name==other.name,self.surname==other.surname,self.age==other.age)


# per1=Character("Bekzod",'Rashidov',90)
# per2=Character('Jony','Muminov',90)
# p3=(per1==per2)
# print(p3.name,p3.surname,p3.age)
# class Animal:
#     def __init__(self,name) :
#         self.name=name

# class Bird(Animal):
#     def __init__(self, name,last_name,color,wings,food):
#         super().__init__(name)
#         self.last_name=last_name
#         self.color=color
#         self.wings=wings
#         self.food=food
#     def __str__(self):
#         return f'Name {self.name}, last_name: {self.last_name} '
#     def __repr__(self):
#         return f'color: {self.color}, wings {self.wings}'


# data_base_1=Animal('Eleghant')
# data_base_2=Bird('Eagle','Sharik','White',5555,'meat')
# print(data_base_2)

class Family:
    def __init__(self,father,mother,children):
        self.father=father
        self.mother=mother
        self.children=children
    
    def info_father(self):
        print(f'Father is {self.father}') 
    
    def info_mother(self):
        print(f'Mother is {self.mother}') 
    
    def info_children(self):
        print (f'Children is {self.children}')

class Family_2(Family):
    def __init__(self, father, mother, children):
        super().__init__(father, mother, children)
    
    def info_father(self):
        print(f'Father is {self.father}') 
    
    def info_mother(self):
        print(f'Mother is {self.mother}') 
    
    def info_children(self):
        print (f'Children is {self.children}')

first_family=Family('Zafar','Munira','sher')
second_family=Family_2('Kamol','Zumrat','lola')

for family in (first_family,second_family):
    family.info_mother()
    family.info_children()