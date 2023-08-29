import datetime
class Bancomat():
    def __init__(self,login,password,balance):
        self.login=login
        self.password=password
        self.balance=balance
    def log(self):
        self.enter_password=1111
        self.enter_login='Bekzod'
        if self.enter_login==self.login and self.enter_password==self.password:
            return f'Welcome {self.login}'
        if self.enter_login!=self.login and self.enter_password==self.password:
            return 'Wrong login' 
        if self.enter_login==self.login and self.enter_password!=self.password:
            return 'Wrong password'

    def Balance(self):
        x = datetime.datetime.now()
        return f'Your balance {self.balance} \nDate  is {x}'

    def Issuance_cash(self):
        quantity=int(input('Quantity: '))
        if quantity<self.balance:
            reminder_1=self.balance-quantity
            reminder_2=(quantity*3)/100
            reminder_3=reminder_1-reminder_2
            x = datetime.datetime.now()
            return f'You took  {quantity}, your balance {reminder_3}, percentage was taken {reminder_2} \nDate  is {x}'
        if quantity>self.balance:
            return f'Not available'
    def Contribution(self):
        quantity = int(input('Quantity: '))
        invest=self.balance+quantity
        x = datetime.datetime.now()
        return f'Your balance was:  ' + str(self.balance) + ' but now your balance: ' + str(invest)+ f'\nDate  is {x}'


    def Exchange(self):
        quantity = int(input('Quantity $: '))
        rate = 11236
        reminder_exchange_1 = self.balance - (rate * quantity)
        reminder_exchange_2 = (rate * quantity * 10) / 100
        reminder_exchange_3 = reminder_exchange_1 - reminder_exchange_2
        x = datetime.datetime.now()
        if reminder_exchange_3 >0:
            return f'Your balance was:  ' + str(self.balance) + f', before taken percentage : ' + str(reminder_exchange_1) + ' but now your balance after taken percentage: ' + str(reminder_exchange_3) + f'\nDate  is {x}'
        if reminder_exchange_3<0:
            return f'Not available,because your balance was:  ' + str(self.balance) + f', before taken without percentage : ' + str(reminder_exchange_1) + ' but balance after taken with  percentage: ' + str(reminder_exchange_3)+ f'\nDate  is {x}'
    def Transfer(self):
        self.choose_card=input('Choose card: 1.Humo 2.Uzcard: ')
        if self.choose_card=='1':
            print(st1.Transfer_Humo())
        if self.choose_card=='2':
            print(st1.Transfer_Uzcard())
        
    def Transfer_Humo(self):
        self.quantity = int(input('Quantity: '))
        self.balance_2=self.balance- self.quantity
        self.percentage=self.quantity*0.5/100
        self.reminder=self.balance_2-self.percentage
        x = datetime.datetime.now()
        return f'Now your balance is : {self.reminder}, your balance was  {self.balance}, perentage was taken {self.percentage} \nDate  is {x}'
        
    def Transfer_Uzcard(self):
        self.quantity = int(input('Quantity: '))
        self.balance_2=self.balance- self.quantity
        self.percentage=self.quantity*1/100
        self.reminder=self.balance_2-self.percentage
        x = datetime.datetime.now()
        return f'Now your balance is : {self.reminder}, your balance was  {self.balance}, perentage was taken {self.percentage} \nDate  is {x}'
    def register(self):
            self.name=input('Write your name: ')
            if self.name.isalpha():
                pass
            else:
                raise SystemExit
            self.email=input("Write your email: ")
            a='@'
            if a in self.email:
                pass
            else:
                raise SystemExit
            self.password=input("Write your password ")
            if  len(self.password)==4:
                pass               
            else:
                raise SystemExit
            self.card=input("Write your number of card: ")
            if  len(self.card)==4:
                pass
            else:
                raise SystemExit
            self.amount=int(input("Your amount: "))
    
   
            self.registers=[{'name': self.name,
                            'email': self.email,
                            'password': self.password,
                            'card': {'code' :self.card,'money':self.amount}
                                     }]
            return self.registers
    def Balance_1(self):
        x = datetime.datetime.now()
        return f'Your balance {self.amount} \nDate  is {x}'

    def Issuance_cash_1(self):
        self.quantity=int(input('Quantity: '))
        if self.quantity<self.amount:
            reminder_1=self.amount-self.quantity
            reminder_2=(self.quantity*3)/100
            reminder_3=reminder_1-reminder_2
            x = datetime.datetime.now()
            return f'You took  {self.quantity}, your balance {reminder_3} percentage was taken {reminder_2} \nDate  is {x}'
        if self.quantity>self.amount:
            return f'Not available'
    def Contribution_1(self):
        self.quantity = int(input('Quantity: '))
        self.invest=self.amount+self.quantity
        x = datetime.datetime.now()
        return f'Your balance was:  ' + str(self.amount) + ' but now your balance: ' + str(self.invest)+ f'\nDate  is {x}'


    def Exchange_1(self):
        self.quantity = int(input('Quantity $: '))
        self.rate = 11236
        reminder_exchange_1 = self.amount - (self.rate * self.quantity)
        reminder_exchange_2 = (self.rate * self.quantity * 10) / 100
        reminder_exchange_3 = reminder_exchange_1 - reminder_exchange_2
        x = datetime.datetime.now()
        if reminder_exchange_3 >0:
            return f'Your balance was:  ' + str(self.amount) + f', before taken percentage : ' + str(reminder_exchange_1) + ' but now your balance after taken percentage: ' + str(reminder_exchange_3) + f'\nDate  is {x}'
        if reminder_exchange_3<0:
            return f'Not available,because your balance was:  ' + str(self.amount) + f', before taken without percentage : ' + str(reminder_exchange_1) + ' but balance after taken with  percentage: ' + str(reminder_exchange_3)+ f'\nDate  is {x}'
    def Transfer_1(self):
        self.choose_card=input('Choose card: 1.Humo 2.Uzcard: ')
        if self.choose_card=='1':
            print(st1.Transfer_Humo_1())
        if self.choose_card=='2':
            print(st1.Transfer_Uzcard_1())
        
    def Transfer_Humo_1(self):
        self.quantity = int(input('Quantity: '))
        self.balance_2=self.amount-self.quantity
        self.percentage=self.quantity*0.5/100
        self.reminder=self.balance_2-self.percentage
        x = datetime.datetime.now()
        return f'Now your balance is : {self.reminder}, your balance was  {self.amount}, perentage was taken {self.percentage} \nDate  is {x}'
        
    def Transfer_Uzcard_1(self):
        self.quantity = int(input('Quantity: '))
        self.balance_2=self.amount- self.quantity
        self.percentage=self.quantity*1/100
        self.reminder=self.balance_2-self.percentage
        x = datetime.datetime.now()
        return f'Now your balance is : {self.reminder}, your balance was  {self.amount}, perentage was taken {self.percentage} \nDate  is {x}'

st1=Bancomat('Bekzod',1111,55550000)
enter_method=input('Choose method: register or login: ')
if enter_method=='login':
    print(st1.log())
    choose=input('choose 1.Balance 2.Issuance of cash 3.Contribution 4.Exchange 5.Transfer :  ')
    if  choose=='1':
        print(st1.Balance())
    if choose=='2':
        print(st1.Issuance_cash())
    if  choose=='3':
        print(st1.Contribution())
    if choose=='4':
        print(st1.Exchange())
    if choose=='5':
        print(st1.Transfer())
if enter_method=='register':
    print(st1.register())
    choose=input('choose 1.Balance 2.Issuance of cash 3.Contribution 4.Exchange 5.Transfer :  ')
    if  choose=='1':
        print(st1.Balance_1())
    if choose=='2':
        print(st1.Issuance_cash_1())
    if  choose=='3':
        print(st1.Contribution_1())
    if choose=='4':
        print(st1.Exchange_1())
    if choose=='5':
        print(st1.Transfer_1())