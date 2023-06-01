database = {
    "name": "Samik",
    "surname": "Rashidov",
    "name": "Bekzod",
    "surname": "Rashidov",
}


def authorize(func):
    def wrapper(*args, **kwargs):
        print("Hello")
        return func(*args, **kwargs)

    return wrapper


@authorize
def Information_about_person(name, surname):
    for key, val in database.items():
        if val == name:
            return f"{name } {surname}"
        elif val != name:
            print("Please register")
            input_name = "Samina"
            input_surname = "Xasanova"
            database.update({"name": input_name, "surname": input_surname})
            return  database


print(Information_about_person("Samina", "Xasanova"))


@authorize
def shopping():
    database_of_products = {"tomato": 300, "potato": 299, "kola": 111}
    counter = 0
    bought = {}
    while counter < 3:
        pr = input("Write your product:")

        # if pr not in database:
        #     print('Not found product\n\n')
        for key, val in database_of_products.items():
            if key == pr:
                bought[pr] = {}
                bought[pr]["price"] = val
                quantity = 12
                bought[pr]["quantity"] = quantity
                amount = quantity * val
                bought[pr]["amount"] = amount
                tax = 10
                total_tax = (amount - tax) / 100
                bought[pr]["tax"] = total_tax
                last_price=amount - total_tax
                bought[pr]["total"] =last_price 
        print(f'Product is {key} quantity: {quantity} amount:{amount} total_tax: {total_tax} last_price:{last_price} ')
        
        counter += 1
shopping()