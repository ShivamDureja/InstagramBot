from selenium.webdriver.common.by import By


def popup(driver):

    method = By.XPATH
    methodValue = "//button[contains(text(),'Not Now')]"

    closeButton = driver.find_element(by=method, value=methodValue)

    # taking action
    closeButton.click()
