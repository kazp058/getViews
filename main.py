from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time


url = 'https://www.facebook.com/watch/?v=215570357045516'

me = ["username/email ","password"]

#send_box = driver.find_element_by_class_name(' _3d2q _65tb  _4w79')
#_5rp7

views = 0

while True:
    try:

        driver = webdriver.Chrome("chromedriver.exe")
        time.sleep(10)
        driver.get(url)

        time.sleep(30)

        time.sleep(174)

        driver.close()
        views += 1
        
        time.sleep(2)

        print('times viewed:',views)

    except Exception:
        print("Error!, reintentando")
        if driver:
            driver.close()

