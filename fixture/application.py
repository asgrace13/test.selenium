from selenium.webdriver.firefox.webdriver import WebDriver

from fixture.session import SessionHelper
from fixture.agreement import AgreementHelper
from fixture.registration import RegistrationHelper
import time


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.session = SessionHelper(self)
        self.agreement = AgreementHelper(self)
        self.registration = RegistrationHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://192.168.242.167:8080/")
        time.sleep(5)

    def destroy(self):
        self.wd.quit()


