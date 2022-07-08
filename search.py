from selenium.webdriver.common.by import By
import time
from selenium.webdriver import Keys, ActionChains

def selector(driver,username):
    method = By.XPATH
    methodValue = "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/nav[1]/div[2]/div[1]/div[1]/div[2]/input[1]"
    element = driver.find_element(by=method, value=methodValue)
    time.sleep(2)
    element.send_keys(username)
    time.sleep(2)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER)