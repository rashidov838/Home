# # 1
# a=('banana','mango','apple',"fama",'amigo')
# b=18,27,35,42,51,64,50,39,68,27
# c=True,False,None
# print(a)
# print(b)
# print(c)

# # 2
# d=('banana',34,89,False,'jake',None)
# print(d)

# # 3
# a=('banana','mango','apple',"fama",'amigo')
# b=18,27,35,42,51,64,50,39,68,27
# c=True,False,None
# print(type(a))
# print(type(b))
# print(type(c))
# #4
# e=tuple(('banana','mango','apple',"fama",'amigo'))
# print(e)
# #5
# a=('banana','mango','apple',"fama",'amigo')
# print(a[-2])
# print(a[2])
# #6
# a=('banana','mango','apple',"fama",'amigo')
# print(a[1:3])   # 1 from start     3 from end  A: mango, apple

# # #7
# a=('banana','mango','apple',"fama",'amigo')  #after apple it will not show items 
# print(a[:3])
# # 8
# a=('banana','mango','apple',"fama",'amigo') # Первые два слова не брать
# print(a[2:])
# # 9
# a=('banana','mango','apple',"fama",'amigo',"cherry", "orange", "kiwi")
# print(a[-4:-1]) #В начале 4 слова пропустить  и в конце пропустить 1 слово

# # # 10
# # a=('banana','mango','apple',"fama",'amigo',"cherry", "orange", "kiwi")
# if 'fama' in a:
#     print('Good')
# elif "amigo" in a:
#     print('So good')
# else:
#     print('Bad')
# # 11
# a=('banana','mango','apple',"fama",'amigo',"cherry", "orange", "kiwi")
# x=list(a)
# x[4]=1234
# print(x)
# # 12
# a=('banana','mango','apple',"fama",'amigo',"cherry", "orange", "kiwi")
# x=list(a)
# x.append('qwerty')
# a=tuple(x)
# print(a)
# # 13
# a=('banana','mango','apple',"fama",'amigo',"cherry", "orange", "kiwi")
# x=list(a)
# x.append('qwerty')
# a=tuple(x)
# print(x)
# print(a)
# #14
# a=('banana','mango','apple',"fama",'amigo',"cherry", "orange", "kiwi")
# x=('yuiop',)  #Запятую обязательно
# a += x
# print(a)

# #15
# a=('banana','mango','apple',"fama",'amigo',"cherry", "orange", "kiwi")
# x=list(a)
# x.remove('fama')
# a=tuple(x)
# print(a)

# #16
# a=('banana','mango','apple')
# (asd,fgh,hjk)=a  
# print(asd)
# print(fgh)
# print(hjk)      # В колонку вниз
# #17
# a=('banana','mango','apple',"fama",'amigo',"cherry", "orange", "kiwi")
# (asd,*fgh,hjk)=a   #Звездочка значит берет с mango до orange
# print(asd)
# print(fgh)
# print(hjk)
# #18
# a=('banana','mango','apple',"fama",'amigo',"cherry", "orange", "kiwi")
# for i in a:
#     print(i)    #Все в столбик вниз
 
#   #19
# a=('banana','mango','apple',"fama",'amigo',"cherry", "orange", "kiwi")
# for i in range(len(a)):
#     print(a)      #range size of 8

#  #20
# a=('banana','mango','apple',"fama",'amigo',"cherry", "orange", "kiwi")
# i=0
# while i<len(a):
#         print(a)

# #Join

a=("fama",'amigo',"cherry")
b=(1,2,3)
c=a+b
print(c)


# a=("fama",'amigo',"cherry")
# b=c*2
# print(b)

# #Method
# a=(1,2,3,4,5,6,7,5,6,5,7,6,5,4,5)
# x=a.count(6)
# print(x)    #count

a=(1,2,3,4,5,6,7,5,6,5,7,6,5,4,5)
x=a.index(6)
print(x)