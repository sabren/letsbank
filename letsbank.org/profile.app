
from letsbank import Bank
from letsbank import ProfileApp

BANK = Bank(CLERK)
print >> RES, ProfileApp(REQ, RES, BANK).act()
