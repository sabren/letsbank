
from letsbank import Account

class Bank(object):

    def __init__(self, clerk):
        self.clerk = clerk
    
    def getAccount(self, username):
        try:
            return self.clerk.match(Account, username=username)[0]
        except:
            raise KeyError(username)

    def allAccounts(self):
        return self.clerk.match(Account)

    def countAccounts(self):
        return len(self.allAccounts())
        

    def transfer(self, source, dest, amount):
        assert amount > 0, "amount must be postive"
        try:
            complete = 0
            s = self.getAccount(source)
            d = self.getAccount(dest)
            s.balance -= amount
            d.balance += amount
            self.clerk.store(s)
            self.clerk.store(d)
            complete = 1
        finally:
            assert complete, "transaction failed" #@TODO: now what?
            

    def createAccount(self, username, password):
        self.clerk.store(Account(username=username,
                                 password=password))


    def balanceFor(self, username):
        a = self.getAccount(username)
        return a.balance
        
