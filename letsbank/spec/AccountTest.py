import unittest
from letsbank import Account


class AccountTest(unittest.TestCase):


    def test_simple(self):
        a = Account()
        assert a.balance == 0
        a2 = Account()
        a.transfer(a2, 1)
        assert a.balance == -1
        assert a2.balance == 1



if __name__=="__main__":
    unittest.main()
    
