from robot.libraries.BuiltIn import BuiltIn
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from robot.api import logger
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import win32com
import win32com.client
import Selenium2Library
import SeleniumLibrary
import os
import glob
import time
import datetime
import sys
import Config
from Logger import Logger
logger=Logger()
###########
#Basic keywords
################
def get_selenium2library():
    return BuiltIn().get_library_instance("Selenium2Library")
def get_webdriver_instance():
    se2lib=BuiltIn().get_library_instance("Selenium2Library")
    return se2lib.driver
def get_webdriver_actionchains_instance():
    driver=get_webdriver_instance()
    actionChains=ActionChains(driver)
    return actionChains
def screenshot():
    driver=get_webdriver_instance()
    se2lib = get_selenium2library()
    se2lib.capture_page_screenshot()
    ts = time.time()
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%d%m%Y_%H%M%S')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    directory = dir_path.replace("Functions","")
    directory=directory+"Screenshots\\"
    if not os.path.exists(directory):
        os.makedirs(directory)
    driver.save_screenshot(directory+'Screenshot'+timeStamp+'.png')
    list_of_files = glob.glob(directory+'/*.png')  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    logger.logScreenshot(latest_file)
def log_msg(str_text=""):
    logger.info(str_text)
    logger.console(str_text)
def enterGoogle():
    driver = get_webdriver_instance()
    driver.find_element_by_xpath(Config.get_test_data("Title")).send_keys("vhjjj")
    logger.info("vinothl gopal")
    Config.set_test_data("Deal","Sreelakshmi")
def loginhexaware():
    driver = get_webdriver_instance()
    driver.find_element_by_xpath("//input[@id='txtUserName']").send_keys(Config.get_test_data("UserName"))
    driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys(Config.get_test_data("Password"))
def log_msg_bold(str_test=""):
    logger.info('<b><i>'+str_test+'</i></b>',html=True)
    logger.console(str_test)
def log_warn(str_test=""):
    logger.warn(str_test)
    logger.console(str_test)
def log_debug(str_text=""):
    logger.debug(str_text)
def log_console(str_text=""):
    logger.console(str_text)
def log_result(exepected,actual,log_level='info'):
    if log_level=='info':
        log_msg("Expected= "+exepected+" ||Actual = "+actual)
    else:
        log_debug("Expected= " + exepected + " ||Actual = " + actual)
def run_vbs_file(filepath):
    filepath=filepath.replace("/",os.sep)
    filepath = filepath.replace( os.sep,"\\")
    os.system(filepath)
#######################################################
#verification method
##################################################

def assert_text(expected_text,actual_text,bol_log=False,cont=False):
    expected_text=str(expected_text).lower()
    actual_text=str(actual_text).lower()
    if expected_text==actual_text:
        if bol_log:
            log_msg("Expected= "+expected_text+" ||Actual = "+actual_text)
    else:
        screenshot()
        if cont:
            log_msg()
        else:
            log_msg()


def assert_text_contains(expected_text, actual_text, bol_log=False, cont=False):
    expected_text = str(expected_text).lower()
    actual_text = str(actual_text).lower()
    if expected_text in actual_text:
        screenshot()
        logger.result(True)
        logger.loginfo("Expected= " + expected_text + " ||Actual = " + actual_text)
    else:
        screenshot()
        logger.result(False)
        logger.loginfo("Expected= " + expected_text + " ||Actual = " + actual_text)
def set_test_variable(variable_name,variable_value):
    BuiltIn().set_tesk_variable("${"+variable_name+"}",variable_value)
    log_msg(variable_name+ "= "+variable_value)
def set_suite_variable(variable_name,variable_value):
    BuiltIn().set_suite_variable("${"+variable_name+"}",variable_value)
    log_msg(variable_name+ "= "+variable_value)
def fail_message(messge="",cont=False):
    if cont:
        log_msg()
    else:
        BuiltIn().fail(messge)
def fail_test_case(expected_text,actual_text):
    BuiltIn().fail("Expected= " + expected_text + " ||Actual = " + actual_text)
###########################################
#web keywords
###########################################
def open_web_browser(url,browser='firefox',alias=None,remote_url=False,desired_capabilities=None,ff_profile_dir=None):
    sel2lib=get_selenium2library()
    #sel2lib=open_browser(url,browser,alias,remote_url,desired_capabilities,ff_profile_dir)
def close_all_browser():
    sel2lib = get_selenium2library()
    sel2lib.close_all_browser()
def maximize_browser(cont=False):
    driver=get_webdriver_instance()
    try:
        driver.maximize_window()
    except:
        if not cont:
            fail_message("Error while maximizing the window")
        log_msg("Error")
def go_to_url(url,cont=False):
    driver=get_webdriver_instance()
    try:
        driver.get(url)
    except:
        if not cont:
            fail_message("Error while maximizing the window")
        log_msg("Error")
def assert_list1inlist2_exact(list1,list2):
    result=all(elm in list1 for elm in list2)
    if result:
        log_msg("pass")
    else:
        screenshot()
        log_msg("Fail")
def enterInputValue(str_xpath,value,timeout=10):
    driver=get_webdriver_instance()
    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, str_xpath)))
        element.send_keys(value)
    except:
        logger.info("Element is not presented in Application")
def clikElement(str_path,timeout=10):
    driver = get_webdriver_instance()
    try:
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, str_path)))
        element.click()
    except:
        logger.info("Element is not presented in Application")
def get_TitleofPage():
    driver=get_webdriver_instance()
    return driver.title









