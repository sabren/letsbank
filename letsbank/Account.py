
from strongbox import *
from pytypes import FixedPoint

class Account(Strongbox):
    ID = attr(long)
    username = attr(str)
    password = attr(str)
    balance = attr(FixedPoint, default=0)

    def transfer(self, other, amount):
        assert isinstance(other, Account)
        other.balance += amount
        self.balance -= amount
    
