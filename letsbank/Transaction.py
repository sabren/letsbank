
from letsbank import Account
from strongbox import *
from pytypes import FixedPoint

class Transaction(Strongbox):
    amount = attr(FixedPoint)
    src = link(Account)
    dst = link(Account)

