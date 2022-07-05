from Loader import Loader
from Login import LoginUser
from LoginButton import submit


page_url = "https://www.instagram.com/"
login_name = "_shivam_dureja"
login_password = "sdshivam"
driver = Loader(page_url)
LoginUser(driver,login_name,login_password)
submit(driver)