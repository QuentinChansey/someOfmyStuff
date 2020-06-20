# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput import keyboard
import threading
#from selenium.common.exceptions import NoSuchElementException

combination = {keyboard.Key.ctrl_l,keyboard.Key.enter}
PROXY = "127.0.0.1:10808"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=socks5://%s' % PROXY)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https:/www.google.com")
driver.execute_script("window.open('');")
driver.switch_to_window(driver.window_handles[1])
driver.get("https://www.cilin.org/zidian/shouxie.html")
driver.execute_script("window.open('');")
driver.switch_to_window(driver.window_handles[2])
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

#use innerText or innerHTML
def hide():    
    Text1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='ib']/strong")))
    Text2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//b[@class='text-yellow text-lg']")))
    Text3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//b[@class='text-info text-lg']")))
    Text4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='gray']/strong")))
    driver.execute_script("arguments[0].innerText = '记得午睡';\
                           arguments[1].innerText = '量力而行';\
                           arguments[2].innerText = '准时吃饭';\
                           arguments[3].innerText = '慢慢来'",Text1,Text2,Text3,Text4)

'''
def on_press(key):
    if key in combination:
        current.add(key)
'''
def on_release(key):
    try:
        combination.remove(key)
        if len(combination) == 0:
            topText = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='ib']/strong")))
            driver.execute_script("arguments[0].innerText = '记得午睡'",topText)
            combination.add(keyboard.Key.ctrl_l)
            combination.add(keyboard.Key.enter)
    except:
        pass

def listen():
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()

def autoRefresh():
    while(True):
        try:
            hide()
            noMission = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "dps-alert")))
            driver.refresh()
        except:
            pass

def pool():
    t1 = threading.Thread(target=listen, name='loop1')
    t2 = threading.Thread(target=autoRefresh,name='loop2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()

pool()

