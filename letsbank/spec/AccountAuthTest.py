
from arlo import MockClerk
from letsbank import DBMAP, Account, AccountAuth
import unittest

class AccountAuthTest(unittest.TestCase):

    def test_validate(self):
        clerk = MockClerk(DBMAP)
        clerk.store(Account(username="fred", password="rufus"))

        auth = AccountAuth({}, clerk)
        assert not auth.validate({"username":"fred",
                                  "password":"ftempy"})



if __name__=="__main__":
    unittest.main()
    
