

from letsbank import AccountAuth
from letsbank import Bank
from letsbank import BankingApp

AUTH = AccountAuth(sess, CLERK)
AUTH.check()

BANK = Bank(CLERK)
print >> RES, BankingApp(REQ, BANK, AUTH.account).act()
