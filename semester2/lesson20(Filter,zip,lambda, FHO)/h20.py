def func(element):
    count=0
    if isinstance(element,list):
        for el in element:
            count+=func(el)
    else:
        count+=1
    return count
print(func([2, [2 , 3, [[[[[[[[5]]]]]]]]]]))


def filter(func, iterable):
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result


def map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result
