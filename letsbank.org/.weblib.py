
## import sys
## print "content-type: text/plain"
## print
## sys.stderr = sys.stdout

from sqlLetsbank import dbc
from letsbank import DBMAP, Account
from arlo import Clerk
from storage import MySQLStorage
CLERK = Clerk(MySQLStorage(dbc), DBMAP)

ENG.do_on_exit(dbc.close)

from weblib import Sess, SessPool
sess = Sess(SessPool.SqlSessPool(dbc), REQ, RES)
sess.start()
ENG.do_on_exit(sess.stop)

