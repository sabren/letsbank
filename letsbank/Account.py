
from strongbox import *
from pytypes import FixedPoint
from handy import randpass

                       

class Account(Strongbox):
    ID = attr(long)
    fname = attr(str)
    lname = attr(str)
    email = attr(str)
    username = attr(str)
    password = attr(str)

    def __init__(self, **args):
        super(Account, self).__init__(**args)
        if not self.password:
            self.password = randpass()
            
