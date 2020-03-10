import Keywords
import Config
#Login page elements
userName="//input[@id='email']"
passWord="//input[@id='pass']"
login="//input[@value='Log In']"
#Login functions
def enterUserNameandPassword(Usernamevalue,Passwordvalue):
    Keywords.enterInputValue(userName,Usernamevalue)
    Keywords.enterInputValue(passWord,Passwordvalue,20)
def clickLoginButton():
    Keywords.clikElement(login)
