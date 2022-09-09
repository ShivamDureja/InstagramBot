from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
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
    
    likeImg = driver.find_elements(by=By.XPATH,value="//button[@class='_abl-']/div/span")
    locateLike = likeImg[1].location
    likeSize = likeImg[1].size
    mouseMovement(locateLike,likeSize,panelH,panelW)
    time.sleep(2)
    like(driver)
    time.sleep(2)
    continueLike(driver)
    close(driver,panelH,panelW)
    time.sleep(3)
    driver.close()


def like(driver):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[name()='svg' and @aria-label='Like']"))).click()

def next(driver):
    nextEle = driver.find_element(by=By.XPATH,value="//div[@class=' _aaqg _aaqh']")
    return nextEle

def likeImg(driver):
    driver.find_element(by=By.XPATH,value="//button//div//span//*[name()='svg' and @aria-label='Like']").click()

def continueLike(driver):
    while True:
        print("Liked")
        try:
            if next(driver).is_displayed():
                next(driver).click()
                time.sleep(2)
                likeImg(driver)
            else: 
                break
        except NoSuchElementException:
            break
            

def close(driver,panelH,panelW):
    closeBtn = driver.find_element(by=By.XPATH,value="//*[name()='svg' and @aria-label='Close']")
    locateClose = closeBtn.location
    sizeClose = closeBtn.size
    mouseMovement(locateClose,sizeClose,panelH,panelW)
    closeBtn.click()