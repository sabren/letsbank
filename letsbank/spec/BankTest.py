import unittest
from letsbank import Bank, Transaction, Account, DBMAP
from arlo import MockClerk

def sum(xs):
    if len(xs):
        return xs[0] + sum(xs[1:])
    else:
        return 0

class BankTest(unittest.TestCase):

    def setUp(self):
        """
        our test bank has two accounts: wanda and rufus.
        """
        self.clerk = MockClerk(DBMAP)
        self.clerk.store(Account(username="rufus"))
        self.clerk.store(Account(username="wanda"))
        self.bank = Bank(self.clerk)        


    def test_zerosum(self):
        """
        LETS currency is a zero sum game.
        Every credit holding account is offset
        by another account holding debt.
        """
        zeroSum = lambda :\
                  0 == sum([a.balance for a in self.clerk.match(Account)])
        assert zeroSum()
        self.bank.transfer("rufus", "wanda", 5, "test")
        self.assertEquals(self.bank.balanceFor("rufus"), -5)
        self.assertEquals(self.bank.balanceFor("wanda"), 5)
        assert zeroSum()


    def test_positive(self):
        """
        you can't give someone a debt, or a 'nothing'
        """
        self.assertRaises(ValueError, self.bank.transfer, "wanda", "rufus", -1, "whatever")
        self.assertRaises(ValueError, self.bank.transfer, "wanda", "rufus", 0, "whatever")

    def test_transfer_to_self(self):
        self.assertRaises(ValueError, self.bank.transfer, "wanda", "wanda", 1, "self transfer")


    def test_history(self):
        assert len(self.clerk.match(Transaction)) == 0
        self.bank.transfer("wanda", "rufus", 1, "history test")
        assert len(self.clerk.match(Transaction)) == 1
        t = self.clerk.fetch(Transaction, 1)
        assert t.src.username=='wanda'
        assert t.dst.username=='rufus'
        assert t.amount == 1
        assert self.clerk.match(Account, username='wanda')[0].balance == -1

        assert len(self.bank.historyFor("wanda")) == 1


if __name__=="__main__":
    unittest.main()
    
