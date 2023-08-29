import csv
import random 
# with open('semester1\lesson33\l33.csv','w', newline='') as file:
#     writer=csv.writer(file)
#     writer.writerow(["NO", "Player", "Record"])
#     writer.writerow([1, "Sabina", "1202"])
#     writer.writerow([2, "Farina", "1502"])
#     writer.writerow([3, "Tamina", "0507"])
#     name=4
#     lastname='Bekzod'
#     age='5088'
#     email='bekzod@gmail.com'
#     if '@'  in email:
#         info_about_me=[name,lastname,age]
#         info_about_me.append(email)
#         writer.writerow(info_about_me)
#     if '@' not in email:
#         info_about_me=[name,lastname,age]
#         writer.writerow(info_about_me)
    

#     file.close()


# with open('semester1\lesson33\l33.csv','r', newline='') as file:
#     reader=csv.reader(file)
#     for i in reader:
#         print(i)
#       file.close()
# row_list= [  ['NO','PLayer','Record'],
#                 [1,'PLayer_1','Record_1'],
#                 [2,'PLayer_2','Record_2'],
#                 [3,'PLayer_3','Record_3'],
#                 [4,'PLayer_4','Record_4']]

# row_list[0][2]='Money'
# with open('semester1\lesson33\l33.csv','w', newline='') as file:
#     writer=csv.writer(file)
#     writer.writerow(row_list)
#     file.close()



counter=0
start=0
money=0
tries=5
result=[]
x=random.randint(0,100)
print("\nGuess the infinite number")

while start <tries:
    number=int(input("Enter your number: "))
    start += 1

    if number < x: 
        counter +=1
        print("Enter number greater than this")
        result.append(number)
    if number > x: 
        counter +=1
        print("Enter number smaller than this")
        result.append(number)
    if number == x: 
        counter +=1
        print("\nYou find the random number. It's " + str(x))
        result.append(number)
        break
    

print ("\nYour number of attempts: " + str(counter))
row_list= ["Your number of attempts: " + str(counter)]
result_list=["Your number were : " + str(result)]
with open('semester1\lesson33\lesson33.csv','w', newline='') as file:
    writer=csv.writer(file)
    writer.writerow(result_list)
    writer.writerow(row_list)

    file.close()
    