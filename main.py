from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver')
urls = []

driver.get("localhost:4040")
urlList = driver.find_elements_by_tag_name("a")
for url in urlList:
    if "tcp" in url.text:
        urls.append(url.text)

for i in urls:
    print(i)

time.sleep(10)
driver.quit()