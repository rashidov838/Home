# unmuataable:(str,float,none)
# On lesson :     list tuple dict set bin
# For self-study:  complex decimal fraction 
# a=2
# a=3
# s='asdsdasd'
# s[0]='r'#error
# Можете сами почитать про: 
#     complex 
#     Decimal 
#     Fraction 
 
# Изменяемые 
#     set - множество 
#     dict - словарь 
#     list - список 
 
# Неизменяемые 
#     bin 
#     frozenset - множество 
#     tuple - кортеж 
#     int 
#     float 
#     str 
#     bool 
#     None
names=[]
print(names)
names=list()
print(names)
names=[1,2,3,4,5,12.5,'abcd',True, False]
print(names)
names[0]=False
print(names)
names[7]='good'
print(names)
print(names[7][0])
names=[[1,2,3],[4.5,5.6,6.7],['go','gp1','go2']]
print(names[2][2])

# Нарезка Slice
# итерировать проходиться по элементам итерируемых перемных(эти такие переменые которые могут хранить большое одного значения)
# 
numbers=[4,5,6,10,22,55,500]
# 

# [начало:конец]
print(numbers[1:5])
print(numbers[:],numbers)
print(numbers[1:])
print(numbers[:5])

# [начало:конец:шаг]
print(numbers[1:5:2])
print(numbers[:6],numbers)
print(numbers[::2])
print(numbers[::10])

print(numbers[-1])




