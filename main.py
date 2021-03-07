from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

edge_driver_path = r"C:\Development\msedgedriver.exe"
driver = webdriver.Edge(executable_path=edge_driver_path)
driver.get("https://tinder.com/")

MAIL_FACE = os.environ["MAIL_FACE"]
PASS_FACE = os.environ["PASS_FACE"]

time.sleep(2)
login = driver.find_element_by_xpath('//*[@id="t--1032254752"]/div/div[1]/div/main/'
                                     'div[1]/div/div/div/div/header/div/div[2]/div[2]/button').click()
time.sleep(2)

login_facebook = driver.find_element_by_xpath('//*[@id="t-1222506740"]/div/div/'
                                              'div[1]/div/div[3]/span/div[2]/button').click()
time.sleep(2)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

facebook_mail = driver.find_element_by_name("email")
facebook_mail.send_keys(MAIL_FACE)
face_pass = driver.find_element_by_name("pass")
face_pass.send_keys(PASS_FACE)
face_pass.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
time.sleep(10)


location = driver.find_element_by_xpath('//*[@id="t-1222506740"]/div/div/div/div/div[3]/button[1]').click()
time.sleep(2)
notifications = driver.find_element_by_xpath('//*[@id="t-1222506740"]/div/div/div/div/div[3]/button[2]').click()
time.sleep(10)
dislike = driver.find_element_by_xpath('//*[@id="t--1032254752"]/div/div[1]/div/main/'
                                       'div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button')

count = 0
while count < 100:
    count += 1
    time.sleep(1)
    dislike.click()
