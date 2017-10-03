import time
import logging
from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app
        self.sessions = {}

    def open_login_page(self):
        wd = self.app.wd
        wd.get("http://192.168.242.167:8080/lk/#/login/")
        time.sleep(5)

    def login(self, email, password):
        wd = self.app.wd
        self.open_login_page()
        wd.find_element(By.CSS_SELECTOR, "md-input-container input[name='email']").click()
        wd.find_element(By.CSS_SELECTOR, "md-input-container input[name='email']").clear()
        wd.find_element(By.CSS_SELECTOR, "md-input-container input[name='email']").send_keys(email)
        wd.find_element(By.CSS_SELECTOR, "md-input-container input[name='password']").click()
        wd.find_element(By.CSS_SELECTOR, "md-input-container input[name='password']").clear()
        wd.find_element(By.CSS_SELECTOR, "md-input-container input[name='password']").send_keys(password)
        wd.find_element(By.ID, "submit").click()
        time.sleep(7)
        # проверка входа

    def ensure_login(self, email, password):
        if self.is_logged_in():
            if self.is_logged_in_as(email):
                return
            else:
                self.logout()
        self.login_as(email, password)

    def login_as(self, email, password):
        self.login(email, password)
        # if not self.ensure_set_session_cookie(email):
        #     self.login(email, password)
        #     self.get_session_cookie(email)

    def logout(self):
        wd = self.app.wd
        wd.delete_all_cookies()
        wd.refresh()
        time.sleep(5)

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
        wd.refresh()
        return True

    def get_session_cookie(self, email):
        wd = self.app.wd
        if email not in self.sessions.keys():
            self.sessions[email] = wd.get_cookie('app')