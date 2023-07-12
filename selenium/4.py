import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.chrome_executable_path = "/usr/local/bin/chromedriver"

options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
driver = webdriver.Chrome(options=options)
driver.get("https://ashine02.medium.com/在-mac-os-上設置-git-server-83dc6009fc03")
time.sleep(3)
logs = driver.get_log('performance')
time.sleep(3)
start_timestamp = None
end_timestamp = None

false = False
true = True


for entry in logs:
    data = entry['message']
    messaged = eval(data)
    if messaged["message"]["method"] == 'Network.requestWillBeSent':
        if start_timestamp is None:
            start_timestamp = messaged["message"]["params"]["timestamp"]
    elif messaged["message"]["method"] == 'Network.loadingFinished':
        end_timestamp = messaged["message"]["params"]["timestamp"]
print(start_timestamp)
print(end_timestamp)

# print(messaged["message"]["params"]["timestamp"])
# print(messaged)


    # if messaged["message"]["params"]["timestamp"] == 'Network.responseReceived':
    #     if start_timestamp is None:
    #         start_timestamp = messaged['timestamp']
    # elif messaged["message"]["params"]["timestamp"] == 'Network.loadingFinished':
    #     end_timestamp = messaged['timestamp']

load_time = end_timestamp - start_timestamp
print("页面加载时间：", load_time, "毫秒")
# print(start_timestamp)
# print(messaged)
# print(type(messaged))
