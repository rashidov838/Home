USERS=[{'name': 'Bekzod',
        'email': 'qwerty@gmail.com',
        'password': '1111',
        'purchases': [],
        'balance':700,
}]
class Bancomat():
    def __init__(self,password, card_balance):
        self.card_balance=card_balance
        self.password=password
    
    @classmethod
    def passwords(cls,password):
        if not password:
            return 'Empty values were given'
        for i in USERS:
            if i['password']==password:
                return cls(password,i['balance'])

        return 'Wrong password'
    def check_balances(self,check_balance):
        if  check_balance  in USERS:
            return 'Not available'
        for key,val in USERS.items():
            if key== and val>3:
                return f'\n Your balance is {val}'
            else:
                return f'Not ooooo'
    
user_1=Bancomat(1,2)
enter_your_password='enter'
if enter_your_password=='enter':
    user_1=Bancomat.passwords('1111')
    if isinstance(user_1,Bancomat):
        print(user_1.check_balances('balance'))
    else:
        print('Wrong email or password')

for user in USERS:
    print(user)
    
