from Account import Account
from Transaction import Transaction
from Bank import Bank
from AccountAuth import AccountAuth
from BankingApp import BankingApp
from ProfileApp import ProfileApp
from arlo import Schema

schema = Schema ({
    Account: "bank_account",    
    Transaction: "bank_transaction",    
    Transaction.dst: "destID",
    Transaction.src: "sourceID",
})


