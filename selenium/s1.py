from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.chrome_executable_path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(options=options)
# driver.maximize_window()
driver.get("https://www.ptt.cc/bbs/Stock/index.html")
# print(driver.page_source)
tit = driver.find_elements(By.CLASS_NAME,"title")
for i in tit:
    print(i.text)

link=driver.find_element(By.LINK_TEXT,"‹ 上頁")
link.click()
# driver.get("https://www.ptt.cc/bbs/Stock/index.html")
tit = driver.find_elements(By.CLASS_NAME,"title")
for i in tit:
    print(i.text)
# driver.save_screenshot("disney.png")

