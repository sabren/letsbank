
from letsbank import AccountAuth
AUTH = AccountAuth(sess, CLERK)
AUTH.check()

#from letsbank import BankingApp
#print >> RES, BankingApp().act()
