# import random
# gueses_made=0
# counter=0
# number=random.randint(0,100)
# print("Загадано число от 0 до 100, отгадайте какое?")
# while  gueses_made<100:
#     guess=int(input('guesss'))
#     gueses_made+=1
#     if guess< number:
#         break
#     if abs(number-guess)<100:
#         print('тепло', end='')
#         counter+=1
#     else:
#         print('Холодно',end='')
#         counter+=1
#     if guess < number:
#         print("(нужно больше)")
#         counter+=1

#     if guess > number:
#         print("(нужно меньше)")
#         counter+=1

# if guess==number:
#     print('Ты угадал мое число!')
# else:
#     print('Не угадалю Я загадал {0}'.format(number))
# print(counter)

# import random
# gueses_made=0
# counter=0
# x=random.randint(0,100)
# print("Загадано число от 0 до 100, отгадайте какое?")
# while  gueses_made<10:
#     guess=int(input('guesss'))
#     gueses_made+=1
    
#     if guess < x: 
#         counter +=1
#         print("Нужно число побольше")
#     if guess > x: 
#         counter +=1
#         print("Нужно число поменьше")
#     if guess == x: 
#         counter +=1
#         print("Поздравляем, ты угадал(a) число!")
#         break
#     print(guess)
#     print ("Ваши попытки: " + str(counter))

# # if counter==1:
# #     money+=100000
# #     print(f'Won'+ str(money))
# # if counter==2:
# #     money+=350
# #     print(f'Won'+ str(money))
# # if counter==3:
# #     money+=300
# #     print(f'Won'+ str(money))
# # if counter==4:
# #     money+=200
# #     print(f'Lose'+ str(money))
# # if counter==5:
# #     money+=100
# #     print(f'Lose'+ str(money))
# # if counter==6:
# #     money+=0
# #     print(f'Lose'+ str(money))
# # if counter==7:
# #     while counter >=7:
# #         money-=100
# #         print(f'Lose'+ str(money))
# counter_2=0
# while counter_2<10:
#     money=0
#     if counter==1:
#         money+=100000
#         print(f'Won'+ str(money))
#     elif counter==2:
#         money+=350
#         print(f'Won'+ str(money))
#     elif counter==3:
#         money+=300
#         print(f'Won'+ str(money))
#     elif counter==4:
#         money+=200
#         print(f'Lose'+ str(money))
#     elif counter==5:
#         money+=100
#         print(f'Lose'+ str(money))
#     elif counter==6:
#         money+=0
#         print(f'Lose'+ str(money))
#     elif counter==7:
#         money-=100
#         print(f'Lose'+ str(money))
#     elif counter==8:
#         money-=100
#         print(f'Lose'+ str(money))
#     elif counter==9:
#         money-=100
#         print(f'Lose'+ str(money))
#     elif counter==10:
#         money-=100
#         print(f'Lose'+ str(money))
#     counter_2+=1
# print(money)
