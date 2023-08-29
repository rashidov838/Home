from datetime import date
class Calculationss:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day

    def found(self):
        years=write//365
        years_2=years*365
        days=write-years_2
        weeks=days//7
        weeks_minus=weeks*7
        last=days-weeks_minus
        return f'\n Years: {years}\n Weeks: {weeks}\n Days: {last} '  

    
info=Calculationss(360,12,30)
write=int(input('write your number: ' ))
print(info.found())
# Exercise2
class String():
    def __init__(self,strings):
        self.strings=strings
    def string(self):
        enter=input('Write string: ')
        if enter in text:
            return f'The substring exists in the string'
        else:
            raise ValueError

str_1=String('someting') 
text='techstudy the complete debugging solution'
print(str_1.string())

# # Exercise3
def is_pangram(s):
     return not set('abcdefghijklmnopqrstuvwxyz') - set(s.lower())
print(is_pangram('The quick brown fox jumps over the lazy dog.'))