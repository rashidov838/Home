# **** 
# *  *  
# *  * 
# **** 
# square_line = 4 
# star = "*" 
# star_width = star * square_line 
# print(star_width) 
# print(f"{star}  {star}") 
# print(f"{star}  {star}") 
# print(star_width) 
# for i in range(square_line): 
#     print(star, end="") 
   
# square_line = 4 
# star = "*" 
# star_width = star * square_line 
# for i in range(square_line):
#     if i>0 and i<(square_line-1):
#         empty_space=' ' *(square_line-2)
#         print(f'{star}{empty_space}{star}')
#     else:
#         print(star*square_line) 



# i=0 
# while i<10:
#     print('i=', i )
#     i +=1


# i=0
# while True:
#     i +=1
#     print('i=', i )
#     if i==100:
#         break

names=[1,2,3,4,5,6,8]
i=0
while i<len(names):
    print(names[i])
    i +=1

s='qwertyui'
for i in range(len(s)):
    print(s[i])
for i,val in enumerate('qwertyui'):  
  print(i,val)

# square_line = 4 
# star = "*" 
# star_width = star * square_line 
# while i in range(square_line):
#     if i>0 and i<(square_line-1):
#         empty_space=' ' *(square_line-2)
#         print(f'{star}{empty_space}{star}')
#     else:
#         print(star*square_line) 

a=[1, 1, 2, 3, 4, 4, 5, 3]
print(set(a))
# Создать программу, которая сортирует словарь по ключу и возвращает в ответ список из кортежей 
# sort_dict({3:1, 2:2, 1:3}) == [(1,3), (2,2), (3,1)] 
# sort_dict({1:2, 2:4, 3:6}) == [(3,6), (2,4), (1,2)]
a=({3:1, 2:2, 1:3})
print(sorted(a.items()))

# print(list(tuple(sorted(({3:1, 2:2, 1:3}),reverse=True))))
