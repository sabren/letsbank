from letsbank import Account
from sixthday import Auth

#@TODO: this is almost exactly like rantelope.AuthorAuth :/

class AccountAuth(Auth):
    def __init__(self, sess, clerk):
        Auth.__init__(self, sess, {})
        self.clerk = clerk
        
    def validate(self, dict):
        if ("username" in dict) and ("password" in dict):
            match = self.clerk.match(Account, username=dict["username"])
            if match and match[0].password == dict["password"]:
                return match[0].ID
        return None


    def fetch(self, key):
        self.account = clerk.fetch(Account, key)

    def prompt(self, message, action, hidden):
        model = {"message": message,
                 "action": action,
                 "hidden": hidden, }
        #@TODO: make this return a string
        self._sess._response.write(zebra.fetch("login", model))
        
