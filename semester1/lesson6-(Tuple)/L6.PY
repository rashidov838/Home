 # import numbers

# numbers=[1,2,3,4, "Hello",5,6,7,8,9]
# numbers.append()
# print(numbers)

#Extend list by appending elements from the iterable 

# numbers.extend([2,3,4])
# print(numbers)

# numbers=numbers+[77,4]
#1+2=3
#'dsa' +"asd"='dsaasd'
#print(numbers*2)

#Полиморфизм

#count

# numbers.pop()
# print(numbers)
# numbers.remove('Hello')
# numbers.remove('Hello')
# print(numbers)

# #numbers.remove('Tee')

# numbers_of_occurence=numbers.count(3)
# print('count',numbers_of_occurence)

# numbers.sort()
# print(numbers)

# numbers.sort()
# print(numbers,reverse=True)

# words=['foo','aasd',"hfdgdg"]
# words.sort()
# print(words)
#Матрица
# [2,3,4,5,6] #
# matrix=[[2,3,4],[5,6,7]]
# print(matrix[1][1]) 
# 2 3 4
# 5 6 7
#random=list(1) #error
#random=list(True) #error
# random=list('Random !)(!@#$%^&*()') #error
# splited_string='Split me  ! random'.split("me  !") # ' '
# print(random,splited_string,''.join(random),sep='\n')
#Tuple - кортеж (итерабле)
import numbers


numbers=(2,3,4,5,6)
print(numbers,numbers[3])
numbers=((4,5),4.5,"asdf",[4,56,7])
print(numbers,numbers[3])
#number[1]='Changed"
#Read and Create

numbers=(2,3,4,[5,6])
numbers[3][0]=24
print(numbers[3],numbers[3][0])
  
#
numbers=([2,3,4],[5,6],7,8,9)
numbers[0][2]
print(numbers[0][2])

numbers=(2,3,4)
print('1', type(numbers),numbers)

numbers=tuple()
print(type(numbers),numbers)

numbers=()
print(type(numbers),numbers)

numbers=5,6,7
print('last',type(numbers),numbers)
