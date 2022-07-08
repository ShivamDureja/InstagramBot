from selenium.webdriver.common.by import By
import time


def selector(driver, username):
    method = By.XPATH
    methodValue = "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/nav[1]/div[2]/div[1]/div[1]/div[2]/input[1]"
    element = driver.find_element(by=method, value=methodValue)
    element.send_keys(username)
    time.sleep(2)
