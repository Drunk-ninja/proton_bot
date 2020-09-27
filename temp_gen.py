import time

from colorama import Back, Fore, init
from functions import find_xpath
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

init(convert=True)

'''- . -.-. .... - .- -. .. -.-.'''
def temp_mail(driver):
    
    print(Fore.CYAN+"\n\n Generating a temp-mail......\n",Fore.WHITE)
    print('\n ')
    driver.get('https://getnada.com/')
    time.sleep(2)
    find_xpath(driver,'//*[@id="app"]/div[1]/div[2]/div[1]/div/div[2]/nav/a[2]').click()
    
    find_xpath(driver,'//*[@id="domain"]').click()

    find_xpath(driver,'//*[@id="domain"]/option[6]').click()

    find_xpath(driver,'//*[@id="app"]/div[1]/div[1]/footer/a[2]').click()
    
    find_xpath(driver,'//*[@id="app"]/div[1]/div[2]/div[1]/div/div[2]/nav/a[1]/i[2]').click()
    print(Fore.CYAN+"Please wait\n\n",Fore.WHITE)
    email=driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/h1/span[2]').text

    return email
