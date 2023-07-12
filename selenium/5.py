from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.chrome_executable_path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(options=options)
driver.get("https://www.youtube.com/")
video_title=driver.find_elements(By.ID,"video-title")
sum=0
for j in range(5):
    print(sum)
    sum += 1
    for i in video_title:
        print(i.text)
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(3)



