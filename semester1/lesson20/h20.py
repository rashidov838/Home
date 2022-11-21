def process_data(data):
    result=1
    differences=[]

    for sub_list in data:
        differences.append(sub_list[0]-sub_list[1])
    for difference in differences:
        result *=difference
    return result