import time
import logging
from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app
        self.sessions = {}
        self.base_url = app.base_url

        server_message = (By.CSS_SELECTOR, "[ng-message='server']")
        registration_button = (By.CSS_SELECTOR, "[ui-sref='registration']")
        lostPassword_button = (By.CSS_SELECTOR, "[ui-sref='lostPassword']")

    def open_login_page(self):
        wd = self.app.wd
        wd.get(self.base_url + "/lk/#/login/")
        self.app.wait_for_page_load()

    def login(self, email, password):
        self.open_login_page()
        self.fill_login_form(email, password)
        # проверка входа
        expect_urls = map(lambda x: self.base_url + x, ['/partnerProgram', '/contracts/supplyAgreement', '/orders'])
        self.app.should_be_open_page(*expect_urls)

    def fill_login_form(self, email, password):
        email_locator = (By.CSS_SELECTOR, "md-input-container input[name='email']")
        self.app.change_field_value(locator=email_locator, text=email)
        password_locator = (By.CSS_SELECTOR, "md-input-container input[name='password']")
        self.app.change_field_value(locator=password_locator, text=password)
        self.app.element_is_clickable(By.ID, "submit").click()

    def ensure_login(self, email, password):
        if self.is_logged_in():
            if self.is_logged_in_as(email):
                return
            else:
                self.logout()
        self.login_as(email, password)

    def login_as(self, email, password):
        if not self.ensure_set_session_cookie(email):
            self.login(email, password)
            self.get_session_cookie(email)

    def logout(self):
        self.delete_all_cookies()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        if wd.get_cookie('app') == None:
            return False
        return True

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.execute_script("return window.DK.me.email") == username

    def ensure_set_session_cookie(self, email):
        logging.info('All saved session cookie %s' % self.sessions)
        if email not in self.sessions.keys():
            return False
        wd = self.app.wd
        wd.delete_cookie('app')
        wd.add_cookie(self.sessions[email])
        self.app.refresh_page()
        return True

    def get_session_cookie(self, email):
        wd = self.app.wd
        if email not in self.sessions.keys():
            self.sessions[email] = wd.get_cookie('app')

    def delete_all_cookies(self):
        self.app.wd.delete_all_cookies()
        self.app.refresh_page()