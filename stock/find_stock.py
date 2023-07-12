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
options=Options()
options.chrome_executable_path="/usr/local/bin/chromedriver"
driver=webdriver.Chrome(options=options)
d={"3443":"創意", "00878":"國泰永續高股息", "00892":"富邦台灣半導體","00713":"元大台灣高息低波","2610":"華航","2337":"旺宏","2303":"聯電",
"0050":"元大台灣50","0056":"元大台灣高股息"}
# driver.get("https://leetcode.com/accounts/login/")
# find_number=driver.find_element(By.ID, "id_login")
# find_number.send_keys("3443")

driver.get("https://www.wantgoo.com/stock")
time.sleep(5)
find_number=driver.find_element(By.TAG_NAME, "input")
l=[]
l1=[]
ln=[]

for i in d.keys():
    driver.get("https://www.wantgoo.com/stock")
    time.sleep(5)
    find_number = driver.find_element(By.TAG_NAME, "input")
    find_number.send_keys(i)
    time.sleep(3)
    find_number.send_keys(Keys.ENTER)
    time.sleep(3)
    name_list = driver.find_elements(By.CLASS_NAME, "breadcrumb-item")

    for name in name_list:
        l.append(name.text)
        time.sleep(3)

for j in range(len(d)):
    l1.append(l[j*3+2])


for i in l1:
    for j in i.split():
        if i.split().index(j)/2==0:
            ln.append(j)


class AllStock:
    def __init__(self,ts):
        self.tsn=ts


    def stockname(self):
        return ln


class Test(unittest.TestCase):
    def test_is_rightname(self):
        rst=AllStock.stockname()
        self.assertTrue(rst,d.values())
