
from arlo import MockClerk
from letsbank import schema, Account, AccountAuth
import unittest

class AccountAuthTest(unittest.TestCase):

    def test_validate(self):
        clerk = MockClerk(schema)
        clerk.store(Account(username="fred", password="rufus"))

        auth = AccountAuth({}, clerk)
        assert not auth.validate({"username":"fred",
                                  "password":"ftempy"})

        assert auth.validate({"username":"fred",
                              "password":"rufus"})



if __name__=="__main__":
    unittest.main()
    
