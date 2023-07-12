import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import unittest
options=Options()
options.chrome_executable_path="/usr/local/bin/chromedriver"
driver=webdriver.Chrome(options=options)
driver.get("https://www.wantgoo.com/login/auth/apilogin")
class Enter:
    def __init__(self):
        self.account=driver.find_element(By.ID,"idUserName")
        time.sleep(3)
        self.password=driver.find_element(By.ID,"idPassword")
        time.sleep(3)

    def log_in(self, username, passwd):
        self.account.send_keys(username)
        time.sleep(3)
        self.password.send_keys(passwd)
        time.sleep(3)
        self.into = driver.find_element(By.ID, "btnLogIn")
        time.sleep(3)
        self.into.click()
        time.sleep(5)
        getword=driver.find_element(By.ID,"divMemberBlock")
        self.login = Enter()
        if getword.text =="sammisandy520":
            return True
        else:
            return False

# a=Enter()
# a.log_in("sammisandy520@hotmail.com","Ayu761311")

#
class TryLogin(unittest.TestCase):
    def setUp(self):
        self.login = Enter()

    def test_tt(self):
        rt=self.login.log_in("sammisandy520@hotmail.com","Ayu761311")

        self.assertEqual(rt,True)

        driver.get("https://www.wantgoo.com/login/auth/apilogin")

    def test_tf(self):
        rt=self.login.log_in("sammisandy520#hotmail.com","sheuy4")

        self.assertEqual(rt,False)

        driver.get("https://www.wantgoo.com/login/auth/apilogin")

    def test_ft(self):
        rt=self.login.log_in("sjdu@dhfu.com.tw","Ayu761311")

        self.assertEqual(rt,False)

        driver.get("https://www.wantgoo.com/login/auth/apilogin")

    def test_ff(self):
        rt=self.login.log_in("zkaic@yahoo.com","skdu3847")

        self.assertEqual(rt,False)

        driver.get("https://www.wantgoo.com/login/auth/apilogin")
