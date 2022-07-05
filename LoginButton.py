from selenium.webdriver.common.by import By


def submit(driver):
    # search submit button

    method = By.XPATH
    methodValue = "//body/div[@id='react-root']/section[1]/main[1]/article[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[3]/button[1]"

    submitButton = driver.find_element(by=method, value=methodValue)

    # taking action
    submitButton.click()
