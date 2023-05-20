def authorize(func):
    def wrapper(*args,**kwargs):
        print("Hello")
        return func(*args,**kwargs)
    return wrapper

@authorize
def Information_about_person(name,surname):
    database={'name':'Samik', 'surname':'Rashidov','name':'Bekzod', 'surname':'Rashidov'}
    for key,val in database.items():
        if val==name:
            return f'{name } {surname}'
        elif val!=name:
            print("Please register")
            input_name='Samina'
            input_surname='Xasanova'
            database.update({'name':input_name,'surname':input_surname})
            return database


print(Information_about_person('Samina','Xasanova'))


@authorize
def shopping():
    database_of_products={'tomato':300,'potato':299,'kola':111}
    counter=0
    bought={}
    list_product=[]
    while counter<3:
        pr=input("Write your product:")
        for key,val in database_of_products.items():
            if key==pr:
                bought[pr]=val
                list_product.append(bought)
                print(list_product)
            if key!=pr:
                print(f" we dont this product{pr}")
                continue
            #     bought.update({key:val})
            # list_product.append(bought)
            # print(list_product)
        counter+=1      
                
shopping()



# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

# people[3] = {}

# people[3]['name'] = 'Luna'
# people[3]['age'] = '24'
# people[3]['sex'] = 'Female'
# people[3]['married'] = 'No'

# print(people[3])