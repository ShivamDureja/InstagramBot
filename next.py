from selenium.webdriver.common.by import By


def nextButton(driver):
    method = By.XPATH
    methodValue = "//div[@class=' _aaqg _aaqh']"
    element = driver.find_element(by=method,value=methodValue)
    element.click()