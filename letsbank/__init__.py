from Account import Account
from Transaction import Transaction
from Bank import Bank
from AccountAuth import AccountAuth
from BankingApp import BankingApp
from ProfileApp import ProfileApp

DBMAP = {
    Account: "bank_account",    
    Transaction: "bank_transaction",    
    Transaction.__attrs__['dst']: (Account, "destID"),
    Transaction.__attrs__['src']: (Account, "sourceID"),
    }


