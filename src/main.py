from automate import automate
from Loader import Loader
from env import *
import time

driver = Loader(InstaUrl)
time.sleep(2)
driver.maximize_window()
panelHeight = driver.execute_script("return window.outerHeight - window.innerHeight;")
panelWidth = driver.execute_script("return window.innerWidth;")
time.sleep(2)
automate(driver,LoginUserName,LoginUserPass,panelHeight,panelWidth,friendUserName)


# firstMedia(driver)
# time.sleep(4)
# likeButton(driver)
# time.sleep(2)
# nextButton(driver)