from selenium.webdriver.common.by import By


def firstMedia(driver):
    method = By.XPATH
    methodValue = "//div[@class='_aagw']"
    element = driver.find_element(by=method,value=methodValue)
    element.click()