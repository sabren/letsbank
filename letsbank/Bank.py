
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

    def balanceFor(self, username):
        a = self.getAccount(username)
        return a.balance
        
    ## transfer management:

    def transfer(self, source, dest, amount):
        if amount <= 0: raise ValueError("amount must be postive")
        try:
            s = self.getAccount(source)
            d = self.getAccount(dest)
            s.balance -= amount
            d.balance += amount
            # this line stores all three objects (because of the links):
            self.clerk.store(Transaction(src=s, dst=d, amount=amount))
        except Exception, e:
            raise Exception("transaction failed: %s" % e)
