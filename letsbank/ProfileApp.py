
import zebra
from sixthday import App

class ProfileApp(App):

    def __init__(self, input, response, bank):
        super(ProfileApp, self).__init__(input)
        self.bank = bank
        self.response = response

    def act_(self):
        whom = self.input.get("user")
        assert whom, "please specify a user in the query string"
        self.model["history"] = self.bank.historyFor(whom)
        self.model["balance"] = self.bank.balanceFor(whom)
        if self.input.get("format")=="xml":
            self.response.contentType = "text/xml"
            self.write(zebra.fetch("profile-xml", self.model))
        else:
            self.write(zebra.fetch("profile", self.model))
        
