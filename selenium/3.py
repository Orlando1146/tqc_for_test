import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.chrome_executable_path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(options=options)
driver.get("https://github.com/Orlando1146?tab=repositories")
time.sleep(2)
driver.execute_script("window.open('https://ithelp.ithome.com.tw/articles/10263959')")
time.sleep(2)
handles = driver.window_handles
print(len(handles))
print(handles)
driver.switch_to.window(handles[0])
time.sleep(2)

elements_from_git = driver.find_elements(By.CLASS_NAME,"vcard-names ")
print("The followimg are from Git")
for i in elements_from_git:
    print(i.text)

time.sleep(2)

driver.switch_to.window(handles[-1])

elements_from_blog = driver.find_elements(By.CLASS_NAME,"header")

time.sleep(2)
print("The followimg are from Blog")

for i in elements_from_blog:
    print(i.text)

