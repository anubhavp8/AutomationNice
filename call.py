### Note -- please start the winium driver in C:\Users\pgomez\Desktop\python\Winium\Winium.Desktop.Driver

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# !/usr/lib/python2.7


import time
import psutil
import ctypes
import logging
import socket
import pyautogui
import traceback
import datetime
import PIL.ImageGrab
from playsound import playsound
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from ie_test import refresh_and_takedata
import datetime
import configparser
import os
import sys





###Definitions of all the functions

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def send_mesgA(mes):
    try:
        s = socket.socket()
        s.connect((hostnameA, 3126))
        s.sendall(mes.encode())
        print('Mesg send to Agent A', mes)
        s.close()
    except:
        time.sleep(1)
        send_mesgA(mes)


def recv_mesgA():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 3125))
    print ('Agent B binded to Agent A')
    s.listen(3)
    print ('Agent B is listening')
    while True:
        c, addr = s.accept()
        print('Got connection from ', addr)
        print('Mesg recvd to agent A')
        return c.recv(1024)


###memory usage
def cpu_usage(mesg):
    ts = time.time()
    if (psutil.virtual_memory()[2]) < 90:
        logging.info(mesg)
        logging.info(str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')) + "cpu percent:" + str(
            psutil.cpu_percent()))
        logging.info(
            str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')) + "virtual memory percent:" + str(
                psutil.virtual_memory()))
        logging.info(str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')) + "memory % used:" + str(
            psutil.virtual_memory()[2]))
        logging.info("")
    else:
        logging.critical(mesg)
        logging.critical(str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')) + "cpu percent:" + str(
            psutil.cpu_percent()))
        logging.critical(
            str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')) + "virtual percent:" + str(
                psutil.virtual_memory()))
        logging.critical(
            str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')) + "memory % used:" + str(
                psutil.virtual_memory()[2]))
        logging.info("")




###open webpage
def Open_page():
    driver.get('https://hc301.tthcslabs.com/agentdesktop/')
    time.sleep(5)


###login
def login_page():
    driver.find_element_by_name('username').send_keys(UsernameB)
    time.sleep(1)
    driver.find_element_by_name('password').send_keys(PasswordB)
    time.sleep(1)
    driver.find_element_by_id("auth-submit").click()
    time.sleep(10)

def login_again():
    time.sleep(1)
    driver.find_element_by_name('password').send_keys(PasswordB)
    time.sleep(1)
    driver.find_element_by_id("auth-submit").click()
    time.sleep(10)


def already_logged_in():
    time.sleep(2)
    elements=driver.find_elements_by_id("gwt-debug-cdbOk")
    if not elements:
        print("User not logged in")
    else:
        driver.find_element_by_id("gwt-debug-cdbOk").click()
        time.sleep(2)
        not_ready_user()


###not ready
def not_ready_user():
    check_network_issue()
    try:
        driver.find_element_by_id("gwt-debug-acStateMenuContainer").click()
        time.sleep(2)
        #if BP == "True":
        elements = driver.find_elements_by_xpath("//*[@title='Not ready']")
        if not elements:
            print('not ready element not found')
        else:
            driver.find_element_by_xpath("//*[@title='Not ready']").click()
        time.sleep(2)
    except:
        driver.find_element_by_id("gwt-debug-acStateMenuContainer").click()
        time.sleep(2)
        #if BP == "True":
        elements = driver.find_elements_by_xpath("//*[@title='Not Ready']")
        if not elements:
            print('not ready element not found')
        else:
            driver.find_element_by_xpath("//*[@title='Not Ready']").click()
        time.sleep(2)


def forced_loggedin():
    try:
        time.sleep(5)
        driver.find_element_by_id('gwt-debug-cdbOk')
    except NoSuchElementException:
        ready_user()
    driver.find_element_by_id('gwt-debug-cdbOk').click()
    ready_user()


def open_nice():
    print('nice')

def brightpattern_login_page():
    driver.get('https://teletech.brightpattern.com/agentdesktop/')
    time.sleep(5)
    driver.find_element_by_name('username').send_keys(QmprouserB)
    driver.find_element_by_name('password').send_keys(QmpasswdB)
    driver.find_element_by_id("auth-submit").click()
    time.sleep(10)


###ready
def ready_user():
    check_network_issue()
    driver.find_element_by_id("gwt-debug-acStateMenuContainer").click()
    time.sleep(2)
    elements = driver.find_elements_by_xpath("//*[@title='Ready']")
    if not elements:
        print('ready not found')
    else:
        driver.find_element_by_xpath("//*[@title='Ready']").click()
        time.sleep(2)

###respond incoming call
def incoming_call():
    sss = driver.find_element_by_id("gwt-debug-acStateMenuContainer")
    i = 0
    while i <= 50:
        try:
            pyautogui.moveTo(125,200)
            action.move_to_element_with_offset(sss, 200, 0).click().perform()
            action.move_to_element_with_offset(sss, 175, 0).click().perform()
            driver.find_element_by_css_selector('.GLEKGWC-S-d:nth-child(2)').click()
            time.sleep(0.5)
            break
        except:
            i = i + 1
            print(i)
            if i==10:
                action.move_to_element_with_offset(sss, 111, 111).click().perform()
            if i==15:
                action.move_to_element_with_offset(sss, 550, 550).click().perform()

###make incoming call using avaya



def reject_call():
    sss = driver.find_element_by_id("gwt-debug-acStateMenuContainer")
    i = 0
    while i <= 50:
        try:
            pyautogui.moveTo(125,200)
            action.move_to_element_with_offset(sss, 200, 0).click().perform()
            action.move_to_element_with_offset(sss, 175, 0).click().perform()
            driver.find_element_by_css_selector('#agent-desktop > div:nth-child(8) > div > div.GLEKGWC-zb-b > div > div > div.b-desk-east > div:nth-child(3) > div > div.b-header-panel.b-flex.GLEKGWC-ub-a > div:nth-child(1) > div > div.b-flex.b-desk-repeater-ixn-view > div.b-desk-repeater-ixn-controls > div > button:nth-child(3)').click()
            time.sleep(0.5)
            break
        except:
            i = i + 1
            print(i)
            if i==10:
                action.move_to_element_with_offset(sss, 111, 111).click().perform()
            if i==15:
                action.move_to_element_with_offset(sss, 550, 550).click().perform()


def agent_hold():
    check_network_issue()
    time.sleep(2)
    action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
    time.sleep(2)
    driver.find_element_by_id("cpHold").click()
    time.sleep(2)


def agent_resize():
    driver.set_window_size(1550, 450)


def leave_conf():
    check_network_issue()
    time.sleep(1)
    action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
    time.sleep(2)
    driver.find_element_by_id("cpLeaveConference").click()


def agent_retrive():
    time.sleep(2)
    action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
    time.sleep(2)
    driver.find_element_by_id("cpRetrieve").click()
    time.sleep(2)


###playsound
def play_sound():
    playsound(App_path + 'AgentBP.mp3')


def check_network_issue():
    ##code to check network issue
    elements = driver.find_elements_by_id("gwt-debug-cdbOk")
    if not elements:
        print('ready not found')
    else:
        driver.find_element_by_id("gwt-debug-cdbOk").click()


###end the call
def end_call():
    check_network_issue()
    try:
        playsound(App_path + 'AgentB hangout.mp3')
        action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
        time.sleep(2)
        driver.find_element_by_id("cpEndCall").click()
        time.sleep(2)
    except:
          print("issue while ending call")

def exception_hangup():
    action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
    time.sleep(2)
    elements=driver.find_elements_by_id("cpEndCall")
    if not elements:
        print("agent not in call")
    else:
        driver.find_element_by_id("cpEndCall").click()



###hangup the call
def hangup_call():
    check_network_issue()
    action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
    time.sleep(2)
    driver.find_element_by_id("cpEndCall").click()
    time.sleep(2)
    driver.find_element_by_id("cpEndCall").click()
    time.sleep(2)


def screenshot():
    driver.save_screenshot("Test.png")


def montor_shot(inst):
    im = PIL.ImageGrab.grab()
    im.save(App_path + "Screenshots/Test"+ str(inst) + str("_") +datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p") + ".png")
    print(App_path + "Screenshots/Test" +str(inst) + str("_") + datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p") + ".png")
    #im.save("Test2" + ".png")


###Transfer the call
def agent_call():
    time.sleep(4)
    action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad2")).perform()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='sp-destination']").send_keys('74777321004')
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='dial-toolbar-call']/button").click()
    time.sleep(3)



def agent_mute():
    time.sleep(2)
    check_network_issue()

    action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
    time.sleep(2)
    elements= driver.find_elements_by_xpath("//*[@title='Mute the microphone']")
    if not elements:
        print('mute is not available')
    else:
        try:
            driver.find_element_by_xpath("//*[@title='Mute the microphone']").click()
            time.sleep(1)
        except:
            print("mute was not clicked")


def agent_unmute():
    time.sleep(2)

    check_network_issue()

    action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
    time.sleep(2)
    elements = driver.find_elements_by_xpath("//*[@title='Unmute the microphone']")
    if not elements:
        print('unmute is not available')
    else:
        try:
            driver.find_element_by_xpath("//*[@title='Unmute the microphone']").click()
            time.sleep(1)
        except:
            print('unmute is not clicked')


def blind_transfer():
    time.sleep(3)
    action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad2")).perform()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='sp-destination']").send_keys('74777321004')
    time.sleep(2)
    driver.find_element_by_id("dial-toolbar-blind").click()
    time.sleep(2)


###Log out user after testing
def log_out():
    check_network_issue()
    driver.find_element_by_id("top-toolbar-logout").click()
    time.sleep(2)
    driver.find_element_by_id("gwt-debug-cdbOk").click()
    time.sleep(4)





###Function calls



### bright pattern test cases


###BP test cases


def login():
    logging.info(" ")
    logging.info(" ")
    BP = recv_mesgA().decode()
    open_nice()
    if BP =="True":
        Open_page()
        login_page()
        log_out()
        login_again()
    else:
        brightpattern_login_page()
    already_logged_in()
    cpu_usage("Usage when Agent logs in")
    if recv_mesgA() == b'getting ready':
        send_mesgA('login A')
    if recv_mesgA() == b'login A comp':
        #not_ready_user()
        print("not ready user")
    send_mesgA('next mesg')
    BP = recv_mesgA().decode()
    send_mesgA('next mesg')
    QMPro = recv_mesgA().decode()
    send_mesgA('next mesg')
    testcall = recv_mesgA().decode()
    send_mesgA('next mesg')
    nooftimes = recv_mesgA().decode()

    print(BP, QMPro, testcall, nooftimes)

    cpu_usage("Usage when Agent goes to ready state")
    agent_resize()
    return BP, QMPro, testcall, nooftimes


def testcase104():
    #time.sleep(5)
    logging.info(" ")
    logging.info("Test case 104: Simple internal call: ")
    send_mesgA('ready')
    incoming_call()
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    print(8)
    send_mesgA('agent A')
    recA= recv_mesgA()
    if recA == b'agent B':
         print('agentB')
    elif recA == b'exception':
        exception_hangup()
        testcase104()
    cpu_usage("Usage when Agent goes to mute state")
    agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    montor_shot(104)
    refresh_and_takedata(104)
    send_mesgA('logout')


def testcase75():
    ###Test case 75 : Internal call conf , blind, Agent A hangs up then agent B
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 75 : Internal call conf , blind, Agent A hangs up then agent B")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        time.sleep(3)
    elif recA == b'exception':
        exception_hangup()
        testcase75()
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    montor_shot(75)
    refresh_and_takedata(75)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
    end_call()
    cpu_usage("Usage when Agent ends the call")
    time.sleep(3)

def testcase76():
    ###Test case 76 : Internal call conf , blind, Agent A hangs up then agent C
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 76 : Internal call conf , blind, Agent A hangs up then agent C")
    time.sleep(3)
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    agent_mute()
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    elif recA == b'exception':
        exception_hangup()
        testcase76()
    play_sound()
    agent_mute()
    montor_shot(76)
    refresh_and_takedata(76)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'finish test':
        print('received mesg to finish the test')
    elif recA == b'exception':
        exception_hangup()
        testcase76()


def testcase77():
    ###Test case 77 : Internal call conf , blind, Agent B hangs up then agent C
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 77 : Internal call conf , blind, Agent B hangs up then agent C")
    time.sleep(7)
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    agent_mute()
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    elif recA == b'exception':
        exception_hangup()
        testcase77()
    play_sound()
    agent_mute()
    montor_shot(77)
    refresh_and_takedata(77)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'hangup':
        agent_unmute()
        end_call()
    elif recA == b'exception':
        exception_hangup()
        testcase77()
    send_mesgA('left conf')


def testcase78():
    ###Test case 78 : Internal call conf , warm, Agent A hangs up then agent B
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 78 : Internal call conf , warm, Agent A hangs up then agent B")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        print('r')
    elif recA == b'exception':
        exception_hangup()
        testcase78()
    time.sleep(3)
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    elif recA == b'exception':
        exception_hangup()
        testcase78()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    montor_shot(78)
    refresh_and_takedata(78)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    elif recA == b'exception':
        exception_hangup()
        testcase78()
    cpu_usage("Usage when Agent ends the call")
    time.sleep(3)

def testcase79():
    ###Test case 79 : Internal call conf , warm, Agent A hangs up then agent C
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 79 : Internal call conf , warm, Agent A hangs up then agent C")
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    agent_mute()
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    elif recA == b'exception':
        exception_hangup()
        testcase79()
    play_sound()
    agent_mute()
    montor_shot(79)
    refresh_and_takedata(79)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'finish test':
        print('received mesg to finish the test')
    elif recA == b'exception':
        exception_hangup()
        testcase79()


def testcase80():
    ###Test case 80 : Internal call conf , warm, Agent B hangs up then agent C
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 80 : Internal call conf , warm, Agent B hangs up then agent C")
    send_mesgA('ready')
    time.sleep(6)
    incoming_call()
    send_mesgA('received call')
    agent_mute()
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    elif recA == b'exception':
        exception_hangup()
        testcase80()
    play_sound()
    agent_mute()
    montor_shot(80)
    refresh_and_takedata(80)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'hangup':
        agent_unmute()
        end_call()
    elif recA == b'exception':
        exception_hangup()
        testcase80()
    send_mesgA('left conf')

#########################################################################################

def testcase81():
    ###Test case 81 : Internal call conf , retriving, Agent A hangs up then agent B
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 81 : Internal call conf , retriving, Agent A hangs up then agent B")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        time.sleep(3)
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    elif recA == b'exception':
        exception_hangup()
        testcase80()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    montor_shot(81)
    refresh_and_takedata(81)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    elif recA == b'exception':
        exception_hangup()
        testcase80()
    cpu_usage("Usage when Agent ends the call")
    time.sleep(3)

def testcase82():
    ###Test case 82 : Internal call conf , retriving, Agent A hangs up then agent C
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 82 : Internal call conf , retriving, Agent A hangs up then agent C")
    time.sleep(6)
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    agent_mute()
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    elif recA == b'exception':
        exception_hangup()
        testcase82()
    play_sound()
    agent_mute()
    montor_shot(82)
    refresh_and_takedata(82)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'finish test':
        print('received mesg to finish the test')
    elif recA == b'exception':
        exception_hangup()
        testcase82()


def testcase83():
    ###Test case 83 : Internal call conf , retriving, Agent B hangs up then agent C
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 83 : Internal call conf , retriving, Agent B hangs up then agent C")
    time.sleep(6)
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    agent_mute()
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    elif recA == b'exception':
        exception_hangup()
        testcase83()
    play_sound()
    agent_mute()
    montor_shot(83)
    refresh_and_takedata(83)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'hangup':
        agent_unmute()
        end_call()
    elif recA == b'exception':
        exception_hangup()
        testcase83()
    send_mesgA('left conf')


####################################################################################


def testcase84():
    ###Test case 84 : Internal call transference , blind, Agent B hangs up
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 84 : Internal call transference , blind, Agent B hangs up")
    time.sleep(8)
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    agent_mute()
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    elif recA == b'exception':
        exception_hangup()
        testcase84()
    play_sound()
    agent_mute()
    montor_shot(84)
    refresh_and_takedata(84)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'hangup':
        agent_unmute()
        end_call()
    elif recA == b'exception':
        exception_hangup()
        testcase84()
    send_mesgA('left conf')



def testcase85():
    ###Test case 85 : Internal call transference , blind, Agent C hangs up
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 85 : Internal call transference , blind, Agent C hangs up")
    time.sleep(8)
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    agent_mute()
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    elif recA == b'exception':
        exception_hangup()
        testcase85()
    play_sound()
    agent_mute()
    montor_shot(85)
    refresh_and_takedata(85)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'ready':
        print('test case 85 completed successully')
    elif recA == b'exception':
        exception_hangup()
        testcase85()


def testcase86():
    ###Test case 86 : Internal call transference , warm, Agent B hangs up
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 86 : Internal call transference , warm, Agent B hangs up")
    time.sleep(8)
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    agent_mute()
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    elif recA == b'exception':
        exception_hangup()
        testcase86()
    play_sound()
    agent_mute()
    montor_shot(86)
    refresh_and_takedata(86)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'hangup':
        agent_unmute()
        end_call()
    elif recA == b'exception':
        exception_hangup()
        testcase86()
    send_mesgA('left conf')



def testcase87():
    ###Test case 87 : Internal call transference , warm, Agent C hangs up
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 87 : Internal call transference , warm, Agent C hangs up")
    time.sleep(8)
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    agent_mute()
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    elif recA == b'exception':
        exception_hangup()
        testcase87()
    play_sound()
    agent_mute()
    montor_shot(87)
    refresh_and_takedata(87)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'ready':
        print('test case 87 completed successully')
    elif recA == b'exception':
        exception_hangup()
        testcase87()

#################################################################


def testcase88():
    ###Test case 88 : Internal call transference , Rerieving agent B
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 88 : Internal call transference , Rerieving agent B")
    time.sleep(6)
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    agent_mute()
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    elif recA == b'exception':
        exception_hangup()
        testcase88()
    play_sound()
    agent_mute()
    montor_shot(87)
    refresh_and_takedata(87)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'hangup':
        agent_unmute()
        end_call()
    elif recA == b'exception':
        exception_hangup()
        testcase88()
    send_mesgA('left conf')



def testcase89():
    ###Test case 89 : Internal call transference ,Rerieving agent B
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 89 : Internal call transference ,Rerieving agent B")
    time.sleep(8)
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    agent_mute()
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    elif recA == b'exception':
        exception_hangup()
        testcase89()
    play_sound()
    agent_mute()
    montor_shot(89)
    refresh_and_takedata(89)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'ready':
        print('test case 89 completed successully')
    elif recA == b'exception':
        exception_hangup()
        testcase89()

########################################################


def testcase90():
    ###Test case 84 : Internal call transference , No hold agent B
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 84 : Internal call transference , No hold agent B")
    time.sleep(6)
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    agent_mute()
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    elif recA == b'exception':
        exception_hangup()
        testcase90()
    play_sound()
    agent_mute()
    montor_shot(90)
    refresh_and_takedata(90)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'hangup':
        agent_unmute()
        end_call()
    elif recA == b'exception':
        exception_hangup()
        testcase90()
    send_mesgA('left conf')



def testcase91():
    ###Test case 91 : Internal call transference , No hold agent C
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 91 : Internal call transference , No hold agent C")
    time.sleep(8)
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    agent_mute()
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    elif recA == b'exception':
        exception_hangup()
        testcase91()
    play_sound()
    agent_mute()
    montor_shot(91)
    refresh_and_takedata(90)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'ready':
        print('test case 91 completed successully')
    elif recA == b'exception':
        exception_hangup()
        testcase91()


def testcase1():
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")

def testcase2():
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")

def testcase3():
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")

def testcase4():
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")


def testcase5():
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")


def testcase6():
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")


def testcase7():
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")


def testcase8():
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")

def testcase37():
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")


def testcase38():
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")

def testcase39():
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")

def testcase40():
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")


def testcase41():
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")


def testcase42():
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")


def testcase43():
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")


def testcase44():
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")


def testcase63():
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 63: Make Outbound call and transfer caller. Customer hangs up. Blind")
    recA= recv_mesgA()
    if recA == b'ready':
        print('ready')
        #ready_user()
    recA = recv_mesgA()
    if recA == b'incoming call':
        incoming_call()
    agent_mute()
    cpu_usage("Usage when Agent receives incoming call")
    time.sleep(7)
    send_mesgA('call received')
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'agent B play sound':
        play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_unmute()
    montor_shot(63)
    refresh_and_takedata(63)
    send_mesgA('logout')


def testcase64():
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 64: Make Outbound call and transfer caller. Customer hangs up. Blind")
    recA= recv_mesgA()
    if recA == b'ready':
        print('ready')
        #ready_user()
    recA = recv_mesgA()
    if recA == b'incoming call':
        incoming_call()
    cpu_usage("Usage when Agent receives incoming call")
    send_mesgA('call received')
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'agent B play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    montor_shot(64)
    refresh_and_takedata(64)
    send_mesgA('logout')


def testcase65():
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 65: Make Outbound call and transfer caller. Customer hangs up. Warm")
    recA= recv_mesgA()
    if recA == b'ready':
        print('ready')
        #ready_user()
    recA = recv_mesgA()
    if recA == b'incoming call':
        incoming_call()
    cpu_usage("Usage when Agent receives incoming call")
    send_mesgA('call received')
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'agent B play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    montor_shot(65)
    refresh_and_takedata(65)
    send_mesgA('logout')


def testcase66():
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 66: Make Outbound call and transfer caller. Customer hangs up. Warm")
    recA= recv_mesgA()
    if recA == b'ready':
        print('ready')
        #ready_user()
    recA = recv_mesgA()
    if recA == b'incoming call':
        incoming_call()
    cpu_usage("Usage when Agent receives incoming call")
    send_mesgA('call received')
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'agent B play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    montor_shot(66)
    refresh_and_takedata(66)
    send_mesgA('logout')


def testcase67():
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 67: Make Outbound call and transfer caller. Customer hangs up. Retrieving")
    recA= recv_mesgA()
    if recA == b'ready':
        print('ready')
        #ready_user()
    recA = recv_mesgA()
    if recA == b'incoming call':
        incoming_call()
    cpu_usage("Usage when Agent receives incoming call")
    send_mesgA('call received')
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'agent B play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    montor_shot(67)
    refresh_and_takedata(67)
    send_mesgA('logout')


def testcase68():
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 68: Make Outbound call and transfer caller. Customer hangs up. Retrieving")
    recA= recv_mesgA()
    if recA == b'ready':
        print('ready')
        #ready_user()
    recA = recv_mesgA()
    if recA == b'incoming call':
        incoming_call()
    cpu_usage("Usage when Agent receives incoming call")
    send_mesgA('call received')
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'agent B play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    montor_shot(68)
    refresh_and_takedata(68)
    send_mesgA('logout')


def testcase69():
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 69: Make Outbound call and transfer caller. Agent hangs up. Blind")
    recA= recv_mesgA()
    if recA == b'ready':
        print('ready')
        #ready_user()
    recA = recv_mesgA()
    if recA == b'incoming call':
        incoming_call()
    cpu_usage("Usage when Agent receives incoming call")
    send_mesgA('call received')
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'agent B play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    montor_shot(69)
    refresh_and_takedata(69)
    end_call()
    cpu_usage("Usage when Agent ends call")
    send_mesgA('logout')


def testcase70():
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 70: Make Outbound call and transfer caller. Agent hangs up. Blind")
    recA= recv_mesgA()
    if recA == b'ready':
        print('ready')
        #ready_user()
    recA = recv_mesgA()
    if recA == b'incoming call':
        incoming_call()
    cpu_usage("Usage when Agent receives incoming call")
    send_mesgA('call received')
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'agent B play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    montor_shot(70)
    refresh_and_takedata(70)
    end_call()
    cpu_usage("Usage when Agent ends call")
    send_mesgA('logout')





def testcase71():
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 71: Make Outbound call and transfer caller. Agent hangs up. Warm")
    recA= recv_mesgA()
    if recA == b'ready':
        print('ready')
        #ready_user()
    recA = recv_mesgA()
    if recA == b'incoming call':
        incoming_call()
    cpu_usage("Usage when Agent receives incoming call")
    send_mesgA('call received')
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'agent B play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    montor_shot(71)
    refresh_and_takedata(71)
    end_call()
    cpu_usage("Usage when Agent ends call")
    send_mesgA('logout')




def testcase72():
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 72: Make Outbound call and transfer caller. Agent hangs up. Warm")
    recA= recv_mesgA()
    if recA == b'ready':
        print('ready')
        #ready_user()
    recA = recv_mesgA()
    if recA == b'incoming call':
        incoming_call()
    cpu_usage("Usage when Agent receives incoming call")
    send_mesgA('call received')
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'agent B play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    montor_shot(72)
    refresh_and_takedata(72)
    end_call()
    cpu_usage("Usage when Agent ends call")
    send_mesgA('logout')




def testcase73():
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case73: Make Outbound call and transfer caller. Agent hangs up. Retrieving")
    recA= recv_mesgA()
    if recA == b'ready':
        print('ready')
        #ready_user()
    recA = recv_mesgA()
    if recA == b'incoming call':
        incoming_call()
    cpu_usage("Usage when Agent receives incoming call")
    send_mesgA('call received')
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'agent B play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    montor_shot(73)
    refresh_and_takedata(73)
    end_call()
    cpu_usage("Usage when Agent ends call")
    send_mesgA('logout')




def testcase74():
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 74: Make Outbound call and transfer caller. Agent hangs up. Retrieving")
    recA= recv_mesgA()
    if recA == b'ready':
        print('ready')
        #ready_user()
    recA = recv_mesgA()
    if recA == b'incoming call':
        incoming_call()
    cpu_usage("Usage when Agent receives incoming call")
    send_mesgA('call received')
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'agent B play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    montor_shot(74)
    refresh_and_takedata(74)
    end_call()
    cpu_usage("Usage when Agent ends call")
    send_mesgA('logout')



def testcase25():
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 25: Make Inbound call and transfer caller. Customer hangs up. Blind")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print(" not ready user")
    recA= recv_mesgA()
    if recA == b'ready':
         #ready_user()
         print("ready user")
    recA = recv_mesgA()
    if recA == b'incoming call':
        incoming_call()
    cpu_usage("Usage when Agent receives incoming call")
    send_mesgA('call received')
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'agent B play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    montor_shot(25)
    refresh_and_takedata(25)
    send_mesgA('logout')


def testcase26():
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 26: Make Inbound call and transfer caller. Customer hangs up. Blind")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")
    recA = recv_mesgA()
    if recA == b'incoming call':
        incoming_call()
    cpu_usage("Usage when Agent receives incoming call")
    send_mesgA('call received')
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'agent B play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    montor_shot(26)
    refresh_and_takedata(26)
    send_mesgA('logout')


def testcase27():
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 27: Make Inbound call and transfer caller. Customer hangs up. Warm")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")
    recA = recv_mesgA()
    if recA == b'incoming call':
        incoming_call()
    cpu_usage("Usage when Agent receives incoming call")
    send_mesgA('call received')
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'agent B play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    montor_shot(27)
    refresh_and_takedata(27)
    send_mesgA('logout')


def testcase28():
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 28: Make Inbound call and transfer caller. Customer hangs up. Warm")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")
    recA = recv_mesgA()
    if recA == b'incoming call':
        incoming_call()
    cpu_usage("Usage when Agent receives incoming call")
    send_mesgA('call received')
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'agent B play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    montor_shot(28)
    refresh_and_takedata(28)
    send_mesgA('logout')


def testcase29():
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 29: Make Inbound call and transfer caller. Customer hangs up. Retrieving")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")
    recA = recv_mesgA()
    if recA == b'incoming call':
        incoming_call()
    cpu_usage("Usage when Agent receives incoming call")
    send_mesgA('call received')
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'agent B play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    montor_shot(29)
    refresh_and_takedata(29)
    send_mesgA('logout')


def testcase30():
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 30: Make Inbound call and transfer caller. Customer hangs up. Retrieving")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")
    recA = recv_mesgA()
    if recA == b'incoming call':
        incoming_call()
    cpu_usage("Usage when Agent receives incoming call")
    send_mesgA('call received')
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'agent B play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    montor_shot(30)
    refresh_and_takedata(30)
    send_mesgA('logout')


def testcase31():
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 31: Make Inbound call and transfer caller. Agent hangs up. Blind")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")
    recA = recv_mesgA()
    if recA == b'incoming call':
        incoming_call()
    cpu_usage("Usage when Agent receives incoming call")
    send_mesgA('call received')
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'agent B play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    montor_shot(31)
    refresh_and_takedata(31)
    end_call()
    cpu_usage("Usage when Agent ends call")
    send_mesgA('logout')


def testcase32():
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 32: Make Inbound call and transfer caller. Agent hangs up. Blind")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")
    recA = recv_mesgA()
    if recA == b'incoming call':
        incoming_call()
    cpu_usage("Usage when Agent receives incoming call")
    send_mesgA('call received')
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'agent B play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    montor_shot(32)
    refresh_and_takedata(32)
    end_call()
    cpu_usage("Usage when Agent ends call")
    send_mesgA('logout')





def testcase33():
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 33: Make Inbound call and transfer caller. Agent hangs up. Warm")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")
    recA = recv_mesgA()
    if recA == b'incoming call':
        incoming_call()
    cpu_usage("Usage when Agent receives incoming call")
    send_mesgA('call received')
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'agent B play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    montor_shot(33)
    refresh_and_takedata(33)
    end_call()
    cpu_usage("Usage when Agent ends call")
    send_mesgA('logout')




def testcase34():
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 34: Make Inbound call and transfer caller. Agent hangs up. Warm")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")
    recA = recv_mesgA()
    if recA == b'incoming call':
        incoming_call()
    cpu_usage("Usage when Agent receives incoming call")
    send_mesgA('call received')
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'agent B play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    montor_shot(34)
    refresh_and_takedata(34)
    end_call()
    cpu_usage("Usage when Agent ends call")
    send_mesgA('logout')




def testcase35():
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case35: Make Inbound call and transfer caller. Agent hangs up. Retrieving")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready':
        print("ready user")
        #ready_user()
    recA = recv_mesgA()
    if recA == b'incoming call':
        incoming_call()
    cpu_usage("Usage when Agent receives incoming call")
    send_mesgA('call received')
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'agent B play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    montor_shot(35)
    refresh_and_takedata(35)
    end_call()
    cpu_usage("Usage when Agent ends call")
    send_mesgA('logout')




def testcase36():
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 36: Make Inbound call and transfer caller. Agent hangs up. Retrieving")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready':
        #ready_user()
        print("ready user")
    recA = recv_mesgA()
    if recA == b'incoming call':
        incoming_call()
    cpu_usage("Usage when Agent receives incoming call")
    send_mesgA('call received')
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'agent B play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    montor_shot(36)
    refresh_and_takedata(36)
    end_call()
    cpu_usage("Usage when Agent ends call")
    send_mesgA('logout')


def testcase47():
    ###Test case 47 : Oubound call conf , blind, 4th party conf , hang up order Customer, Agent A hangs up then agent B, blind
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 47 : Oubound call conf , blind, 4th party conf , hang up order Customer, Agent A hangs up then agent B, blind")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(47)
    montor_shot(47)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")



def testcase48():
    ###Test case 48 : Oubound call conf , blind, 4th party conf , hang up order Customer, Agent B hangs up then agent A
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 48 : Oubound call conf , blind, 4th party conf , hang up order Customer, Agent B hangs up then agent A, blind")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(48)
    montor_shot(48)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    send_mesgA('hangup')
    cpu_usage("Usage when Agent ends the call")



def testcase49():
    ###Test case 49 : Oubound call conf , blind, 4th party conf , hang up order Customer, Agent B hangs up then agent C, warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 49 : Oubound call conf , blind, 4th party conf , hang up order Customer, Agent B hangs up then agent C, warm")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(49)
    montor_shot(49)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    send_mesgA('hangup')
    cpu_usage("Usage when Agent ends the call")



def testcase50():
    ###Test case 50 : Oubound call conf , blind, 4th party conf , hang up order Customer, Agent C hangs up then agent B, warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 50 : Oubound call conf , blind, 4th party conf , hang up order Customer, Agent C hangs up then agent B, warm")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(50)
    montor_shot(50)
    time.sleep(3)
    send_mesgA('play sound C')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")



def testcase51():
    ###Test case 51 : Oubound call conf , blind, 4th party conf , hang up order Customer, Agent C hangs up then agent A, retriving
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 51 : Oubound call conf , blind, 4th party conf , hang up order Customer, Agent C hangs up then agent A, retriving")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(51)
    montor_shot(51)
    time.sleep(3)
    send_mesgA('play sound C')
    cpu_usage("Usage when Agent ends the call")



def testcase52():
    ###Test case 52 : Oubound call conf , blind, 4th party conf , hang up order Customer, Agent A hangs up then agent C, blind
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 52 : Oubound call conf , blind, 4th party conf , hang up order Customer, Agent A hangs up then agent C, blind")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(52)
    montor_shot(52)
    time.sleep(3)
    send_mesgA('play sound C')
    cpu_usage("Usage when Agent ends the call")




def testcase57():
    ###Test case 57 : Outbound call conf , blind, 4th party conf , hang up order Agent A hangs up then agent B, then Agent C, blind
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 57 : Outbound call conf , blind, 4th party conf , hang up order Agent A hangs up then agent B, then Agent C, blind")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(57)
    montor_shot(57)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    send_mesgA('C logout')
    cpu_usage("Usage when Agent ends the call")



def testcase58():
    ###Test case 58 : Outbound call conf , blind, 4th party conf , hang up order Agent A, Agent C hangs up then agent B, blind
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 58 : Outbound call conf , blind, 4th party conf , hang up order Agent A, Agent C hangs up then agent B, blind")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    time.sleep(7)
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(58)
    montor_shot(58)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")



def testcase59():
    ###Test case 59 : Outbound call conf , blind, 4th party conf , hang up order Agent B hangs up then Agent A, then agent C, warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 59 : Outbound call conf , blind, 4th party conf , hang up order Agent B hangs up then then Agent A, then agent C, warm")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(59)
    montor_shot(59)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    send_mesgA('hangup')
    cpu_usage("Usage when Agent ends the call")



def testcase60():
    ###Test case 60 : Outbound call conf , blind, 4th party conf , hang up order Agent B, then agent C hangs up then agent A, warm
    logging.info(" ")
    logging.info(" ")
    logging.info(
        "Test case 60 : Outbound call conf , blind, 4th party conf , hang up order Agent B, then agent C hangs up then agent A, warm")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(60)
    montor_shot(60)
    time.sleep(3)
    send_mesgA('play sound C')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")
    send_mesgA('logout')



def testcase61():
    ###Test case 61 : Outbound call conf , blind, 4th party conf , hang up order Agent C hangs up then agent A, then Agent B , retriving
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 61 : Outbound call conf , blind, 4th party conf , hang up order Agent C hangs up then agent A, then Agent B , retriving")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(61)
    montor_shot(61)
    time.sleep(3)
    send_mesgA('play sound C')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")



def testcase62():
    ###Test case 62 : Outbound call conf , blind, 4th party conf , hang up order Agent C, Agent B, Agent A, blind
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 62 : Outbound call conf , blind, 4th party conf , hang up order Agent C, Agent B, Agent A blind")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(62)
    montor_shot(62)
    time.sleep(3)
    send_mesgA('play sound C')
    cpu_usage("Usage when Agent ends the call")
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
    end_call()




def testcase11():
    ###Test case 11 : Inbound call conf , blind, 4th party conf , hang up order Customer, Agent A hangs up then agent B, blind
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 11 : Inbound call conf , blind, 4th party conf , hang up order Customer, Agent A hangs up then agent B, blind")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(11)
    montor_shot(11)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")



def testcase12():
    ###Test case 12 : Inbound call conf , blind, 4th party conf , hang up order Customer, Agent B hangs up then agent A
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 12 : Inbound call conf , blind, 4th party conf , hang up order Customer, Agent B hangs up then agent A, blind")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(12)
    montor_shot(12)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    send_mesgA('hangup')
    cpu_usage("Usage when Agent ends the call")



def testcase13():
    ###Test case 13 : Inbound call conf , blind, 4th party conf , hang up order Customer, Agent B hangs up then agent C, warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 13 : Inbound call conf , blind, 4th party conf , hang up order Customer, Agent B hangs up then agent C, warm")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(13)
    montor_shot(13)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    send_mesgA('hangup')
    cpu_usage("Usage when Agent ends the call")



def testcase14():
    ###Test case 14 : Inbound call conf , blind, 4th party conf , hang up order Customer, Agent C hangs up then agent B, warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 14 : Inbound call conf , blind, 4th party conf , hang up order Customer, Agent C hangs up then agent B, warm")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(14)
    montor_shot(14)
    time.sleep(3)
    send_mesgA('play sound C')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")



def testcase15():
    ###Test case 15 : Inbound call conf , blind, 4th party conf , hang up order Customer, Agent C hangs up then agent A, retriving
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 15 : Inbound call conf , blind, 4th party conf , hang up order Customer, Agent C hangs up then agent A, retriving")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(15)
    montor_shot(15)
    time.sleep(3)
    send_mesgA('play sound C')
    cpu_usage("Usage when Agent ends the call")


def testcase16():
    ###Test case 16 : Inbound call conf , blind, 4th party conf , hang up order Customer, Agent A hangs up then agent C, blind
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 16 : Inbound call conf , blind, 4th party conf , hang up order Customer, Agent A hangs up then agent C, blind")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(16)
    montor_shot(16)
    time.sleep(3)
    send_mesgA('play sound C')
    cpu_usage("Usage when Agent ends the call")




def testcase19():
    ###Test case 19 : Inbound call conf , blind, 4th party conf , hang up order Agent A hangs up then agent B, then Agent C, blind
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 19 : Inbound call conf , blind, 4th party conf , hang up order Agent A hangs up then agent B, then Agent C, blind")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(19)
    montor_shot(19)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    send_mesgA('C logout')
    cpu_usage("Usage when Agent ends the call")



def testcase20():
    ###Test case 20 : Inbound call conf , blind, 4th party conf , hang up order Agent A, Agent C hangs up then agent B, blind
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 20 : Inbound call conf , blind, 4th party conf , hang up order Agent A, Agent C hangs up then agent B, blind")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(20)
    montor_shot(20)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
    end_call()
    cpu_usage("Usage when Agent ends the call")



def testcase21():
    ###Test case 21 : Inbound call conf , blind, 4th party conf , hang up order Agent B hangs up then Agent A, then agent C, warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 21 : Inbound call conf , blind, 4th party conf , hang up order Agent B hangs up then then Agent A, then agent C, warm")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(21)
    montor_shot(21)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    send_mesgA('hangup')
    cpu_usage("Usage when Agent ends the call")



def testcase22():
    ###Test case 22 : Inbound call conf , blind, 4th party conf , hang up order Agent B, then agent C hangs up then agent A, warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 22 : Inbound call conf , blind, 4th party conf , hang up order Agent B, then agent C hangs up then agent A, warm")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(22)
    montor_shot(22)
    time.sleep(3)
    send_mesgA('play sound C')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")
    send_mesgA('logout')



def testcase23():
    ###Test case 23 : Inbound call conf , blind, 4th party conf , hang up order Agent C hangs up then agent A, then Agent B , retriving
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 23 : Inbound call conf , blind, 4th party conf , hang up order Agent C hangs up then agent A, then Agent B , retriving")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(23)
    montor_shot(23)
    time.sleep(3)
    send_mesgA('play sound C')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")



def testcase24():
    ###Test case 24 : Inbound call conf , blind, 4th party conf , hang up order Agent C, Agent B, Agent A, blind
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 24 : Inbound call conf , blind, 4th party conf , hang up order Agent C, Agent B, Agent A blind")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(24)
    montor_shot(24)
    time.sleep(3)
    send_mesgA('play sound C')
    cpu_usage("Usage when Agent ends the call")
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()


def testcase92():
    ###Test case 92 : Oubound 4th party conference, merging all calls , hang up order Customer, Agent A hangs up then agent B
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 92 : Oubound 4th party conference, merging all calls , hang up order Customer, Agent A hangs up then agent B")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(92)
    montor_shot(92)
    time.sleep(3)
    send_mesgA('play sound C')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")


def testcase93():
    ###Test case 93 : Oubound 4th party conference, merging all calls , hang up order Customer, Agent B hangs up then agent C
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 93 : Oubound 4th party conference, merging all calls , hang up order Customer, Agent B hangs up then agent C")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(93)
    montor_shot(93)
    time.sleep(3)
    send_mesgA('play sound C')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    send_mesgA('hangup')
    cpu_usage("Usage when Agent ends the call")


def testcase94():
    ###Test case 94 : Oubound 4th party conference, merging all calls , hang up order Customer, Agent A hangs up then agent C
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 94 : Oubound 4th party conference, merging all calls , hang up order Customer, Agent A hangs up then agent C")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(94)
    montor_shot(94)
    time.sleep(3)
    send_mesgA('play sound C')
    cpu_usage("Usage when Agent ends the call")


def testcase95():
    ###Test case 95 : Outbound 4th party conference, merging all calls , hang up order Agent A hangs up then agent B, then Agent C
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 95 : Outbound 4th party conference, merging all calls , hang up order Agent A hangs up then agent B, then Agent C")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(95)
    montor_shot(95)
    time.sleep(3)
    send_mesgA('play sound C')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    send_mesgA('C logout')
    cpu_usage("Usage when Agent ends the call")


def testcase96():
    ###Test case 96 : Outbound 4th party conference, merging all calls , hang up order Agent B, then agent C hangs up then agent A
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 96 : Outbound 4th party conference, merging all calls , hang up order Agent B, then agent C hangs up then agent A")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    refresh_and_takedata(96)
    montor_shot(96)
    time.sleep(3)
    send_mesgA('play sound C')
    recA = recv_mesgA()
    if recA == b'logout':
        end_call()
    cpu_usage("Usage when Agent ends the call")
    send_mesgA('logout')


def testcase97():
    ###Test case 97 : Outbound 4th party conference, merging all calls , hang up order Agent C hangs up then agent A, then Agent B
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 97 : Outbound 4th party conference, merging all calls , hang up order Agent C hangs up then agent A, then Agent B")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(97)
    montor_shot(97)
    time.sleep(3)
    send_mesgA('play sound C')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")


def testcase98():
    ###Test case 98 : Inbound 4th party conference, merging all calls , hang up order Customer, Agent A hangs up then agent B
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 98 : Inbound 4th party conference, merging all calls , hang up order Customer, Agent A hangs up then agent B")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(98)
    montor_shot(98)
    time.sleep(3)
    send_mesgA('play sound C')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
    end_call()
    cpu_usage("Usage when Agent ends the call")


def testcase99():
    ###Test case 99 : Inbound 4th party conference, merging all calls , hang up order Customer, Agent B hangs up then agent C
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 99 : Inbound 4th party conference, merging all calls , hang up order Customer, Agent B hangs up then agent C")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(99)
    montor_shot(99)
    time.sleep(3)
    send_mesgA('play sound C')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    send_mesgA('hangup')
    cpu_usage("Usage when Agent ends the call")


def testcase100():
    ###Test case 100 : Inbound 4th party conference, merging all calls , hang up order Customer, Agent A hangs up then agent C
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 100 : Inbound 4th party conference, merging all calls , hang up order Customer, Agent A hangs up then agent C")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(100)
    montor_shot(100)
    time.sleep(3)
    send_mesgA('play sound C')
    cpu_usage("Usage when Agent ends the call")


def testcase101():
    ###Test case 101 : Inbound 4th party conference, merging all calls , hang up order Agent A hangs up then agent B, then Agent C
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 101 : Inbound 4th party conference, merging all calls , hang up order Agent A hangs up then agent B, then Agent C")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(101)
    montor_shot(101)
    time.sleep(3)
    send_mesgA('play sound C')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    send_mesgA('C logout')
    cpu_usage("Usage when Agent ends the call")


def testcase102():
    ###Test case 102 : Inbound 4th party conference, merging all calls , hang up order Agent B, then agent C hangs up then agent A
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 102 : Inbound 4th party conference, merging all calls , hang up order Agent B, then agent C hangs up then agent A")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(102)
    montor_shot(102)
    time.sleep(3)
    send_mesgA('play sound C')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")
    send_mesgA('logout')


def testcase103():
    ###Test case 103 : Inbound 4th party conference, merging all calls , hang up order Agent C hangs up then agent A, then Agent B
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 103 : Inbound 4th party conference, merging all calls , hang up order Agent C hangs up then agent A, then Agent B")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(103)
    montor_shot(103)
    time.sleep(3)
    send_mesgA('play sound C')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")


def testcase9():
    ###Test case 9 : Inbound call conf , blind, 3rd party conf , hang up order Customer, Agent A hangs up. blind
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 9 : Inbound call conf , blind, 3rd party conf , hang up order Customer, Agent A hangs up, blind")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    time.sleep(5)
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(9)
    montor_shot(9)
    time.sleep(3)
    send_mesgA('hangup')
    cpu_usage("Usage when Agent ends the call")


def testcase10():
    ###Test case 10 : Inbound call conf , blind, 3rd party conf , hang up order Customer, Agent B hangs up
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 10 : Inbound call conf , blind, 3rd party conf , hang up order Customer, Agent B hangs up, blind")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(10)
    montor_shot(10)
    time.sleep(3)
    send_mesgA('hangup')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")


def testcase17():
    ###Test case 17 : Inbound call conf , blind, 3rd party conf , hang up order Agent A hangs up then agent B blind
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 17 : Inbound call conf , blind, 3rd party conf , hang up order Agent A hangs up then agent B, blind")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(17)
    montor_shot(17)
    time.sleep(3)
    send_mesgA('hangup')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")


def testcase18():
    ###Test case 18 : Inbound call conf , blind, 3rd party conf , hang up order Agent B hangs up then Agent A warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 18 : Inbound call conf , blind, 3rd party conf , hang up order Agent B hangs up then then Agent A warm")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(18)
    montor_shot(18)
    end_call()
    send_mesgA('hangup')
    cpu_usage("Usage when Agent ends the call")


def testcase45():
    ###Test case 45 : Oubound call conf , blind, 3rd party conf , hang up order Customer, Agent A hangs up, blind
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 45 : Oubound call conf , blind, 3rd party conf , hang up order Customer, Agent A hangs up, blind")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(45)
    montor_shot(45)
    time.sleep(3)
    send_mesgA('hangup')
    cpu_usage("Usage when Agent ends the call")


def testcase46():
    ###Test case 46 : Oubound call conf , blind, 3rd party conf , hang up order Customer, Agent B hangs up
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 46 : Oubound call conf , blind, 3rd party conf , hang up order Customer, Agent B hangs up blind")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(46)
    montor_shot(46)
    time.sleep(3)
    send_mesgA('hangup')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")


def testcase53():
    ###Test case 53 : Outbound call conf , blind, 3rd party conf , hang up order Agent A hangs up then agent B, blind
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 53 : Outbound call conf , blind, 3rd party conf , hang up order Agent A hangs up then agent B, blind")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(53)
    montor_shot(53)
    time.sleep(3)
    send_mesgA('hangup')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
    end_call()
    cpu_usage("Usage when Agent ends the call")


def testcase54():
    ###Test case 54 : Outbound call conf , blind, 3rd party conf , hang up order Agent B hangs up then Agent A, warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 54 : Outbound call conf , blind, 3rd party conf , hang up order Agent B hangs up then then Agent A, warm")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    refresh_and_takedata(54)
    montor_shot(54)
    end_call()
    send_mesgA('hangup')
    cpu_usage("Usage when Agent ends the call")


def testcase55():
    ###Test case 55 : Outbound call conf , blind, 3rd party conf , hang up order Agent A hangs up then agent B, warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 55 : Outbound call conf , blind, 3rd party conf , hang up order Agent A hangs up then agent B, warm")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(55)
    montor_shot(55)
    time.sleep(3)
    send_mesgA('hangup')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
    end_call()
    cpu_usage("Usage when Agent ends the call")


def testcase56():
    ###Test case 56 : Outbound call conf , blind, 3rd party conf , hang up order Agent B hangs up then Agent A, warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 56 : Outbound call conf , blind, 3rd party conf , hang up order Agent B hangs up then then Agent A, warm")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    refresh_and_takedata(56)
    montor_shot(56)
    end_call()
    send_mesgA('hangup')
    cpu_usage("Usage when Agent ends the call")



def testcase105():
    ###Test case 105 : Inbound call conf , warm, 3rd party conf , hang up order Customer, Agent A hangs up. warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 105 : Inbound call conf , warm, 3rd party conf , hang up order Customer, Agent A hangs up, warm")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    time.sleep(5)
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(105)
    montor_shot(105)
    time.sleep(3)
    send_mesgA('hangup')
    cpu_usage("Usage when Agent ends the call")


def testcase106():
    ###Test case 106 : Inbound call conf , warm, 3rd party conf , hang up order Customer, Agent B hangs up
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 106 : Inbound call conf , warm, 3rd party conf , hang up order Customer, Agent B hangs up, warm")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(106)
    montor_shot(106)
    time.sleep(3)
    send_mesgA('hangup')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")


def testcase107():
    ###Test case 107 : Inbound call conf , warm, 3rd party conf , hang up order Agent A hangs up then agent B warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 107 : Inbound call conf , warm, 3rd party conf , hang up order Agent A hangs up then agent B, warm")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(107)
    montor_shot(107)
    time.sleep(3)
    send_mesgA('hangup')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")


def testcase108():
    ###Test case 108 : Inbound call conf , warm, 3rd party conf , hang up order Agent B hangs up then Agent A warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 108 : Inbound call conf , warm, 3rd party conf , hang up order Agent B hangs up then then Agent A warm")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(108)
    montor_shot(108)
    end_call()
    send_mesgA('hangup')
    cpu_usage("Usage when Agent ends the call")


def testcase109():
    ###Test case 109 : Inbound call conf , warm, 3rd party conf , hang up order Agent A hangs up then agent B warm, retriving user
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 109 : Inbound call conf , warm, 3rd party conf , hang up order Agent A hangs up then agent B, warm, retriving user")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(109)
    montor_shot(109)
    time.sleep(3)
    send_mesgA('hangup')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")





def testcase110():
    ###Test case 110 : Outbound call conf , blind, 3rd party conf , hang up order Agent A hangs up then agent B, warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 110 : Outbound call conf , blind, 3rd party conf , hang up order Agent A hangs up then agent B, warm")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(110)
    montor_shot(110)
    time.sleep(3)
    send_mesgA('hangup')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
    end_call()
    cpu_usage("Usage when Agent ends the call")



def testcase111():
    ###Test case 111 : Oubound call conf , warm, 3rd party conf , hang up order Customer, Agent A hangs up, warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 111 : Oubound call conf , warm, 3rd party conf , hang up order Customer, Agent A hangs up, warm")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(111)
    montor_shot(111)
    time.sleep(3)
    send_mesgA('hangup')
    cpu_usage("Usage when Agent ends the call")


def testcase112():
    ###Test case 112 : Oubound call conf , warm, 3rd party conf , hang up order Customer, Agent B hangs up
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 112 : Oubound call conf , warm, 3rd party conf , hang up order Customer, Agent B hangs up warm")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(112)
    montor_shot(112)
    time.sleep(3)
    send_mesgA('hangup')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")



def testcase113():
    ###Test case 113 : Oubound call conf , blind, 4th party conf , hang up order Customer, Agent A hangs up then agent B, warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 113 : Oubound call conf , blind, 4th party conf , hang up order Customer, Agent A hangs up then agent B, warm")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(113)
    montor_shot(113)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")



def testcase114():
    ###Test case 114 : Oubound call conf , warm, 4th party conf , hang up order Customer, Agent B hangs up then agent A
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 114 : Oubound call conf , blind, 4th party conf , hang up order Customer, Agent B hangs up then agent A, warm")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(114)
    montor_shot(114)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    send_mesgA('hangup')
    cpu_usage("Usage when Agent ends the call")



def testcase115():
    ###Test case 115 : Oubound call conf , blind, 4th party conf , hang up order Customer, Agent B hangs up then agent C, blind
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 115 : Oubound call conf , blind, 4th party conf , hang up order Customer, Agent B hangs up then agent C, blind")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(115)
    montor_shot(115)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    send_mesgA('hangup')
    cpu_usage("Usage when Agent ends the call")



def testcase116():
    ###Test case 116 : Oubound call conf , 4th party conf , hang up order Customer, Agent C hangs up then agent B, blind
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 116 : Oubound call conf ,4th party conf , hang up order Customer, Agent C hangs up then agent B, blind")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(116)
    montor_shot(116)
    time.sleep(3)
    send_mesgA('play sound C')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")





def testcase117():
    ###Test case 117 : Oubound call conf , blind, 4th party conf , hang up order Customer, Agent A hangs up then agent C, warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 117 : Oubound call conf , blind, 4th party conf , hang up order Customer, Agent A hangs up then agent C, warm")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(117)
    montor_shot(117)
    time.sleep(3)
    send_mesgA('play sound C')
    cpu_usage("Usage when Agent ends the call")




def testcase118():
    ###Test case 118 : Outbound call conf ,4th party conf , hang up order Agent A hangs up then agent B, then Agent C, warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 118 : Outbound call conf , 4th party conf , hang up order Agent A hangs up then agent B, then Agent C, warm")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(118)
    montor_shot(118)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    send_mesgA('C logout')
    cpu_usage("Usage when Agent ends the call")



def testcase119():
    ###Test case 119 : Outbound call conf , 4th party conf , hang up order Agent A, Agent C hangs up then agent B, warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 119 : Outbound call conf , 4th party conf , hang up order Agent A, Agent C hangs up then agent B, warm")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    time.sleep(7)
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(119)
    montor_shot(119)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")



def testcase120():
    ###Test case 120 : Outbound call conf , blind, 4th party conf , hang up order Agent B hangs up then Agent A, then agent C, blind
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 120 : Outbound call conf , blind, 4th party conf , hang up order Agent B hangs up then then Agent A, then agent C, blind")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(120)
    montor_shot(120)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    send_mesgA('hangup')
    cpu_usage("Usage when Agent ends the call")



def testcase121():
    ###Test case 121 : Outbound call conf , blind, 4th party conf , hang up order Agent B, then agent C hangs up then agent A, blind
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 121 : Outbound call conf , blind, 4th party conf , hang up order Agent B, then agent C hangs up then agent A, blind")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(121)
    montor_shot(121)
    time.sleep(3)
    send_mesgA('play sound C')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")
    send_mesgA('logout')



def testcase122():
    ###Test case 122 : Inbound call conf , 4th party conf , hang up order Customer, Agent A hangs up then agent B, warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 122 : Inbound call conf , 4th party conf , hang up order Customer, Agent A hangs up then agent B, warm")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(122)
    montor_shot(122)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")



def testcase123():
    ###Test case 123 : Inbound call conf , 4th party conf , hang up order Customer, Agent B hangs up then agent A, warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 123 : Inbound call conf , 4th party conf , hang up order Customer, Agent B hangs up then agent A, warm")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(123)
    montor_shot(123)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    send_mesgA('hangup')
    cpu_usage("Usage when Agent ends the call")



def testcase124():
    ###Test case 124 : Inbound call conf , 4th party conf , hang up order Customer, Agent B hangs up then agent C, blind
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 124 : Inbound call conf, 4th party conf , hang up order Customer, Agent B hangs up then agent C, blind")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(124)
    montor_shot(124)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    send_mesgA('hangup')
    cpu_usage("Usage when Agent ends the call")



def testcase125():
    ###Test case 125 : Inbound call conf , 4th party conf , hang up order Customer, Agent C hangs up then agent B, blind
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 125 : Inbound call conf , 4th party conf , hang up order Customer, Agent C hangs up then agent B, blind")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(125)
    montor_shot(125)
    time.sleep(3)
    send_mesgA('play sound C')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")




def testcase126():
    ###Test case 126 : Inbound call conf , 4th party conf , hang up order Customer, Agent A hangs up then agent C, warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 126 : Inbound call conf , 4th party conf , hang up order Customer, Agent A hangs up then agent C, warm")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(126)
    montor_shot(126)
    time.sleep(3)
    send_mesgA('play sound C')
    cpu_usage("Usage when Agent ends the call")




def testcase127():
    ###Test case 127 : Inbound call conf ,4th party conf , hang up order Agent A hangs up then agent B, then Agent C, warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 127 : Inbound call conf ,4th party conf , hang up order Agent A hangs up then agent B, then Agent C, warm")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(127)
    montor_shot(127)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    send_mesgA('C logout')
    cpu_usage("Usage when Agent ends the call")



def testcase128():
    ###Test case 128 : Inbound call conf , 4th party conf , hang up order Agent A, Agent C hangs up then agent B, warm
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 128 : Inbound call conf , 4th party conf , hang up order Agent A, Agent C hangs up then agent B, warm")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(128)
    montor_shot(128)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
    end_call()
    cpu_usage("Usage when Agent ends the call")



def testcase129():
    ###Test case 129 : Inbound call conf , 4th party conf , hang up order Agent B hangs up then Agent A, then agent C, blind
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 129 : Inbound call conf , 4th party conf , hang up order Agent B hangs up then then Agent A, then agent C, blind")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(129)
    montor_shot(129)
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    send_mesgA('hangup')
    cpu_usage("Usage when Agent ends the call")



def testcase130():
    ###Test case 130 : Inbound call conf ,4th party conf , hang up order Agent B, then agent C hangs up then agent A, blind
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case 130 : Inbound call conf , 4th party conf , hang up order Agent B, then agent C hangs up then agent A, blind")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata(130)
    montor_shot(130)
    time.sleep(3)
    send_mesgA('play sound C')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")
    send_mesgA('logout')


def testcased1():
    ###Test case d1 : Outbound call conf, 3rd party conf , hang up order Agent A hangs up then agent B conference does not get connected,
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case d1 : Outbound call conf, 3rd party conf , hang up order Agent A hangs up then agent B, conference does not get connected")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata('d1')
    montor_shot('d1')
    time.sleep(3)
    send_mesgA('hangup')




def testcased2():
    ###Test case d2 : Outbound call conf, 3rd party conf , Agent B rejects the call from Agent A
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case d2 : Outbound call conf, 3rd party conf , Agent B rejects the call from Agent A")
    recA = recv_mesgA()
    if recA == b'not ready':
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        print('ready')
    send_mesgA('ready')
    reject_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata('d2')
    montor_shot('d2')
    time.sleep(3)
    send_mesgA('hangup')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
    end_call()
    cpu_usage("Usage when Agent ends the call")




def testcased3():
    ###Test case d3 : Outbound call conf , 3rd party conf , hang up order Agent B doesnt answer the call from Agent A
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case d3 : Outbound call conf , 3rd party conf , hang up order Agent B doesnt answer the call from Agent A")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    time.sleep(180)
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata('d3')
    montor_shot('d3')
    time.sleep(3)
    send_mesgA('hangup')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
    end_call()
    cpu_usage("Usage when Agent ends the call")



def testcased4():
    ###Test case d4 : Oubound call conf , blind, 4th party conf , Agent C rejects the call
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case d4 : Oubound call conf , blind, 4th party conf , Agent C rejects the call")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata('d4')
    montor_shot('d4')
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")



def testcased5():
    ###Test case d5 : Oubound call conf , blind, 4th party conf , Agent C doesnt answer the call from Agent B
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case d5 : Oubound call conf , blind, 4th party conf , Agent C doesnt answer the call from Agent B")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata('d5')
    montor_shot('d5')
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")



def testcased6():
    ###Test case d6 : Oubound call conf , blind, 4th party conf , Customer drops the call before 4th party conference is established
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case d6 : Oubound call conf , blind, 4th party conf , Customer drops the call before 4th party conference is established")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata('d6')
    montor_shot('d6')
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")



def testcased7():
    ###Test case d7 : Oubound call conf , blind, 4th party conf , Agent C logs out before the conferenence is established
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case d7 : Oubound call conf , blind, 4th party conf , Agent C logs out before the conferenence is established")
    recA= recv_mesgA()
    if recA == b'not ready':
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata('d7')
    montor_shot('d7')
    time.sleep(3)
    send_mesgA('play sound C')
    cpu_usage("Usage when Agent ends the call")



def testcased8():
    ###Test case d8 : Inbound call conf, 3rd party conf , hang up order Agent A hangs up then agent B conference does not get connected,
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case d8 : Inbound call conf, 3rd party conf , hang up order Agent A hangs up then agent B, conference does not get connected")
    recA = recv_mesgA()
    if recA == b'not ready':
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata('d8')
    montor_shot('d8')
    time.sleep(3)
    send_mesgA('hangup')
    cpu_usage("Usage when Agent ends the call")



def testcased9():
    ###Test case d9 : Inbound call conf, 3rd party conf , Agent B rejects the call from Agent A
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case d9 : Inbound call conf, 3rd party conf , Agent B rejects the call from Agent A")
    recA = recv_mesgA()
    if recA == b'not ready':
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        print('ready')
    send_mesgA('ready')
    time.sleep(4)
    reject_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata('d9')
    montor_shot('d9')
    time.sleep(3)
    send_mesgA('hangup')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
    end_call()
    cpu_usage("Usage when Agent ends the call")




def testcased10():
    ###Test case d10 : Inbound call conf , 3rd party conf , hang up order Agent B doesnt answer the call from Agent A
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case d10 : Inbound call conf , 3rd party conf , hang up order Agent B doesnt answer the call from Agent A")
    recA = recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA = recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    time.sleep(180)
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA = recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata('d10')
    montor_shot('d10')
    time.sleep(3)
    send_mesgA('hangup')
    recA = recv_mesgA()
    if recA == b'logout':
        agent_unmute()
    end_call()
    cpu_usage("Usage when Agent ends the call")



def testcased11():
    ###Test case d11 : Inbound call conf , blind, 4th party conf , Agent C rejects the call
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case d11 : Inbound call conf , blind, 4th party conf , Agent C rejects the call")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata('d11')
    montor_shot('d11')
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")



def testcased12():
    ###Test case d12 : Inbound call conf , blind, 4th party conf , Agent C doesnt answer the call from Agent B
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case d12 : Inbound call conf , blind, 4th party conf , Agent C doesnt answer the call from Agent B")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata('d12')
    montor_shot('d12')
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")



def testcased13():
    ###Test case d13 : Inbound call conf , blind, 4th party conf , Customer drops the call before 4th party conference is established
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case d13 : Inbound call conf , blind, 4th party conf , Customer drops the call before 4th party conference is established")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata('d13')
    montor_shot('d13')
    time.sleep(3)
    send_mesgA('play sound C')
    recA= recv_mesgA()
    if recA == b'logout':
        agent_unmute()
        end_call()
    cpu_usage("Usage when Agent ends the call")



def testcased14():
    ###Test case d14 : Inbound call conf , blind, 4th party conf , Agent C logs out before the conferenence is established
    logging.info(" ")
    logging.info(" ")
    logging.info("Test case d14 : Inbound call conf , blind, 4th party conf , Agent C logs out before the conferenence is established")
    recA= recv_mesgA()
    if recA == b'not ready':
        #not_ready_user()
        print("not ready user")
    recA= recv_mesgA()
    if recA == b'ready Agent B':
        #ready_user()
        print('ready')
    send_mesgA('ready')
    incoming_call()
    send_mesgA('received call')
    cpu_usage("Usage when Agent receives incoming call")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    recA= recv_mesgA()
    if recA == b'b play sound':
        agent_unmute()
    play_sound()
    cpu_usage("Usage when Agent is playing sound")
    agent_mute()
    cpu_usage("Usage when Agent goes to mute state")
    refresh_and_takedata('d14')
    montor_shot('d14')
    time.sleep(3)
    send_mesgA('play sound C')
    cpu_usage("Usage when Agent ends the call")






###config file
App_path = os.path.dirname(sys.argv[0]) + '/'

config = configparser.ConfigParser(allow_no_value=True)
config.read_file(open(App_path + r'config.txt'))
hostnameA = config.get('automationconfig', 'hostnameA')
hostnameB = config.get('automationconfig', 'hostnameB')
hostnameC = config.get('automationconfig', 'hostnameC')
UsernameB = config.get('automationconfig', 'UsernameB')
PasswordB = config.get('automationconfig', 'PasswordB')
QmprouserB = config.get('automationconfig', 'QmprouserB')
QmpasswdB = config.get('automationconfig', 'QmpasswdB')
print (QmpasswdB)


logging.basicConfig(filename=App_path +'Logs/' + datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"), level=logging.INFO)

### declarations of drivers
options = webdriver.ChromeOptions()
# options.extension.getURL('index.html');
options.add_extension(App_path + 'Store_v1.16.crx')
driver = webdriver.Chrome(chrome_options=options)
action = ActionChains(driver)


BP, QMPro, testcall, nooftimes = login()

j, i ,k=[0, 1, 1]

while j < int(nooftimes):
    if testcall =='All':
        """testcase104()
        testcase75()
        testcase76()
        testcase77()
        testcase78()
        testcase79()
        testcase80()
        testcase81()
        testcase82()
        testcase83()
        testcase84()
        testcase85()
        testcase86()
        testcase87()
        testcase88()"""
        testcase89()
        testcase90()
        testcase91()
        testcase37()
        testcase38()
        testcase39()
        testcase40()
        testcase41()
        testcase42()
        testcase43()
        testcase44()
        testcase47()
        testcase48()
        testcase49()
        testcase50()
        testcase51()
        testcase52()
        testcase57()
        testcase58()
        testcase59()
        testcase60()
        testcase61()
        testcase62()
        testcase63()
        testcase64()
        testcase65()
        testcase66()
        testcase67()
        testcase68()
        testcase69()
        testcase70()
        testcase71()
        testcase72()
        testcase73()
        testcase74()
        testcase92()
        testcase93()
        testcase94()
        testcase95()
        testcase96()
        testcase97()
        testcase45()
        testcase46()
        testcase53()
        testcase54()
        testcase55()
        testcase56()
        testcase110()
        testcase111()
        testcase112()
        testcase113()
        testcase114()
        testcase115()
        testcase116()
        testcase117()
        testcase118()
        testcase119()
        testcase120()
        testcase121()
        testcase1()
        testcase2()
        testcase3()
        testcase4()
        testcase5()
        testcase6()
        testcase7()
        testcase8()
        testcase11()
        testcase12()
        testcase13()
        testcase14()
        testcase15()
        testcase16()
        testcase19()
        testcase20()
        testcase21()
        testcase22()
        testcase23()
        testcase24()
        testcase25()
        testcase26()
        testcase27()
        testcase28()
        testcase29()
        testcase30()
        testcase31()
        testcase32()
        testcase33()
        testcase34()
        testcase35()
        testcase36()
        testcase98()
        testcase99()
        testcase100()
        testcase101()
        testcase102()
        testcase103()
        testcase9()
        testcase10()
        testcase17()
        testcase18()
        testcase105()
        testcase106()
        testcase107()
        testcase108()
        testcase109()
        testcase122()
        testcase123()
        testcase124()
        testcase125()
        testcase126()
        testcase127()
        testcase128()
        testcase129()
        testcase130()
    elif testcall == "Inbound":
        testcase1()
        testcase2()
        testcase3()
        testcase4()
        testcase5()
        testcase6()
        testcase7()
        testcase8()
        testcase11()
        testcase12()
        testcase13()
        testcase14()
        testcase15()
        testcase16()
        testcase19()
        testcase20()
        testcase21()
        testcase22()
        testcase23()
        testcase24()
        testcase25()
        testcase26()
        testcase27()
        testcase28()
        testcase29()
        testcase30()
        testcase31()
        testcase32()
        testcase33()
        testcase34()
        testcase35()
        testcase36()
        testcase98()
        testcase99()
        testcase100()
        testcase101()
        testcase102()
        testcase103()
        testcase9()
        testcase10()
        testcase17()
        testcase18()
        testcase105()
        testcase106()
        testcase107()
        testcase108()
        testcase109()
        testcase122()
        testcase123()
        testcase124()
        testcase125()
        testcase126()
        testcase127()
        testcase128()
        testcase129()
        testcase130()
    elif testcall == "Outbound":
        testcase37()
        testcase38()
        testcase39()
        testcase40()
        testcase41()
        testcase42()
        testcase43()
        testcase44()
        testcase47()
        testcase48()
        testcase49()
        testcase50()
        testcase51()
        testcase52()
        testcase57()
        testcase58()
        testcase59()
        testcase60()
        testcase61()
        testcase62()
        testcase63()
        testcase64()
        testcase65()
        testcase66()
        testcase67()
        testcase68()
        testcase69()
        testcase70()
        testcase71()
        testcase72()
        testcase73()
        testcase74()
        testcase92()
        testcase93()
        testcase94()
        testcase95()
        testcase96()
        testcase97()
        testcase45()
        testcase46()
        testcase53()
        testcase54()
        testcase55()
        testcase56()
        testcase110()
        testcase111()
        testcase112()
        testcase113()
        testcase114()
        testcase115()
        testcase116()
        testcase117()
        testcase118()
        testcase119()
        testcase120()
        testcase121()
    elif testcall == "Internal":
        testcase104()
        testcase75()
        testcase76()
        testcase77()
        testcase78()
        testcase79()
        testcase80()
        testcase81()
        testcase82()
        testcase83()
        testcase84()
        testcase85()
        testcase86()
        testcase87()
        testcase88()
        testcase89()
        testcase90()
        testcase91()
    elif testcall == "Preliminary":
        """testcase1()
        testcase5()"""
        testcase25()
        testcase27()
        testcase29()
        testcase9()
        testcase109()
        testcase11()
        testcase92()
        testcase45()
        testcase110()
        testcase47()
        testcase37()
        testcase41()
        testcase63()
        testcase65()
        testcase67()
        testcase75()
        testcase86()
    elif testcall == "Destructive":
        testcased1()
        testcased2()
        testcased3()
        testcased4()
        testcased5()
        testcased6()
        testcased7()
        testcased8()
        testcased9()
        testcased10()
        testcased11()
        testcased12()
        testcased13()
        testcased14()
    else:
        if testcall[1:2] == '-':
            i = int(testcall[0:1])
            k = int(testcall[2:4])
        elif testcall[2:3] == '-':
            i = int(testcall[0:2])
            k = int(testcall[3:6])
        elif testcall[3:4] == '-':
            i = int(testcall[0:3])
            k = int(testcall[4:7])
        while i <= k:
            if i == 1:
                    testcase104()
            if i == 2:
                    testcase75()
            if i == 3:
                    testcase76()
            if i == 4:
                    testcase77()
            if i == 5:
                    testcase78()
            if i == 6:
                    testcase79()
            if i == 7:
                    testcase80()
            if i == 8:
                    testcase81()
            if i == 9:
                    testcase82()
            if i == 10:
                    testcase83()
            if i == 11:
                    testcase84()
            if i == 12:
                    testcase85()
            if i == 13:
                    testcase86()
            if i == 14:
                    testcase87()
            if i == 15:
                    testcase88()
            if i == 16:
                    testcase89()
            if i == 17:
                    testcase90()
            if i == 18:
                    testcase91()
            if i==19:
                    testcase37()
            if i==20:
                    testcase38()
            if i==21:
                    testcase39()
            if i==22:
                    testcase40()
            if i==23:
                    testcase41()
            if i==24:
                    testcase42()
            if i==25:
                    testcase43()
            if i==26:
                    testcase44()
            if i==27:
                    testcase45()
            if i==28:
                    testcase46()
            if i==29:
                    testcase47()
            if i==30:
                    testcase48()
            if i==31:
                    testcase49()
            if i==32:
                    testcase50()
            if i==33:
                    testcase51()
            if i==34:
                    testcase52()
            if i==35:
                    testcase57()
            if i==36:
                    testcase58()
            if i==37:
                    testcase59()
            if i==38:
                    testcase60()
            if i==39:
                    testcase61()
            if i==40:
                    testcase62()
            if i==41:
                    testcase63()
            if i==42:
                    testcase64()
            if i==43:
                    testcase65()
            if i==44:
                    testcase66()
            if i==45:
                    testcase67()
            if i==46:
                    testcase68()
            if i==47:
                    testcase69()
            if i==48:
                    testcase70()
            if i==49:
                    testcase71()
            if i==50:
                    testcase72()
            if i==51:
                    testcase73()
            if i==52:
                    testcase74()
            if i==53:
                    testcase92()
            if i==54:
                    testcase93()
            if i==55:
                    testcase94()
            if i==56:
                    testcase95()
            if i==57:
                    testcase96()
            if i==58:
                    testcase97()
            if i==59:
                    testcase45()
            if i==60:
                    testcase46()
            if i==61:
                    testcase53()
            if i ==62:
                    testcase54()
            if i==63:
                    testcase55()
            if i==64:
                    testcase56()
            if i==65:
                    testcase110()
            if i==66:
                    testcase111()
            if i==67:
                    testcase112()
            if i==68:
                    testcase113()
            if i==69:
                    testcase114()
            if i==70:
                    testcase115()
            if i==71:
                    testcase116()
            if i==72:
                    testcase117()
            if i==73:
                    testcase118()
            if i==74:
                    testcase119()
            if i==75:
                    testcase120()
            if i==76:
                    testcase121()
            if i==77:
                    testcase1()
            if i==78:
                    testcase2()
            if i==79:
                    testcase3()
            if i==80:
                    testcase4()
            if i==81:
                    testcase5()
            if i==82:
                    testcase6()
            if i==83:
                    testcase7()
            if i==84:
                    testcase8()
            if i==85:
                    testcase11()
            if i==86:
                    testcase12()
            if i==87:
                    testcase13()
            if i==88:
                    testcase14()
            if i==89:
                    testcase15()
            if i==90:
                    testcase16()
            if i==91:
                    testcase19()
            if i==92:
                    testcase20()
            if i==93:
                    testcase21()
            if i==94:
                    testcase22()
            if i==95:
                    testcase23()
            if i==96:
                    testcase24()
            if i==97:
                    testcase25()
            if i==98:
                    testcase26()
            if i==99:
                    testcase27()
            if i==100:
                    testcase28()
            if i==101:
                    testcase29()
            if i==102:
                    testcase30()
            if i==103:
                    testcase31()
            if i==104:
                    testcase32()
            if i==105:
                    testcase33()
            if i==106:
                    testcase34()
            if i==107:
                    testcase35()
            if i==108:
                    testcase36()
            if i==109:
                    testcase98()
            if i==110:
                    testcase99()
            if i==111:
                    testcase100()
            if i==112:
                    testcase101()
            if i==113:
                    testcase102()
            if i==114:
                    testcase103()
            if i==115:
                    testcase9()
            if i==116:
                    testcase10()
            if i==117:
                    testcase17()
            if i==118:
                    testcase18()
            if i==119:
                    testcase105()
            if i==120:
                    testcase106()
            if i==121:
                    testcase107()
            if i==122:
                    testcase108()
            if i==123:
                    testcase109()
            if i == 124:
                    testcase122()
            if i == 125:
                    testcase123()
            if i == 126:
                    testcase124()
            if i == 127:
                    testcase125()
            if i == 128:
                     testcase126()
            if i == 129:
                     testcase127()
            if i == 130:
                     testcase128()
            if i == 131:
                     testcase129()
            if i == 132:
                     testcase130()
            i+=1
    print(j)
    if j == int(nooftimes):
        break
    j+=1