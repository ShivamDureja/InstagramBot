from selenium.webdriver.common.by import By
import time


def LoginUser(driver, username, password):
    method = By.NAME
    methodValue = "username"
    methodValuePass = "password"

    loginName = driver.find_element(by=method, value=methodValue)
    loginPass = driver.find_element(by=method, value=methodValuePass)
    loginName.send_keys(username)
    time.sleep(2)
    loginPass.send_keys(password)
    time.sleep(2)
