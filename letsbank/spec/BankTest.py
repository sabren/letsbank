import unittest
from letsbank import Bank, Transaction, Account
from arlo import MockClerk

def sum(xs):
    if len(xs):
        return xs[0] + sum(xs[1:])
    else:
        return 0

class BankTest(unittest.TestCase):

    def setUp(self):
        self.clerk = MockClerk({
            Transaction.__attrs__['dst']: (Account, "dstID"),
            Transaction.__attrs__['src']: (Account, "srcID"),
            }) 
        b = Bank(self.clerk)
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


    def test_positive(self):
        """
        you can't give someone a debt, or a 'nothing'
        """
        self.assertRaises(ValueError, self.bank.transfer, "wanda", "rufus", -1)
        self.assertRaises(ValueError, self.bank.transfer, "wanda", "rufus", 0)


    def test_history(self):
        assert len(self.clerk.match(Transaction)) == 0
        self.bank.transfer("wanda", "rufus", 1)
        assert len(self.clerk.match(Transaction)) == 1
        t = self.clerk.fetch(Transaction, 1)
        assert t.src.username=='wanda'
        assert t.dst.username=='rufus'
        assert t.amount == 1



if __name__=="__main__":
    unittest.main()
    
