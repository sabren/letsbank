
from letsbank import Account
from strongbox import *
from pytypes import FixedPoint, Date

class Transaction(Strongbox):
    amount = attr(FixedPoint)
    posted = attr(Date, default="now")
    note = attr(str, okay=lambda s: len(s) <= 255)
    src = link(Account)
    dst = link(Account)

