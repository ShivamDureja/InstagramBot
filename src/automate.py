from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from humanMimicking import slow_type
from humanMimicking import mouseMovement
import time
from env import *

def automate(driver,username,password,panelH,panelW,friend):
    LoginUser(driver,username,password,panelH,panelW)
    submit(driver,panelH,panelW)
    time.sleep(2)
    popup(driver,panelH,panelW)
    time.sleep(2)
    Hider(driver,panelH,panelW)
    time.sleep(2)
    search(driver,friend,panelH,panelW)
    time.sleep(3)

def LoginUser(driver, username, password,panelH,panelW):
    clickName = driver.find_element(by=By.XPATH, value="//body/div[@id='react-root']/section[1]/main[1]/article[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/label[1]/input[1]")
    locate = clickName.location
    size = clickName.size
    mouseMovement(locate,size,panelH,panelW)
    clickName.click()
    method = By.NAME
    methodValue = "username"
    methodValuePass = "password"

    loginName = driver.find_element(by=method, value=methodValue)
    loginPass = driver.find_element(by=method, value=methodValuePass)
    slow_type(loginName,username)
    slow_type(loginPass,password)
    time.sleep(2)

def submit(driver,panelH,panelW):
    # search submit button
    method = By.XPATH
    methodValue = "//div[contains(text(),'Log In')]"
    submitButton = driver.find_element(by=method, value=methodValue)
    # taking action
    locate = submitButton.location
    size = submitButton.size
    mouseMovement(locate,size,panelH,panelW)
    submitButton.click()

def popup(driver,panelH,panelW):

    method = By.XPATH
    methodValue = "/html[1]/body[1]/div[1]/section[1]/main[1]/div[1]/div[1]/div[1]/div[1]/button[1]"

    closeButton = driver.find_element(by=method, value=methodValue)
    locate = closeButton.location
    size = closeButton.size
    mouseMovement(locate,size,panelH,panelW)
    # taking action
    closeButton.click()

def Hider(driver,panelH,panelW):

    method = By.XPATH
    methodValue = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/button[2]"

    closeButton = driver.find_element(by=method, value=methodValue)
    locate = closeButton.location
    size = closeButton.size
    mouseMovement(locate,size,panelH,panelW)
    # taking action
    closeButton.click()

def search(driver, friend,panelH,panelW):
    method = By.XPATH
    methodValue = "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/nav[1]/div[2]/div[1]/div[1]/div[2]/input[1]"
    element = driver.find_element(by=method, value=methodValue)
    locate = element.location
    size = element.size
    mouseMovement(locate,size,panelH,panelW)
    slow_type(element,friend)
    time.sleep(2)
    element.send_keys(Keys.ENTER)
    element.send_keys(Keys.ENTER)

