import re
# Task-1
staff = {
    'Austin': {
        'floor managers': 1,
        'sales associates': 5
    },
    'Melbourne': {
        'floor managers': 0,
        'sales associates': 8
    },
    'Beijing': {
        'floor managers': 2,
        'sales associates': 5
    },
}

def print_staff_report(location, staff_dict):
    managers = staff_dict['floor managers']
    sales_people = staff_dict['sales associates']
    
    print('Instrument World ' + location + ' has:')
    print(str(sales_people) + ' sales employees')
    print(str(managers) + ' floor managers')
    try:
        ratio = sales_people / managers
        print('The ratio of sales people to managers is ' + str(ratio))
    except ZeroDivisionError as err:
        print(f'The ratio of sales people to managers is not available because we have {err}')

        
for location, staff in staff.items():
    print_staff_report(location, staff)

# ____________________________________________________________________________________________________________________________________________________
# TAsk-2
# Используя исключения, исправьте код ниже и создайте собственное исключение, которое должно вывести ошибку, если количество покупаемых больше 
# количеств товаров в наличии. Также добавьте сообщение для созданного исключения с строкой: 'We don't' + str(self.supply) + ' in stock'
inventory = {
    'Piano': 3,
    'Lute': 1,
    'Sitar': 2
}

def submit_order(instrument, quantity):
    try:
        supply = inventory[instrument]
    except KeyError as err:
        print(f'We dont have' + str(err) + 'in stock')
    for inv in inventory:
        name=inv
        id=inventory[name]
        try:
            id- inventory[quantity]
        except KeyError as err:
            print(f'Quantity: {err} is bigger than  {id}')
        

instrument = 'Guitar'
quantity = 5
print(submit_order(instrument, quantity))
# ____________________________________________________________________________________________________________________________________________________
#Task-3

titles = [
    "Middle JavaScript Developer",
    "Middle JavaScript Developer (AngularJS 9)",
    "Middle JavaScript Developer (React)",
    "Senior JavaScript Developer (Angular)",
    "middle JavaScript angularjs "
]
pattern_angularjs=re.compile("angularjs")
for i in titles:
    print(pattern_angularjs.findall(i))

pattern_angularjs=re.compile("AngularJS")
for i in titles:
    print(pattern_angularjs.findall(i))


pattern_javascript=re.compile("JavaScript")
for i in titles:
    print(pattern_javascript.findall(i))

pattern_node_js=re.compile(" node js")
for i in titles:
    print(pattern_node_js.findall(i))

pattern_react=re.compile("React")
for i in titles:
    print(pattern_react.findall(i))
# ____________________________________________________________________________________________________________________________________________________