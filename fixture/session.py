from selenium.webdriver.common.by import By
import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_login_page()
        wd.find_element(By.CSS_SELECTOR, "md-input-container input[name='email']").click()
        wd.find_element(By.CSS_SELECTOR, "md-input-container input[name='email']").clear()
        wd.find_element(By.CSS_SELECTOR, "md-input-container input[name='email']").send_keys(username)
        wd.find_element(By.CSS_SELECTOR, "md-input-container input[name='password']").click()
        wd.find_element(By.CSS_SELECTOR, "md-input-container input[name='password']").clear()
        wd.find_element(By.CSS_SELECTOR, "md-input-container input[name='password']").send_keys(password)
        wd.find_element(By.ID, "submit").click()
        time.sleep(7)

    def logout(self):
        wd = self.app.wd