import unittest
from letsbank import Account


class AccountTest(unittest.TestCase):

    def test_simple(self):
        a = Account()
        assert a.balance == 0


if __name__=="__main__":
    unittest.main()
    
