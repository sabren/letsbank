
from letsbank import Account
from strongbox import *
from pytypes import FixedPoint, DateTime

class Transaction(Strongbox):
    ID = attr(long)
    amount = attr(FixedPoint)
    posted = attr(DateTime, default="now")
    note = attr(str, okay=lambda s: len(s) <= 255)
    src = link(Account)
    dst = link(Account)

