import Keywords
import Config
import POM.LoginPom as LP
from Logger import Logger
logger=Logger()
def LoginFBandVerifyTitle():
    LP.enterUserNameandPassword(Config.get_test_data("UserName"),Config.get_test_data("PassWord"))
    LP.clickLoginButton()
    value=Keywords.get_TitleofPage()
    Keywords.assert_text_contains(Config.get_test_data("Title"),value)