from re import L
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
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
    time.sleep(3)
    # like_pic(driver)

    # try:
    #     driver.find_element(by=By.XPATH,value="//button[@class='_abl-']//span//*[local-name()='svg'][@aria-label='Unlike']")
    # except NoSuchElementException:
    
    likeImg = driver.find_elements(by=By.XPATH,value="//button[@class='_abl-']/div/span")
    locateLike = likeImg[1].location
    likeSize = likeImg[1].size
    mouseMovement(locateLike,likeSize,panelH,panelW)
    time.sleep(2)
    like(driver)
    # continueLike(driver)
    while(int(numb_of_post)-1):
        ActionChains(driver).send_keys(Keys.ARROW_RIGHT)
        time.sleep(2)
        like(driver)
        numb_of_post = numb_of_post-1


def like(driver):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[name()='svg' and @aria-label='Like']"))).click()

def next(driver):
    nextEle = driver.find_element(by=By.XPATH,value="//div[@class=' _aaqg _aaqh']")
    return nextEle

def continueLike(driver):
    while(True):
        next_el = next(driver)
        if next_el != False:
 
            # click the next button
            next_el.click()
            time.sleep(2)
 
            # like the picture
            like(driver)
            time.sleep(2)
        else:
            print("not found")
            break
# def like_pic(driver):
# 	time.sleep(2)
# 	like = driver.find_element(by=By.XPATH,value="//button/div")
# 	soup = BeautifulSoup(like.get_attribute('innerHTML'),'html.parser')
# 	if(soup.find('svg')['aria-label'] == 'Like'):
# 		like.click()
# 	time.sleep(2)

