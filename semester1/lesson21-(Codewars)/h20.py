def sort_by_length(arr):
    return sorted(arr,key=len)
a=["Telescopes", "Glasses", "Eyes", "Monocles"]
print(sort_by_length(a))
# Next
def process_data(data):
    result=1
    differences=[]
a=["Telescopes", "Glasses", "Eyes", "Monocles"]
print(sort_by_length(a))
# https://www.codewars.com/kata/586e1d458cb711f0a800033b/train/python
# Thinkful - List and Loop Drills: Lists of lists
def process_data(data):
    result=1
    differences=[]
    for sub_list in data:
        differences.append(sub_list[0]-sub_list[1])
    for difference in differences:
        result *=difference
    return result
    
# [2, 5] --> 2 - 5 --> -3
# [3, 4] --> 3 - 4 --> -1
# [8, 7] --> 8 - 7 --> 1
# ['i', 'have','no','space']---->['i','ihave','ihaveno','ihavenospace']
def spacey(array):
    strr = ''
    out = []
    for el in array:
        strr += str(el)
        out.append(strr)
    return out
a=['i', 'have','no','space']
print(spacey(a))
print(spacey(a))
# Next
my_sentence = "Jessica found a dollar on the ground"
print("Original sentence: ", my_sentence)
print(sorted(my_sentence.split(), key=len))
print(sorted(my_sentence.split(), key=len)) 

# * 'Hello world'   => true
# * ' Hello world'  => false
# * 'Hello world  ' => false
# * 'Hello  world'  => false
# * 'Hello'         => true  
def valid_spacing(s):
    return s == ' '.join(s.split())
print(valid_spacing('Hello world  '))