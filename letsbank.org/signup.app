
from signup import SignupApp
from sixthday import Form


class LetsBankSignupApp(SignupApp):

    def setupRequiredFields(self):
        ## set up default and required fields:
        f = Form(Account())
        f.require("fname")
        f.require("lname")
        f.require("email")
        f.require("username")
        self.f = f

    def checkDuplicates(self):
        name = self.f["username"]
        if self.clerk.match(Account, username=name):
            self.errors.append({"error":"sorry, that name is taken"})


if __name__=="__main__":
    
    print >> RES, LetsBankSignupApp(REQ, CLERK, RES,
                                    thankspage='thanks.html').act()
