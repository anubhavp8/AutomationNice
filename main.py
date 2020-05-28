### Note -- please start the winium driver in C:\Users\7053516\Desktop\python\Winium\Winium.Desktop.Driver

# !/usr/bin/env pythonak
# -*- coding: utf-8 -*-

import time
import psutil
import ctypes
import socket
import subprocess
import logging
import traceback
import pyautogui
import PIL.ImageGrab
import PySimpleGUI as sg
from retrying import retry
from selenium.webdriver import ActionChains
from playsound import playsound
from selenium.webdriver.common.keys import Keys
from appium import webdriver
import datetime
import configparser
import os
import sys
import signal
from xlwt import Workbook
from xlrd import open_workbook
from xlutils.copy import copy
import threading
import multiprocessing.pool
import functools
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os.path
from os import path
from xlutils.margins import number_of_good_rows
import pytest
import schedule




def timeout(max_timeout):
    """Timeout decorator, parameter in seconds."""
    def timeout_decorator(item):
        """Wrap the original function."""
        @functools.wraps(item)
        def func_wrapper(*args, **kwargs):
            """Closure for function."""
            pool = multiprocessing.pool.ThreadPool(processes=1)
            async_result = pool.apply_async(item, args, kwargs)
            # raises a TimeoutError if execution exceeds max_timeout
            return async_result.get(max_timeout)
        return func_wrapper
    return timeout_decorator



###Definitions of all the functions

def running():
    prog = [line.split() for line in subprocess.check_output("tasklist").splitlines()]
    [prog.pop(e) for e in [0, 1, 2]]  # useless
    for task in prog:
        for loop in task:
            print(loop.decode())
            if (loop.decode() == 'Avaya'):
                return ("found")




def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)



def job():
    raise Exception('test')



def user_input():
    sg.ChangeLookAndFeel('GreenTan')


    form = sg.FlexForm('Automation Panel', default_element_size=(40, 1))

    layout = [
        [sg.Text('Automation tool to test BP and QM PRO!', size=(30, 1), font=("Helvetica", 25))],
        [sg.Text('Please select if you want to run test on BP or QM Pro')],
        [sg.Radio('BP', "RADIO1", default=True), sg.Radio('QM Pro', "RADIO1")],
        [sg.Text('Please enter the range of test you want to test Eg All for running all the test')],
        [sg.Text('Or Outbound for running all the Outbound test or Inbound for all Inbound test')],
        [sg.Text('Or enter Internal for running all the Internal test or enter range lke 1-5')],
        [sg.InputText('All')],
        [sg.Text('how many times you want to run it')],
        [sg.InputText('2')],
        [sg.Text('_' * 80)],
        [sg.Submit(), sg.Cancel()]
    ]


    button, values = form.Layout(layout).Read()


    form.hide()

    return(values[0], values[1], values[2], values[3])



@timeout(2200)
def send_mesgB(mes):
    try:
        s = socket.socket()
        s.connect((hostnameB, 3125))
        s.sendall(mes.encode())
        print('Mesg sent to agent B', mes)
        s.close()
    except:
        time.sleep(1)
        print(mes)
        send_mesgB(mes)


@timeout(2000)
def recv_mesgB():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 3126))
    print('Agent A binded to the Agent B')
    try:
        s.listen(3)
        print('Agent A is listening')
    except:
        print(socket.error)
    while True:
        c, addr = s.accept()
        print('Got connection from ', addr)
        print('Mesg received from Agent B')
        return c.recv(1024)



@timeout(2200)
def send_mesgC(mes):
    try:
        s = socket.socket()
        s.connect((hostnameC, 3123))
        s.sendall(mes.encode())
        print('Mesg sent to Agent C', mes)
        s.close()
    except:
        time.sleep(1)
        send_mesgC(mes)



@timeout(2000)
def recv_mesgC():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 3124))
    print ('Agent A binded to the Agent B')
    s.listen(3)
    print('Agent A is listening')
    while True:
        c, addr = s.accept()
        print('Got connection from ', addr)
        print('Mesg recvd from Agent C')
        return c.recv(1024)


###memory usage
def cpu_usage(mesg):
    ts = time.time()
    if (psutil.virtual_memory()[2]) < 90:
        logging.info(mesg)

        logging.info(str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')) + " cpu percent: " + str(psutil.cpu_percent()))

        logging.info(str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')) + " virtual memory percent: " + str(psutil.virtual_memory()))

        logging.info(str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')) + " memory % used: " + str(psutil.virtual_memory()[2]))

        logging.info("")
    else:
        logging.critical(mesg)
        logging.critical(str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')) + " cpu percent: " + str(
            psutil.cpu_percent()))
        logging.critical(
            str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')) + " virtual percent: " + str(
                psutil.virtual_memory()))
        logging.critical(
            str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')) + " memory % used: " + str(
                psutil.virtual_memory()[2]))
        logging.info("")




###open webpage
def Open_page():
    driver.get('https://hc301.tthcslabs.com/agentdesktop/')
    time.sleep(5)





###login
def login_page():
    driver.find_element_by_name('username').send_keys(UsernameA)
    time.sleep(1)
    driver.find_element_by_name('password').send_keys(PasswordA)
    time.sleep(1)
    driver.find_element_by_id("auth-submit").click()
    time.sleep(10)


###login
def login_again():
    time.sleep(1)
    driver.find_element_by_name('password').send_keys(PasswordA)
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



def login_brightpattern():
    driver.get('https://teletech.brightpattern.com/agentdesktop/')
    time.sleep(5)
    driver.find_element_by_name('username').send_keys(QmprouserA)
    time.sleep(1)
    driver.find_element_by_name('password').send_keys(QmpasswdA)
    time.sleep(1)
    driver.find_element_by_id("auth-submit").click()
    time.sleep(10)


###ready
def ready_user():
    try:

        check_network_issue()

        driver.find_element_by_id("gwt-debug-acStateMenuContainer").click()
        time.sleep(2)
        elements = driver.find_elements_by_xpath("//*[@title='Ready']")
        if not elements:
            print('ready not found')
        else:
            driver.find_element_by_xpath("//*[@title='Ready']").click()
            time.sleep(2)
    except:
        if BP == True:
            elements = driver.find_elements_by_xpath("//*[@title='Not ready']")
            if not elements:
                print('not ready element not found')
            else:
                driver.find_element_by_xpath("//*[@title='Not ready']").click()
        else:
            driver.find_element_by_xpath("//*[@title='Not Ready']").click()
        time.sleep(2)



def check_if_not_ready():
    driver.find_element_by_id("gwt-debug-acStateMenuContainer").click()
    time.sleep(2)
    print('checking ready element found')
    elements = driver.find_elements_by_xpath("//*[@title='Ready']")
    if not elements:
        print('ready element not found')
        if BP == True:
            driver.find_element_by_xpath("//*[@title='Not ready']").click()
        else:
            driver.find_element_by_xpath("//*[@title='Not Ready']").click()
    else:
        print('ready element found')
        driver.find_element_by_xpath("//*[@title='Ready']").click()



###not ready

def not_ready_user():
    try:

        check_network_issue()

        driver.find_element_by_id("gwt-debug-acStateMenuContainer").click()
        time.sleep(2)
        if BP == True:
            elements = driver.find_elements_by_xpath("//*[@title='Not ready']")
            if not elements:
                print('not ready element not found')
            else:
                driver.find_element_by_xpath("//*[@title='Not ready']").click()
        else:
            driver.find_element_by_xpath("//*[@title='Not Ready']").click()
        time.sleep(2)
    except:
        elements = driver.find_elements_by_xpath("//*[@title='Ready']")
        if not elements:
            print('ready not found')
        else:
            driver.find_element_by_xpath("//*[@title='Ready']").click()
            time.sleep(2)
        print(4)


###respond incoming call


def incoming_call():
    sss = driver.find_element_by_id("gwt-debug-acStateMenuContainer")
    i = 0
    while i <= 30:
        try:

            pyautogui.moveTo(100, 200)
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
            if i ==15:
                action.move_to_element_with_offset(sss, 550, 550).click().perform()


def incoming_call2():
    try:
        i = 0
        while i <= 30:
            elements = driver.find_elements_by_id("b-navigation-item-dialpad2")
            if not elements:
                print('call not found')
            else:
                action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad2")).perform()
                time.sleep(0.2)
                driver.find_element_by_id("b-navigation-item-dialpad2").click()
                time.sleep(0.2)
                elements = driver.find_elements_by_id("cpAccept")
                if not elements:
                    print('call not found')
                else:
                    driver.find_element_by_id("cpAccept").click()
                    break
            i = i + 1
            print(i)
    except:
        time.sleep(10)
        ready_user()
        incoming_call2()


###make incoming call using avaya
def Call_from_Avaya_equinox():
    try:
        #    Mbox('MsgBox', 'Please press ok when avaya has loaded completely', 1)
        #win_driver.find_element_by_name("Show Dialpad").click()
        #time.sleep(2)
        if BP == True:
            win_driver.find_element_by_class_name("TextBox").send_keys(AvayaToAgent)
        else:
            win_driver.find_element_by_class_name("TextBox").send_keys(QmAvayaToAgent)
        time.sleep(2)
        win_driver.find_element_by_class_name("TextBox").send_keys(Keys.ENTER)
        #win_driver.find_element_by_name("Voice Call").click()
        time.sleep(10)
        elements = win_driver.find_elements_by_name("Drop")
        if not elements:
            print('r')
            win_driver.find_element_by_name("Show Dialpad").click()
            time.sleep(2)
            if BP == True:
                win_driver.find_element_by_class_name("TextBox").send_keys(AvayaToAgent)
            else:
                win_driver.find_element_by_class_name("TextBox").send_keys(QmAvayaToAgent)
            time.sleep(2)
            win_driver.find_element_by_name("Voice Call").click()
            time.sleep(5)
        else:
            print('element found')
        win_driver.find_element_by_name("Show Dialpad").click()
        time.sleep(2)
        win_driver.find_element_by_name("1").click()
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
    except:
        time.sleep(10)
        Call_from_Avaya_equinox()


def call_from_avaya_again():
    time.sleep(1)
    elements= win_driver.find_elements_by_name("Pause")
    if not elements:
        print('call not found')
        win_driver.find_element_by_name("Show Dialpad").click()
        time.sleep(2)
        win_driver.find_element_by_name("TextBox").send_keys(AvayaToAgent)
        time.sleep(2)
        win_driver.find_element_by_name("Voice Call").click()
        time.sleep(5)
        win_driver.find_element_by_name("Show Dialpad").click()
        time.sleep(2)
        win_driver.find_element_by_name("TextBox").send_keys('1')
        incoming_call()
    else:
        print("call going on")
    Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))



def agent_hold():
    try:

        check_network_issue()

        playsound('Agent hold.mp3')
        time.sleep(1)
        action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
        time.sleep(2)
        driver.find_element_by_id("cpHold").click()
        time.sleep(2)
    except:
        try:
            playsound('Agent hold.mp3')
            time.sleep(1)
            action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
            time.sleep(2)
            driver.find_element_by_id("cpHold").click()
            time.sleep(2)
        except:
            print("agent hold not found")


def check_network_issue():
    ##code to check network issue
    elements = driver.find_elements_by_id("gwt-debug-cdbOk")
    if not elements:
        print('ready not found')
    else:
        driver.find_element_by_id("gwt-debug-cdbOk").click()
        raise Exception('test')


def agent_retrive(inst):

    check_network_issue()

    playsound('Agent Retrive.mp3')
    if inst == 'hold':
        """time.sleep(1)
        action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
        time.sleep(2)
        driver.find_element_by_id("cpHold").click()
        time.sleep(2)"""
    else:
        try:
            time.sleep(1)
            action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
            time.sleep(2)
            driver.find_element_by_xpath("//*[@class='b-icon b-icon-hold']").click()
            playsound('confirmretrieve.mp3')
            action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
            time.sleep(2)
            driver.find_element_by_id("cpRetrieve").click()
            time.sleep(2)
        except:
            print("error while retreive")


def agent_mute():
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
            print('mute is not clicked')


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

def screenshot(testcase):
    driver.save_screenshot("Screenshot_" + str(testcase) + ".png")


###playsound
def play_sound_agent():
    playsound('Record Agent.mp3')


def play_sound_customer():
    playsound('Record - Customer.mp3')


def monitor_shot(inst):
    im = PIL.ImageGrab.grab()
    im.save("./Screenshots/Test" + str(inst)+ str("_") + datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p") + ".png")


def agent_minimize():
    time.sleep(1)
    driver.minimize_window()


def client_minimize():
    time.sleep(1)
    win_action.move_to_element(win_driver.find_element_by_name("Avaya Equinox - 1 running window")).click().perform()
    time.sleep(1)


def agent_maximize():
    time.sleep(1)
    handleofthewindow = driver.current_window_handle
    driver.switch_to.window(handleofthewindow)


def client_maximize():
    time.sleep(1)
    win_action.move_to_element(win_driver.find_element_by_name("Avaya Equinox - 1 running window")).click().perform()
    time.sleep(1)


def leave_conf():
    try:
        check_network_issue()

        time.sleep(1)
        action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
        time.sleep(2)
        driver.find_element_by_id("cpLeaveConference").click()
    except:
        end_call()


###end the call
def end_call():
    check_network_issue()
    try:
        playsound('Agent hangup.mp3')
        action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
        time.sleep(2)
        driver.find_element_by_id("cpEndCall").click()
        time.sleep(2)
    except:
        print("element not found")


def exp_hang_up():
    elements = driver.find_elements_by_id("b-navigation-item-dialpad2")
    if not elements:
        action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
        time.sleep(1)
        elements2 = driver.find_elements_by_id("cphold")
        if not elements2:
            print('call not found')
        else:
            print('call found')
            driver.find_element_by_id("cpEndCall").click()
    else:
        action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad2")).perform()
        time.sleep(2)
        driver.find_element_by_id("b-navigation-item-dialpad2").click()
        print('a')
        elements2 = driver.find_elements_by_id("cphold")
        if not elements2:
            print('call not found')
            driver.find_element_by_id("b-navigation-item-dialpad1").click()
        else:
            print('call found')
            action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad2")).perform()
            time.sleep(1)
            driver.find_element_by_id("b-navigation-item-dialpad2").click()
            print('s')
            time.sleep(1)
            driver.find_element_by_id("cpEndCall").click()
            print('call ended')


###hangup the call
def hangup_call():
    check_network_issue()

    playsound('Agent hangup.mp3')
    time.sleep(1)
    action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
    time.sleep(2)
    driver.find_element_by_id("cpEndCall").click()


def customer_mute():
    check_network_issue()
    try:
        elements= win_driver.find_elements_by_name("Mute call")
        if not elements:
            print("mute not found")
        else:
            print("mute found")
            win_driver.find_element_by_name("Mute call").click()
    
        time.sleep(1)
        elements= win_driver.find_elements_by_name("Mute call")
        if not elements:
            print("mute not found")
        else:
            print("mute found")
            win_driver.find_element_by_name("Mute call").click()
    
        time.sleep(1)
        elements= win_driver.find_elements_by_name("Mute call")
        if not elements:
            print("mute not found")
        else:
            print("mute found")
            win_driver.find_element_by_name("Mute call").click()
    except:
        print("customer hangup not found")


def customer_unmute():
    check_network_issue()
    try:
        time.sleep(1)
        elements= win_driver.find_elements_by_name("Unmute call")
        if not elements:
            print("unmute not found")
        else:
            print("unmute found")
            win_driver.find_element_by_name("Unmute call").click()
        time.sleep(1)
    
        elements= win_driver.find_elements_by_name("Unmute call")
        if not elements:
            print("unmute not found")
        else:
            print("unmute found")
            win_driver.find_element_by_name("Unmute call").click()
    
        time.sleep(1)
        elements= win_driver.find_elements_by_name("Unmute call")
        if not elements:
            print("unmute not found")
        else:
            print("unmute found")
            win_driver.find_element_by_name("Unmute call").click()
    except:
        print("customer unmute not found")


def customer_hangsup():
    try:
        playsound('Customer hangup.mp3')

        elements= win_driver.find_elements_by_name("Drop")
        if not elements:
            print("Customer hangup not found")
        else:
            print('customer hangup found')
            win_driver.find_element_by_name("Drop").click()
        time.sleep(1)

        elements = win_driver.find_elements_by_name("Drop")
        if not elements:
            print("Customer hangup not found")
        else:
            print('customer hangup found')
            win_driver.find_element_by_name("Drop").click()
        time.sleep(1)

        elements = win_driver.find_elements_by_name("Drop")
        if not elements:
            print("Customer hangup not found")
        else:
            print('customer hangup found')
            win_driver.find_element_by_name("Drop").click()
    except:
        print("customer hangup not found")


def agent_resize():
    driver.set_window_size(1050, 450)


def merge_all():
    check_network_issue()

    time.sleep(2)
    driver.find_element_by_id("MergeCallsDialogBox").click()



###making the call
def agent_call():
    try:

        check_network_issue()
        if BP ==True:
            time.sleep(2)
            action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad2")).perform()
            time.sleep(2)
            driver.find_element_by_xpath("//*[@id='sp-destination']").send_keys(ExtensionB)
            time.sleep(2)
            driver.find_element_by_xpath("//*[@id='dial-toolbar-call']/button").click()
            time.sleep(2)
        else:
            brightpattern_agent_call()
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
    except:
        staleElement = True
        while (staleElement):
            try:
                print(traceback.format_exc())
                time.sleep(2)
                #WebDriverWait(driver, 10).until(EC.element_to_be_clickable(driver.find_elements_by_name'b-navigation-item-dialpad2')).click()
                action.move_to_element(driver.find_element_by_name("b-navigation-item-dialpad2")).perform()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='sp-destination']").send_keys(AgentToAvaya)
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='dial-toolbar-call']/button").click()
                staleElement = False
            except:
                staleElement = True



def agent_call_to_customer():
    try:
        check_network_issue()
        time.sleep(2)
        action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad2")).perform()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='sp-destination']").send_keys(AgentToAvaya)
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='dial-toolbar-call']/button").click()
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
    except:
         try:
             print(traceback.format_exc())
             time.sleep(2)
             action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad2")).perform()
             time.sleep(2)
             driver.find_element_by_xpath("//*[@id='sp-destination']").send_keys(AgentToAvaya)
             time.sleep(2)
             driver.find_element_by_xpath("//*[@id='dial-toolbar-call']/button").click()
         except:
             print(traceback.format_exc())
             if BP == True:
                 elements = driver.find_elements_by_xpath("//*[@title='Not ready']")
                 if not elements:
                     print('not ready element not found')
                 else:
                     driver.find_element_by_xpath("//*[@title='Not ready']").click()
             else:
                 driver.find_element_by_xpath("//*[@title='Not Ready']").click()
             time.sleep(2)
             agent_call_to_customer()




def customer_answer():
    i = 0
    while i <= 30:
         elements= win_driver.find_elements_by_name("Answer")
         if not elements:
             print("Customer Answer not found")
         else:
             print('customer answer found')
             win_driver.find_element_by_name("Answer").click()
             return
    i = i + 1
    print(i)
    time.sleep(1)



def brightpattern_agent_call():
    check_network_issue()
    time.sleep(4)
    action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad2")).perform()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='sp-destination']").send_keys(QmextnB)
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='dial-toolbar-call']/button").click()
    time.sleep(3)



def brightpattern_blind_conference():
    check_network_issue()
    time.sleep(3)
    action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
    time.sleep(2)
    driver.find_element_by_id("b-navigation-item-dialpad1").click()
    time.sleep(2)
    driver.find_element_by_id("sp-destination").send_keys(QmextnC)
    time.sleep(2)
    driver.find_element_by_id("gwt-uid-20").click()
    # driver.find_element_by_id("dial-toolbar-blind").click()
    time.sleep(2)
    driver.find_element_by_id("gwt-uid-26").click()
    time.sleep(2)
    driver.find_element_by_css_selector("#dial-toolbar-call > button").click()


def blind_conference():
    check_network_issue()
    if BP ==True:
        time.sleep(2)
        action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
        time.sleep(2)
        driver.find_element_by_id("b-navigation-item-dialpad1").click()
        time.sleep(2)
        driver.find_element_by_id("sp-destination").send_keys(ExtensionC)
        time.sleep(2)
        driver.find_element_by_id("gwt-uid-20").click()
        time.sleep(2)
        driver.find_element_by_id("gwt-uid-26").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#dial-toolbar-call > button").click()
    else:
        brightpattern_blind_conference()



def bright_pattern_blind_conference2():
    check_network_issue()
    time.sleep(2)
    action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
    time.sleep(2)
    driver.find_element_by_id("b-navigation-item-dialpad1").click()
    time.sleep(2)
    driver.find_element_by_id("sp-destination").send_keys(QmextnB)
    time.sleep(2)
    driver.find_element_by_id("gwt-uid-20").click()
    time.sleep(2)
    driver.find_element_by_id("gwt-uid-26").click()
    time.sleep(2)
    driver.find_element_by_css_selector("#dial-toolbar-call > button").click()


def blind_conference2():
    check_network_issue()
    if BP ==True:
        time.sleep(2)
        action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
        time.sleep(2)
        driver.find_element_by_id("b-navigation-item-dialpad1").click()
        time.sleep(2)
        driver.find_element_by_id("sp-destination").send_keys(ExtensionB)
        time.sleep(2)
        driver.find_element_by_id("gwt-uid-20").click()
        time.sleep(2)
        driver.find_element_by_id("gwt-uid-26").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#dial-toolbar-call > button").click()
    else:
        bright_pattern_blind_conference2()


def bright_pattern_warm_conference():
    check_network_issue()
    time.sleep(2)
    action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
    time.sleep(2)
    driver.find_element_by_id("b-navigation-item-dialpad1").click()
    time.sleep(2)
    driver.find_element_by_id("sp-destination").send_keys(QmextnC)
    time.sleep(2)
    driver.find_element_by_id("gwt-uid-20").click()
    time.sleep(2)
    driver.find_element_by_id("gwt-uid-24").click()
    time.sleep(2)
    driver.find_element_by_css_selector("#dial-toolbar-call > button").click()


def warm_conference():
    check_network_issue()
    if BP ==True:
        time.sleep(2)
        action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
        time.sleep(2)
        driver.find_element_by_id("b-navigation-item-dialpad1").click()
        time.sleep(2)
        driver.find_element_by_id("sp-destination").send_keys(ExtensionC)
        time.sleep(2)
        driver.find_element_by_id("gwt-uid-20").click()
        time.sleep(2)
        driver.find_element_by_id("gwt-uid-24").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#dial-toolbar-call > button").click()
    else:
        bright_pattern_warm_conference()


def bright_pattern_warm_conference2():
    check_network_issue()
    time.sleep(2)
    action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
    time.sleep(2)
    driver.find_element_by_id("b-navigation-item-dialpad1").click()
    time.sleep(2)
    driver.find_element_by_id("sp-destination").send_keys(QmextnB)
    time.sleep(2)
    driver.find_element_by_id("gwt-uid-20").click()
    time.sleep(2)
    driver.find_element_by_id("gwt-uid-24").click()
    time.sleep(2)
    driver.find_element_by_css_selector("#dial-toolbar-call > button").click()


def warm_conference2():
    check_network_issue()
    if BP == True:
        time.sleep(2)
        action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
        time.sleep(2)
        driver.find_element_by_id("b-navigation-item-dialpad1").click()
        time.sleep(2)
        driver.find_element_by_id("sp-destination").send_keys(ExtensionB)
        time.sleep(2)
        driver.find_element_by_id("gwt-uid-20").click()
        time.sleep(2)
        driver.find_element_by_id("gwt-uid-24").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#dial-toolbar-call > button").click()
    else:
        bright_pattern_warm_conference2()


def blind_transferencia():
    check_network_issue()
    time.sleep(2)
    action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
    time.sleep(2)
    driver.find_element_by_id("b-navigation-item-dialpad1").click()
    time.sleep(2)
    if BP == True:
        driver.find_element_by_id("sp-destination").send_keys(ExtensionC)
    else:
        driver.find_element_by_id("sp-destination").send_keys(QmextnC)
    time.sleep(2)
    driver.find_element_by_id("dial-toolbar-blind").click()


def blind_transferencia2():
    check_network_issue()
    try:
        time.sleep(2)
        action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
        time.sleep(2)
        driver.find_element_by_id("b-navigation-item-dialpad1").click()
        time.sleep(2)
        if BP == True:
            driver.find_element_by_id("sp-destination").send_keys(ExtensionB)
        else:
            driver.find_element_by_id("sp-destination").send_keys(QmextnB)
        time.sleep(2)
        driver.find_element_by_id("dial-toolbar-blind").click()
    except:
        try:
            time.sleep(2)
            action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
            time.sleep(2)
            driver.find_element_by_id("b-navigation-item-dialpad1").click()
            time.sleep(2)
            if BP == True:
                driver.find_element_by_id("sp-destination").send_keys(ExtensionB)
            else:
                driver.find_element_by_id("sp-destination").send_keys(QmextnB)
            time.sleep(2)
            driver.find_element_by_id("dial-toolbar-blind").click()
        except:
            print("blind transfer element not found")


def bright_pattern_blind_transferencia():
    check_network_issue()
    time.sleep(2)
    action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
    time.sleep(2)
    driver.find_element_by_id("b-navigation-item-dialpad1").click()
    time.sleep(2)
    driver.find_element_by_id("sp-destination").send_keys(QmextnC)
    time.sleep(2)
    driver.find_element_by_id("dial-toolbar-blind").click()


def bright_pattern_blind_transferencia2():
    check_network_issue()
    time.sleep(2)
    action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
    time.sleep(2)
    driver.find_element_by_id("b-navigation-item-dialpad1").click()
    time.sleep(2)
    driver.find_element_by_id("sp-destination").send_keys(QmextnB)
    time.sleep(2)
    driver.find_element_by_id("dial-toolbar-blind").click()

def agent_merge():
    check_network_issue()
    time.sleep(2)
    playsound('Merge.mp3')
    action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
    time.sleep(2)
    driver.find_element_by_id("cpMerge").click()


def comp_transf():
    check_network_issue()
    time.sleep(2)
    playsound('complete transf.mp3')
    action.move_to_element(driver.find_element_by_id("b-navigation-item-dialpad1")).perform()
    time.sleep(2)
    driver.find_element_by_id("cpTransfer").click()



###Log out user after testing
def log_out():
    check_network_issue()
    driver.find_element_by_id("top-toolbar-logout").click()
    time.sleep(2)
    driver.find_element_by_id("gwt-debug-cdbOk").click()
    time.sleep(4)
    #win_driver.quit()


######################################

###Function calls

#########################################


######BP test cases

def testcase0(exp):
    try:
        logging.info(" ")
        logging.info(" ")
        if exp == 'exception':
            subprocess.Popen("killB.bat", cwd=r"./")
            subprocess.Popen("killC.bat", cwd=r"./")
            time.sleep(5)
            subprocess.Popen("executecall.bat", cwd=r"./")
            subprocess.Popen("executecall2.bat", cwd=r"./")
            customer_hangsup()
            time.sleep(50)
        time.sleep(30)
        send_mesgB(str(BP))
        time.sleep(15)
        #if recv_mesgC() == b'ready':
        send_mesgC(str(BP))
        if exp != 'exception':
            if BP == True:
                 Open_page()
                 cpu_usage("Usage when Agent is loading")
                 login_page()
            else:
                login_brightpattern()
                already_logged_in()
        time.sleep(6)
        if exp == 'exception':
            time.sleep(10)
        send_mesgB('getting ready')
        if recv_mesgB() == b'login A':
            print('test case 0 running')
        if exp == 'exception':
            print("not ready user")
        else:
            #ready_user()
            print("ready user")
        print('resizing agent')
        agent_resize()
        print('login a comp')
        send_mesgB('login A comp')
        cpu_usage("Usage when Agent goes to ready state")
        print('line618')
        if recv_mesgB() == b'next mesg':
            send_mesgB(str(BP))
        print('line621')
        if recv_mesgB() == b'next mesg':
            send_mesgB(str(QMPro))
        print('line624')
        if recv_mesgB() == b'next mesg':
            send_mesgB(str(testcall))
        print('line627')
        if recv_mesgB() == b'next mesg':
            send_mesgB(str(nooftimes))
        time.sleep(3)
        send_mesgC(str(BP))
        if recv_mesgC() == b'next mesg':
            send_mesgC(str(QMPro))
        print('line634')
        if recv_mesgC() == b'next mesg':
            send_mesgC(str(testcall))
        print('line637')
        if recv_mesgC() == b'next mesg':
            send_mesgC(str(nooftimes))
        print('line640')
    except:
        print(9)
        logging.error(traceback.format_exc())
        #nice_driver.close()
        #exp_hang_up()
        testcase0('exception')




def testcase104():
    try:
        recB = recv_mesgB()
        if recB == b'ready':
            print('agentcall')
        logging.info("Test case 104: Simple Internal conference between A and B. Blind (A, B)")
        Report.write(row, 2, item)
        Report.write(row, 3, '104')
        Report.write(row, 4, 'Simple Internal conference between A and B. Blind (A, B)')
        agent_call()
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        recB = recv_mesgB()
        if recB == b'agent A':
            agent_mute()
        agent_unmute()
        playsound('Testcase104.mp3')
        play_sound_agent()
        agent_mute()
        send_mesgB('agent B')
        refresh_and_takedata(104)
        monitor_shot(104)
        recB = recv_mesgB()
        if recB == b'logout':
            agent_unmute()
            end_call()  # agent hang up
        elif recB == b'exception':
            testcase104()
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        print(88)
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinternal
        if testcall == "All":
            testcall = "01-" + str(totaltest)
        if testcall == "Internal":
            testcall = "01-" + str(totalinternal)
        #nice_driver.close()
        #exp_hang_up()
        testcase0('exception')
        testcase104()



def testcaseint75():
    try:
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 75: Internal call conference between A, B, C. (Blind). Hang up Order Agent A , Agent B")
        cpu_usage("Usage when Agent goes to ready state")
        Report.write(row, 2, item)
        Report.write(row, 3, '75')
        Report.write(row, 4, 'Internal call conference between A, B, C. (Blind). Hang up Order Agent A , Agent B')
        time.sleep(3)
        send_mesgB('ready Agent B')
        recB = recv_mesgB()
        print(recB)
        if recB == b'ready':
            print("mesg receive from B")
        agent_call()
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        print(1)
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        elif recB == b'exception':
            testcaseint75()
        agent_mute()
        refresh_and_takedata(75)
        monitor_shot(75.1)
        cpu_usage("Usage when AgentB receives incoming call")
        time.sleep(3)
        agent_unmute()
        playsound('Testcase75.mp3')
        time.sleep(1)
        playsound('AgentAtoC.mp3')
        agent_mute()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_unmute()
        elif recC == b'exception':
            testcaseint75()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        elif recB == b'exception':
            testcaseint75()
        send_mesgC('agent C play sound')
        monitor_shot(75.3)
        refresh_and_takedata(75)
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
        elif recC == b'exception':
            testcaseint75()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
        #raise Exception('test')
    except:
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        logging.error(traceback.format_exc())
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinternal
        if testcall == "All":
            testcall = "02-" + str(totaltest)
        if testcall == "Internal":
            testcall = "02-" + str(totalinternal)
        #exp_hang_up()
       # nice_driver.close()
        testcase0('exception')
        testcaseint75()



def testcaseint76():
    try:
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 76: Internal call conference between A, B, C. (Blind). Hang up Order Agent A , Agent C")
        cpu_usage("Usage when Agent goes to ready state")
        Report.write(row, 2, item)
        Report.write(row, 3, '76')
        Report.write(row, 4, 'Internal call conference between A, B, C. (Blind). Hang up Order Agent A , Agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            agent_call()
        elif recB == b'exception':
            testcaseint76()
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        elif recB == b'exception':
            testcaseint76()
        agent_mute()
        monitor_shot(76.1)
        refresh_and_takedata(76)
        cpu_usage("Usage when AgentB receives incoming call")
        time.sleep(3)
        agent_unmute()
        playsound('Testcase76.mp3')
        time.sleep(1)
        playsound('AgentAtoC.mp3')
        agent_mute()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_unmute()
        elif recC == b'exception':
            testcaseint76()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        elif recB == b'exception':
            testcaseint76()
        send_mesgC('agent C play sound')
        monitor_shot(76.3)
        recC = recv_mesgC()
        if recC == b'hangup':
             agent_unmute()
        elif recC == b'exception':
            testcaseint76()
        playsound('Agent hangup.mp3')
        leave_conf()
        time.sleep(3)
        send_mesgC('hangup')
        send_mesgB('finish test')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
        #raise Exception('test')
    except:
        logging.error(traceback.format_exc())
        global testcall, totaltest, totalinternal
        if testcall == "All":
            testcall = "03-" + str(totaltest)
        if testcall == "Internal":
            testcall = "03-" + str(totalinternal)
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        testcase0('exception')
        testcaseint76()



def testcaseint77():
    try:
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 77: Internal call conference between A, B, C. (Blind). Hang up Order Agent B , Agent C")
        Report.write(row, 2, item)
        Report.write(row, 3, '77')
        Report.write(row, 4, 'Internal call conference between A, B, C. (Blind). Hang up Order Agent B , Agent C')
        cpu_usage("Usage when Agent goes to ready state")
        recB = recv_mesgB()
        if recB == b'ready':
            print('r')
        elif recB == b'exception':
            testcaseint77()
        agent_call()
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        elif recB == b'exception':
            testcaseint77()
        agent_mute()
        refresh_and_takedata(77)
        monitor_shot(77.1)
        cpu_usage("Usage when AgentB receives incoming call")
        time.sleep(3)
        agent_unmute()
        playsound('Testcase77.mp3')
        playsound('AgentAtoC.mp3')
        agent_mute()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_unmute()
        elif recC == b'exception':
            testcaseint77()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        elif recB == b'exception':
            testcaseint77()
        send_mesgC('agent C play sound')
        monitor_shot(77.3)
        refresh_and_takedata(77)
        recC = recv_mesgC()
        if recC == b'hangup':
             print('a')
        elif recB == b'exception':
            testcaseint77()
        send_mesgB('hangup')
        recB = recv_mesgB()
        if recB == b'left conf':
            print("si")
        elif recB == b'exception':
            testcaseint77()
        send_mesgC('hangup')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinternal
        if testcall == "All":
            testcall = "04-" + str(totaltest)
        if testcall == "Internal":
            testcall = "04-" + str(totalinternal)
        #exp_hang_up()
       # nice_driver.close()
        testcase0('exception')
        testcaseint77()


#########################################################################################
def testcaseint78():
    try:
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 78: Internal call conference between A, B, C. (Warm). Hang up Order Agent A , Agent B")
        Report.write(row, 2, item)
        Report.write(row, 3, '78')
        Report.write(row, 4, 'Internal call conference between A, B, C. (Warm). Hang up Order Agent A , Agent B')
        cpu_usage("Usage when Agent goes to ready state")
        time.sleep(7)
        send_mesgB('ready Agent B')
        recB = recv_mesgB()
        if recB == b'ready':
            time.sleep(6)
            agent_call()
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_mute()
        monitor_shot(78.1)
        refresh_and_takedata(78)
        cpu_usage("Usage when AgentB receives incoming call")
        time.sleep(3)
        agent_unmute()
        playsound('Testcase78.mp3')
        time.sleep(1)
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        agent_hold()
        time.sleep(1)
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            print('a')
        elif recC == b'exception':
            testcaseint78()
        agent_merge()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        elif recB == b'exception':
            testcaseint78()
        send_mesgC('agent C play sound')
        monitor_shot(78.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
        elif recC == b'exception':
            testcaseint78()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinternal
        if testcall == "All":
            testcall = "05-" + str(totaltest)
        if testcall == "Internal":
            testcall = "05-" + str(totalinternal)
        #exp_hang_up()
       # nice_driver.close()
        testcase0('exception')
        testcaseint78()



def testcaseint79():
    try:
        logging.info(" ")
        logging.info(" ")
        time.sleep(7)
        logging.info("Test case 79: Internal call conference between A, B, C. (Warm) Hang up Order Agent A , Agent C")
        Report.write(row, 2, item)
        Report.write(row, 3, '79')
        Report.write(row, 4, 'Internal call conference between A, B, C. (Warm) Hang up Order Agent A , Agent C')
        cpu_usage("Usage when Agent goes to ready state")
        recB = recv_mesgB()
        if recB == b'ready':
            agent_call()
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        elif recB == b'exception':
            testcaseint79()
        agent_mute()
        refresh_and_takedata(79)
        monitor_shot(79.1)
        cpu_usage("Usage when AgentB receives incoming call")
        time.sleep(3)
        agent_unmute()
        playsound('Testcase79.mp3')
        time.sleep(1)
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        agent_hold()
        time.sleep(1)
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            print('a')
        elif recC == b'exception':
            testcaseint79()
        agent_merge()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        elif recB == b'exception':
            testcaseint79()
        send_mesgC('agent C play sound')
        monitor_shot(79.3)
        recC = recv_mesgC()
        if recC == b'hangup':
             agent_unmute()
        elif recC == b'exception':
            testcaseint79()
        playsound('Agent hangup.mp3')
        leave_conf()
        send_mesgC('hangup')
        send_mesgB('finish test')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinternal
        if testcall == "All":
            testcall = "06-" + str(totaltest)
        if testcall == "Internal":
            testcall = "06-" + str(totalinternal)
        #exp_hang_up()
       # nice_driver.close()
        testcase0('exception')
        testcaseint79()



def testcaseint80():
    try:
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 80: Internal call conference between A, B, C. (Warm). Hang up Order Agent B , Agent C")
        Report.write(row, 2, item)
        Report.write(row, 3, '80')
        Report.write(row, 4, 'Internal call conference between A, B, C. (Warm). Hang up Order Agent B , Agent C')
        cpu_usage("Usage when Agent goes to ready state")
        recB = recv_mesgB()
        if recB == b'ready':
            agent_call()
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        elif recB == b'exception':
            testcaseint80()
        agent_mute()
        refresh_and_takedata(80)
        monitor_shot(80.1)
        cpu_usage("Usage when AgentB receives incoming call")
        time.sleep(3)
        agent_unmute()
        playsound('Testcase80.mp3')
        time.sleep(1)
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        agent_hold()
        time.sleep(1)
        agent_mute()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            print('a')
        elif recC == b'exception':
            testcaseint80()
        agent_merge()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        elif recB == b'exception':
            testcaseint80()
        send_mesgC('agent C play sound')
        monitor_shot(80.3)
        recC = recv_mesgC()
        if recC == b'hangup':
             print('a')
        elif recC == b'exception':
            testcaseint80()
        send_mesgB('hangup')
        recB = recv_mesgB()
        if recB == b'left conf':
            print("si")
        elif recB == b'exception':
            testcaseint80()
        send_mesgC('hangup')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinternal
        if testcall == "All":
            testcall = "07-" + str(totaltest)
        if testcall == "Internal":
            testcall = "07-" + str(totalinternal)
        #exp_hang_up()
       # nice_driver.close()
        testcase0('exception')
        testcaseint80()

#######################################################################


def testcaseint81():
    try:
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 81: Internal call conference between A, B, C. (retreiving A, B).")
        Report.write(row, 2, item)
        Report.write(row, 3, '81')
        Report.write(row, 4, 'Internal call conference between A, B, C. (retreiving A, B).')
        cpu_usage("Usage when Agent goes to ready state")
        time.sleep(7)
        send_mesgB('ready Agent B')
        recB = recv_mesgB()
        if recB == b'ready':
            print('s')
        elif recB == b'exception':
            testcaseint81()
        time.sleep(6)
        agent_call()
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        elif recB == b'exception':
            testcaseint81()
        agent_mute()
        refresh_and_takedata(81)
        monitor_shot(81.1)
        cpu_usage("Usage when AgentB receives incoming call")
        time.sleep(3)
        agent_unmute()
        playsound('Testcase81.mp3')
        time.sleep(1)
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        agent_hold()
        time.sleep(1)
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            print('a')
        elif recC == b'exception':
            testcaseint81()
        agent_retrive('hold')
        agent_merge()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        elif recB == b'exception':
            testcaseint81()
        send_mesgC('agent C play sound')
        monitor_shot(81.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
        elif recC == b'exception':
            testcaseint81()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinternal
        if testcall == "All":
            testcall = "08-" + str(totaltest)
        if testcall == "Internal":
            testcall = "08-" + str(totalinternal)
        #exp_hang_up()
       # nice_driver.close()
        testcase0('exception')
        testcaseint81()



def testcaseint82():
    try:
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 82: Internal call conference between A, B, C. (Retrieving A,C )")
        Report.write(row, 2, item)
        Report.write(row, 3, '82')
        Report.write(row, 4, 'Internal call conference between A, B, C. (Retrieving A,C )')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        recB = recv_mesgB()
        if recB == b'ready':
            agent_call()
        elif recB == b'exception':
            testcaseint82()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        elif recB == b'exception':
            testcaseint82()
        agent_mute()
        refresh_and_takedata(82)
        monitor_shot(82.1)
        cpu_usage("Usage when AgentB receives incoming call")
        time.sleep(3)
        agent_unmute()
        playsound('Testcase82.mp3')
        time.sleep(1)
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        agent_hold()
        time.sleep(1)
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            print('a')
        elif recC == b'exception':
            testcaseint82()
        agent_retrive('hold')
        agent_merge()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        elif recB == b'exception':
            testcaseint82()
        send_mesgC('agent C play sound')
        monitor_shot(82.3)
        recC = recv_mesgC()
        if recC == b'hangup':
             agent_unmute()
        elif recC == b'exception':
            testcaseint82()
        playsound('Agent hangup.mp3')
        leave_conf()
        send_mesgC('hangup')
        send_mesgB('finish test')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinternal
        if testcall == "All":
            testcall = "09-" + str(totaltest)
        if testcall == "Internal":
            testcall = "09-" + str(totalinternal)
        logging.error(traceback.format_exc())
        testcase0('exception')
        testcaseint82()

@pytest.mark.timeout(1200)
def testcaseint83():
    try:
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 83: Internal call conference between A, B, C. (Retrieving B, C")
        Report.write(row, 2, item)
        Report.write(row, 3, '83')
        Report.write(row, 4, 'Internal call conference between A, B, C. (Retrieving B, C')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        recB = recv_mesgB()
        if recB == b'ready':
            print('s')
        elif recB == b'exception':
            testcaseint83()
        time.sleep(6)
        agent_call()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        elif recB == b'exception':
            testcaseint83()
        agent_mute()
        refresh_and_takedata(83)
        monitor_shot(83.1)
        cpu_usage("Usage when AgentB receives incoming call")
        time.sleep(3)
        agent_unmute()
        playsound('Testcase83.mp3')
        time.sleep(1)
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        agent_hold()
        time.sleep(1)
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            print('a')
        elif recC == b'exception':
            testcaseint83()
        agent_retrive('hold')
        agent_merge()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        elif recB == b'exception':
            testcaseint83()
        send_mesgC('agent C play sound')
        monitor_shot(83.3)
        recC = recv_mesgC()
        if recC == b'hangup':
             print('a')
        elif recC == b'exception':
            testcaseint83()
        send_mesgB('hangup')
        recB = recv_mesgB()
        if recB == b'left conf':
            print("si")
        elif recB == b'exception':
            testcaseint83()
        send_mesgC('hangup')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinternal
        if testcall == "All":
            testcall = "10-" + str(totaltest)
        if testcall == "Internal":
            testcall = "10-" + str(totalinternal)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcaseint83()

#######################################################################

@pytest.mark.timeout(1200)
def testcaseint84():
    try:
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 84: Internal call Transfer to Agent. (Blind). Agent B to hangup")
        Report.write(row, 2, item)
        Report.write(row, 3, '84')
        Report.write(row, 4, 'Internal call Transfer to Agent. (Blind). Agent B to hangup')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        recB = recv_mesgB()
        if recB == b'ready':
            print('y')
        elif recB == b'exception':
            testcaseint84()
        time.sleep(10)
        agent_call()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        elif recB == b'exception':
            testcaseint84()
        agent_mute()
        refresh_and_takedata(84)
        monitor_shot(84.1)
        cpu_usage("Usage when AgentB receives incoming call")
        time.sleep(1)
        agent_unmute()
        playsound('Testcase84.mp3')
        time.sleep(1)
        playsound('AgentAtrasnfertoB.mp3')
        agent_mute()
        blind_transferencia()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            send_mesgB('b play sound')
        elif recC == b'exception':
            testcaseint84()
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        elif recB == b'exception':
            testcaseint84()
        send_mesgC('agent C play sound')
        monitor_shot(84.3)
        recC = recv_mesgC()
        if recC == b'hangup':
             print('a')
        elif recC == b'exception':
            testcaseint84()
        send_mesgB('hangup')
        recB = recv_mesgB()
        if recB == b'left conf':
            print("test 84 completed successfully")
        elif recB == b'exception':
            testcaseint84()
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinternal
        if testcall == "All":
            testcall = "11-" + str(totaltest)
        if testcall == "Internal":
            testcall = "11-" + str(totalinternal)
        #exp_hang_up()
       # nice_driver.close()
        testcase0('exception')
        testcaseint84()


@pytest.mark.timeout(1200)
def testcaseint85():
    try:
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 85: Internal call Transfer to Agent. (Blind). Agent C to hangup")
        Report.write(row, 2, item)
        Report.write(row, 3, '85')
        Report.write(row, 4, 'Internal call Transfer to Agent. (Blind). Agent B to hangup')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        recB = recv_mesgB()
        if recB == b'ready':
            time.sleep(10)
            agent_call()
        elif recB == b'exception':
            testcaseint85()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        elif recB == b'exception':
            testcaseint85()
        agent_mute()
        refresh_and_takedata(85)
        monitor_shot(85.1)
        cpu_usage("Usage when AgentB receives incoming call")
        time.sleep(3)
        agent_unmute()
        playsound('Testcase85.mp3')
        time.sleep(1)
        playsound('AgentAtrasnfertoB.mp3')
        agent_mute()
        blind_transferencia()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
               send_mesgB('b play sound')
        elif recC == b'exception':
            testcaseint85()
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        elif recB == b'exception':
            testcaseint85()
        send_mesgC('agent C play sound')
        monitor_shot(85.3)
        recC = recv_mesgC()
        if recC == b'hangup':
             print('a')
        elif recC == b'exception':
            testcaseint85()
        send_mesgB('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinternal
        if testcall == "All":
            testcall = "12-" + str(totaltest)
        if testcall == "Internal":
            testcall = "12-" + str(totalinternal)
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcaseint85()

################################################################

@pytest.mark.timeout(1200)
def testcaseint86():
    try:
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 86: Internal call Transfer to Agent. (Warm). Agent B to hangup")
        Report.write(row, 2, item)
        Report.write(row, 3, '86')
        Report.write(row, 4, 'Internal call Transfer to Agent. (Blind). Agent B to hangup')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        recB = recv_mesgB()
        if recB == b'ready':
            time.sleep(10)
            agent_call()
        elif recB == b'exception':
            testcaseint86()
        cpu_usage("Usage when conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        elif recB == b'exception':
            testcaseint86()
        agent_mute()
        refresh_and_takedata(86)
        monitor_shot(86.1)
        cpu_usage("Usage when AgentB receives incoming call")
        time.sleep(1)
        agent_unmute()
        playsound('Testcase86.mp3')
        time.sleep(1)
        playsound('AgentAtrasnfertoB.mp3')
        agent_mute()
        agent_hold()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            comp_transf()
        elif recC == b'exception':
            testcaseint86()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        elif recB == b'exception':
            testcaseint86()
        send_mesgC('agent C play sound')
        monitor_shot(86.3)
        recC = recv_mesgC()
        if recC == b'hangup':
             print('a')
        elif recC == b'exception':
            testcaseint86()
        send_mesgB('hangup')
        recB = recv_mesgB()
        if recB == b'left conf':
            print("test 86 completed successfully")
        elif recB == b'exception':
            testcaseint86()
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinternal
        if testcall == "All":
            testcall = "13-" + str(totaltest)
        if testcall == "Internal":
            testcall = "13-" + str(totalinternal)
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcaseint86()

@pytest.mark.timeout(1200)
def testcaseint87():
    try:
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 87: Internal call Transfer to Agent. (Warm). Agent C to hangup")
        Report.write(row, 2, item)
        Report.write(row, 3, '87')
        Report.write(row, 4, 'Internal call Transfer to Agent. (Warm). Agent C to hangup')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        recB = recv_mesgB()
        if recB == b'ready':
            time.sleep(10)
            agent_call()
        elif recB == b'exception':
            testcaseint87()
        cpu_usage("Usage when conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        elif recB == b'exception':
            testcaseint87()
        agent_mute()
        refresh_and_takedata(87)
        monitor_shot(87.1)
        cpu_usage("Usage when AgentB receives incoming call")
        time.sleep(3)
        agent_unmute()
        playsound('Testcase87.mp3')
        time.sleep(1)
        playsound('AgentAtrasnfertoB.mp3')
        agent_mute()
        agent_hold()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            comp_transf()
        elif recC == b'exception':
            testcaseint87()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        elif recB == b'exception':
            testcaseint87()
        send_mesgC('agent C play sound')
        monitor_shot(87.3)
        recC = recv_mesgC()
        if recC == b'hangup':
             print('a')
        elif recC == b'exception':
            testcaseint87()
        send_mesgB('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinternal
        if testcall == "All":
            testcall = "14-" + str(totaltest)
        if testcall == "Internal":
            testcall = "14-" + str(totalinternal)
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcaseint87()

###############################################

@pytest.mark.timeout(1200)
def testcaseint88():
    try:
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 88: Internal call Transfer to Agent. Retrieving agent B")
        Report.write(row, 2, item)
        Report.write(row, 3, '88')
        Report.write(row, 4, 'Internal call Transfer to Agent. Retrieving agent B')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        recB = recv_mesgB()
        if recB == b'ready':
            time.sleep(10)
            agent_call()
        elif recB == b'exception':
            testcaseint88()
        cpu_usage("Usage when conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        elif recB == b'exception':
            testcaseint88()
        agent_mute()
        refresh_and_takedata(88)
        monitor_shot(88.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('Testcase88.mp3')
        time.sleep(1)
        playsound('AgentAtrasnfertoB.mp3')
        agent_mute()
        agent_hold()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            print('88case is running')
        elif recC == b'exception':
            testcaseint88()
        agent_retrive('hold')
        agent_retrive('h')
        comp_transf()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        elif recB == b'exception':
            testcaseint88()
        send_mesgC('agent C play sound')
        monitor_shot(88.3)
        recC = recv_mesgC()
        if recC == b'hangup':
             print('a')
        elif recC == b'exception':
            testcaseint88()
        send_mesgB('hangup')
        recB = recv_mesgB()
        if recB == b'left conf':
            print("test 88 completed successfully")
        elif recB == b'exception':
            testcaseint88()
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinternal
        if testcall == "All":
            testcall = "15-" + str(totaltest)
        if testcall == "Internal":
            testcall = "15-" + str(totalinternal)
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcaseint88()
################################################


@pytest.mark.timeout(1200)
def testcaseint89():
    try:
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 89: Internal call Transfer to Agent. Retrieving agent C")
        Report.write(row, 2, item)
        Report.write(row, 3, '89')
        Report.write(row, 4, 'Internal call Transfer to Agent. Retrieving agent C')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        recB = recv_mesgB()
        if recB == b'ready':
            agent_call()
        elif recB == b'exception':
            testcaseint89()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        elif recB == b'exception':
            testcaseint89()
        agent_mute()
        refresh_and_takedata(89)
        monitor_shot(89.1)
        cpu_usage("Usage when AgentB receives incoming call")
        time.sleep(3)
        agent_unmute()
        playsound('Testcase89.mp3')
        time.sleep(1)
        playsound('AgentAtrasnfertoB.mp3')
        agent_mute()
        agent_hold()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        agent_retrive('hold')
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_retrive('h')
            comp_transf()
        elif recC == b'exception':
            testcaseint89()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        elif recB == b'exception':
            testcaseint89()
        send_mesgC('agent C play sound')
        monitor_shot(89.3)
        recC = recv_mesgC()
        if recC == b'hangup':
             print('a')
        elif recC == b'exception':
            testcaseint89()
        send_mesgB('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinternal
        if testcall == "All":
            testcall = "16-" + str(totaltest)
        if testcall == "Internal":
            testcall = "16-" + str(totalinternal)
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcaseint89()

###############################################

@pytest.mark.timeout(1200)
def testcaseint90():
    try:
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 90: Internal call Transfer to Agent. No hold Agent B")
        Report.write(row, 2, item)
        Report.write(row, 3, '90')
        Report.write(row, 4, 'Internal call Transfer to Agent. No hold Agent B')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        recB = recv_mesgB()
        if recB == b'ready':
            time.sleep(7)
            agent_call()
        elif recB == b'exception':
            testcaseint90()
        cpu_usage("Usage when conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        elif recB == b'exception':
            testcaseint90()
        agent_mute()
        refresh_and_takedata(90)
        monitor_shot(90.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('Testcase90.mp3')
        time.sleep(1)
        playsound('AgentAtrasnfertoB.mp3')
        agent_mute()
        blind_transferencia()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        print('test1')
        if recC == b'c ready':
            send_mesgB('b play sound')
        elif recC == b'exception':
            testcaseint90()
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        elif recB == b'exception':
            testcaseint90()
        send_mesgC('agent C play sound')
        monitor_shot(90.3)
        recC = recv_mesgC()
        if recC == b'hangup':
             print('a')
        elif recC == b'exception':
            testcaseint90()
        send_mesgB('hangup')
        recB = recv_mesgB()
        if recB == b'left conf':
            print("test 90 completed successfully")
        elif recB == b'exception':
            testcaseint90()
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinternal
        if testcall == "All":
            testcall = "17-" + str(totaltest)
        if testcall == "Internal":
            testcall = "17-" + str(totalinternal)
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcaseint90()


@pytest.mark.timeout(1200)
def testcaseint91():
    try:
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 91: Internal call Transfer to Agent. No hold Agent C")
        Report.write(row, 2, item)
        Report.write(row, 3, '91')
        Report.write(row, 4, 'Internal call Transfer to Agent. No hold Agent C')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        recB = recv_mesgB()
        if recB == b'ready':
            time.sleep(7)
            agent_call()
        elif recB == b'exception':
            testcaseint91()
        cpu_usage("Usage when conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        elif recB == b'exception':
            testcaseint91()
        agent_mute()
        refresh_and_takedata(91)
        monitor_shot(91.1)
        cpu_usage("Usage when AgentB receives incoming call")
        time.sleep(3)
        agent_unmute()
        playsound('Testcase91.mp3')
        time.sleep(1)
        playsound('AgentAtrasnfertoB.mp3')
        agent_mute()
        blind_transferencia()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            send_mesgB('b play sound')
        elif recC == b'exception':
            testcaseint91()
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        elif recB == b'exception':
            testcaseint91()
        send_mesgC('agent C play sound')
        monitor_shot(91.3)
        recC = recv_mesgC()
        if recC == b'hangup':
             print('a')
        elif recC == b'exception':
            testcaseint91()
        send_mesgB('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinternal
        if testcall == "All":
            testcall = "18-" + str(totaltest)
        if testcall == "Internal":
            testcall = "18-" + str(totalinternal)
        testcase0('exception')
        testcaseint91()
###################################################################################

##############customer calls
###Test case 1 : Inbound call Customer hangs up
@pytest.mark.timeout(1200)
def testcase1():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 1: Inbound call. Customer hangs up")
        Report.write(row, 2, item)
        Report.write(row, 3, '1')
        Report.write(row, 4, 'Inbound call. Customer hangs up')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase1.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        play_sound_agent()
        customer_unmute()
        cpu_usage("Usage when recording is happening")
        refresh_and_takedata(1)
        monitor_shot(1)
        cpu_usage("Usage while taking screenshot")
        agent_mute()
        customer_hangsup()
        cpu_usage("Usage when Customer ends the call")
        send_mesgB('ready')
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "67-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "67-" + str(totalinbound)
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase1()

@pytest.mark.timeout(1200)
###Test case 2 : (Receive inbound call and place customer on hold 1X. Customer hangs up)
def testcase2():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 2: Place customer on hold 1X. Customer hangs up")
        Report.write(row, 2, item)
        Report.write(row, 3, '2')
        Report.write(row, 4, 'Place customer on hold 1X. Customer hangs up')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        ready_user()
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase2.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        agent_mute()
        play_sound_agent()
        agent_unmute()
        cpu_usage("Usage when recording is happening")
        refresh_and_takedata(2)
        monitor_shot(2)
        cpu_usage("Usage when recording is happening")
        agent_hold()
        cpu_usage("Usage when customer goes on hold")
        time.sleep(5)
        agent_retrive('h')
        customer_unmute()
        agent_mute()
        cpu_usage("Usage when customer is retrieved")
        customer_hangsup()  ##customer hang up
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('ready')
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "68-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "68-" + str(totalinbound)
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase2()

@pytest.mark.timeout(1200)
###Test case 3 : (Receive inbound call and place customer on hold 2X. Customer hangs up)
def testcase3():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 3: Place customer on hold 2X. Customer hangs up")
        Report.write(row, 2, item)
        Report.write(row, 3, '3')
        Report.write(row, 4, 'Place customer on hold 2X. Customer hangs up')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        ready_user()
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase3.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        play_sound_agent()
        cpu_usage("Usage when recording is happening")
        customer_unmute()
        agent_mute()
        agent_hold()
        cpu_usage("Usage when customer is on hold")
        time.sleep(3)
        agent_retrive('h')
        time.sleep(3)
        cpu_usage("Usage when customer is retrieved")
        agent_hold()
        time.sleep(3)
        cpu_usage("Usage when customer is on hold 2")
        agent_retrive('h')
        refresh_and_takedata(3)
        monitor_shot(3)
        time.sleep(3)
        cpu_usage("Usage when customer is retrieved 2")
        customer_hangsup()  ##customer hang up
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('ready')
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "69-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "69-" + str(totalinbound)
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase3()

@pytest.mark.timeout(1200)
###Test case 4 : (Receive inbound call and place customer on hold 3X. Customer hangs up)
def testcase4():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 4: Place customer on hold 3X. Customer hangs up")
        Report.write(row, 2, item)
        Report.write(row, 3, '4')
        Report.write(row, 4, 'Place customer on hold 3X. Customer hangs up')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        ready_user()
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase4.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        play_sound_agent()
        cpu_usage("Usage when recording is happening")
        agent_hold()
        cpu_usage("Usage when customer is on hold")
        time.sleep(3)
        agent_retrive('h')
        cpu_usage("Usage when customer is retrieved")
        time.sleep(3)
        agent_hold()
        cpu_usage("Usage when customer is hold 2")
        time.sleep(3)
        agent_retrive('h')
        refresh_and_takedata(4)
        monitor_shot(4)
        cpu_usage("Usage when customer is on retrieved 2")
        time.sleep(3)
        agent_hold()
        cpu_usage("Usage when customer is on hold 3")
        time.sleep(3)
        agent_retrive('h')
        cpu_usage("Usage when customer is retrieved 3")
        time.sleep(3)
        customer_unmute()
        agent_mute()
        customer_hangsup()  ##customer hang up
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('ready')
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "70-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "70-" + str(totalinbound)
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase4()

###Test case 5 : (Receive inbound call, Agent Hangs Up)
@pytest.mark.timeout(1200)
def testcase5():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 5: Agent hangs up")
        Report.write(row, 2, item)
        Report.write(row, 3, '5')
        Report.write(row, 4, 'Test case 5: Agent hangs up')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        ready_user()
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase5.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        play_sound_agent()
        cpu_usage("Usage when recording is happening")
        refresh_and_takedata(5)
        monitor_shot(5)
        cpu_usage("Usage while taking screenshot")
        end_call()  ##agent hang up
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('ready')
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "71-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "71-" + str(totalinbound)
        wb.save('Report/Report' + localtime+ '.xls')
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase5()

@pytest.mark.timeout(1200)
###Test case 6 : (Receive inbound call and place customer on hold 1X. Agent hangs up)
def testcase6():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 6: Place customer on hold 1X. Agent hangs up")
        Report.write(row, 2, item)
        Report.write(row, 3, '6')
        Report.write(row, 4, 'Place customer on hold 1X. Agent hangs up')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        ready_user()
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase6.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        play_sound_agent()
        cpu_usage("Usage when recording is happening")
        agent_hold()
        cpu_usage("Usage when customer is on hold")
        time.sleep(3)
        agent_retrive('h')
        cpu_usage("Usage when customer is on retrieved")
        refresh_and_takedata(6)
        monitor_shot(6)
        time.sleep(3)
        end_call()  ##agent hang up
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('ready')
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "72-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "72-" + str(totalinbound)
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase6()

###Test case 7 : (Receive inbound call and place customer on hold 2X. Agent hangs up)
@pytest.mark.timeout(1200)
def testcase7():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 7: Receive inbound call and place customer on hold 2X. Agent hangs up")
        Report.write(row, 2, item)
        Report.write(row, 3, '7')
        Report.write(row, 4, 'Receive inbound call and place customer on hold 2X. Agent hangs up')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        ready_user()
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase7.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        play_sound_agent()
        cpu_usage("Usage when recording is happening")
        agent_hold()
        cpu_usage("Usage when customer is on hold")
        time.sleep(3)
        agent_retrive('h')
        cpu_usage("Usage when customer is on retrieved")
        time.sleep(3)
        agent_hold()
        cpu_usage("Usage when customer is on hold 2")
        time.sleep(3)
        agent_retrive('h')
        refresh_and_takedata(7)
        monitor_shot(7)
        cpu_usage("Usage when customer is on retrieved 2")
        time.sleep(3)
        end_call()  ##agent hang up
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('ready')
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "73-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "73-" + str(totalinbound)
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase7()


###Test case 8 : (Receive inbound call and place customer on hold 3X. Agent hangs up)
@pytest.mark.timeout(1200)
def testcase8():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 8: Receive inbound call and place customer on hold 3X. Agent hangs up")
        Report.write(row, 2, item)
        Report.write(row, 3, '8')
        Report.write(row, 4, 'Receive inbound call and place customer on hold 3X. Agent hangs up')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        ready_user()
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase8.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        play_sound_agent()
        cpu_usage("Usage when recording is happening")
        agent_hold()
        cpu_usage("Usage when customer is on hold")
        time.sleep(3)
        agent_retrive('h')
        cpu_usage("Usage when customer is on retrieved")
        time.sleep(3)
        agent_hold()
        cpu_usage("Usage when customer is on hold 2")
        time.sleep(3)
        agent_retrive('h')
        cpu_usage("Usage when customer is on retrieved 2")
        time.sleep(3)
        agent_hold()
        cpu_usage("Usage when customer is on hold 3")
        time.sleep(3)
        agent_retrive('h')
        refresh_and_takedata(8)
        monitor_shot(8)
        cpu_usage("Usage when customer is on retrieved 3")
        end_call()  ##agent hang up
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('ready')
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "74-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "74-" + str(totalinbound)
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase8()

###Test case 37 : Outbound call Customer hangs up
@pytest.mark.timeout(1200)
def testcase37():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 37: Outbound call. Customer hangs up")
        Report.write(row, 2, item)
        Report.write(row, 3, '37')
        Report.write(row, 4, 'Outbound call. Customer hangs up')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        customer_answer()
        cpu_usage("Usage when Avaya makes a call")
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase37.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        play_sound_agent()
        customer_unmute()
        agent_mute()
        cpu_usage("Usage when recording is happening")
        refresh_and_takedata(37)
        monitor_shot(37)
        cpu_usage("Usage while taking screenshot")
        customer_hangsup()
        cpu_usage("Usage when Customer ends the call")
        send_mesgB('ready')
        send_mesgC('ready')
        #raise Exception('test')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "19-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "19-" + str(totalOutbound)
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase37()


###Test case 38 : (Receive Outbound call and place customer on hold 1X. Customer hangs up)
@pytest.mark.timeout(1200)
def testcase38():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 38: Receive Outbound call and place customer on hold 1X. Customer hangs up")
        Report.write(row, 2, item)
        Report.write(row, 3, '38')
        Report.write(row, 4, 'Receive Outbound call and place customer on hold 1X. Customer hangs up')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        ready_user()
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase38.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        play_sound_agent()
        cpu_usage("Usage when recording is happening")
        refresh_and_takedata(38)
        monitor_shot(38)
        cpu_usage("Usage when recording is happening")
        agent_hold()
        cpu_usage("Usage when customer goes on hold")
        time.sleep(5)
        agent_retrive('h')
        customer_unmute()
        agent_mute()
        cpu_usage("Usage when customer is retrieved")
        customer_hangsup()  ##customer hang up
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('ready')
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
        #raise Exception('test')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "20-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "20-" + str(totalOutbound)
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase38()

###Test case 39 : (Receive Outbound call and place customer on hold 2X. Customer hangs up)
@pytest.mark.timeout(1200)
def testcase39():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 39: Receive Outbound call and place customer on hold 2X. Customer hangs up")
        Report.write(row, 2, item)
        Report.write(row, 3, '39')
        Report.write(row, 4, 'Receive Outbound call and place customer on hold 2X. Customer hangs up')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase39.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        play_sound_agent()
        cpu_usage("Usage when recording is happening")
        customer_unmute()
        agent_mute()
        agent_hold()
        cpu_usage("Usage when customer is on hold")
        time.sleep(3)
        agent_retrive('h')
        time.sleep(3)
        cpu_usage("Usage when customer is retrieved")
        agent_hold()
        time.sleep(3)
        cpu_usage("Usage when customer is on hold 2")
        agent_retrive('h')
        refresh_and_takedata(39)
        monitor_shot(39)
        time.sleep(3)
        cpu_usage("Usage when customer is retrieved 2")
        customer_hangsup()  ##customer hang up
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('ready')
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        #exp_hang_up()
        #nice_driver.close()
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "21-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "21-" + str(totalOutbound)
        testcase0('exception')
        testcase39()

###Test case 40 : (Receive Outbound call and place customer on hold 3X. Customer hangs up)
@pytest.mark.timeout(1200)
def testcase40():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 40: Receive Outbound call and place customer on hold 3X. Customer hangs up")
        Report.write(row, 2, item)
        Report.write(row, 3, '40')
        Report.write(row, 4, 'Receive Outbound call and place customer on hold 3X. Customer hangs up')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase4.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        play_sound_agent()
        cpu_usage("Usage when recording is happening")
        agent_hold()
        cpu_usage("Usage when customer is on hold")
        time.sleep(3)
        agent_retrive('h')
        cpu_usage("Usage when customer is retrieved")
        time.sleep(3)
        agent_hold()
        cpu_usage("Usage when customer is hold 2")
        time.sleep(3)
        agent_retrive('h')
        refresh_and_takedata(40)
        monitor_shot(40)
        cpu_usage("Usage when customer is on retrieved 2")
        time.sleep(3)
        agent_hold()
        cpu_usage("Usage when customer is on hold 3")
        time.sleep(3)
        agent_retrive('h')
        cpu_usage("Usage when customer is retrieved 3")
        time.sleep(3)
        customer_unmute()
        agent_mute()
        customer_hangsup()  ##customer hang up
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('ready')
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "22-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "22-" + str(totalOutbound)
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase40()


###Test case 41 : (Receive Outbound call, Agent Hangs Up)
@pytest.mark.timeout(1200)
def testcase41():
    try:
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 41: Receive Outbound call, Agent hangs up")
        Report.write(row, 2, item)
        Report.write(row, 3, '41')
        Report.write(row, 4, 'Receive Outbound call, Agent hangs up')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        #ready_user()
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase41.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        play_sound_agent()
        customer_unmute()
        agent_mute()
        cpu_usage("Usage when recording is happening")
        refresh_and_takedata(41)
        monitor_shot(41)
        cpu_usage("Usage while taking screenshot")
        end_call()  ##agent hang up
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('ready')
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "23-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "23-" + str(totalOutbound)
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase41()


###Test case 42 : (Receive Outbound call and place customer on hold 1X. Agent hangs up)
@pytest.mark.timeout(1200)
def testcase42():
    try:
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 42: Receive Outbound call and place customer on hold 1X. Agent hangs up")
        Report.write(row, 2, item)
        Report.write(row, 3, '42')
        Report.write(row, 4, 'Receive Outbound call and place customer on hold 1X. Agent hangs up')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        #ready_user()
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase42.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        play_sound_agent()
        cpu_usage("Usage when recording is happening")
        agent_hold()
        cpu_usage("Usage when customer is on hold")
        time.sleep(3)
        agent_retrive('h')
        cpu_usage("Usage when customer is on retrieved")
        refresh_and_takedata(42)
        monitor_shot(42)
        time.sleep(3)
        end_call()  ##agent hang up
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('ready')
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "24-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "24-" + str(totalOutbound)
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase42()



###Test case 43 : (Receive Outbound call and place customer on hold 2X. Agent hangs up)
@pytest.mark.timeout(1200)
def testcase43():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 43: Receive Outbound call and place customer on hold 2X. Agent hangs up")
        Report.write(row, 2, item)
        Report.write(row, 3, '43')
        Report.write(row, 4, 'Receive Outbound call and place customer on hold 2X. Agent hangs up')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        #ready_user()
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase43.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        play_sound_agent()
        cpu_usage("Usage when recording is happening")
        agent_hold()
        cpu_usage("Usage when customer is on hold")
        time.sleep(3)
        agent_retrive('h')
        cpu_usage("Usage when customer is on retrieved")
        time.sleep(3)
        agent_hold()
        cpu_usage("Usage when customer is on hold 2")
        time.sleep(3)
        agent_retrive('h')
        refresh_and_takedata(43)
        monitor_shot(43)
        cpu_usage("Usage when customer is on retrieved 2")
        time.sleep(3)
        end_call()  ##agent hang up
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('ready')
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "25-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "25-" + str(totalOutbound)
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase43()


###Test case 44 : (Receive Outbound call and place customer on hold 3X. Agent hangs up)
@pytest.mark.timeout(1200)
def testcase44():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info(" ")
        logging.info(" ")
        logging.info("Test case 44: Receive Outbound call and place customer on hold 3X. Agent hangs up")
        Report.write(row, 2, item)
        Report.write(row, 3, '44')
        Report.write(row, 4, 'Receive Outbound call and place customer on hold 3X. Agent hangs up')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        #ready_user()
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase44.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        play_sound_agent()
        cpu_usage("Usage when recording is happening")
        agent_hold()
        cpu_usage("Usage when customer is on hold")
        time.sleep(3)
        agent_retrive('h')
        cpu_usage("Usage when customer is on retrieved")
        time.sleep(3)
        agent_hold()
        cpu_usage("Usage when customer is on hold 2")
        time.sleep(3)
        agent_retrive('h')
        cpu_usage("Usage when customer is on retrieved 2")
        time.sleep(3)
        agent_hold()
        cpu_usage("Usage when customer is on hold 3")
        time.sleep(3)
        agent_retrive('h')
        refresh_and_takedata(44)
        monitor_shot(44)
        cpu_usage("Usage when customer is on retrieved 3")
        end_call()  ##agent hang up
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('ready')
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "26-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "26-" + str(totalOutbound)
        #exp_hang_up()
       # nice_driver.close()
        testcase0('exception')
        testcase44()


###Test case 63 : Make Outbound call and transfer caller. Customer hangs up. Blind
@pytest.mark.timeout(1200)
def testcase63():
    try:
        time.sleep(2)
        send_mesgB('ready')
        send_mesgC('not ready')
        #ready_user()
        logging.info("Test case 63: Make Outbound call and transfer caller. Customer hangs up. Blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '63')
        Report.write(row, 4, 'Make Outbound call and transfer caller. Customer hangs up. Blind')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        #agent_mute()
        playsound('Testcase63.mp3')
        time.sleep(2)
        playsound('AgentAtoB.mp3')
        customer_mute()
        blind_transferencia2()
        send_mesgB('incoming call')
        recB = recv_mesgB()
        if recB == b'call received':
            customer_unmute()
        play_sound_customer()
        customer_mute()
        send_mesgB('agent B play sound')
        refresh_and_takedata(63)
        monitor_shot(63)
        cpu_usage("Usage while taking screenshot")
        recB = recv_mesgB()
        if recB == b'logout':
            customer_unmute()
        customer_hangsup()
        cpu_usage("Usage when Customer ends the call")
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "41-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "41-" + str(totalOutbound)
        #exp_hang_up()
       # nice_driver.close()
        testcase0('exception')
        testcase63()


###Test case 64 : Make Outbound call and transfer caller. Customer hangs up. Blind
@pytest.mark.timeout(1200)
def testcase64():
    try:
        time.sleep(2)
        send_mesgB('ready')
        send_mesgC('not ready')
        #ready_user()
        logging.info("Test case 64: Make Outbound call and transfer caller. Customer hangs up. Blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '64')
        Report.write(row, 4, 'Make Outbound call and transfer caller. Customer hangs up. Blind')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        #agent_mute()
        playsound('Testcase64.mp3')
        time.sleep(2)
        playsound('AgentAtoB.mp3')
        blind_transferencia2()
        send_mesgB('incoming call')
        recB = recv_mesgB()
        if recB == b'call received':
            play_sound_customer()
        customer_mute()
        send_mesgB('agent B play sound')
        refresh_and_takedata(64)
        monitor_shot(64)
        cpu_usage("Usage while taking screenshot")
        recB = recv_mesgB()
        if recB == b'logout':
            customer_unmute()
            customer_hangsup()
        cpu_usage("Usage when Customer ends the call")
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "42-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "42-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase64()


###Test case 65 : Make Outbound call and transfer caller. Customer hangs up. Warm
@pytest.mark.timeout(1200)
def testcase65():
    try:
        time.sleep(2)
        send_mesgB('ready')
        send_mesgC('not ready')
        #ready_user()
        logging.info("Test case 65: Make Outbound call and transfer caller. Customer hangs up. Warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '65')
        Report.write(row, 4, 'Make Outbound call and transfer caller. Customer hangs up. Warm')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        #agent_mute()
        playsound('Testcase65.mp3')
        time.sleep(2)
        playsound('AgentAtoB.mp3')
        agent_hold()
        warm_conference2()
        send_mesgB('incoming call')
        recB = recv_mesgB()
        if recB == b'call received':
            comp_transf()
            play_sound_customer()
        customer_mute()
        send_mesgB('agent B play sound')
        refresh_and_takedata(65)
        monitor_shot(65)
        cpu_usage("Usage while taking screenshot")
        recB = recv_mesgB()
        if recB == b'logout':
            customer_unmute()
        customer_hangsup()
        cpu_usage("Usage when Customer ends the call")
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "43-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "43-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase65()



###Test case 66 : Make Outbound call and transfer caller. Customer hangs up. Warm
@pytest.mark.timeout(1200)
def testcase66():
    try:
        time.sleep(2)
        send_mesgB('ready')
        send_mesgC('not ready')
        #ready_user()
        logging.info("Test case 66: Make Outbound call and transfer caller. Customer hangs up. Warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '66')
        Report.write(row, 4, 'Make Outbound call and transfer caller. Customer hangs up. Warm')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        #agent_mute()
        playsound('Testcase66.mp3')
        time.sleep(2)
        playsound('AgentAtoB.mp3')
        agent_hold()
        warm_conference2()
        send_mesgB('incoming call')
        recB = recv_mesgB()
        if recB == b'call received':
            comp_transf()
            play_sound_customer()
        customer_mute()
        send_mesgB('agent B play sound')
        refresh_and_takedata(66)
        monitor_shot(66)
        cpu_usage("Usage while taking screenshot")
        recB = recv_mesgB()
        if recB == b'logout':
            customer_unmute()
        customer_hangsup()
        cpu_usage("Usage when Customer ends the call")
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "44-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "44-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase66()


###Test case 67 : Make Outbound call and transfer caller. Customer hangs up. Retrieving
@pytest.mark.timeout(1200)
def testcase67():
    try:
        time.sleep(2)
        send_mesgB('ready')
        send_mesgC('not ready')
        #ready_user()
        logging.info("Test case 67: Make Outbound call and transfer caller. Customer hangs up. Retrieving")
        Report.write(row, 2, item)
        Report.write(row, 3, '67')
        Report.write(row, 4, 'Make Outbound call and transfer caller. Customer hangs up. Retrieving')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        #agent_mute()
        playsound('Testcase67.mp3')
        time.sleep(2)
        playsound('AgentAtoB.mp3')
        agent_hold()
        warm_conference2()
        send_mesgB('incoming call')
        recB = recv_mesgB()
        if recB == b'call received':
            agent_retrive('hold')
        agent_retrive('h')
        comp_transf()
        play_sound_customer()
        customer_mute()
        send_mesgB('agent B play sound')
        refresh_and_takedata(67)
        monitor_shot(67)
        cpu_usage("Usage while taking screenshot")
        recB = recv_mesgB()
        if recB == b'logout':
            customer_unmute()
        customer_hangsup()
        cpu_usage("Usage when Customer ends the call")
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "45-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "45-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase67()


###Test case 68 : Make Outbound call and transfer caller. Customer hangs up. Retrieving
@pytest.mark.timeout(1200)
def testcase68():
    try:
        time.sleep(2)
        send_mesgB('ready')
        send_mesgC('not ready')
        #ready_user()
        logging.info("Test case 68: Make Outbound call and transfer caller. Customer hangs up. Retrieving")
        Report.write(row, 2, item)
        Report.write(row, 3, '68')
        Report.write(row, 4, 'Make Outbound call and transfer caller. Customer hangs up. Retrieving')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        #agent_mute()
        playsound('Testcase68.mp3')
        time.sleep(2)
        playsound('AgentAtoB.mp3')
        agent_hold()
        warm_conference2()
        send_mesgB('incoming call')
        recB = recv_mesgB()
        if recB == b'call received':
             agent_retrive('hold')
        agent_retrive('h')
        comp_transf()
        play_sound_customer()
        customer_mute()
        send_mesgB('agent B play sound')
        refresh_and_takedata(68)
        monitor_shot(68)
        cpu_usage("Usage while taking screenshot")
        recB = recv_mesgB()
        if recB == b'logout':
            customer_unmute()
        customer_hangsup()
        cpu_usage("Usage when Customer ends the call")
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "46-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "46-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase68()


###Test case 69 : Make Outbound call and transfer caller. Agent hangs up. Blind
@pytest.mark.timeout(1200)
def testcase69():
    try:
        time.sleep(2)
        send_mesgB('ready')
        send_mesgC('not ready')
        #ready_user()
        logging.info("Test case 69: Make Outbound call and transfer caller. Agent hangs up. Blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '69')
        Report.write(row, 4, 'Make Outbound call and transfer caller. Agent hangs up. Blind')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        #agent_mute()
        playsound('Testcase69.mp3')
        time.sleep(2)
        playsound('AgentAtoB.mp3')
        blind_transferencia2()
        send_mesgB('incoming call')
        recB = recv_mesgB()
        if recB == b'call received':
            play_sound_customer()
        customer_mute()
        send_mesgB('agent B play sound')
        refresh_and_takedata(69)
        monitor_shot(69)
        cpu_usage("Usage while taking screenshot")
        recB = recv_mesgB()
        if recB == b'logout':
            send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "47-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "47-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase69()


###Test case 70 : Make Outbound call and transfer caller. Agent hangs up. Blind
@pytest.mark.timeout(1200)
def testcase70():
    try:
        time.sleep(2)
        send_mesgB('ready')
        send_mesgC('not ready')
        #ready_user()
        logging.info("Test case 70: Make Outbound call and transfer caller. Agent hangs up. Blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '70')
        Report.write(row, 4, 'Make Outbound call and transfer caller. Agent hangs up. Blind')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        #agent_mute()
        playsound('Testcase70.mp3')
        time.sleep(2)
        playsound('AgentAtoB.mp3')
        blind_transferencia2()
        send_mesgB('incoming call')
        recB = recv_mesgB()
        if recB == b'call received':
            play_sound_customer()
        customer_mute()
        send_mesgB('agent B play sound')
        refresh_and_takedata(70)
        monitor_shot(70)
        cpu_usage("Usage while taking screenshot")
        recB = recv_mesgB()
        if recB == b'logout':
            send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "48-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "48-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase70()


###Test case 71 : Make Outbound call and transfer caller. Agent hangs up. Warm
def testcase71():
    try:
        time.sleep(2)
        send_mesgB('ready')
        send_mesgC('not ready')
        #ready_user()
        logging.info("Test case 71: Make Outbound call and transfer caller. Agent hangs up. Warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '71')
        Report.write(row, 4, 'Make Outbound call and transfer caller. Agent hangs up. Warm')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        #agent_mute()
        playsound('Testcase71.mp3')
        time.sleep(2)
        playsound('AgentAtoB.mp3')
        agent_hold()
        warm_conference2()
        send_mesgB('incoming call')
        recB = recv_mesgB()
        if recB == b'call received':
            comp_transf()
            play_sound_customer()
        customer_mute()
        send_mesgB('agent B play sound')
        refresh_and_takedata(71)
        monitor_shot(71)
        cpu_usage("Usage while taking screenshot")
        recB = recv_mesgB()
        if recB == b'logout':
            send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "49-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "49-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase71()



###Test case 72 : Make Outbound call and transfer caller. Agent hangs up. Warm
def testcase72():
    try:
        time.sleep(2)
        send_mesgB('ready')
        send_mesgC('not ready')
        #ready_user()
        logging.info("Test case 72: Make Outbound call and transfer caller. Agent hangs up. Warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '72')
        Report.write(row, 4, 'Make Outbound call and transfer caller. Agent hangs up. Warm')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        #agent_mute()
        playsound('Testcase72.mp3')
        time.sleep(1)
        playsound('AgentAtoB.mp3')
        agent_hold()
        warm_conference2()
        send_mesgB('incoming call')
        recB = recv_mesgB()
        if recB == b'call received':
            comp_transf()
            play_sound_customer()
        customer_mute()
        send_mesgB('agent B play sound')
        refresh_and_takedata(72)
        monitor_shot(72)
        cpu_usage("Usage while taking screenshot")
        recB = recv_mesgB()
        if recB == b'logout':
            send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "50-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "50-" + str(totalOutbound)
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase72()


###Test case 73 : Make Outbound call and transfer caller. Agent hangs up. Retrieving
def testcase73():
    try:
        time.sleep(2)
        send_mesgB('ready')
        send_mesgC('not ready')
        #ready_user()
        logging.info("Test case73: Make Outbound call and transfer caller. Agent hangs up. Retrieving")
        Report.write(row, 2, item)
        Report.write(row, 3, '73')
        Report.write(row, 4, 'Make Outbound call and transfer caller. Agent hangs up. Retrieving')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        #agent_mute()
        playsound('Testcase73.mp3')
        time.sleep(1)
        playsound('AgentAtoB.mp3')
        agent_hold()
        warm_conference2()
        send_mesgB('incoming call')
        recB = recv_mesgB()
        if recB == b'call received':
            agent_retrive('hold')
        agent_retrive('h')
        comp_transf()
        play_sound_customer()
        customer_mute()
        send_mesgB('agent B play sound')
        refresh_and_takedata(73)
        monitor_shot(73)
        cpu_usage("Usage while taking screenshot")
        recB = recv_mesgB()
        if recB == b'logout':
            send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        # exp_hang_up()
        #nice_driver.close()
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "51-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "51-" + str(totalOutbound)
        testcase0('exception')
        testcase73()


###Test case 74 : Make Outbound call and transfer caller. Agent hangs up. Retrieving
def testcase74():
    try:
        time.sleep(2)
        send_mesgB('ready')
        send_mesgC('not ready')
        #ready_user()
        logging.info("Test case 74: Make Outbound call and transfer caller. Agent hangs up. Retrieving")
        Report.write(row, 2, item)
        Report.write(row, 3, '74')
        Report.write(row, 4, 'Make Outbound call and transfer caller. Agent hangs up. Retrieving')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        #agent_mute()
        playsound('Testcase68.mp3')
        time.sleep(1)
        playsound('AgentAtoB.mp3')
        agent_hold()
        warm_conference2()
        send_mesgB('incoming call')
        recB = recv_mesgB()
        if recB == b'call received':
            agent_retrive('hold')
        agent_retrive('h')
        comp_transf()
        play_sound_customer()
        customer_mute()
        send_mesgB('agent B play sound')
        refresh_and_takedata(74)
        monitor_shot(74)
        cpu_usage("Usage while taking screenshot")
        recB = recv_mesgB()
        if recB == b'logout':
            send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "52-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "52-" + str(totalOutbound)
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase74()


###Test case 25 : Make Inbound call and transfer caller. Customer hangs up. Blind
def testcase25():
    try:
        time.sleep(7)
        send_mesgB('not ready')
        send_mesgC('not ready')
        ready_user()
        logging.info("Test case 25: Make Inbound call and transfer caller. Customer hangs up. Blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '25')
        Report.write(row, 4, 'Make Inbound call and transfer caller. Customer hangs up. Blind')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        #agent_mute()
        send_mesgB('ready')
        playsound('Testcase25.mp3')
        time.sleep(1)
        playsound('AgentAtoB.mp3')
        blind_transferencia2()
        send_mesgB('incoming call')
        recB = recv_mesgB()
        if recB == b'call received':
            play_sound_customer()
        customer_mute()
        send_mesgB('agent B play sound')
        refresh_and_takedata(25)
        monitor_shot(25)
        cpu_usage("Usage while taking screenshot")
        recB = recv_mesgB()
        if recB == b'logout':
            customer_unmute()
            customer_hangsup()
        cpu_usage("Usage when Customer ends the call")
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        # exp_hang_up()
        #nice_driver.close()
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "87-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "87-" + str(totalinbound)
        testcase0('exception')
        testcase25()


###Test case 26 : Make Inbound call and transfer caller. Customer hangs up. Blind
def testcase26():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        ready_user()
        logging.info("Test case 26: Make Inbound call and transfer caller. Customer hangs up. Blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '26')
        Report.write(row, 4, 'Make Inbound call and transfer caller. Customer hangs up. Blind')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        #agent_mute()
        send_mesgB('ready')
        playsound('Testcase26.mp3')
        time.sleep(1)
        playsound('AgentAtoB.mp3')
        blind_transferencia2()
        send_mesgB('incoming call')
        recB = recv_mesgB()
        if recB == b'call received':
            play_sound_customer()
        customer_mute()
        send_mesgB('agent B play sound')
        refresh_and_takedata(26)
        monitor_shot(26)
        cpu_usage("Usage while taking screenshot")
        recB = recv_mesgB()
        if recB == b'logout':
            customer_unmute()
            customer_hangsup()
        cpu_usage("Usage when Customer ends the call")
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "88-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "88-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase26()


###Test case 27 : Make Inbound call and transfer caller. Customer hangs up. Warm
def testcase27():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        ready_user()
        logging.info("Test case 27: Make Inbound call and transfer caller. Customer hangs up. Warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '27')
        Report.write(row, 4, 'Make Inbound call and transfer caller. Customer hangs up. Warm')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        #agent_mute()
        send_mesgB('ready')
        playsound('Testcase27.mp3')
        time.sleep(1)
        playsound('AgentAtoB.mp3')
        agent_hold()
        warm_conference2()
        send_mesgB('incoming call')
        recB = recv_mesgB()
        if recB == b'call received':
            comp_transf()
            play_sound_customer()
        customer_mute()
        send_mesgB('agent B play sound')
        refresh_and_takedata(27)
        monitor_shot(27)
        cpu_usage("Usage while taking screenshot")
        recB = recv_mesgB()
        if recB == b'logout':
            customer_unmute()
            customer_hangsup()
        cpu_usage("Usage when Customer ends the call")
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "89-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "89-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase27()



###Test case 28 : Make Inbound call and transfer caller. Customer hangs up. Warm
def testcase28():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        ready_user()
        logging.info("Test case 28: Make Inbound call and transfer caller. Customer hangs up. Warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '28')
        Report.write(row, 4, 'Make Inbound call and transfer caller. Customer hangs up. Warm')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        #agent_mute()
        send_mesgB('ready')
        playsound('Testcase28.mp3')
        time.sleep(1)
        playsound('AgentAtoB.mp3')
        agent_hold()
        warm_conference2()
        send_mesgB('incoming call')
        recB = recv_mesgB()
        if recB == b'call received':
            comp_transf()
            play_sound_customer()
        customer_mute()
        send_mesgB('agent B play sound')
        refresh_and_takedata(28)
        monitor_shot(28)
        cpu_usage("Usage while taking screenshot")
        recB = recv_mesgB()
        if recB == b'logout':
            customer_unmute()
            customer_hangsup()
        cpu_usage("Usage when Customer ends the call")
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "90-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "90-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase28()


###Test case 29 : Make Inbound call and transfer caller. Customer hangs up. Retrieving
def testcase29():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        ready_user()
        logging.info("Test case 29: Make Inbound call and transfer caller. Customer hangs up. Retrieving")
        Report.write(row, 2, item)
        Report.write(row, 3, '29')
        Report.write(row, 4, 'Make Inbound call and transfer caller. Customer hangs up. Retrieving')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        #agent_mute()
        send_mesgB('ready')
        playsound('Testcase29.mp3')
        time.sleep(1)
        playsound('AgentAtoB.mp3')
        agent_hold()
        warm_conference2()
        send_mesgB('incoming call')
        recB = recv_mesgB()
        if recB == b'call received':
            agent_retrive('hold')
        agent_retrive('h')
        comp_transf()
        play_sound_customer()
        customer_mute()
        send_mesgB('agent B play sound')
        refresh_and_takedata(29)
        monitor_shot(29)
        cpu_usage("Usage while taking screenshot")
        recB = recv_mesgB()
        if recB == b'logout':
            customer_unmute()
            customer_hangsup()
        cpu_usage("Usage when Customer ends the call")
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "91-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "91-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase29()


###Test case 30 : Make Inbound call and transfer caller. Customer hangs up. Retrieving
def testcase30():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        ready_user()
        logging.info("Test case 30: Make Inbound call and transfer caller. Customer hangs up. Retrieving")
        Report.write(row, 2, item)
        Report.write(row, 3, '30')
        Report.write(row, 4, 'Make Inbound call and transfer caller. Customer hangs up. Retrieving')
        Report.write(row, 5, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        #agent_mute()
        send_mesgB('ready')
        playsound('Testcase30.mp3')
        time.sleep(1)
        playsound('AgentAtoB.mp3')
        agent_hold()
        warm_conference2()
        send_mesgB('incoming call')
        recB = recv_mesgB()
        if recB == b'call received':
            agent_retrive('hold')
        agent_retrive('h')
        comp_transf()
        play_sound_customer()
        customer_mute()
        send_mesgB('agent B play sound')
        refresh_and_takedata(30)
        monitor_shot(30)
        cpu_usage("Usage while taking screenshot")
        recB = recv_mesgB()
        if recB == b'logout':
            customer_unmute()
            customer_hangsup()
        cpu_usage("Usage when Customer ends the call")
        send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "92-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "92-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase30()


###Test case 31 : Make Inbound call and transfer caller. Agent hangs up. Blind
def testcase31():
    try:
        time.sleep(2)
        print(22)
        send_mesgB('not ready')
        send_mesgC('not ready')
        ready_user()
        logging.info("Test case 31: Make Inbound call and transfer caller. Agent hangs up. Blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '31')
        Report.write(row, 4, 'Make Inbound call and transfer caller. Agent hangs up. Blind')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        #agent_mute()
        send_mesgB('ready')
        playsound('Testcase31.mp3')
        time.sleep(1)
        playsound('AgentAtoB.mp3')
        blind_transferencia2()
        send_mesgB('incoming call')
        recB = recv_mesgB()
        if recB == b'call received':
            play_sound_customer()
        customer_mute()
        send_mesgB('agent B play sound')
        refresh_and_takedata(31)
        monitor_shot(31)
        cpu_usage("Usage while taking screenshot")
        recB = recv_mesgB()
        if recB == b'logout':
            send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
        #raise Exception('test')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "93-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "93-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase31()


###Test case 32 : Make Inbound call and transfer caller. Agent hangs up. Blind
def testcase32():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        ready_user()
        logging.info("Test case 32: Make Inbound call and transfer caller. Agent hangs up. Blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '32')
        Report.write(row, 4, 'Make Inbound call and transfer caller. Agent hangs up. Blind')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        #agent_mute()
        send_mesgB('ready')
        playsound('Testcase32.mp3')
        time.sleep(1)
        playsound('AgentAtoB.mp3')
        blind_transferencia2()
        send_mesgB('incoming call')
        recB = recv_mesgB()
        if recB == b'call received':
            play_sound_customer()
        customer_mute()
        send_mesgB('agent B play sound')
        refresh_and_takedata(32)
        monitor_shot(32)
        cpu_usage("Usage while taking screenshot")
        recB = recv_mesgB()
        if recB == b'logout':
            send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "94-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "94-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase32()


###Test case 33 : Make Inbound call and transfer caller. Agent hangs up. Warm
def testcase33():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        ready_user()
        logging.info("Test case 33: Make Inbound call and transfer caller. Agent hangs up. Warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '33')
        Report.write(row, 4, 'Make Inbound call and transfer caller. Agent hangs up. Warm')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        #agent_mute()
        send_mesgB('ready')
        playsound('Testcase33.mp3')
        time.sleep(1)
        playsound('AgentAtoB.mp3')
        agent_hold()
        warm_conference2()
        send_mesgB('incoming call')
        recB = recv_mesgB()
        if recB == b'call received':
            comp_transf()
            play_sound_customer()
        customer_mute()
        send_mesgB('agent B play sound')
        refresh_and_takedata(33)
        monitor_shot(33)
        cpu_usage("Usage while taking screenshot")
        recB = recv_mesgB()
        if recB == b'logout':
            send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "95-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "95-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase33()



###Test case 34 : Make Inbound call and transfer caller. Agent hangs up. Warm
def testcase34():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        ready_user()
        logging.info("Test case 34: Make Inbound call and transfer caller. Agent hangs up. Warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '34')
        Report.write(row, 4, 'Make Inbound call and transfer caller. Agent hangs up. Warm')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        #agent_mute()
        send_mesgB('ready')
        playsound('Testcase34.mp3')
        time.sleep(1)
        playsound('AgentAtoB.mp3')
        agent_hold()
        warm_conference2()
        send_mesgB('incoming call')
        recB = recv_mesgB()
        if recB == b'call received':
            comp_transf()
            play_sound_customer()
        customer_mute()
        send_mesgB('agent B play sound')
        refresh_and_takedata(34)
        monitor_shot(34)
        cpu_usage("Usage while taking screenshot")
        recB = recv_mesgB()
        if recB == b'logout':
            send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "96-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "96-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase34()


###Test case 35 : Make Inbound call and transfer caller. Agent hangs up. Retrieving
def testcase35():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        ready_user()
        logging.info("Test case35: Make Inbound call and transfer caller. Agent hangs up. Retrieving")
        Report.write(row, 2, item)
        Report.write(row, 3, '35')
        Report.write(row, 4, 'Make Inbound call and transfer caller. Agent hangs up. Retrieving')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        #agent_mute()
        send_mesgB('ready')
        playsound('Testcase35.mp3')
        time.sleep(1)
        playsound('AgentAtoB.mp3')
        agent_hold()
        warm_conference2()
        send_mesgB('incoming call')
        recB = recv_mesgB()
        if recB == b'call received':
            agent_retrive('hold')
        agent_retrive('h')
        comp_transf()
        play_sound_customer()
        customer_mute()
        send_mesgB('agent B play sound')
        refresh_and_takedata(35)
        monitor_shot(35)
        cpu_usage("Usage while taking screenshot")
        recB = recv_mesgB()
        if recB == b'logout':
            send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "97-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "97-" + str(totalinbound)
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase35()


###Test case 36 : Make Inbound call and transfer caller. Agent hangs up. Retrieving
def testcase36():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        ready_user()
        logging.info("Test case 36: Make Inbound call and transfer caller. Agent hangs up. Retrieving")
        Report.write(row, 2, item)
        Report.write(row, 3, '36')
        Report.write(row, 4, 'Make Inbound call and transfer caller. Agent hangs up. Retrieving')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        #agent_mute()
        send_mesgB('ready')
        playsound('Testcase36.mp3')
        time.sleep(1)
        playsound('AgentAtoB.mp3')
        agent_hold()
        warm_conference2()
        send_mesgB('incoming call')
        recB = recv_mesgB()
        if recB == b'call received':
            agent_retrive('hold')
        agent_retrive('h')
        comp_transf()
        play_sound_customer()
        customer_mute()
        send_mesgB('agent B play sound')
        refresh_and_takedata(36)
        monitor_shot(36)
        cpu_usage("Usage while taking screenshot")
        recB = recv_mesgB()
        if recB == b'logout':
            send_mesgC('ready')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "98-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "98-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase36()



###Test case 47 : Outbound call and conference 4th party. Hang up order customer , Agent A, Agent B, blind
def testcase47():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 47: Outbound call and conference 4th party. Hang up order customer , Agent A, Agent B")
        Report.write(row, 2, item)
        Report.write(row, 3, '47')
        Report.write(row, 4, 'Outbound call and conference 4th party. Hang up order customer , Agent A, Agent B')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase47.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_mute()
        refresh_and_takedata(47)
        monitor_shot(47.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_unmute()
            playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(47)
        monitor_shot(47.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "29-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "29-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase47()


###Test case 48 : Outbound call and conference 4th party. Hang up order customer , Agent B, Agent A, blind
def testcase48():
    try:
        time.sleep(4)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 48: Outbound call and conference 4th party. Hang up order customer , Agent B, Agent A")
        Report.write(row, 2, item)
        Report.write(row, 3, '48')
        Report.write(row, 4, 'Outbound call and conference 4th party. Hang up order customer , Agent B, Agent A')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase48.mp3')
        agent_unmute()
        play_sound_customer()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_mute()
        refresh_and_takedata(48)
        monitor_shot(48.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_unmute()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(48)
        monitor_shot(48.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'hangup':
            agent_unmute()
            playsound('Agent hangup.mp3')
            end_call()
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "30-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "30-" + str(totalOutbound)
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase48()


###Test case 49 : Outbound call and conference 4th party. Hang up order customer , Agent B, Agent C, warm
def testcase49():
    try:
        time.sleep(4)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 49: Outbound call and conference 4th party. Hang up order customer , Agent B, Agent C")
        Report.write(row, 2, item)
        Report.write(row, 3, '49')
        Report.write(row, 4, 'Outbound call and conference 4th party. Hang up order customer , Agent B, Agent C')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase49.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             agent_hold()
             warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(49)
        monitor_shot(49.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        agent_hold()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(49)
        monitor_shot(49.2)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'hangup':
            send_mesgC('logout')
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "31-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "31-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase49()


###Test case 50 : Outbound call and conference 4th party. Hang up order customer , Agent C, Agent B, warm
def testcase50():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 50: Outbound call and conference 4th party. Hang up order customer , Agent C, Agent B")
        Report.write(row, 2, item)
        Report.write(row, 3, '50')
        Report.write(row, 4, 'Outbound call and conference 4th party. Hang up order customer , Agent C, Agent B')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase50.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
            time.sleep(1)
            agent_hold()
            warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(50)
        monitor_shot(50.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        agent_hold()
        agent_unmute()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(50)
        monitor_shot(50.2)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
        customer_hangsup()
        send_mesgC('logout')
        recC = recv_mesgC()
        if recC == b'hangup B':
            send_mesgB('logout')
        cpu_usage("Usage when Agent ends the call")
        time.sleep(5)
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "32-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "32-" + str(totalOutbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase50()


###Test case 51 : Outbound call and conference 4th party. Hang up order customer , Agent C, Agent A, retriving
def testcase51():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 51: Outbound call and conference 4th party. Hang up order customer , Agent C, Agent A")
        Report.write(row, 2, item)
        Report.write(row, 3, '51')
        Report.write(row, 4, 'Outbound call and conference 4th party. Hang up order customer , Agent C, Agent A')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase51.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
            time.sleep(3)
            agent_hold()
            warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(51)
        monitor_shot(51.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(2)
        agent_hold()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(51)
        monitor_shot(51.2)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
        customer_hangsup()
        send_mesgC('logout')
        recC = recv_mesgC()
        if recC == b'hangup B':
            agent_unmute()
            end_call()
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "33-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "33-" + str(totalOutbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase51()


###Test case 52 : Outbound call and conference 4th party. Hang up order customer , Agent A, Agent C, blind
def testcase52():
    try:
        time.sleep(5)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 52: Outbound call and conference 4th party. Hang up order customer , Agent A, Agent C")
        Report.write(row, 2, item)
        Report.write(row, 3, '52')
        Report.write(row, 4, 'Outbound call and conference 4th party. Hang up order customer , Agent A, Agent C')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase52.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_mute()
        refresh_and_takedata(52)
        monitor_shot(52.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_unmute()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(52)
        monitor_shot(52.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgC('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "34-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "34-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase52()



###Test case 57 : Outbound call and conference 4th party. Hang up order Agent A, Agent B, Agent C, blind
def testcase57():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 57: Outbound call and conference 4th party. Hang up order Agent A, Agent B, Agent C, blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '57')
        Report.write(row, 4, 'Outbound call and conference 4th party. Hang up order Agent A, Agent B, Agent C, blind')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase57.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_mute()
        refresh_and_takedata(57)
        monitor_shot(57.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_unmute()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(57)
        monitor_shot(57.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
            playsound('Agent hangup.mp3')
            leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'C logout':
            send_mesgC('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "35-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "35-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase57()


###Test case 58 : Outbound call and conference 4th party. Hang up order Agent A, Agent C, Agent B, blind
def testcase58():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 58: Outbound call and conference 4th party. Hang up order Agent A, Agent C, Agent B, blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '58')
        Report.write(row, 4, 'Outbound call and conference 4th party. Hang up order Agent A, Agent C, Agent B, blind')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase58.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        time.sleep(3)
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_mute()
        refresh_and_takedata(58)
        monitor_shot(58.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_unmute()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(5)
        send_mesgC('agent C play sound')
        refresh_and_takedata(58)
        monitor_shot(58.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
            playsound('Agent hangup.mp3')
            leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgC('logout')
        recC = recv_mesgC()
        if recC == b'logout':
             send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "36-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "36-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase58()


###Test case 59 : Outbound call and conference 4th party. Hang up order Agent B, Agent A, Agent C, warm
def testcase59():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 59: Outbound call and conference 4th party. Hang up order Agent B, Agent A, Agent C, warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '59')
        Report.write(row, 4, 'Outbound call and conference 4th party. Hang up order Agent B, Agent A, Agent C, warm')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase59.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        print(recB)
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             agent_hold()
             warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(59)
        monitor_shot(59.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        print(recC)
        if recC == b'c ready':
            agent_merge()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(59)
        monitor_shot(59.2)
        recC = recv_mesgC()
        print(recC)
        if recC == b'hangup':
            send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'hangup':
            agent_unmute()
            playsound('Agent hangup.mp3')
            leave_conf()
            send_mesgC('logout')
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "37-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "37-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase59()


###Test case 60 : Outbound call and conference 4th party. Hang up order Agent B, Agent C, Agent A, warm
def testcase60():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 60: Outbound call and conference 4th party. Hang up order Agent B, Agent C, Agent A, warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '60')
        Report.write(row, 4, 'Outbound call and conference 4th party. Hang up order Agent B, Agent C, Agent A, warm')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase60.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
            time.sleep(1)
            agent_hold()
            warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(60)
        monitor_shot(60.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        agent_hold()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
            playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(60)
        monitor_shot(60.2)
        recC = recv_mesgC()
        if recC == b'hangup':
            send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'logout':
            send_mesgC('logout')
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
            playsound('Agent hangup.mp3')
            end_call()
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "38-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "38-" + str(totalOutbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase60()


###Test case 61 : Outbound call and conference 4th party. Hang up order Agent C, Agent A, Agent B, retriving
def testcase61():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 61: Outbound call and conference 4th party. Hang up order Agent C, Agent A, Agent B, retriving")
        Report.write(row, 2, item)
        Report.write(row, 3, '61')
        Report.write(row, 4, 'Outbound call and conference 4th party. Hang up order Agent C, Agent A, Agent B, retriving')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase61.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
            time.sleep(1)
            agent_hold()
            warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(61)
        monitor_shot(61.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        agent_hold()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
            playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(61)
        monitor_shot(61.2)
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        send_mesgB('logout')
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "39-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "39-" + str(totalOutbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase61()


###Test case 62 : Outbound call and conference 4th party. Hang up order Agent C , Agent B, Agent A, retriving
def testcase62():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 62: Outbound call and conference 4th party. Hang up order Agent C , Agent B, Agent A, retriving")
        Report.write(row, 2, item)
        Report.write(row, 3, '62')
        Report.write(row, 4, 'Outbound call and conference 4th party. Hang up order Agent C, Agent A, Agent B, retriving')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase62.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_mute()
        refresh_and_takedata(62)
        monitor_shot(62.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_unmute()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(62)
        monitor_shot(62.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "40-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "40-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase62()




###Test case 11 : Inbound call and conference 4th party. Hang up order customer , Agent A, Agent B, blind
def testcase11():
    try:
        time.sleep(7)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 11: Inbound call and conference 4th party. Hang up order customer , Agent A, Agent B")
        Report.write(row, 2, item)
        Report.write(row, 3, '11')
        Report.write(row, 4, 'Inbound call and conference 4th party. Hang up order customer , Agent A, Agent B, blind')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        time.sleep(2)
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase11.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_mute()
        refresh_and_takedata(11)
        monitor_shot(11.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_unmute()
        if BP != True:
            agent_merge()
            merge_all()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(11)
        monitor_shot(11.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
        customer_hangsup()
        agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "75-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "75-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase11()


###Test case 12 : Inbound call and conference 4th party. Hang up order customer , Agent B, Agent A, blind
def testcase12():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 12: Inbound call and conference 4th party. Hang up order customer , Agent B, Agent A")
        Report.write(row, 2, item)
        Report.write(row, 3, '12')
        Report.write(row, 4, 'Inbound call and conference 4th party. Hang up order customer , Agent B, Agent A, blind')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase12.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_mute()
        refresh_and_takedata(12)
        monitor_shot(12.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_unmute()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(12)
        monitor_shot(12.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'hangup':
            agent_unmute()
            playsound('Agent hangup.mp3')
            end_call()
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "76-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "76-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase12()


###Test case 13 : Inbound call and conference 4th party. Hang up order customer , Agent B, Agent C, warm
def testcase13():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 13: Inbound call and conference 4th party. Hang up order customer , Agent B, Agent C")
        Report.write(row, 2, item)
        Report.write(row, 3, '13')
        Report.write(row, 4, 'Inbound call and conference 4th party. Hang up order customer , Agent B, Agent C')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase13.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             agent_hold()
             time.sleep(1)
             warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(13)
        monitor_shot(13.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(13)
        monitor_shot(13.2)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'hangup':
            send_mesgC('logout')
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "77-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "77-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase13()


###Test case 14 : Inbound call and conference 4th party. Hang up order customer , Agent C, Agent B, warm
def testcase14():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 14: Inbound call and conference 4th party. Hang up order customer , Agent C, Agent B, warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '14')
        Report.write(row, 4, 'Test case 14: Inbound call and conference 4th party. Hang up order customer , Agent C, Agent B, warm')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase14.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        agent_hold()
        time.sleep(1)
        warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(14)
        monitor_shot(14.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        agent_hold()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(14)
        monitor_shot(14.2)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
        customer_hangsup()
        send_mesgC('logout')
        recC = recv_mesgC()
        if recC == b'hangup B':
            send_mesgB('logout')
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "78-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "78-" + str(totalinbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase14()


###Test case 15 : Inbound call and conference 4th party. Hang up order customer , Agent C, Agent A, retriving
def testcase15():
    try:
        time.sleep(5)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 15: Inbound call and conference 4th party. Hang up order customer , Agent C, Agent A")
        Report.write(row, 2, item)
        Report.write(row, 3, '15')
        Report.write(row, 4, 'Inbound call and conference 4th party. Hang up order customer , Agent C, Agent A')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase15.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        agent_hold()
        time.sleep(1)
        warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(15)
        monitor_shot(15.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        agent_hold()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(15)
        monitor_shot(15.2)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
        customer_hangsup()
        send_mesgC('logout')
        recC = recv_mesgC()
        if recC == b'hangup B':
            agent_unmute()
            end_call()
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "79-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "79-" + str(totalinbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase15()


###Test case 16 : Inbound call and conference 4th party. Hang up order customer , Agent A, Agent C, blind
def testcase16():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 16: Inbound call and conference 4th party. Hang up order customer , Agent A, Agent C")
        Report.write(row, 2, item)
        Report.write(row, 3, '16')
        Report.write(row, 4, 'Inbound call and conference 4th party. Hang up order customer , Agent A, Agent C')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase16.mp3')
        play_sound_customer()
        agent_unmute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_mute()
        refresh_and_takedata(16)
        monitor_shot(16.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_unmute()
        playsound('4thpartconf.mp3')
        agent_mute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(16)
        monitor_shot(16.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
        customer_hangsup()
        agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgC('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "80-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "80-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase16()


###Test case 19 : Inbound call and conference 4th party. Hang up order Agent A, Agent B, Agent C, blind
def testcase19():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 19: Inbound call and conference 4th party. Hang up order Agent A, Agent B, Agent C, blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '19')
        Report.write(row, 4, 'Inbound call and conference 4th party. Hang up order Agent A, Agent B, Agent C, blind')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase19.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_mute()
        refresh_and_takedata(19)
        monitor_shot(19.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_unmute()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(19)
        monitor_shot(19.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
            playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'C logout':
            send_mesgC('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "81-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "81-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase19()


###Test case 20 : Inbound call and conference 4th party. Hang up order Agent A, Agent C, Agent B, blind
def testcase20():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 20: Inbound call and conference 4th party. Hang up order Agent A, Agent C, Agent B, blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '20')
        Report.write(row, 4, 'Inbound call and conference 4th party. Hang up order Agent A, Agent C, Agent B, blind')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase20.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_mute()
        refresh_and_takedata(20)
        monitor_shot(20.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_unmute()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(20)
        monitor_shot(20.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
            playsound('Agent hangup.mp3')
            leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgC('logout')
        recC = recv_mesgC()
        if recC == b'logout':
             send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "82-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "82-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase20()


###Test case 21 : Inbound call and conference 4th party. Hang up order Agent B, Agent A, Agent C, warm
def testcase21():
    try:
        time.sleep(7)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 21: Inbound call and conference 4th party. Hang up order Agent B, Agent A, Agent C, warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '21')
        Report.write(row, 4, 'Inbound call and conference 4th party. Hang up order Agent B, Agent A, Agent C, warm')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase21.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
        time.sleep(1)
        agent_hold()
        warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(21)
        monitor_shot(21.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        agent_hold()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(21)
        monitor_shot(21.2)
        recC = recv_mesgC()
        if recC == b'hangup':
            send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'hangup':
            agent_unmute()
            playsound('Agent hangup.mp3')
            leave_conf()
        send_mesgC('logout')
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "83-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "83-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase21()


###Test case 22 : Inbound call and conference 4th party. Hang up order Agent B, Agent C, Agent A, warm
def testcase22():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 22: Inbound call and conference 4th party. Hang up order Agent B, Agent C, Agent A, warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '22')
        Report.write(row, 4, 'Inbound call and conference 4th party. Hang up order Agent B, Agent C, Agent A, warm')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase22.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        agent_hold()
        warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(22)
        monitor_shot(22.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        agent_hold()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(22)
        monitor_shot(22.2)
        recC = recv_mesgC()
        if recC == b'hangup':
            send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'logout':
            send_mesgC('logout')
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
        playsound('Agent hangup.mp3')
        end_call()
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "84-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "84-" + str(totalinbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase22()


###Test case 23 : Inbound call and conference 4th party. Hang up order Agent C, Agent A, Agent B, retriving
def testcase23():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 23: Inbound call and conference 4th party. Hang up order Agent C, Agent A, Agent B, retriving")
        Report.write(row, 2, item)
        Report.write(row, 3, '23')
        Report.write(row, 4, 'Inbound call and conference 4th party. Hang up order Agent C, Agent A, Agent B, retriving')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase23.mp3')
        play_sound_customer()
        agent_unmute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        agent_hold()
        time.sleep(1)
        warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_merge()
        refresh_and_takedata(23)
        monitor_shot(23.1)
        cpu_usage("Usage when AgentB receives incoming call")
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        agent_hold()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
            playsound('4thpartconf.mp3')
        agent_mute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(23)
        monitor_shot(23.2)
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        send_mesgB('logout')
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "85-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "85-" + str(totalinbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase23()


###Test case 24 : Inbound call and conference 4th party. Hang up order Agent C , Agent B, Agent A, retrieving
def testcase24():
    try:
        time.sleep(4)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 24: Inbound call and conference 4th party. Hang up order Agent C , Agent B, Agent A, retrieving")
        Report.write(row, 2, item)
        Report.write(row, 3, '24')
        Report.write(row, 4,'Inbound call and conference 4th party. Hang up order Agent C , Agent B, Agent A, retriving')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase24.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        agent_hold()
        time.sleep(1)
        warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(24)
        monitor_shot(24.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        agent_hold()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
            playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(24)
        monitor_shot(24.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "86-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "86-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase24()


###Test case 92 :Outbound, 4th Party conference and merging all call together. Hang up order customer , Agent A, Agent B, blind
def testcase92():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 92: 4th Party conference and merging all call together. Hang up order customer , Agent A, Agent B")
        Report.write(row, 2, item)
        Report.write(row, 3, '92')
        Report.write(row, 4, '4th Party conference and merging all call together. Hang up order customer , Agent A, Agent B')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase92.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_mute()
        refresh_and_takedata(92)
        monitor_shot(92.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        merge_all()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(92)
        monitor_shot(92.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "53-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "53-" + str(totalOutbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase92()


###Test case 93 :Outbound, 4th Party conference and merging all call together. Hang up order customer , Agent B, Agent C, blind
def testcase93():
    try:
        time.sleep(4)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 93: 4th Party conference and merging all call together. Hang up order customer , Agent B, Agent C")
        Report.write(row, 2, item)
        Report.write(row, 3, '93')
        Report.write(row, 4, '4th Party conference and merging all call together. Hang up order customer , Agent B, Agent C')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase93.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_mute()
        refresh_and_takedata(93)
        monitor_shot(93.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        merge_all()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(93)
        monitor_shot(93.2)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'hangup':
            send_mesgC('logout')
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "54-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "54-" + str(totalOutbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase93()


###Test case 94 :Outbound, 4th Party conference and merging all call together. Hang up order customer , Agent A, Agent C, blind
def testcase94():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 94: 4th Party conference and merging all call together. Hang up order customer , Agent A, Agent C")
        Report.write(row, 2, item)
        Report.write(row, 3, '94')
        Report.write(row, 4, '4th Party conference and merging all call together. Hang up order customer , Agent A, Agent C')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase94.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_mute()
        refresh_and_takedata(94)
        monitor_shot(94.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
            merge_all()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(94)
        monitor_shot(94.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgC('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "55-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "55-" + str(totalOutbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase94()


###Test case 95 : 4th Party conference and merging all call together. Hang up order Agent A, Agent B, Agent C, blind
def testcase95():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 95: 4th Party conference and merging all call together. Hang up order Agent A, Agent B, Agent C, blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '95')
        Report.write(row, 4, '4th Party conference and merging all call together. Hang up order Agent A, Agent B, Agent C, blind')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase95.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_mute()
        refresh_and_takedata(95)
        monitor_shot(95.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
            merge_all()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(95)
        monitor_shot(95.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'C logout':
            send_mesgC('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "56-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "56-" + str(totalOutbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase95()


###Test case 96 :Outbound, 4th Party conference and merging all call together. Hang up order Agent B, Agent C, Agent A, blind
def testcase96():
    try:
        time.sleep(7)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 96: 4th Party conference and merging all call together. Hang up order Agent B, Agent C, Agent A, blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '96')
        Report.write(row, 4, '4th Party conference and merging all call together. Hang up order Agent B, Agent C, Agent A, blind')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase96.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_mute()
        refresh_and_takedata(96)
        monitor_shot(96.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        merge_all()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(96)
        monitor_shot(96.2)
        recC = recv_mesgC()
        if recC == b'hangup':
            send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'logout':
            send_mesgC('logout')
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
            playsound('Agent hangup.mp3')
            end_call()
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "57-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "57-" + str(totalOutbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase96()


###Test case 97 :Outbound, 4th Party conference and merging all call together. Hang up order Agent C, Agent A, Agent B
def testcase97():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 97: 4th Party conference and merging all call together. Hang up order Agent C, Agent A, Agent B")
        Report.write(row, 2, item)
        Report.write(row, 3, '97')
        Report.write(row, 4,'4th Party conference and merging all call together. Hang up order Agent C, Agent A, Agent B')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase97.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_mute()
        refresh_and_takedata(97)
        monitor_shot(97.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        merge_all()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(97)
        monitor_shot(97.2)
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        send_mesgB('logout')
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "58-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "58-" + str(totalOutbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase97()


###Test case 98 :Inbound, 4th Party conference and merging all call together. Hang up order customer , Agent A, Agent B, blind
def testcase98():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 98: 4th Party conference and merging all call together. Hang up order customer , Agent A, Agent B")
        Report.write(row, 2, item)
        Report.write(row, 3, '98')
        Report.write(row, 4, '4th Party conference and merging all call together. Hang up order customer , Agent A, Agent B')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase98.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_mute()
        refresh_and_takedata(98)
        monitor_shot(98.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        merge_all()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(98)
        monitor_shot(98.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "99-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "99-" + str(totalinbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase98()


###Test case 99 :Inbound, 4th Party conference and merging all call together. Hang up order customer , Agent B, Agent C, blind
def testcase99():
    try:
        time.sleep(6)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 99: 4th Party conference and merging all call together. Hang up order customer , Agent B, Agent C")
        Report.write(row, 2, item)
        Report.write(row, 3, '99')
        Report.write(row, 4,  '4th Party conference and merging all call together. Hang up order customer , Agent B, Agent C')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase99.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_mute()
        refresh_and_takedata(99)
        monitor_shot(99.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        merge_all()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(99)
        monitor_shot(99.2)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'hangup':
            send_mesgC('logout')
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "100-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "100-" + str(totalinbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase99()


###Test case 100 :Inbound, 4th Party conference and merging all call together. Hang up order customer , Agent A, Agent C, blind
def testcase100():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 100: 4th Party conference and merging all call together. Hang up order customer , Agent A, Agent C")
        Report.write(row, 2, item)
        Report.write(row, 3, '100')
        Report.write(row, 4, '4th Party conference and merging all call together. Hang up order customer , Agent A, Agent C')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase100.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_mute()
        refresh_and_takedata(100)
        monitor_shot(100.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        merge_all()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(100)
        monitor_shot(100.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgC('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "101-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "101-" + str(totalinbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase100()


###Test case 101 :Inbound, 4th Party conference and merging all call together. Hang up order Agent A, Agent B, Agent C, blind
def testcase101():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 101: 4th Party conference and merging all call together. Hang up order Agent A, Agent B, Agent C, blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '101')
        Report.write(row, 4,  '4th Party conference and merging all call together. Hang up order Agent A, Agent B, Agent C, blind')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase101.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_mute()
        refresh_and_takedata(101)
        monitor_shot(101.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        merge_all()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(101)
        monitor_shot(101.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
            playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'C logout':
            send_mesgC('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "102-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "102-" + str(totalinbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase101()


###Test case 102 :Inbound, 4th Party conference and merging all call together. Hang up order Agent B, Agent C, Agent A, blind
def testcase102():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 102: 4th Party conference and merging all call together. Hang up order Agent B, Agent C, Agent A, blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '102')
        Report.write(row, 4, '4th Party conference and merging all call together. Hang up order Agent B, Agent C, Agent A, blind')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase102.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_mute()
        refresh_and_takedata(102)
        monitor_shot(102.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        merge_all()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(102)
        monitor_shot(102.2)
        recC = recv_mesgC()
        if recC == b'hangup':
            send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'logout':
            send_mesgC('logout')
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
            playsound('Agent hangup.mp3')
            end_call()
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "103-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "103-" + str(totalinbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase102()


###Test case 103 :Inbound, 4th Party conference and merging all call together. Hang up order Agent C, Agent A, Agent B
def testcase103():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 103: 4th Party conference and merging all call together. Hang up order Agent C, Agent A, Agent B")
        Report.write(row, 2, item)
        Report.write(row, 3, '103')
        Report.write(row, 4, '4th Party conference and merging all call together. Hang up order Agent C, Agent A, Agent B')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase103.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_mute()
        refresh_and_takedata(103)
        monitor_shot(103.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        merge_all()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(103)
        monitor_shot(103.2)
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
            playsound('Agent hangup.mp3')
            leave_conf()
        send_mesgB('logout')
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "104-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "104-" + str(totalinbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase103()


###Test case 9 : Inbound call and conference 3rd party. Hang up order customer , Agent A, blind
def testcase9():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 9: Inbound call and conference 3rd party. Hang up order customer , Agent B")
        Report.write(row, 2, item)
        Report.write(row, 3, '9')
        Report.write(row, 4, 'Inbound call and conference 3rd party. Hang up order customer , Agent B')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase9.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        refresh_and_takedata(9)
        monitor_shot(9.1)
        cpu_usage("Usage when AgentB receives incoming call")
        playsound('3rdpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'hangup':
            customer_hangsup()
        playsound('Agent hangup.mp3')
        end_call()
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "105-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "105-" + str(totalinbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase9()


###Test case 10 : Inbound call and conference 3rd party. Hang up order customer , Agent B, blind
def testcase10():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 10: Inbound call and conference 3rd party. Hang up order customer , Agent B")
        Report.write(row, 2, item)
        Report.write(row, 3, '10')
        Report.write(row, 4, 'Inbound call and conference 3rd party. Hang up order customer , Agent B, blind')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase10.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        refresh_and_takedata(10)
        monitor_shot(10.1)
        cpu_usage("Usage when AgentB receives incoming call")
        playsound('3rdpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'hangup':
            customer_unmute()
        customer_hangsup()
        send_mesgB('logout')
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "106-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "106-" + str(totalinbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase10()


###Test case 17 : Inbound call and conference 3rd party. Hang up order Agent A, Agent B, blind
def testcase17():
    try:
        time.sleep(5)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 17: Inbound call and conference 3rd party. Hang up order Agent A, Agent B, blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '17')
        Report.write(row, 4, 'Inbound call and conference 3rd party. Hang up order Agent A, Agent B, blind')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase17.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_mute()
        refresh_and_takedata(17)
        monitor_shot(17.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('3rdpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'hangup':
            agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "107-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "107-" + str(totalinbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase17()


###Test case 18 : Inbound call and conference 3rd party. Hang up order Agent B, Agent A, blind
def testcase18():
    try:
        time.sleep(10)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 18: Inbound call and conference 3rd party. Hang up order Agent B, Agent A, blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '18')
        Report.write(row, 4, 'Inbound call and conference 3rd party. Hang up order Agent B, Agent A, blind')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase18.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
            time.sleep(1)
        blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        refresh_and_takedata(18)
        monitor_shot(18.1)
        cpu_usage("Usage when AgentB receives incoming call")
        playsound('3rdpartconf.mp3')
        customer_unmute()
        agent_mute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'hangup':
            playsound('Agent hangup.mp3')
        end_call()
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "108-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "108-" + str(totalinbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase18()


###Test case 45 : Outbound call and conference 3rd party. Hang up order customer , Agent A, blind
def testcase45():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 45: Outbound call and conference 3rd party. Hang up order customer , Agent A,")
        Report.write(row, 2, item)
        Report.write(row, 3, '45')
        Report.write(row, 4, 'Outbound call and conference 3rd party. Hang up order customer , Agent A')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase45.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        refresh_and_takedata(45)
        monitor_shot(45.1)
        cpu_usage("Usage when AgentB receives incoming call")
        playsound('3rdpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'hangup':
            customer_unmute()
        customer_hangsup()
        agent_unmute()
        playsound('Agent hangup.mp3')
        end_call()
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "59-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "59-" + str(totalOutbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase45()


###Test case 46 : Outbound call and conference 3rd party. Hang up order customer , Agent B, blind
def testcase46():
    try:
        time.sleep(4)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 46: Outbound call and conference 3rd party. Hang up order customer , Agent B")
        Report.write(row, 2, item)
        Report.write(row, 3, '46')
        Report.write(row, 4, 'Outbound call and conference 3rd party. Hang up order customer , Agent B, blin')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase46.mp3')
        play_sound_customer()
        customer_mute()
        agent_unmute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        refresh_and_takedata(46)
        monitor_shot(46.1)
        cpu_usage("Usage when AgentB receives incoming call")
        playsound('3rdpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        cpu_usage("Usage when recording is happening")
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'hangup':
            customer_unmute()
        customer_hangsup()
        send_mesgB('logout')
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        # exp_hang_up()
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "60-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "60-" + str(totalOutbound)
        # nice_driver.close()
        testcase0('exception')
        testcase46()


###Test case 53 : Outbound call and conference 3rd party. Hang up order Agent A, Agent B, blind
def testcase53():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 53: Outbound call and conference 3rd party. Hang up order Agent A, Agent B, blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '53')
        Report.write(row, 4, 'Outbound call and conference 3rd party. Hang up order Agent A, Agent B, blind')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase53.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        refresh_and_takedata(53)
        monitor_shot(53.1)
        cpu_usage("Usage when AgentB receives incoming call")
        playsound('3rdpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'hangup':
            agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "61-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "61-" + str(totalOutbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase53()


###Test case 54 : Outbound call and conference 3rd party. Hang up order Agent B, Agent A, blind
def testcase54():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 54: Outbound call and conference 3rd party. Hang up order Agent B, Agent A, blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '54')
        Report.write(row, 4, 'Outbound call and conference 3rd party. Hang up order Agent B, Agent A, blind')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase54.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        refresh_and_takedata(54)
        monitor_shot(54.1)
        cpu_usage("Usage when AgentB receives incoming call")
        playsound('3rdpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'hangup':
            playsound('Agent hangup.mp3')
        end_call()
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "62-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "62-" + str(totalOutbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase54()


###Test case 55 : Outbound call and conference 3rd party. Hang up order Agent A, Agent B, warm
def testcase55():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 55: Outbound call and conference 3rd party. Hang up order Agent A, Agent B, warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '55')
        Report.write(row, 4, 'Outbound call and conference 3rd party. Hang up order Agent A, Agent B, warm')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase55.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_merge()
        refresh_and_takedata(55)
        monitor_shot(55.1)
        cpu_usage("Usage when AgentB receives incoming call")
        playsound('3rdpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'logout':
            print('logout')
        agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "63-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "63-" + str(totalOutbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase55()


###Test case 56 : Outbound call and conference 3rd party. Hang up order Agent B, Agent A, warm
def testcase56():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 56: Outbound call and conference 3rd party. Hang up order Agent B, Agent A, warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '56')
        Report.write(row, 4, 'Outbound call and conference 3rd party. Hang up order Agent B, Agent A, warm')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase56.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        agent_hold()
        warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(56)
        monitor_shot(56.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        playsound('3rdpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'hangup':
            agent_unmute()
            playsound('Agent hangup.mp3')
            end_call()
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "64-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "64-" + str(totalOutbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase56()




###Test case 105 : Inbound call and conference 3rd party. Hang up order customer , Agent A, warm
def testcase105():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 105: Inbound call and conference 3rd party. Hang up order customer , Agent A, warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '105')
        Report.write(row, 4, 'Inbound call and conference 3rd party. Hang up order customer , Agent A, warm')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase105.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        agent_hold()
        warm_conference2()
        cpu_usage("Usage when warm conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(105)
        monitor_shot(105.1)
        cpu_usage("Usage when AgentB receives incoming call")
        playsound('3rdpartconf.mp3')
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'hangup':
            customer_hangsup()
        playsound('Agent hangup.mp3')
        end_call()
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "109-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "109-" + str(totalinbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase105()


###Test case 106 : Inbound call and conference 3rd party. Hang up order customer , Agent B, warm
def testcase106():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 106: Inbound call and conference 3rd party. Hang up order customer , Agent B, warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '106')
        Report.write(row, 4, 'Inbound call and conference 3rd party. Hang up order customer , Agent B, warm')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase106.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        agent_hold()
        warm_conference2()
        cpu_usage("Usage when warm conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(106)
        monitor_shot(106.1)
        cpu_usage("Usage when AgentB receives incoming call")
        playsound('3rdpartconf.mp3')
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'hangup':
            customer_unmute()
        customer_hangsup()
        send_mesgB('logout')
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "110-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "110-" + str(totalinbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase106()


###Test case 107 : Inbound call and conference 3rd party. Hang up order Agent A, Agent B, warm
def testcase107():
    try:
        time.sleep(5)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 107: Inbound call and conference 3rd party. Hang up order Agent A, Agent B, warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '107')
        Report.write(row, 4, 'Inbound call and conference 3rd party. Hang up order Agent A, Agent B, warm')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase107.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        agent_hold()
        warm_conference2()
        cpu_usage("Usage when warm conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(107)
        monitor_shot(107.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('3rdpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'hangup':
            agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "111-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "111-" + str(totalinbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase107()


###Test case 108 : Inbound call and conference 3rd party. Hang up order Agent B, Agent A, warm
def testcase108():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 108: Inbound call and conference 3rd party. Hang up order Agent B, Agent A, warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '108')
        Report.write(row, 4, 'Inbound call and conference 3rd party. Hang up order Agent B, Agent A, warm')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase108.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        agent_hold()
        warm_conference2()
        cpu_usage("Usage when warm conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_merge()
        refresh_and_takedata(108)
        monitor_shot(108.1)
        cpu_usage("Usage when AgentB receives incoming call")
        playsound('3rdpartconf.mp3')
        customer_unmute()
        agent_mute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'hangup':
            playsound('Agent hangup.mp3')
        end_call()
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        # exp_hang_up()
        # nice_driver.close()
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "112-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "112-" + str(totalinbound)
        testcase0('exception')
        testcase108()




###Test case 109 : Inbound call and conference 3rd party. Hang up order Agent A, Agent B, warm, Retrieving customer
def testcase109():
    try:
        time.sleep(5)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 109: Inbound call and conference 3rd party. Hang up order Agent A, Agent B, warm, Retrieving customer")
        Report.write(row, 2, item)
        Report.write(row, 3, '109')
        Report.write(row, 4, 'Inbound call and conference 3rd party. Hang up order Agent A, Agent B, warm, Retrieving customer')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase109.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        agent_hold()
        warm_conference2()
        cpu_usage("Usage when warm conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(109)
        monitor_shot(109.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('3rdpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'hangup':
            agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase109()




###Test case 110 : Outbound call and conference 3rd party. Hang up order Agent A, Agent B, warm, Retriving customer
def testcase110():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 110: Outbound call and conference 3rd party. Hang up order Agent A, Agent B, warm, Retrieving customer")
        Report.write(row, 2, item)
        Report.write(row, 3, '110')
        Report.write(row, 4, 'Outbound call and conference 3rd party. Hang up order Agent A, Agent B, warm, Retrieving customer')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase110.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        agent_hold()
        warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_merge()
        refresh_and_takedata(110)
        monitor_shot(110.1)
        cpu_usage("Usage when AgentB receives incoming call")
        playsound('3rdpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'logout':
            agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase110()


###Test case 111 : Outbound call and conference 3rd party. Hang up order customer , Agent A, warm
def testcase111():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 111: Outbound call and conference 3rd party. Hang up order customer , Agent A, warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '111')
        Report.write(row, 4, 'Outbound call and conference 3rd party. Hang up order customer , Agent A, warm')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase111.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        agent_hold()
        warm_conference2()
        cpu_usage("Usage when warm conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_merge()
        refresh_and_takedata(111)
        monitor_shot(111.1)
        cpu_usage("Usage when AgentB receives incoming call")
        playsound('3rdpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'hangup':
            print('hangup')
        customer_unmute()
        customer_hangsup()
        agent_unmute()
        playsound('Agent hangup.mp3')
        end_call()
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "65-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "65-" + str(totalOutbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase111()


###Test case 112 : Outbound call and conference 3rd party. Hang up order customer , Agent B, warm
def testcase112():
    try:
        time.sleep(4)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 112: Outbound call and conference 3rd party. Hang up order customer , Agent B, warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '112')
        Report.write(row, 4, 'Outbound call and conference 3rd party. Hang up order customer , Agent B, warm')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase112.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        agent_hold()
        warm_conference2()
        cpu_usage("Usage when warm conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_merge()
        refresh_and_takedata(112)
        monitor_shot(112.1)
        cpu_usage("Usage when AgentB receives incoming call")
        playsound('3rdpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        cpu_usage("Usage when recording is happening")
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'hangup':
            customer_unmute()
        customer_hangsup()
        send_mesgB('logout')
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "66-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "66-" + str(totalOutbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase112()



###Test case 113 : Outbound call and conference 4th party. Hang up order customer , Agent A, Agent B, warm
def testcase113():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 113: Outbound call and conference 4th party. Hang up order customer , Agent A, Agent B")
        Report.write(row, 2, item)
        Report.write(row, 3, '113')
        Report.write(row, 4, 'Outbound call and conference 4th party. Hang up order customer , Agent A, Agent B')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase113.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             warm_conference2()
        cpu_usage("Usage when warm conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(113)
        monitor_shot(113.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(113)
        monitor_shot(113.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "29-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "29-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase113()


###Test case 114 : Outbound call and conference 4th party. Hang up order customer , Agent B, Agent A, warm
def testcase114():
    try:
        time.sleep(4)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 114: Outbound call and conference 4th party. Hang up order customer , Agent B, Agent A")
        Report.write(row, 2, item)
        Report.write(row, 3, '114')
        Report.write(row, 4, 'Outbound call and conference 4th party. Hang up order customer , Agent B, Agent A')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase114.mp3')
        agent_unmute()
        play_sound_customer()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             warm_conference2()
        cpu_usage("Usage when warm conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(114)
        monitor_shot(114.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        agent_unmute()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(114)
        monitor_shot(114.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'hangup':
            agent_unmute()
            playsound('Agent hangup.mp3')
            end_call()
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "30-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "30-" + str(totalOutbound)
        #exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase114()


###Test case 115 : Outbound call and conference 4th party. Hang up order customer , Agent B, Agent C, blind
def testcase115():
    try:
        time.sleep(4)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 115: Outbound call and conference 4th party. Hang up order customer , Agent B, Agent C")
        Report.write(row, 2, item)
        Report.write(row, 3, '115')
        Report.write(row, 4, 'Outbound call and conference 4th party. Hang up order customer , Agent B, Agent C')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase115.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             agent_hold()
             blind_conference2()
        cpu_usage("Usage when blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_mute()
        refresh_and_takedata(115)
        monitor_shot(115.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        agent_hold()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(115)
        monitor_shot(115.2)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'hangup':
            send_mesgC('logout')
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "31-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "31-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase115()


###Test case 116 : Outbound call and conference 4th party. Hang up order customer , Agent C, Agent B, blind
def testcase116():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 116: Outbound call and conference 4th party. Hang up order customer , Agent C, Agent B")
        Report.write(row, 2, item)
        Report.write(row, 3, '116')
        Report.write(row, 4, 'Outbound call and conference 4th party. Hang up order customer , Agent C, Agent B')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase116.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
            time.sleep(1)
            agent_hold()
            blind_conference2()
        cpu_usage("Usage when blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_mute()
        refresh_and_takedata(116)
        monitor_shot(116.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        agent_hold()
        agent_unmute()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
             playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(116)
        monitor_shot(116.2)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
        customer_hangsup()
        send_mesgC('logout')
        recC = recv_mesgC()
        if recC == b'hangup B':
            send_mesgB('logout')
        cpu_usage("Usage when Agent ends the call")
        time.sleep(5)
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "32-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "32-" + str(totalOutbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase116()





###Test case 117 : Outbound call and conference 4th party. Hang up order customer , Agent A, Agent C, warm
def testcase117():
    try:
        time.sleep(5)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 117: Outbound call and conference 4th party. Hang up order customer , Agent A, Agent C")
        Report.write(row, 2, item)
        Report.write(row, 3, '117')
        Report.write(row, 4, 'Outbound call and conference 4th party. Hang up order customer , Agent A, Agent C')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase117.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             warm_conference2()
        cpu_usage("Usage when warm conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(117)
        monitor_shot(117.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        agent_unmute()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(117)
        monitor_shot(117.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgC('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "34-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "34-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase117()



###Test case 118 : Outbound call and conference 4th party. Hang up order Agent A, Agent B, Agent C, warm
def testcase118():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 118: Outbound call and conference 4th party. Hang up order Agent A, Agent B, Agent C, warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '118')
        Report.write(row, 4, 'Outbound call and conference 4th party. Hang up order Agent A, Agent B, Agent C, warm')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase118.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             warm_conference2()
        cpu_usage("Usage when warm conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(118)
        monitor_shot(118.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        agent_unmute()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(118)
        monitor_shot(118.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
            playsound('Agent hangup.mp3')
            leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'C logout':
            send_mesgC('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "35-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "35-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase118()


###Test case 119 : Outbound call and conference 4th party. Hang up order Agent A, Agent C, Agent B, warm
def testcase119():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 119: Outbound call and conference 4th party. Hang up order Agent A, Agent C, Agent B, warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '119')
        Report.write(row, 4, 'Outbound call and conference 4th party. Hang up order Agent A, Agent C, Agent B, warm')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase119.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        time.sleep(3)
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             warm_conference2()
        cpu_usage("Usage when warm conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(119)
        monitor_shot(119.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        agent_unmute()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(5)
        send_mesgC('agent C play sound')
        refresh_and_takedata(119)
        monitor_shot(119.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
            playsound('Agent hangup.mp3')
            leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgC('logout')
        recC = recv_mesgC()
        if recC == b'logout':
             send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "36-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "36-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase119()


###Test case 120 : Outbound call and conference 4th party. Hang up order Agent B, Agent A, Agent C, blind
def testcase120():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 120: Outbound call and conference 4th party. Hang up order Agent B, Agent A, Agent C, blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '120')
        Report.write(row, 4, 'Outbound call and conference 4th party. Hang up order Agent B, Agent A, Agent C, blind')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase120.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        print(recB)
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             agent_hold()
             blind_conference2()
        cpu_usage("Usage when warm conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_mute()
        refresh_and_takedata(120)
        monitor_shot(120.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        print(recC)
        if recC == b'c ready':
            playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(120)
        monitor_shot(120.2)
        recC = recv_mesgC()
        print(recC)
        if recC == b'hangup':
            send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'hangup':
            agent_unmute()
            playsound('Agent hangup.mp3')
            leave_conf()
            send_mesgC('logout')
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "37-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "37-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase120()


###Test case 121 : Outbound call and conference 4th party. Hang up order Agent B, Agent C, Agent A, blind
def testcase121():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 121: Outbound call and conference 4th party. Hang up order Agent B, Agent C, Agent A, blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '121')
        Report.write(row, 4, 'Outbound call and conference 4th party. Hang up order Agent B, Agent C, Agent A, blind')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase121.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
            time.sleep(1)
            agent_hold()
            blind_conference2()
        cpu_usage("Usage when warm conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_mute()
        refresh_and_takedata(121)
        monitor_shot(121.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        agent_hold()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(121)
        monitor_shot(121.2)
        recC = recv_mesgC()
        if recC == b'hangup':
            send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'logout':
            send_mesgC('logout')
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
            playsound('Agent hangup.mp3')
            end_call()
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "38-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "38-" + str(totalOutbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase121()


###Test case 122 : Inbound call and conference 4th party. Hang up order customer , Agent A, Agent B, warm
def testcase122():
    try:
        time.sleep(7)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 122: Inbound call and conference 4th party. Hang up order customer , Agent A, Agent B, warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '122')
        Report.write(row, 4, 'Inbound call and conference 4th party. Hang up order customer , Agent A, Agent B, warm')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        time.sleep(2)
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase122.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             warm_conference2()
        cpu_usage("Usage when warm conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(122)
        monitor_shot(122.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
           agent_merge()
        agent_unmute()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(122)
        monitor_shot(122.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
        customer_hangsup()
        agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "75-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "75-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase122()


###Test case 123 : Inbound call and conference 4th party. Hang up order customer , Agent B, Agent A, warm
def testcase123():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 123: Inbound call and conference 4th party. Hang up order customer , Agent B, Agent A, warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '123')
        Report.write(row, 4, 'Inbound call and conference 4th party. Hang up order customer , Agent B, Agent A, warm')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase123.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(123)
        monitor_shot(123.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        agent_unmute()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(123)
        monitor_shot(123.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'hangup':
            agent_unmute()
            playsound('Agent hangup.mp3')
            end_call()
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "76-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "76-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase123()


###Test case 124 : Inbound call and conference 4th party. Hang up order customer , Agent B, Agent C, blind
def testcase124():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 124: Inbound call and conference 4th party. Hang up order customer , Agent B, Agent C")
        Report.write(row, 2, item)
        Report.write(row, 3, '124')
        Report.write(row, 4, 'Inbound call and conference 4th party. Hang up order customer , Agent B, Agent C')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase124.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             agent_hold()
        playsound('AgentAtoB.mp3')
        time.sleep(1)
        blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_mute()
        refresh_and_takedata(124)
        monitor_shot(124.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
             playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(124)
        monitor_shot(124.2)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'hangup':
            send_mesgC('logout')
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "77-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "77-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase124()


###Test case 125 : Inbound call and conference 4th party. Hang up order customer , Agent C, Agent B, blind
def testcase125():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 125: Inbound call and conference 4th party. Hang up order customer , Agent C, Agent B, blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '125')
        Report.write(row, 4, 'Test case 125: Inbound call and conference 4th party. Hang up order customer , Agent C, Agent B, blind')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase125.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            agent_hold()
        playsound('AgentAtoB.mp3')
        time.sleep(1)
        blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_mute()
        refresh_and_takedata(125)
        monitor_shot(125.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        agent_hold()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(125)
        monitor_shot(125.2)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
        customer_hangsup()
        send_mesgC('logout')
        recC = recv_mesgC()
        if recC == b'hangup B':
            send_mesgB('logout')
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "78-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "78-" + str(totalinbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase125()




###Test case 126 : Inbound call and conference 4th party. Hang up order customer , Agent A, Agent C, warm
def testcase126():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 126: Inbound call and conference 4th party. Hang up order customer , Agent A, Agent C")
        Report.write(row, 2, item)
        Report.write(row, 3, '126')
        Report.write(row, 4, 'Inbound call and conference 4th party. Hang up order customer , Agent A, Agent C')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase126.mp3')
        play_sound_customer()
        agent_unmute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             warm_conference2()
        cpu_usage("Usage when warm conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(126)
        monitor_shot(126.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        agent_unmute()
        playsound('4thpartconf.mp3')
        agent_mute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(126)
        monitor_shot(126.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
        customer_hangsup()
        agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgC('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "80-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "80-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase126()


###Test case 127 : Inbound call and conference 4th party. Hang up order Agent A, Agent B, Agent C, warm
def testcase127():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 127: Inbound call and conference 4th party. Hang up order Agent A, Agent B, Agent C, warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '127')
        Report.write(row, 4, 'Inbound call and conference 4th party. Hang up order Agent A, Agent B, Agent C, warm')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase127.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             warm_conference2()
        cpu_usage("Usage when warm conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(127)
        monitor_shot(127.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        agent_unmute()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(127)
        monitor_shot(127.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
            playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'C logout':
            send_mesgC('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "81-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "81-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase127()


###Test case 128 : Inbound call and conference 4th party. Hang up order Agent A, Agent C, Agent B, warm
def testcase128():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 128: Inbound call and conference 4th party. Hang up order Agent A, Agent C, Agent B, warm")
        Report.write(row, 2, item)
        Report.write(row, 3, '128')
        Report.write(row, 4, 'Inbound call and conference 4th party. Hang up order Agent A, Agent C, Agent B, warm')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase128.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
        time.sleep(1)
        warm_conference2()
        cpu_usage("Usage when warm conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_merge()
        agent_mute()
        refresh_and_takedata(128)
        monitor_shot(128.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        warm_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_merge()
        agent_unmute()
        playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(128)
        monitor_shot(128.3)
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
            playsound('Agent hangup.mp3')
            leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgC('logout')
        recC = recv_mesgC()
        if recC == b'logout':
             send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "82-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "82-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase128()


###Test case 129 : Inbound call and conference 4th party. Hang up order Agent B, Agent A, Agent C, blind
def testcase129():
    try:
        time.sleep(7)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 129: Inbound call and conference 4th party. Hang up order Agent B, Agent A, Agent C, blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '129')
        Report.write(row, 4, 'Inbound call and conference 4th party. Hang up order Agent B, Agent A, Agent C, blind')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase129.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
        time.sleep(1)
        agent_hold()
        blind_conference2()
        cpu_usage("Usage when blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_mute()
        refresh_and_takedata(129)
        monitor_shot(129.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        agent_hold()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
             playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(129)
        monitor_shot(129.2)
        recC = recv_mesgC()
        if recC == b'hangup':
            send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'hangup':
            agent_unmute()
            playsound('Agent hangup.mp3')
            end_call()
        send_mesgC('logout')
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "83-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "83-" + str(totalinbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcase129()


###Test case 130 : Inbound call and conference 4th party. Hang up order Agent B, Agent C, Agent A, blind
def testcase130():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case 130: Inbound call and conference 4th party. Hang up order Agent B, Agent C, Agent A, blind")
        Report.write(row, 2, item)
        Report.write(row, 3, '130')
        Report.write(row, 4, 'Inbound call and conference 4th party. Hang up order Agent B, Agent C, Agent A, blind')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcase130.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        agent_hold()
        blind_conference2()
        cpu_usage("Usage when blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        agent_mute()
        refresh_and_takedata(130)
        monitor_shot(130.1)
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        time.sleep(1)
        agent_hold()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
             playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
            time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata(130)
        monitor_shot(130.2)
        recC = recv_mesgC()
        if recC == b'hangup':
            send_mesgB('logout')
        recB = recv_mesgB()
        if recB == b'logout':
            send_mesgC('logout')
        recC = recv_mesgC()
        if recC == b'hangup':
            agent_unmute()
        playsound('Agent hangup.mp3')
        end_call()
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalinbound
        if testcall == "All":
            testcall = "84-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "84-" + str(totalinbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcase130()



###Test case d1 :Outbound conference 3rd party. Hang up order Agent A, Agent B, conference does not get connected,
def testcased1():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case d1 : Outbound conference 3rd party. Hang up order Agent A, Agent B, conference does not get connected")
        Report.write(row, 2, item)
        Report.write(row, 3, 'd1')
        Report.write(row, 4, 'Test case d1 : Outbound conference 3rd party. Hang up order Agent A, Agent B, conference does not get connected')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcased1.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        refresh_and_takedata('d1')
        monitor_shot('d1.1')
        cpu_usage("Usage when AgentB receives incoming call")
        playsound('3rdpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'hangup':
            agent_unmute()
        playsound('Agent hangup.mp3')
        end_call()
        end_call()
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "61-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "61-" + str(totalOutbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcased1()




###Test case d2 :Outbound, Conference 3rd party. Agent B rejects the call from Agent A
def testcased2():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case d2: Outbound, Conference 3rd party. Agent B rejects the call from Agent A")
        Report.write(row, 2, item)
        Report.write(row, 3, 'd2')
        Report.write(row, 4, 'Outbound, Conference 3rd party. Agent B rejects the call from Agent A')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcased2.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        refresh_and_takedata('d2')
        monitor_shot('d2.1')
        cpu_usage("Usage when AgentB receives incoming call")
        playsound('3rdpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'hangup':
            agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "61-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "61-" + str(totalOutbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcased2()



###Test case d3 : Outbound call and conference 3rd party. Agent B doesnt answer the call from Agent A
def testcased3():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case d3: Outbound call and conference 3rd party. Agent B doesnt answer the call from Agent A")
        Report.write(row, 2, item)
        Report.write(row, 3, 'd3')
        Report.write(row, 4, 'Outbound call and conference 3rd party. Agent B doesnt answer the call from Agent A')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcased3.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        refresh_and_takedata('d3')
        monitor_shot('d3.1')
        cpu_usage("Usage when AgentB receives incoming call")
        playsound('3rdpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'hangup':
            agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "61-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "61-" + str(totalOutbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcased3()



###Test case d4 : Outbound call and conference 4th party. Agent C rejects the call from Agent A
def testcased4():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case d4: Outbound call and conference 4th party. Agent C rejects the call from Agent A")
        Report.write(row, 2, item)
        Report.write(row, 3, 'd4')
        Report.write(row, 4, 'Outbound call and conference 4th party. Agent C rejects the call from Agent A')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcased4.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_mute()
        refresh_and_takedata('d4')
        monitor_shot('d4.1')
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_unmute()
            playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata('d4')
        monitor_shot('d4.3')
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "29-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "29-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcased4()



###Test case d5 : Outbound call and conference 4th party. AgentC doesnt answer the call from Agent B
def testcased5():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case d5: Outbound call and conference 4th party. AgentC doesnt answer the call from Agent B")
        Report.write(row, 2, item)
        Report.write(row, 3, 'd5')
        Report.write(row, 4, 'Outbound call and conference 4th party. AgentC doesnt answer the call from Agent B')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcased5.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_mute()
        refresh_and_takedata('d5')
        monitor_shot('d5.1')
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_unmute()
            playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata('d5')
        monitor_shot('d5.3')
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "29-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "29-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcased5()





###Test case d6 : Outbound call and conference 4th party. Customer drops the call before 4th party conference is established
def testcased6():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case d6: Outbound call and conference 4th party. Customer drops the call before 4th party conference is established")
        Report.write(row, 2, item)
        Report.write(row, 3, 'd6')
        Report.write(row, 4, 'Outbound call and conference 4th party. Customer drops the call before 4th party conference is established')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcased6.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_mute()
        refresh_and_takedata('d6')
        monitor_shot('d6.1')
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        blind_conference()
        customer_hangsup()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata('d6')
        monitor_shot('d6.3')
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
        agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "29-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "29-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcased6()





###Test case d7 : Outbound call and conference 4th party. Agent C logs out before the conference is established
def testcased7():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case d7: Outbound call and conference 4th party. Agent C logs out before the conference is established")
        Report.write(row, 2, item)
        Report.write(row, 3, 'd7')
        Report.write(row, 4, 'Outbound call and conference 4th party. Agent C logs out before the conference is established')
        cpu_usage("Usage when Agent goes to ready state")
        agent_call_to_customer()
        cpu_usage("Usage when Avaya makes a call")
        customer_answer()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcased7.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_mute()
        refresh_and_takedata('d7')
        monitor_shot('d7.1')
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_unmute()
            playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata('d7')
        monitor_shot('d7.3')
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        agent_unmute()
        playsound('Agent hangup.mp3')
        end_call()
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalOutbound
        if testcall == "All":
            testcall = "29-" + str(totaltest)
        if testcall == "Outbound":
            testcall = "29-" + str(totalOutbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcased7()



###Test case d8 :Inbound conference 3rd party. Hang up order Agent A, Agent B, conference does not get connected,
def testcased8():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case d8 : Inbound conference 3rd party. Hang up order Agent A, Agent B, conference does not get connected")
        Report.write(row, 2, item)
        Report.write(row, 3, 'd8')
        Report.write(row, 4, 'Test case d8 : Inbound conference 3rd party. Hang up order Agent A, Agent B, conference does not get connected')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcased8.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        warm_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        refresh_and_takedata('d8')
        monitor_shot('d8.1')
        cpu_usage("Usage when AgentB receives incoming call")
        playsound('3rdpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'hangup':
            agent_unmute()
        playsound('Agent hangup.mp3')
        end_call()
        end_call()
        cpu_usage("Usage when Agent ends the call")
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalInbound
        if testcall == "All":
            testcall = "61-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "61-" + str(totalInbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcased8()




###Test case d9 :Inbound, Conference 3rd party. Agent B rejects the call from Agent A
def testcased9():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case d9: Inbound, Conference 3rd party. Agent B rejects the call from Agent A")
        Report.write(row, 2, item)
        Report.write(row, 3, 'd9')
        Report.write(row, 4, 'Inbound, Conference 3rd party. Agent B rejects the call from Agent A')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcased9.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        refresh_and_takedata('d9')
        monitor_shot('d9.1')
        cpu_usage("Usage when AgentB receives incoming call")
        playsound('3rdpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'hangup':
            agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalInbound
        if testcall == "All":
            testcall = "61-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "61-" + str(totalInbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcased9()



###Test case d10 : Inbound call and conference 3rd party. Agent B doesnt answer the call from Agent A
def testcased10():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case d10: Inbound call and conference 3rd party. Agent B doesnt answer the call from Agent A")
        Report.write(row, 2, item)
        Report.write(row, 3, 'd10')
        Report.write(row, 4, 'Inbound call and conference 3rd party. Agent B doesnt answer the call from Agent A')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcased10.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
            playsound('AgentAtoB.mp3')
        time.sleep(1)
        blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
            print('call received')
        refresh_and_takedata('d10')
        monitor_shot('d10.1')
        cpu_usage("Usage when AgentB receives incoming call")
        playsound('3rdpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'hangup':
            agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalInbound
        if testcall == "All":
            testcall = "61-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "61-" + str(totalInbound)
        # exp_hang_up()
        # nice_driver.close()
        testcase0('exception')
        testcased10()



###Test case d11 : Inbound call and conference 4th party. Agent C rejects the call from Agent A
def testcased11():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case d11: Inbound call and conference 4th party. Agent C rejects the call from Agent A")
        Report.write(row, 2, item)
        Report.write(row, 3, 'd11')
        Report.write(row, 4, 'Inbound call and conference 4th party. Agent C rejects the call from Agent A')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcased11.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_mute()
        refresh_and_takedata('d11')
        monitor_shot('d11.1')
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_unmute()
            playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata('d11')
        monitor_shot('d11.3')
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalInbound
        if testcall == "All":
            testcall = "29-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "29-" + str(totalInbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcased11()



###Test case d12 : Inbound call and conference 4th party. AgentC doesnt answer the call from Agent B
def testcased12():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case d12: Inbound call and conference 4th party. AgentC doesnt answer the call from Agent B")
        Report.write(row, 2, item)
        Report.write(row, 3, 'd12')
        Report.write(row, 4, 'Inbound call and conference 4th party. AgentC doesnt answer the call from Agent B')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcased12.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_mute()
        refresh_and_takedata('d12')
        monitor_shot('d12.1')
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_unmute()
            playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata('d12')
        monitor_shot('d12.3')
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalInbound
        if testcall == "All":
            testcall = "29-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "29-" + str(totalInbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcased12()





###Test case d13 : Inbound call and conference 4th party. Customer drops the call before 4th party conference is established
def testcased13():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case d13: Inbound call and conference 4th party. Customer drops the call before 4th party conference is established")
        Report.write(row, 2, item)
        Report.write(row, 3, 'd13')
        Report.write(row, 4, 'Inbound call and conference 4th party. Customer drops the call before 4th party conference is established')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcased13.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_mute()
        refresh_and_takedata('d13')
        monitor_shot('d13.1')
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_unmute()
            playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata('d13')
        monitor_shot('d13.3')
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        agent_unmute()
        playsound('Agent hangup.mp3')
        leave_conf()
        cpu_usage("Usage when Agent ends the call")
        send_mesgB('logout')
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalInbound
        if testcall == "All":
            testcall = "29-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "29-" + str(totalInbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcased13()





###Test case d14 : Inbound call and conference 4th party. Agent C logs out before the conference is established
def testcased14():
    try:
        time.sleep(2)
        send_mesgB('not ready')
        send_mesgC('not ready')
        logging.info("Test case d14: Inbound call and conference 4th party. Agent C logs out before the conference is established")
        Report.write(row, 2, item)
        Report.write(row, 3, 'd14')
        Report.write(row, 4, 'Inbound call and conference 4th party. Agent C logs out before the conference is established')
        cpu_usage("Usage when Agent goes to ready state")
        Call_from_Avaya_equinox()
        cpu_usage("Usage when Avaya makes a call")
        incoming_call2()
        cpu_usage("Usage when Agent receives incoming call")
        agent_mute()
        playsound('Testcased14.mp3')
        play_sound_customer()
        agent_unmute()
        customer_mute()
        send_mesgB('ready Agent B')
        send_mesgC('ready agent C')
        recB = recv_mesgB()
        if recB == b'ready':
             playsound('AgentAtoB.mp3')
             time.sleep(1)
             blind_conference2()
        cpu_usage("Usage when Blind conf happens")
        recB = recv_mesgB()
        if recB == b'received call':
             print('call received')
        agent_mute()
        refresh_and_takedata('d14')
        monitor_shot('d14.1')
        cpu_usage("Usage when AgentB receives incoming call")
        agent_unmute()
        playsound('AgentAtoC.mp3')
        agent_mute()
        blind_conference()
        send_mesgC('incoming call')
        cpu_usage("Usage when recording is happening")
        recC = recv_mesgC()
        if recC == b'c ready':
            agent_unmute()
            playsound('4thpartconf.mp3')
        agent_mute()
        customer_unmute()
        play_sound_customer()
        customer_mute()
        agent_unmute()
        play_sound_agent()
        agent_mute()
        send_mesgB('b play sound')
        recB = recv_mesgB()
        if recB == b'play sound C':
             time.sleep(3)
        send_mesgC('agent C play sound')
        refresh_and_takedata('d14')
        monitor_shot('d14.3')
        recC = recv_mesgC()
        if recC == b'hangup':
            customer_unmute()
            customer_hangsup()
        agent_unmute()
        playsound('Agent hangup.mp3')
        end_call()
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Pass')
    except:
        logging.error(traceback.format_exc())
        Report.write(row, 6, datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
        Report.write(row, 7, 'Fail')
        wb.save('Report/Report' + localtime+ '.xls')
        global testcall, totaltest, totalInbound
        if testcall == "All":
            testcall = "29-" + str(totaltest)
        if testcall == "Inbound":
            testcall = "29-" + str(totalInbound)
        # exp_hang_up()
        #nice_driver.close()
        testcase0('exception')
        testcased14()





#######
#######  Definition of Main




App_path = os.path.dirname(sys.argv[0]) + '/'

row = 2
item = 0

localtime = datetime.datetime.now().strftime("%d-%m-%Y")

wb = Workbook()
if os.path.exists(App_path + 'Report/Report'+ str(localtime) + '.xls'):
    Rep = open_workbook(App_path + 'Report/Report'+ str(localtime) + '.xls', formatting_info=True)
    Repo = Rep.sheet_by_name('Report')
    row = number_of_good_rows(Repo)
    wb=copy(Rep)
    Report= wb.get_sheet(0)
    wb.save('Report/Report' + localtime + '.xls')
else:
    Report = wb.add_sheet('Report', cell_overwrite_ok=True)
    Report.write(row, 2, 'Item')
    Report.write(row, 3, 'Test Case#')
    Report.write(row, 4, 'Scenario')
    Report.write(row, 5, 'Start Time')
    Report.write(row, 6, 'End Time')
    Report.write(row, 7, 'Status (Pass/Fail)')
    wb.save('Report/Report' + localtime + '.xls')


logging.basicConfig(filename='Logs/'+ datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"), level=logging.INFO)



BP, QMPro, testcall, nooftimes = user_input()
print (BP, QMPro, testcall, nooftimes)
### declarations of drivers


totaltest = 132
totalInternal = 18
totalInbound = 132
totalOutbound = 76


###config file

config = configparser.ConfigParser(allow_no_value=True)
config.read_file(open(App_path + r'config.txt'))
hostnameA = config.get('automationconfig', 'hostnameA')
hostnameB = config.get('automationconfig', 'hostnameB')
hostnameC = config.get('automationconfig', 'hostnameC')
UsernameA = config.get('automationconfig', 'UsernameA')
PasswordA = config.get('automationconfig', 'PasswordA')
AvayaToAgent = config.get('automationconfig', 'AvayaToAgent')
ExtensionB = config.get('automationconfig', 'ExtensionB')
ExtensionC = config.get('automationconfig', 'ExtensionC')
AgentToAvaya = config.get('automationconfig', 'AgentToAvaya')
QmprouserA = config.get('automationconfig', 'QmprouserA')
QmpasswdA = config.get('automationconfig', 'QmpasswdA')
QmextnB = config.get('automationconfig', 'QmextnB')
QmextnC = config.get('automationconfig', 'QmextnC')
QmAvayaToAgent = config.get('automationconfig', 'QmAvayaToAgent')


############ avaya call

try:
    win_driver = webdriver.Remote(command_executor='http://127.0.0.1:4723',
                                      desired_capabilities={
                                          "app": r"C:/Program Files (x86)/Avaya/Avaya Equinox/Avaya Equinox.exe"})

except:
    win_driver = webdriver.Remote(command_executor='http://127.0.0.1:4723',
                                  desired_capabilities={
                                      "app": r"C:/Program Files (x86)/Avaya/Avaya Equinox/Avaya Equinox.exe"})

#signal.signal(signal.SIGVTALRM ,timeout_handler)



subprocess.Popen("executecall.bat", cwd=r"./")
subprocess.Popen("executecall2.bat", cwd=r"./")

j, i , k =[0,1,1]


##initilizing nice here.
from ie_test import refresh_and_takedata
from selenium import webdriver

win_action = ActionChains(win_driver)
options = webdriver.ChromeOptions()
options.add_extension('./Agent-Desktop-Chrome-Extension-Chrome Web Store_v1.16.crx')
driver = webdriver.Chrome(chrome_options=options)
action = ActionChains(driver)



testcase0('normal')


row+=1
item+=1


while j < int(nooftimes):
        if testcall == 'All':
            """testcase104()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint75()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint76()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint77()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint78()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint79()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint80()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint81()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint82()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint83()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint84()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint85()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint86()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint87()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint88()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint89()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')"""
            testcaseint90()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint91()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            testcase37()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            # not_ready_user()
            testcase38()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(4)
            # not_ready_user()
            testcase39()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase40()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase41()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase42()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase43()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase44()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            testcase47()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase48()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase49()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase50()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase51()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase52()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase57()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(28)
            testcase58()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase59()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase60()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase61()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase62()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            # not_ready_user()
            testcase63()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase64()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase65()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase66()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase67()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase68()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase69()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase70()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase71()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase72()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase73()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase74()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase92()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase93()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase94()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase95()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase96()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase97()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase45()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase46()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase53()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase54()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase55()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase56()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase111()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase112()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase113()
            row += 1
            item += 1
            wb.save('Report/Report' + localtime + '.xls')
            time.sleep(25)
            testcase114()
            row += 1
            item += 1
            wb.save('Report/Report' + localtime + '.xls')
            time.sleep(25)
            testcase115()
            row += 1
            item += 1
            wb.save('Report/Report' + localtime + '.xls')
            time.sleep(25)
            testcase116()
            row += 1
            item += 1
            wb.save('Report/Report' + localtime + '.xls')
            time.sleep(25)
            testcase117()
            row += 1
            item += 1
            wb.save('Report/Report' + localtime + '.xls')
            time.sleep(25)
            testcase118()
            row += 1
            item += 1
            wb.save('Report/Report' + localtime + '.xls')
            time.sleep(28)
            testcase119()
            row += 1
            item += 1
            wb.save('Report/Report' + localtime + '.xls')
            time.sleep(25)
            testcase120()
            row += 1
            item += 1
            wb.save('Report/Report' + localtime + '.xls')
            time.sleep(25)
            testcase121()
            row += 1
            item += 1
            wb.save('Report/Report' + localtime + '.xls')
            time.sleep(25)
            ready_user()
            testcase1()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            not_ready_user()
            testcase2()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            not_ready_user()
            testcase3()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            not_ready_user()
            testcase4()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            not_ready_user()
            testcase5()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            not_ready_user()
            testcase6()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            not_ready_user()
            testcase7()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            not_ready_user()
            testcase8()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase11()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase12()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase13()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase14()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            not_ready_user()
            ready_user()
            testcase15()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase16()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase19()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase20()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase21()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase22()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase23()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase24()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            not_ready_user()
            testcase25()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            not_ready_user()
            testcase26()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            not_ready_user()
            testcase27()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            not_ready_user()
            testcase28()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            not_ready_user()
            testcase29()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            not_ready_user()
            testcase30()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            not_ready_user()
            testcase31()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            not_ready_user()
            testcase32()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            not_ready_user()
            testcase33()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            not_ready_user()
            testcase34()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            not_ready_user()
            testcase35()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            not_ready_user()
            testcase36()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            ready_user()
            testcase98()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase99()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase100()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase101()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase102()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase103()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase9()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase10()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(20)
            ready_user()
            testcase17()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(20)
            ready_user()
            testcase18()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(20)
            ready_user()
            testcase105()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(20)
            ready_user()
            testcase106()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(20)
            ready_user()
            testcase107()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(20)
            ready_user()
            testcase108()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase122()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase123()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase124()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase125()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase126()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase127()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase128()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase129()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase130()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
        elif testcall == "Inbound":
            ready_user()
            testcase1()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            not_ready_user()
            testcase2()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            not_ready_user()
            testcase3()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            not_ready_user()
            testcase4()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            not_ready_user()
            testcase5()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            not_ready_user()
            testcase6()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            not_ready_user()
            testcase7()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            not_ready_user()
            testcase8()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase11()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase12()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase13()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase14()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            not_ready_user()
            ready_user()
            testcase15()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase16()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase19()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase20()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase21()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase22()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase23()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase24()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            not_ready_user()
            testcase25()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            not_ready_user()
            testcase26()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            not_ready_user()
            time.sleep(8)
            not_ready_user()
            testcase27()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            not_ready_user()
            testcase28()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            not_ready_user()
            testcase29()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            not_ready_user()
            testcase30()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            not_ready_user()
            testcase31()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            not_ready_user()
            testcase32()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            not_ready_user()
            testcase33()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            not_ready_user()
            testcase34()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            not_ready_user()
            testcase35()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            not_ready_user()
            testcase36()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            ready_user()
            testcase98()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase99()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase100()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase101()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase102()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase103()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase9()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase10()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(20)
            ready_user()
            testcase17()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(20)
            ready_user()
            testcase18()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(20)
            ready_user()
            testcase105()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(20)
            ready_user()
            testcase106()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(20)
            ready_user()
            testcase107()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(20)
            ready_user()
            testcase108()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            ready_user()
            testcase109()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase122()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase123()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase124()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase125()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase126()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase127()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase128()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase129()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase130()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
        elif testcall == "Outbound":
            testcase37()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            # not_ready_user()
            testcase38()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(4)
            # not_ready_user()
            testcase39()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase40()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase41()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase42()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase43()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase44()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            testcase47()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase48()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase49()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase50()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase51()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase52()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase57()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(28)
            testcase58()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase59()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase60()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase61()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase62()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            # not_ready_user()
            testcase63()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase64()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase65()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase66()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase67()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase68()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase69()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase70()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase71()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase72()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase73()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase74()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(8)
            # not_ready_user()
            testcase92()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase93()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase94()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase95()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase96()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase97()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase45()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase46()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase53()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase54()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase55()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase56()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase110()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            testcase111()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(25)
            testcase112()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            testcase113()
            row += 1
            item += 1
            wb.save('Report/Report' + localtime + '.xls')
            time.sleep(25)
            testcase114()
            row += 1
            item += 1
            wb.save('Report/Report' + localtime + '.xls')
            time.sleep(25)
            testcase115()
            row += 1
            item += 1
            wb.save('Report/Report' + localtime + '.xls')
            time.sleep(25)
            testcase116()
            row += 1
            item += 1
            wb.save('Report/Report' + localtime + '.xls')
            time.sleep(25)
            testcase117()
            row += 1
            item += 1
            wb.save('Report/Report' + localtime + '.xls')
            time.sleep(25)
            testcase118()
            row += 1
            item += 1
            wb.save('Report/Report' + localtime + '.xls')
            time.sleep(28)
            testcase119()
            row += 1
            item += 1
            wb.save('Report/Report' + localtime + '.xls')
            time.sleep(25)
            testcase120()
            row += 1
            item += 1
            wb.save('Report/Report' + localtime + '.xls')
            time.sleep(25)
            testcase121()
            row += 1
            item += 1
            wb.save('Report/Report' + localtime + '.xls')
            time.sleep(25)
        elif testcall == "Internal":
            testcase104()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint75()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint76()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint77()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint78()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint79()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint80()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint81()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint82()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint83()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint84()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint85()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint86()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint87()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint88()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint89()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint90()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            testcaseint91()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
        elif testcall == "Preliminary":
            """ready_user()
            testcase1()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            testcase5()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            not_ready_user()"""
            testcase25()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            not_ready_user()
            testcase27()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            not_ready_user()
            testcase29()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            not_ready_user()
            time.sleep(15)
            ready_user()
            testcase9()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase109()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            ready_user()
            testcase11()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            testcase92()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            testcase45()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            testcase110()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            testcase47()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            testcase37()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            testcase41()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            testcase63()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            testcase65()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            testcase67()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            testcaseint75()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            testcaseint86()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            not_ready_user()
        elif testcall == "Destructive":
            """testcased1()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            testcased2()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            testcased3()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            testcased4()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            testcased5()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            testcased6()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(15)
            testcased7()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(20)
            ready_user()
            testcased8()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(20)
            ready_user()
            testcased9()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(20)
            ready_user()
            testcased10()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(20)"""
            ready_user()
            testcased11()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(20)
            ready_user()
            testcased12()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(20)
            ready_user()
            testcased13()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(20)
            ready_user()
            testcased14()
            row+=1
            item+=1
            wb.save('Report/Report' + localtime+ '.xls')
            time.sleep(20)
            ready_user()
        else:
            if testcall[1:2]=='-':
                i = int(testcall[0:1])
                k = int(testcall[2:4])
            elif testcall[2:3]=='-':
                i = int(testcall[0:2])
                k = int(testcall[3:6])
            elif testcall[3:4]=='-':
                i = int(testcall[0:3])
                k = int(testcall[4:7])
            while i <= k:
                if i == 1:
                    testcase104()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 2:
                    testcaseint75()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 3:
                    testcaseint76()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 4:
                    testcaseint77()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 5:
                    testcaseint78()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 6:
                    testcaseint79()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 7:
                    testcaseint80()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 8:
                    testcaseint81()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 9:
                    testcaseint82()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 10:
                    testcaseint83()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 11:
                    testcaseint84()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 12:
                    testcaseint85()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 13:
                    testcaseint86()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 14:
                    testcaseint87()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 15:
                    testcaseint88()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 16:
                    testcaseint89()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 17:
                    testcaseint90()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 18:
                    testcaseint91()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 19:
                    time.sleep(8)
                    testcase37()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 20:
                    time.sleep(8)
                    testcase38()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 21:
                    time.sleep(8)
                    testcase39()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 22:
                    time.sleep(8)
                    testcase40()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 23:
                    time.sleep(8)
                    testcase41()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 24:
                    time.sleep(8)
                    testcase42()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 25:
                    time.sleep(8)
                    testcase43()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 26:
                    time.sleep(8)
                    testcase44()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 27:
                    time.sleep(8)
                    testcase45()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 28:
                    time.sleep(8)
                    testcase46()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 29:
                    time.sleep(8)
                    testcase47()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 30:
                    time.sleep(25)
                    testcase48()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 31:
                    time.sleep(25)
                    testcase49()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 32:
                    time.sleep(25)
                    testcase50()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 33:
                    time.sleep(25)
                    testcase51()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 34:
                    time.sleep(25)
                    testcase52()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 35:
                    time.sleep(25)
                    testcase57()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 36:
                    time.sleep(25)
                    testcase58()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 37:
                    time.sleep(25)
                    testcase59()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 38:
                    time.sleep(25)
                    testcase60()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 39:
                    time.sleep(25)
                    testcase61()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 40:
                    time.sleep(25)
                    testcase62()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 41:
                    time.sleep(25)
                    testcase63()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 42:
                    time.sleep(8)
                    testcase64()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 43:
                    time.sleep(8)
                    testcase65()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 44:
                    time.sleep(8)
                    testcase66()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 45:
                    time.sleep(8)
                    testcase67()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 46:
                    time.sleep(8)
                    testcase68()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 47:
                    time.sleep(8)
                    testcase69()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 48:
                    time.sleep(8)
                    testcase70()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 49:
                    time.sleep(8)
                    testcase71()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 50:
                    time.sleep(8)
                    testcase72()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 51:
                    time.sleep(8)
                    testcase73()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 52:
                    time.sleep(8)
                    testcase74()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 53:
                    time.sleep(8)
                    testcase92()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 54:
                    time.sleep(25)
                    testcase93()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 55:
                    time.sleep(25)
                    testcase94()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 56:
                    time.sleep(25)
                    testcase95()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 57:
                    time.sleep(25)
                    testcase96()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 58:
                    time.sleep(25)
                    testcase97()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 59:
                    time.sleep(25)
                    testcase45()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 60:
                    time.sleep(25)
                    testcase46()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 61:
                    time.sleep(25)
                    testcase53()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 62:
                    time.sleep(25)
                    testcase54()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 63:
                    time.sleep(25)
                    testcase55()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 64:
                    time.sleep(25)
                    testcase56()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 65:
                    time.sleep(25)
                    testcase110()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 66:
                    time.sleep(25)
                    testcase111()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 67:
                    time.sleep(25)
                    testcase112()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 68:
                    time.sleep(25)
                    testcase113()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 69:
                    time.sleep(25)
                    testcase114()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 70:
                    time.sleep(25)
                    testcase115()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 71:
                    time.sleep(25)
                    testcase116()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 72:
                    time.sleep(25)
                    testcase117()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 73:
                    time.sleep(25)
                    testcase118()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 74:
                    time.sleep(25)
                    testcase119()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 75:
                    time.sleep(25)
                    testcase120()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 76:
                    time.sleep(25)
                    testcase121()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 77:
                    time.sleep(25)
                    ready_user()
                    testcase1()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 78:
                    not_ready_user()
                    testcase2()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 79:
                    not_ready_user()
                    testcase3()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 80:
                    not_ready_user()
                    testcase4()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 81:
                    not_ready_user()
                    testcase5()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 82:
                    not_ready_user()
                    testcase6()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 83:
                    not_ready_user()
                    testcase7()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 84:
                    not_ready_user()
                    testcase8()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 85:
                    time.sleep(15)
                    ready_user()
                    testcase11()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 86:
                    time.sleep(15)
                    ready_user()
                    testcase12()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 87:
                    time.sleep(15)
                    ready_user()
                    testcase13()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 88:
                    time.sleep(15)
                    ready_user()
                    testcase14()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 89:
                    time.sleep(15)
                    ready_user()
                    testcase15()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 90:
                    time.sleep(15)
                    ready_user()
                    testcase16()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 91:
                    time.sleep(15)
                    ready_user()
                    testcase19()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 92:
                    time.sleep(15)
                    ready_user()
                    testcase20()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 93:
                    time.sleep(15)
                    ready_user()
                    testcase21()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 94:
                    time.sleep(15)
                    ready_user()
                    testcase22()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 95:
                    time.sleep(15)
                    ready_user()
                    testcase23()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 96:
                    time.sleep(15)
                    ready_user()
                    testcase24()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 97:
                    time.sleep(15)
                    not_ready_user()
                    testcase25()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 98:
                    time.sleep(15)
                    not_ready_user()
                    testcase26()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 99:
                    time.sleep(8)
                    not_ready_user()
                    testcase27()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 100:
                    time.sleep(8)
                    not_ready_user()
                    testcase28()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 101:
                    time.sleep(8)
                    not_ready_user()
                    testcase29()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 102:
                    time.sleep(8)
                    not_ready_user()
                    testcase30()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 103:
                    time.sleep(8)
                    not_ready_user()
                    testcase31()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 104:
                    time.sleep(8)
                    not_ready_user()
                    testcase32()
                if i == 105:
                    time.sleep(8)
                    not_ready_user()
                    testcase33()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 106:
                    time.sleep(8)
                    not_ready_user()
                    testcase34()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 107:
                    time.sleep(8)
                    not_ready_user()
                    testcase35()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 108:
                    time.sleep(8)
                    not_ready_user()
                    testcase36()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 109:
                    ready_user()
                    testcase98()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 110:
                    time.sleep(15)
                    ready_user()
                    testcase99()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 111:
                    time.sleep(15)
                    ready_user()
                    testcase100()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 112:
                    time.sleep(15)
                    ready_user()
                    testcase101()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 113:
                    time.sleep(15)
                    ready_user()
                    testcase102()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 114:
                    time.sleep(15)
                    ready_user()
                    testcase103()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 115:
                    time.sleep(15)
                    ready_user()
                    testcase9()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 116:
                    testcase10()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 117:
                    time.sleep(15)
                    ready_user()
                    testcase17()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 118:
                    time.sleep(15)
                    ready_user()
                    testcase18()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 119:
                    time.sleep(15)
                    ready_user()
                    testcase105()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 120:
                    time.sleep(15)
                    ready_user()
                    testcase106()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 121:
                    time.sleep(15)
                    ready_user()
                    testcase107()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 122:
                    time.sleep(15)
                    ready_user()
                    testcase108()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 123:
                    time.sleep(15)
                    ready_user()
                    testcase109()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 124:
                    time.sleep(15)
                    ready_user()
                    testcase122()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 125:
                    time.sleep(15)
                    ready_user()
                    testcase123()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 126:
                    time.sleep(15)
                    ready_user()
                    testcase124()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 127:
                    time.sleep(15)
                    ready_user()
                    testcase125()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 128:
                    time.sleep(15)
                    ready_user()
                    testcase126()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 129:
                    time.sleep(15)
                    ready_user()
                    testcase127()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 130:
                    time.sleep(15)
                    ready_user()
                    testcase128()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 131:
                    time.sleep(15)
                    ready_user()
                    testcase129()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                if i == 132:
                    time.sleep(15)
                    ready_user()
                    testcase130()
                    row += 1
                    item += 1
                    wb.save('Report/Report' + localtime+ '.xls')
                time.sleep(15)
                i+=1
        print(j)
        if j == int(nooftimes):
            break
        j+=1













