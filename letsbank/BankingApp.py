
import zebra
from sixthday import AdminApp
from letsbank import Account
from strongbox import BoxView
from pytypes import FixedPoint

class BankingApp(AdminApp):

    MESSAGES = {
        "transok": "transfer successful!",
        "nonpos": "amount must be positive",
        "badamt": "invalid amount!",
        "xferself": "can't transfer money to yourself",
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
        self.model["history"] = self.bank.historyFor(self.account.username)
        self.model["balance"] = self.bank.balanceFor(self.account.username)
        self.write(zebra.fetch("main", self.model))

    def act_transfer(self):
        try:
            self.bank.transfer(self.account.username,
                               self.input["dest"],
                               self.input["amount"],
                               self.input.get("note"))
        except ValueError, e:
            self.input["msg"] = str(e)
            self.act_main()
        else:
            self.redirect("banking.app?action=main&msg=transok")
        
