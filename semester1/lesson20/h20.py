def sort_by_length(arr):
    return sorted(arr,key=len)
a=["Telescopes", "Glasses", "Eyes", "Monocles"]
print(sort_by_length(a))
# Next
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
# Next
my_sentence = "Jessica found a dollar on the ground"
print("Original sentence: ", my_sentence)
print(sorted(my_sentence.split(), key=len))