import os
import time
import urllib
import urllib.request
from lib2to3.pgen2 import driver

import requests
import wget as wget
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from urllib import request

df = pd.read_excel('produse.xlsx')
print(df)
browser = webdriver.Chrome('C:/webdriver/chromedriver.exe')
#browser.get('https://www2.bing.com/?scope=images&nr=1&FORM=NOFORM')
#bing1img = browser.find_element_by_xpath('//*[@id="mmComponent_images_2"]/ul[1]/li[1]/div/div[1]/a/div/img').click()

browser.get('https://www.google.ro/imghp')



time.sleep(2)
biscuit = browser.find_element_by_xpath('//*[@id="L2AGLb"]/div')
biscuit.click()
time.sleep(2)

for i in df.index:
    entry = df.loc[i]
    search = browser.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
    search.send_keys(entry['Produs'])
    time.sleep(2)
    search.send_keys(Keys.RETURN) # hit return after you enter search text
    fimg = browser.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[1]').click()

    fimg2 = browser.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img')
    fimg2.click()

    src = fimg2.get_attribute('src')
    print(src)
    urllib.request.urlretrieve(src, "rez1.jpg")

    #f = open('a00000001.jpg','wb')
    #f.write(urllib.request.urlopen(src).read())

    time.sleep(2)
    browser.get('https://www.google.ro/imghp')

    time.sleep(2)





browser.quit()
