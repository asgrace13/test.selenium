import time
import re
from urllib import parse
from selenium import webdriver
from contextlib import contextmanager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from fixture.session import SessionHelper
from fixture.agreement import AgreementHelper
from fixture.registration import RegistrationHelper
from fixture.my_contacts import MyContactsHelper


def timeout_waiting(timeout=5):
    def decorator(function_to_decorate):
        def wrapper(self, *args):
            iteration = 0
            POLL = 0.5
            while iteration < timeout // POLL:
                try:
                    return function_to_decorate(self, *args)
                except:
                    iteration += 1
                time.sleep(POLL)
            return function_to_decorate(self, *args)
        return wrapper
    return decorator


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

    @contextmanager
    def wait_for_page_load(self, timeout=30):
        wd = self.wd
        old_page = wd.find_element_by_tag_name('html')
        yield
        WebDriverWait(wd, timeout).until(
            staleness_of(old_page)
        )

    @timeout_waiting(20)
    def should_be_open_page(self, *expect_url):
        self.wait_for_page_load()
        expect_urls = [self.regulation_url(url) for url in expect_url]
        current_url = self.regulation_url(parse.unquote(self.wd.current_url))
        assert current_url in expect_urls

    def regulation_url(self, url):
        return ''.join(re.findall('(.+?)\/?$', url))

    def refresh_page(self):
        self.wd.refresh()
        self.wait_for_page_load()

    def get_element(self, element, timeout=20):
        return WebDriverWait(self.wd, timeout).until(lambda driver: driver.find_element(*element))

    def get_elements(self, element, timeout=20):
        return WebDriverWait(self.wd, timeout).until(lambda driver: driver.find_elements(*element))

    def element_is_displayed(self, element, timeout=20):
        wait = WebDriverWait(self.wd, timeout)
        if type(element) is tuple:
            element = wait.until(EC.visibility_of_element_located(element))
        else:
            element = wait.until(EC.visibility_of(element))
        return element

    def element_is_clickable(self, element, timeout=20):
        return WebDriverWait(self.wd, timeout).until(EC.element_to_be_clickable(element))

    def element_is_hidden(self, element, timeout=20):
        return WebDriverWait(self.wd, timeout).until(EC.invisibility_of_element_located(element))

    def text_to_be_present_in_element(self, element, text, timeout=20):
        return WebDriverWait(self.wd, timeout).until(EC.text_to_be_present_in_element(element, text))

    def scroll_to_displayed_element_and_click(self, element):
        element = self.element_is_displayed(element)
        try:
            element.click()
            print('element is visible without scroll')
        except:
            self.wd.execute_script("arguments[0].scrollIntoView();", element)
            print('scroll to element')
            element = WebDriverWait(self.wd, 5).until(EC.visibility_of(element))
            element.click()
        return element

    def js_delete_local_storage_by_key(self, item):
        self.wd.execute_script("window.localStorage.setItem('%s','%s');" % (item, {}))

    def change_field_value(self, locator, text, index=0):
        if text is not None:
            element = self.get_elements(*locator)[index]
            element.click()
            element.clear()
            element.send_keys(text)

    def get_value_of_element(self, element, locator):
        wd = self.wd
        attribute = element.find_element(*locator).get_attribute('name')
        return wd.execute_script('return document.getElementsByName("%s")[0].value' % attribute)

    def click_on_the_checkbox(self, locator):
        element = self.element_is_displayed(locator)
        ActionChains(self.wd).move_to_element(element).perform()
