
from pytypes import FixedPoint
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
        balance = 0 
        for item in self.historyFor(username):
            balance += item["change"]            
        return balance


    def historyFor(self, username):
        # @TODO: THIS SUCKS!! NEED TO ADD QUERIES TO ARLO
        a = self.getAccount(username)
        history = [t for t in self.clerk.match(Transaction)
                   if (t.src.ID == a.ID) or (t.dst.ID == a.ID)]
        history.sort(lambda a,b: cmp(a.posted, b.posted))
        res = []
        for t in history:
            change = t.amount
            if t.src.ID == a.ID:
                change *= -1
                other = t.dst.username
            else:
                other = t.src.username
            res.append({"posted":t.posted,
                        "change":change,
                        "other":other,
                        "note":t.note,})
        return res
    
    
        
    ## transfer management:

    def transfer(self, source, dest, amount, note):
        try:
            amount = FixedPoint(amount)
        except:
            raise ValueError("badamt")
        if amount <= 0: raise ValueError("nonpos")
        if source==dest: raise ValueError("xferself")
        try:
            s = self.getAccount(source)
            d = self.getAccount(dest)
            s.balance -= amount
            d.balance += amount
            # this line stores all three objects (because of the links):
            self.clerk.store(Transaction(src=s, dst=d, amount=amount,
                                         note=note))
        except Exception, e:
            raise Exception("transaction failed: %s" % e)
