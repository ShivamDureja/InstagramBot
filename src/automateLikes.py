from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from humanMimicking import slow_type
from humanMimicking import mouseMovement
import time
from env import *

def automateLikes(driver,panelH,panelW):
    # To find the number of posts
    details = driver.find_elements(by=By.XPATH,value="//span[@class='_ac2a']")
    numb_of_post = details[0].text
    # click to open the first instagram post
    Posts = driver.find_elements(by=By.XPATH,value= ".//div[@class='_aabd _aa8k _aanf']")
    locate = Posts[0].location
    size = Posts[0].size
    mouseMovement(locate,size,panelH,panelW)
    time.sleep(2)
    Posts[0].click()
    time.sleep(6)
    try:
        driver.find_element(by=By.XPATH,value="//button/span[@aria-label='UnLike']")
    except NoSuchElementException:
        driver.find_element(by=By.XPATH,value="//button/span[@aria-label='Like']").click()

# def like(driver):
#     likeImg = driver.find_element(by=By.XPATH,value="//button[@type='button']//*[name()='svg' and @aria-label='Like' and @height='24']")
#     likeImg.click()

