import time
from selenium import webdriver

from fixture.session import SessionHelper
from fixture.agreement import AgreementHelper
from fixture.registration import RegistrationHelper
from fixture.my_contacts import MyContactsHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError('Unrecognized browser %s' % browser)
        self.base_url = base_url
        self.session = SessionHelper(self)
        self.agreement = AgreementHelper(self)
        self.registration = RegistrationHelper(self)
        self.my_contacts = MyContactsHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)
        time.sleep(5)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url()
            return True
        except:
            return False

