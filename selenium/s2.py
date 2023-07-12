from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
options=Options()
options.chrome_executable_path="/usr/local/bin/chromedriver"
driver=webdriver.Chrome(options=options)
# driver.maximize_window()
driver.get("https://www.ptt.cc/bbs/Stock/index.html")
# print(driver.page_source)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(5)
tit=driver.find_elements(By.CLASS_NAME,"title")
for i in tit:
    print(i.text)

