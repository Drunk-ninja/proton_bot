import os
import platform
import sys
import time

import colorama
from colorama import Back, Fore, init
from create_acc import create_account
from functions import calculate_move
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from temp_gen import temp_mail
from verify import verification

init(convert = True)

driver_path = "default"
driver_path = 'Drivers/chromedriver.exe'
clear_cmd = 'cls'


os_name = platform.system()
if os_name == "Linux":
    driver_path = 'Drivers/chromedriver_linux'
    clear_cmd = 'cls'

if os_name == "Windows":
    driver_path = 'Drivers/chromedriver.exe'
    clear_cmd = 'cls'
    
if os_name == "Darwin":
    driver_path = 'Drivers/chromedriver_mac'
    clear_cmd = 'clear'
    

def clear():
    return os.system(clear_cmd)

clear()


print(Fore.BLUE+'''
                  
                ██████╗ ██████╗  █████╗ ████████╗ █████╗ ███╗  ██╗
                ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗░██║
                ██████╔╝██████╔╝██║░░██║░░░██║░░░██║░░██║██╔██╗██║
                ██╔═══╝░██╔══██╗██║░░██║░░░██║░░░██║░░██║██║╚████║
                ██║░░░░░██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░╚███║
                ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚══╝

        ████████╗██████╗ ██╗ █████╗ ██╗       ██████╗  █████╗ ████████╗
        ╚══██╔══╝██╔══██╗██║██╔══██╗██║░░░░░  ██╔══██╗██╔══██╗╚══██╔══╝
        ░░░██║░░░██████╔╝██║███████║██║░░░░░  ██████╦╝██║░░██║░░░██║░░░
        ░░░██║░░░██╔══██╗██║██╔══██║██║░░░░░  ██╔══██╗██║░░██║░░░██║░░░
        ░░░██║░░░██║░░██║██║██║░░██║███████╗  ██████╦╝╚█████╔╝░░░██║░░░
        ░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚══════╝  ╚═════╝░░╚════╝░░░░╚═╝░░░                                      
    ''', Fore.WHITE)

print(Fore.GREEN+'''
                ▀█▀ █▀▀ █▀▀ █ █ ▀█▀ ▄▀█ █▄ █ █ █▀▀  
                ░█░ ██▄ █▄▄ █▀█ ░█░ █▀█ █░▀█ █ █▄▄  

                        ▄▀█ █▄ █ █▀▄
                        █▀█ █░▀█ █▄▀

                █▀█ █▀▀ ▀█▀ ▄▀█ █▀▀ █▀█ █▄ █
                █▄█ █▄▄ ░█░ █▀█ █▄█ █▄█ █░▀█
''', Fore.WHITE)
print("Discord: TECHTANIC#8090")
options = Options()
options.headless = True
options.add_argument("--log-level=3")
driver = webdriver.Chrome(options = options, executable_path = driver_path)
print("- . -.-. .... - .- -. .. -.-.")


x_i, y_i = calculate_move()
email = temp_mail(driver)
randuser, randpwd, email = create_account(driver, email, x_i, y_i)
verification(driver, randuser, randpwd, email)
