"""
    Name: Võ Viết Thanh
    Date:30/10/2021
    File: rational.py
    This module defines the SavingsAccount class.
"""
class SavingsAccount(object):
    RATE = 0.02

    def __init__(self,name,pin,balance = 0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self):
        result = 'Name ' + self.name + "\n"
        result += 'Pin ' + self.pin + "\n"
        result += 'Balance ' + str(self.balance) + "\n"
        return result

    def getbalance(self):
        return self.balance

    def getname(self):
        return self.name

    def getpin(self):
        return self.pin

    def deposit(self, amount):
        self.balance += amount
        return None

    def withdraw(self, amount):
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return None

    def computeInterest(self):
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest

class Bank(object):
    def __init__(self):
        self.accounts = {}

    def __str__(self):
        return '\n'.join(map(str, self.accounts.values()))

    def makeKey(self, name, pin):
        return name + "/" + pin

    def add(self, account):
        key = self.makeKey(account.getName(),
                           account.getPin())
        self.accounts[key] = account
    def remove(self, name, pin):
        key = self.makeKey(name, pin)
        return self.accounts.pop(key, None)

    def get(self, name, pin):
        key = self.makeKey(name, pin)
        return self.accounts.get(key, None)

    def computeInterest(self):
        total = 0.0
        for account in self.accounts.values():
            total += account.computelnterest()
        return total

def test_bank():
    bank = Bank()
    bank.add(SavingsAccount("Jackson", "2991", 4000.00))
    bank.add(SavingsAccount("Emma", "2997", 7000.00))
    print(bank)
    print(f"bank.computeInterest: ", bank.computeInterest())


if __name__=='__main__':
    test_bank()