
import unittest
from letsbank import Bank
from arlo import MockClerk


def sum(xs):
    if len(xs):
        return xs[0] + sum(xs[1:])
    else:
        return 0


class BankTest(unittest.TestCase):

    def setUp(self):
        b = Bank(MockClerk())
        assert b.countAccounts() == 0

        b.createAccount("rufus", "pass")
        b.createAccount("wanda", "word")
        assert b.countAccounts() == 2
        self.bank = b 


    def test_zero(self):
        """
        LETS currency is a zero sum game.
        Every credit holding account is offset
        by another account holding debt.
        """
        sumIsZero = lambda: sum([a.balance
                                 for a in self.bank.allAccounts()]) == 0
        assert sumIsZero()
        self.bank.transfer("rufus", "wanda", 5)
        self.assertEquals(self.bank.balanceFor("rufus"), -5)
        assert self.bank.balanceFor("wanda") == 5
        assert sumIsZero()



if __name__=="__main__":
    unittest.main()
    
