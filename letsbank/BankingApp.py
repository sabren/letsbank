
import zebra
from sixthday import AdminApp
from letsbank import Account
from strongbox import BoxView
from pytypes import FixedPoint

class BankingApp(AdminApp):

    MESSAGES = {
        "transok": "transfer successful!",
        "badamt": "invalid amount!",
        }

    def __init__(self, input, bank, account):
        super(BankingApp, self).__init__(bank.clerk, input)
        self.bank = bank
        self.account = account
        self.model["message"] = ""
        self.model["username"] = account.username
        
        #@TODO: filter this for demurrage... :)
        self.model["users"] = [a.username for a in self.clerk.match(Account)
                               if a.username != self.account.username]

    def act_(self):
        self.act_main()

    def act_main(self):
        if self.input.get("msg") in self.MESSAGES:
            self.model["message"] = self.MESSAGES[self.input["msg"]]
        hist = self.bank.historyFor(self.account.username)
        self.model["transactions"] = [{"posted":t.posted,
                                       "amount":t.amount,
                                       "source":t.src.username,
                                       "dest":t.dst.username,
                                       "note":t.note,} for t in hist]
        self.write(zebra.fetch("main", self.model))

    def act_transfer(self):
        try:
            amount = FixedPoint(self.input["amount"])
        except:
            self.redirect("banking.app?action=main&msg=badamt")
        self.bank.transfer(self.account.username,
                           self.input["dest"],
                           amount, self.input.get("note"))
        self.redirect("banking.app?action=main&msg=transok")
        
