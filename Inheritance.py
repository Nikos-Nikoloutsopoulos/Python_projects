
class BackAccount():
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f"Account {self.account_number} has $ {self.balance}"

    def deposit(self,amount):
        self.balance += amount

    def can_withdraw(self,amount):
        return self.balance >= amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -=amount
            return True
        return False

class CheckAccount(BackAccount):
    def __init__(self, account_number, balance=0, mounthly_fee=1.5):
        super().__init__(account_number, balance)
        self.mounthly_fee= mounthly_fee

    def deduct_fee(self):
        self.balance -= self.mounthly_fee

    def can_withdraw(self,amount):
        return True
    
    def withdraw(self, amount):
        self.balance -= 35
        super().withdraw(amount)



class SavingAccount(BackAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.05):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest=self.balance*self.interest_rate
        self.balance+=interest

    def withdraw(self, amount):
        self.balance +=20
        super().withdraw(amount)
    

account=BackAccount("1234567890",100)
print(account)

account.deposit(3000)
print(account)

account.withdraw(4000)

print(account)

print("----------1-------")
account1=CheckAccount("a1b2", 500)
account1.deduct_fee()
print(account1)
account1.deposit(500)
account1.deduct_fee()
print(account1)

print("----------2-------")
account2=SavingAccount("3c4d", 400)
account2.add_interest()
print(account2)
account2.deposit(500)
account2.add_interest()
print(account2)

print("----------3-------")
account3=CheckAccount("a1b2", 500)
print(account3)
print(account3.can_withdraw(1000))
account3.withdraw(1000)
print(account3)

print("----------4-------")
account4=SavingAccount("a1b2", 500)
print(account4)
print(account4.can_withdraw(500))
if account4.can_withdraw(500):
    account4.withdraw(500)
else:
    print("Not enough monay")
print(account4)