from automate import automate
from Loader import Loader
from env import *
import time
from automateLikes import automateLikes

driver = Loader(InstaUrl)
time.sleep(2)
driver.maximize_window()
panelHeight = driver.execute_script("return window.outerHeight - window.innerHeight;")
panelWidth = driver.execute_script("return window.innerWidth;")
time.sleep(2)
driver.implicitly_wait(30)
automate(driver,LoginUserName,LoginUserPass,panelHeight,panelWidth,friendUserName)
automateLikes(driver,panelHeight,panelWidth)
