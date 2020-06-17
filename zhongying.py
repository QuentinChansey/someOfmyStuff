# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchElementException

#driver = webdriver.Firefox(executable_path="C:\Program Files (x86)\geckodriver.exe")
PROXY = "127.0.0.1:10808"
#PATH = "/usr/lib/chromium-browser/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=socks5://%s' % PROXY)
driver = webdriver.Chrome(options=chrome_options)
#driver = webdriver.Chrome(PATH)
driver.get("URL")   #URL like https://abc.com

username = driver.find_element_by_id("input-login-account")
username.send_keys("USERNAME")   #USERNAME
password = driver.find_element_by_id("input-login-password")
password.send_keys("PASSWORD")  #PASSWORD

login = driver.find_element_by_link_text("登录")
login.click()

try:
    known = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT,"我已知道"))
    )
    known.click()
except:
    driver.quit()
    
while(True):
    try:
        noMission = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "dps-alert"))
        )
        driver.refresh()
    except:
        pass
    try:
        Text = driver.find_element_by_xpath("//div[@id='loading-text']/a[1]")
        Text.click()
    except:
        pass
