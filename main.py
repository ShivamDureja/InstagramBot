from Loader import Loader
from Login import LoginUser
from LoginButton import submit
from removePopup import popup
from NotificationHider import Hider
import time



page_url = "https://www.instagram.com/"
login_name = "_shivam_dureja"
login_password = "sdshivam"
driver = Loader(page_url)
time.sleep(2)
LoginUser(driver,login_name,login_password)
time.sleep(1)
submit(driver)
time.sleep(1)
popup(driver)
Hider(driver)
