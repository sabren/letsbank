from Account import Account
from Transaction import Transaction
from Bank import Bank
from AccountAuth import AccountAuth

DBMAP = {
    Account: "bank_account",    
    Transaction: "bank_transaction",    
    Transaction.__attrs__['dst']: (Account, "dstID"),
    Transaction.__attrs__['src']: (Account, "srcID"),
    }


