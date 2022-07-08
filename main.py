from Loader import Loader
from Login import LoginUser
from LoginButton import submit
from removePopup import popup
from NotificationHider import Hider
import time
from search import selector
from clickUser import click
from firstElement import firstMedia
from like import likeButton
from next import nextButton


page_url = "https://www.instagram.com/"
login_name = "_shivam_dureja"
login_password = "sdshivam"
friend = "real._.nature_beauty"
driver = Loader(page_url)
driver.maximize_window()
time.sleep(2)
LoginUser(driver, login_name, login_password)
time.sleep(2)
submit(driver)
time.sleep(2)
popup(driver)
time.sleep(3)

Hider(driver)
time.sleep(2)

selector(driver, friend)
time.sleep(4)
click(driver, friend)
time.sleep(4)
firstMedia(driver)
time.sleep(4)
likeButton(driver)
time.sleep(2)
nextButton(driver)