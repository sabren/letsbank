from letsbank import Account
from sixthday import Auth
import weblib
import zebra

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
        self.account = self.clerk.fetch(Account, key)

    def prompt(self, message, action, hidden):
        model = {"message": message,
                 "action": action,
                 "hidden": hidden, }
        #@TODO: make this return a string
        self._sess._response.write(zebra.fetch("login", model))
        
    def _getAction(self):
        
        ## MAJOR KLUDGE HERE! #################################

        res = "banking.app"

        ####### this stuff is stolen from AUTH ################
        
        # add in a query string of our own:
        res = res + "?auth_check_flag=1"

        for item in self._sess._request.query.keys():
            if item[:5] == "auth_":
                pass # IGNORE old auth stuff
            else:
                res = res + "&" + weblib.urlEncode(item) + \
                      "=" + weblib.urlEncode(self._sess._request.query[item])
        return res
