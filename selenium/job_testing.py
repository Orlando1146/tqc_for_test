from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from lxml import etree
options = Options()
options.chrome_executable_path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(options=options)
driver.get("https://ithelp.ithome.com.tw/articles/10263959")
driver.get("https://github.com/Orlando1146?tab=repositories")
time.sleep(3)

# id = driver.find_elements(By.CLASS_NAME,"header__inner clearfix")
# # id = driver.find_elements_by_class_name("header")
#
# time.sleep(5)
# for i in id:
#     print(i.text)



# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# </body></html>
# """

# html = driver.find_element(By.XPATH,'//a/@href')
# url = html.find_elements("href")
# for i in html:
#     print(i)
"""
同時多個網頁要切換測試需要怎麼做?
使用 driver.window_handles 得到所有網頁視窗的 list
再用 driver.switch_to.window() 切換 windows = driver.window_handles
driver.switch_to.window(windows[-1])
"""

driver.switch_to.window()
windows = driver.window_handles
driver.switch_to.window(windows[-1])



