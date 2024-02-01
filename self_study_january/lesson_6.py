# import numbers
# numbers=[1,2,3,4,"Hello",123,53,75,5,2,3,3,3]
# numbers.append("Hi")
# print(numbers)


# second_list=["It is my program"]
# numbers.extend(second_list)
# print(numbers)
# numbers+=[77,4]
# print(numbers)

# print(numbers*20)

# print(numbers.pop())
# print(numbers)

# numbers.remove(123)
# print(numbers)

# print(numbers.count(3))

# print(list(str(i)for i in numbers))

# matrix =[[2,3,4],[5,6,7]]
# print(matrix[1][1])


# try:
#     random=tuple(1)
# except Exception as e:
#     print(e)
# finally:
#     print("It is completed")

# information=' .. "C:/Users/WINDOWS 10/AppData/Local/Programs/Python/Python310/python.exe" "c:/Users/WINDOWS 10/Documents/Githome/self_study_january/lesson_6.py"'

# print(dict( val for val in  enumerate(information.split('/'))))
# splited_string='Split me  ! random'
# random=["HIIIIIIIIII"]
# print(random)
# print(''.join(random))


# numbers=(2,3,4,5)
# print(numbers[3])

# numbers=((4,5),4.5,"asd",[11,55,22])
# print(numbers[3][2])

# numbers[3][1]="Heii"
# print(numbers)

# print(type(numbers))


# a=('banana','mango','apple',"fama",'amigo')
# b=12,32,43,65,86
# c=True,False,None
# print(a)
# print(b)
# print(c)

# --------------------------------------------------------------------
info=('banana','mango','apple',"fama",'amigo',"cherry", "orange", "kiwi")
# print(info[-2])
# print(info[1:4])
# print(info[2:])

# print(info[:2])
# print(info[-3:-1])

# if 'fama' in info:
#     print("Good")
# elif "amigo" in info:
#     print("Not bad")
# else:
#     print('Bad')

# second_info=list(info)
# second_info.append('Normalno budet')
# print(second_info)
# x=('yuiop',123)
# second_info+=x
# print(second_info)

# 12
x=('yuiop',123)
# new_info=list(x)
# new_info.remove(123)
# print(new_info)

a=('banana','mango','apple',"fama",'amigo',"cherry", "orange", "kiwi")
# (first,*second,third)=a
# print(first)
# print(second)
# print(third)

# for i in a:
#     print(a)

for i in range(len(a)):
    print(i)
# ///////////////////////////////////
i=0
while i<len(a):
    break
# ///////////////////////////////////

tuple_mul=a*10
print(tuple_mul)
print(tuple_mul.count("kiwi"))

info=(1,00,3,3,3,3,4567890,3,4,12)
x=info.index(4567890)
print(x)