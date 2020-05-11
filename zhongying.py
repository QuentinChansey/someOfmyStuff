# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox(executable_path="C:\Program Files (x86)\geckodriver.exe")
driver.get("https://www.juzijianzhi.com/studio/room/1")

username = driver.find_element_by_id("input-login-account")
username.send_keys("13662382812")
password = driver.find_element_by_id("input-login-password")
password.send_keys("o;.;,fn+lE&=JH\j~gOH")

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
