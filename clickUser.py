from selenium.webdriver.common.by import By
import time


def click(driver, username):
    method = By.XPATH
    methodValue = f"//a[@href='/" + username + "/']"
    element = driver.find_element(by=method, value=methodValue)
    time.sleep(2)
    element.click()
