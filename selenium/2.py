from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.chrome_executable_path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(options=options)
driver.get("https://www.ptt.cc/bbs/Stock/index.html")
element = WebDriverWait(driver,10).until(
EC.presence_of_element_located((By.LINK_TEXT,"‹ 上頁")))
time.sleep(2)
# element = driver.find_elements(By.CLASS_NAME, "title")
# time.sleep(3)
# for i in element:
#     print(i.text)
element.click()
time.sleep(2)
