def sort_by_length(arr):
    return sorted(arr,key=len)

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