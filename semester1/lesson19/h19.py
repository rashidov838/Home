def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x
arr=[1,2,1,1,1,1,1]

stray(arr)
def filter_list(l):
    a=[]
    for i in l:
        if isinstance(i,(int)):
            a.append(i)
    return  a 
