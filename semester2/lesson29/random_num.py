import random

def find_num(x,guess):
    if 0<guess<11:
        if guess==x:
            print("Вы гений")
    else:
        print("Enter number range 1-10")
        return False



x=random.randint(1,10)
while True:
    guess=int(input("Find secret number in range 1-10: "))
    if 0<guess<11:
        if guess==x:
            print("Вы гений")
            break
    else:
        print("Enter number range 1-10")
        