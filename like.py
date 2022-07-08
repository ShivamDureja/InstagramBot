from selenium.webdriver.common.by import By


def likeButton(driver):
    method = By.XPATH
    methodValue = "//button[@class='_abl-']//div[@class='_abm0 _abl_']//*[@aria-label='Like']"
    element = driver.find_element(by=method,value=methodValue)
    element.click()