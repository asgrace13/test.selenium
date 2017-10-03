from selenium.webdriver.common.by import By
import time


class MyContactsHelper:

    def __init__(self, app):
        self.app = app

    def open_my_contact_page(self):
        wd = self.app.wd
        time.sleep(5)
        wd.get("http://192.168.242.167:8080/lk/#/contracts/supplyAgreement")
        time.sleep(5)

    def create(self, MyContact):
        self.open_my_contact_page()
        self.add_new_contact()
        self.fill_contact_form(MyContact)
        self.save_contacts()
        time.sleep(5)
        # проверка создания

    def modify_first_contact(self, MyContact):
        self.open_my_contact_page()
        self.fill_contact_form(MyContact)
        self.save_contacts()
        time.sleep(5)
        # проверка создания

    def save_contacts(self):
        wd = self.app.wd
        wd.find_element(By.ID, "submit").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_my_contact_page()
        wd.find_element(By.ID, "submit").click()
        time.sleep(1)
        # проверка удаления

    def add_new_contact(self):
        wd = self.app.wd
        wd.find_element(By.CLASS_NAME, "dk-section-notifications__add-phone").click()
        time.sleep(1)

    def fill_contact_form(self, MyContact):
        self.change_field_value((By.CSS_SELECTOR, ".address-input input"), MyContact.address)
        self.change_field_value((By.CLASS_NAME, "sales-phone-input"), MyContact.sales_phone)
        self.change_field_value((By.CLASS_NAME, "repair-phone-input"), MyContact.asc_phone)

    def change_field_value(self, locator, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(*locator).click()
            wd.find_element(*locator).clear()
            wd.find_element(*locator).send_keys(text)