import os
import random
import string
import time

import colorama
from colorama import Back, Fore, init
from functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

init(convert=True)

def create_account(driver,email,x_i,y_i):

    print(Fore.CYAN+"Creating Account...........",Fore.WHITE)
    if email=='': 
        email=input("Please enter email: \t")

    print('\n\n\n')
    
    try:
        new_tab(driver,"https://protonmail.com/signup")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(.5)
        human_move(driver,'//*[@id="signup-plans"]/div[5]/div[1]/div[1]/div',x_i,y_i)
        human_move(driver,'//*[@id="freePlan"]',x_i,y_i)
        randpwd="pwd4PROTON@me"
        time.sleep(.5)

        WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
            (By.TAG_NAME, 'iframe')))
        time.sleep(.5)
        
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        WebDriverWait(driver, 60).until(EC.presence_of_element_located(
            (By.ID, 'username'))).click
        username=WebDriverWait(driver, 60).until(EC.presence_of_element_located(
            (By.ID, 'username')))
        randuser=random_user()
        for i in randuser:
            username.send_keys(i)
            time.sleep(.1)
        driver.switch_to.default_content()
        print(Fore.CYAN+"Please wait\n\n",Fore.WHITE)
        password=WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, 'password')))
        for i in randpwd:
            password.send_keys(i)
            time.sleep(.1)
        time.sleep(1)
        print(Fore.CYAN+"Please wait\n\n",Fore.WHITE)
        input_value(driver,'//*[@id="passwordc"]',randpwd)


        driver.switch_to.frame(driver.find_element_by_class_name("bottom"))
        human_move(driver,'//*[@id="app"]/div/footer/button',x_i,y_i)
        driver.switch_to.default_content()
        time.sleep(1)

        check_error=True
        while check_error==True:
            try:
                WebDriverWait(driver, 4).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="modal-footer"]')))
                check_error=False
            except:
                print(Fore.RED+"\nUsername error\n",Fore.WHITE)
                print(Fore.LIGHTGREEN_EX+"Solving",Fore.WHITE)
                randuser=random_user()

                driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
                while username.get_attribute('value') !='':
                    username.send_keys(Keys.BACKSPACE)
                randuser=random_user() 
                for i in randuser:
                    username.send_keys(i)
                    time.sleep(.1)
                driver.switch_to.default_content()
                driver.switch_to.frame(driver.find_element_by_class_name("bottom"))
                human_move(driver,'//*[@id="app"]/div/footer/button',x_i,y_i)
                driver.switch_to.default_content()
                print(Fore.LIGHTGREEN_EX+"Maybe solved",Fore.WHITE)
                check_error=True
                time.sleep(.3)
        human_move(driver,'//*[@id="confirmModalBtn"]',x_i,y_i)

        while True:
            try:
                human_move(driver,'//*[@id="verification-panel"]/div[2]',x_i,y_i)
                break
            except:
                print(Fore.RED+"Looks like YOU have abused the bot!! Try Again later",Fore.WHITE)
                input("Press enter/return key to exit.")
                os.system(exit)

        input_value(driver,'//*[@id="emailVerification"]',email)
        human_move(driver,'//*[@id="verification-panel"]/form[1]/div[1]/div[2]/button',x_i,y_i)
        
    except BaseException as E:
        print(E)
        print(Fore.RED+"\nBroken\n")
        print("\n\nLooks like something broke,don't worry. I will handle it.\n\n",Fore.WHITE)

    except:
        print(Fore.RED+"\n\nLooks like something broke,Worry!!\n\n",Fore.WHITE)
        print("\n\n3\n\n")
        time.sleep(1)
        print("\n\n2\n\n")
        time.sleep(1)
        print("\n\n1\n\n")
        time.sleep(1)

        try:
            driver.close()
        except:
            print()
    return randuser,randpwd,email
