import csv
# import json
# comprised_users=[]
# with open('password.csv',newline='') as file:
#     all_info=csv.DictReader(file,delimiter=',')
#     for row in all_info:
#         comprised_users.append(row['Username'])
#     print(comprised_users)
#     with open('comprised_users.txt',mode='w') as file:
#         for i in comprised_users:
#             file.write(f'{i}\n')  
# boss_message_dict = {
#     "recipient": "The Boss",
#     "message": "Mission Success",
# }
# with open('boss_message.json',"w") as file:
#     json.dump(boss_message_dict,file)

# info=[["    _  _     ___   __  ____   " ],
#    [ "  / )( \   / __) /  \(_  _) " ],          
#    [ "  ) \/ (  ( (_ \(  O ) )(   "],     
#     ["  \____/   \___/ \__/ (__)  "],           
#     [" _  _   __    ___  __ _  ____  ____ "], 
#     ["  / )( \ / _\  / __)(  / )(  __)(    \ "], 
#     ["  ) __ (/    \( (__  )  (  ) _)  ) D ( "],
#     ["  \_)(_/\_/\_/ \___)(__\_)(____)(____/ "],
#     ["            ____  __     __   ____  _  _"], 
#     ["    ___   / ___)(  )   / _\ / ___)/ )( \ "],
#     ["   (___)  \___ \/ (_/\/    \\___ \) __ ( "],
#     [ "         (____/\____/\_/\_/(____/\_)(_/"],
#     ["    __ _  _  _  __    __                "],
#     ["    (  ( \/ )( \(  )  (  )               "],
#     ["    /    /) \/ (/ (_/\/ (_/\             "],
#     ["    \_)__)\____/\____/\____/"]]
# with open('new_passwords.csv','w',newline="",encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerows(info)
PRODUCTS = [
    {
        "product_name": "sweater",
        "count": 10,
        "price": 100,
        "type": "black",
    },
    {
        "product_name": "sweater",
        "count": 10,
        "price": 100,
        "color": "black",
    }
]


USERS = [
    {
        'name': 'Behruz',
        'password': '234fjfdsd',
        'email': 'behruz@gmail.com',
        'purchases': [],
        'card': {'code': '3647583465734283', 'balance': 1000}
    }
]



class StoreOwner:
    pass


class Store:
    purchases = []

    def __init__(self, name, email, password, card_code, card_balance):
        self.name = name
        self.email = email
        self.password = password
        self.card_code = card_code
        self.card_balance = card_balance

    @classmethod
    def login(cls, email, password):
        if not (email and password):
            return 'Empty values were given.'
        for user in USERS:
            if user['email'] == email and user['password'] == password:
                return cls(user['name'], email, password, user['card']['code'], user['card']['balance'])
        return 'Wrong email or password'

    @classmethod
    def register(cls, name, email, password, card_code, card_balance):

        users_data=[]
        user_keys=""
        with open("users.csv") as users:
            users_reader=csv.DictReader(users,delimiter=";")
            user_keys=users_reader.fieldnames
            for row in users_reader:
                users_data.append(
                    {
                    "id":row["id"],
                    "name":row["name"],
                    "password":row["password"],
                    "email":row["email"],
                    "purchases":row["purchases"],
                    "card_code":row["card_code"],
                    "card_balance":row["card_balance"],
                    }
                )

        for user in users_data:
            if user['email'] == email and user['password'] == password:
                return "Пользователь с такими данными уже есть."

        if not (name and email and password and card_code and card_balance):
            return 'Empty values were given.'
        if name.isalpha() and '@' in email and len(password) >= 6 and len(card_code) == 16 and card_balance >= 0:
            
            
            with open("users.csv",mode="a",newline="") as users_file:
                users_writer=csv.DictWriter(users_file,fieldnames=user_keys,delimiter=";")
                users_writer.writerow({
                    "id":int(users_data[-1]["id"])+1,
                    "name": name,
                    "password":password,
                    "email": email,
                    "purchases":[],
                    "card_code":card_code,
                    "card_balance":card_balance,
                }
                )



            # USERS.append(
            #     {
            #         'name': name,
            #         'password': password,
            #         'email': email,
            #         'purchases': [],
            #         'card': {'code': card_code, 'balance': card_balance}
            #     }
            # )
            return cls(name, email, password, card_code, card_balance)
        else:
            return 'Wrong credentials!'

    def purchase(self, product):
        if product not in PRODUCTS.keys():
            return 'Not available!'
        if self.card_balance <= 0:
            return "Not enough money!"

        for key, val in PRODUCTS.items():
            if key == product and self.card_balance - val >= 0:
                self.card_balance -= val
                self.purchases.append(product)
                for id, user in enumerate(USERS):
                    if user["email"] == self.email:
                        USERS[id]['purchases'].append(product)
                PRODUCTS.pop(key)
                return f'\nSuccesfully bought {product} and added into purchases!\nBalance: {self.card_balance}\nYour purchases: {self.purchases}'

        return f'{self.name} | {self.card_balance}: Not enough money.'

user_1=Store.register("Random","skjhikjdafds@gmail.com","adsfsfasdsa12312","31213213498849465546",10000)   