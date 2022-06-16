from selenium import webdriver
import time
import discord_webhook

driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver')
URL = "localhost:4040"

urls = []

driver.get(URL)
urlList = driver.find_elements_by_tag_name("a")
for url in urlList:
    if "tcp" in url.text:
        urls.append(url.text)

time.sleep(10)

discord_webhook.send_msg(ssh=urls[0], vnc=urls[1])

driver.quit()