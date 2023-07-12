import os
import sys
import json
import string
import random
import time
import unittest
import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.edge.service import Service as eService
from selenium.webdriver.chrome.service import Service as cService
from selenium.webdriver.safari.service import Service as sService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import unittest
# options=Options()
# options.chrome_executable_path="/usr/local/bin/chromedriver"
# driver=webdriver.Chrome(options=options)
# d={"3443":"創意", "00878":"國泰永續高股息", "00892":"富邦台灣半導體","00713":"元大台灣高息低波","2610":"華航","2337":"旺宏","2303":"聯電",
# "0050":"元大台灣50","0056":"元大台灣高股息"}
# driver.get("https://leetcode.com/accounts/login/")
# find_number=driver.find_element(By.ID, "id_login")
# find_number.send_keys("3443")

# driver.get("https://www.wantgoo.com/stock")
# time.sleep(5)
# find_number=driver.find_element(By.TAG_NAME, "input")


class AllStock:
    def __init__(self):
        self.l = []
        self.l1 = []
        self.ln = []
        self.options = Options()
        self.options.chrome_executable_path = "/usr/local/bin/chromedriver"
        self.driver = webdriver.Chrome(options=self.options)
        self.d = {"3443": "創意", "00878": "國泰永續高股息", "00892": "富邦台灣半導體", "00713": "元大台灣高息低波",
             "2610": "華航", "2337": "旺宏", "2303": "聯電",
             "0050": "元大台灣50", "0056": "元大台灣高股息"}
    def stockname(self):

        for i in self.d.keys():
            self.driver.get("https://www.wantgoo.com/stock")
            time.sleep(5)
            find_number = self.driver.find_element(By.TAG_NAME, "input")
            find_number.send_keys(i)
            time.sleep(3)
            find_number.send_keys(Keys.ENTER)
            time.sleep(3)
            name_list = self.driver.find_elements(By.CLASS_NAME, "breadcrumb-item")

            for name in name_list:
                self.l.append(name.text)
                time.sleep(3)

        for j in range(len(self.d)):
            self.l1.append(self.l[j*3+2])

        for i in self.l1:
            for j in i.split():
                if i.split().index(j)/2 == 0:
                    self.ln.append(j)
        return self.ln


class Test(unittest.TestCase):
    def setUp(self):
        self.AS = AllStock()
        self.d = {"3443": "創意", "00878": "國泰永續高股息", "00892": "富邦台灣半導體", "00713": "元大台灣高息低波",
                  "2610": "華航", "2337": "旺宏", "2303": "聯電",
                  "0050": "元大台灣50", "0056": "元大台灣高股息"}

    def tearDown(self):
        print("teardown")

    def test_is_right_name(self):
        rst = self.AS.stockname()
        print(rst)
        print(self.d.values())
        self.assertEqual(rst, self.d.values())


