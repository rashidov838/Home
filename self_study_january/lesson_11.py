# square_line = 4 
# star = "*" 
# for i in range(square_line):
#     if i>0 and i< (square_line-1):
#         empty=' '*(square_line-2)
#         print(f'{star}{empty}{star}')
#     else:
#         print(square_line*star)


# count=0
# while True:
#     count+=1
#     print(count)
#     if count==100:
#         break

# numbers=[1,2,3,4,5,6,8]
# count=0
# while count<len(numbers):
#     print(numbers[count]*4)
#     count+=1


# word='EURQPOEI'


# for i in range(len(word)):
#     print(word[i]*5)


# for id,val in enumerate(word):
#     print(id,val)

# a={3:1, 2:2, 1:3}
# print(sorted(a.items()))


# num=int(input("Write 6: "))
# for i in range(1,num+1):
#     print(' '*(num-i)+'* '*i)
# for i in range(1,num+1):
#     print(' '*(num-1)+'* '*1)

b=[2,3,4,5,6]


# for i in b:
#     if i%2==0:
#         print(f'Chetnoe: {i}')
#     else:
#         print(f'Nechetnoe: {i}')


faranheits = [20, 19, 24, 45, 140]

count=0
while count<len(faranheits):
    result=(faranheits[count]- 32) * 5 / 9
    count+=1 
    if result >= 50:
        print(f"Слишком горячо: {result}")
        continue
    else: 
        print(f"Жить можно: {result}")




