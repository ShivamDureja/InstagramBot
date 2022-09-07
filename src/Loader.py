from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from env import *
from selenium.webdriver.chrome.service import Service
from env import *


# it loads the web page and return the driver
def Loader(url):

    options = Options()
    options._binary_location = chromePath
    s = Service(chromeDriver)
    # options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
    prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False}
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options, service=s)
    driver.implicitly_wait(20)
    driver.get(url)
    return driver
