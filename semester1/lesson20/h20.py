def sort_by_length(arr):
    return sorted(arr,key=len)

a=["Telescopes", "Glasses", "Eyes", "Monocles"]
print(sort_by_length(a))
def spacey(array):
    strr = ''
    out = []
    for el in array:
        strr += str(el)
        out.append(strr)
    return out
a=['i', 'have','no','space']
print(spacey(a))