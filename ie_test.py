import sys
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import traceback
import logging
import pyperclip
import pyautogui
from tkinter import Tk
from appium import webdriver
import clipboard
import configparser
import os
import sys
import multiprocessing.pool
import functools


def refresh_and_takedata(num):
    try:
        elements = nice_driver.find_elements_by_name('OK')
        if not elements:
            print('Monitor server running')
        else:
            nice_driver.find_element_by_name('OK').click()
            nice_driver.find_element_by_name('Logout').click()
            print('Monitor server not running')
            nice_login()


        nice_driver.find_element_by_name('My Groups').click()
        nice_driver.find_element_by_name('my agents').click()

        logging.info("Agent  Name   Station   Activity   Record   ANI   DNIS   SegmentID   StartTime   Direction")

        nice_driver.find_element_by_name('Agent Name row 0').click()
        nice_driver.find_element_by_name('Agent Name row 0').click()
        nice_driver.find_element_by_name('Agent Name row 0').send_keys(Keys.CONTROL + "c" + Keys.CONTROL)
        nice_driver.find_element_by_name('Agent Name row 0').click()

        time.sleep(3)
        logging.info(clipboard.paste())


        nice_driver.find_element_by_name('Agent Name row 1').click()
        nice_driver.find_element_by_name('Agent Name row 1').click()
        nice_driver.find_element_by_name('Agent Name row 1').send_keys(Keys.CONTROL + "c" + Keys.CONTROL)
        nice_driver.find_element_by_name('Agent Name row 1').click()

        time.sleep(3)
        logging.info(clipboard.paste())


        nice_driver.find_element_by_name('Agent Name row 2').click()
        nice_driver.find_element_by_name('Agent Name row 2').click()
        nice_driver.find_element_by_name('Agent Name row 2').send_keys(Keys.CONTROL + "c" + Keys.CONTROL)
        nice_driver.find_element_by_name('Agent Name row 2').click()

        time.sleep(3)
        logging.info(clipboard.paste())
    except:
        time.sleep(10)
        refresh_and_takedata(num)


def nice_login():
    nice_driver.set_window_size(1350, 1400)

    zz = 0

    while zz == 0:
        try:
            nice_driver.find_element_by_name("Login name").click()
            zz = 1
        except:

            zz = 0
    nice_driver.find_element_by_name("Login name").send_keys(Niceuser)
    nice_driver.find_element_by_name("Login password").send_keys(Nicepwd)
    nice_driver.find_element_by_name("Login password").send_keys(Keys.ENTER)
    zz = 0
    while (zz == 0):
        try:
            nice_driver.find_element_by_name("Monitor").click()
            zz = 1
        except:
            zz = 0

    nice_driver.set_window_size(1050, 450)
    nice_driver.set_window_position(0, 400)

    action.double_click(nice_driver.find_element_by_name('My Groups')).double_click().perform()
    nice_driver.find_element_by_name('my agents').click()

    nice_driver.find_element_by_name('My Groups').click()

    nice_driver.find_element_by_name('my agents').click()


App_path = os.path.dirname(sys.argv[0]) + '/'
config = configparser.ConfigParser(allow_no_value=True)
config.read_file(open(App_path + r'niceconfig.txt'))
Niceuser = config.get('automationconfig', 'Niceuser')
Nicepwd = config.get('automationconfig', 'Nicepwd')

# nice driver
desired_caps = {}
desired_caps["app"] = "C:\Program Files (x86)\Internet Explorer\iexplore.exe"
nice_driver = webdriver.Remote(command_executor='http://127.0.0.1:4723', desired_capabilities=desired_caps)

action = ActionChains(nice_driver)

nice_login()

