# import csv
# with open('semester2\lesson1\doc.txt','r') as file:
#     reader=csv.reader(file)
#     for i in reader:
#         # for line in lines:
#         # print(len(i))
        
        
# file.close()




with open('semester2\lesson1\doc.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(len(line))


 
colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('semester2\lesson1\doct1.txt', 'w') as file:
    for color in colors:
        file.write(color + '\n')



