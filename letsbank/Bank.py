
from letsbank import Account
from letsbank import Transaction

class Bank(object):

    def __init__(self, clerk):
        self.clerk = clerk

    ## account management:
    
    def getAccount(self, username):
        try:
            return self.clerk.match(Account, username=username)[0]
        except:
            raise KeyError(username)

    def allAccounts(self):
        return self.clerk.match(Account)

    def countAccounts(self):
        return len(self.allAccounts())
        

    def createAccount(self, username, password):
        self.clerk.store(Account(username=username,
                                 password=password))
            
    def balanceFor(self, username):
        a = self.getAccount(username)
        return a.balance
        
    ## transfer management:

    def transfer(self, source, dest, amount):
        if amount <= 0: raise ValueError("amount must be postive")
        try:
            complete = 0
            s = self.getAccount(source)
            d = self.getAccount(dest)
            s.balance -= amount
            d.balance += amount
            self.clerk.store(s)
            self.clerk.store(d)
            complete = 1
        except:
            raise Exception("transaction failed") #@TODO: now what?
        self.clerk.store(Transaction(src=s, dst=d, amount=amount))
