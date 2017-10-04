import time
from selenium.webdriver.common.by import By
from model.my_contact import MyContact


class MyContactsHelper:

    def __init__(self, app):
        self.app = app

    def open_my_contact_page(self):
        time.sleep(5)
        wd = self.app.wd
        if not wd.current_url.endswith("lk/#/profile/company"):
            wd.get("http://192.168.242.167:8080/lk/#/profile/company")
            time.sleep(10)

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
        wd.find_element(By.CLASS_NAME, "dk-section-new-order__item-remove").click()
        time.sleep(1)

        # проверка удаления

    def count(self):
        wd = self.app.wd
        self.open_my_contact_page()
        return len(wd.find_elements(By.CLASS_NAME, "dk-form__group"))

    def add_new_contact(self):
        time.sleep(5)
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

    def get_my_contacts_list(self):
        wd = self.app.wd
        self.open_my_contact_page()
        my_contacts = []
        for index, element in enumerate(wd.find_elements(By.CLASS_NAME, "dk-form__group")):
            address = self.get_value_of_element(element, (By.CLASS_NAME, "address-input input"))
            sale_phone = self.get_value_of_element(element, (By.CLASS_NAME, "sales-phone-input"))
            asc_phone = self.get_value_of_element(element, (By.CLASS_NAME, "repair-phone-input"))
            my_contacts.append(MyContact(address, sale_phone, asc_phone, index))
        return my_contacts

    def get_value_of_element(self, element, locator):
        wd = self.app.wd
        attribute = element.find_element(*locator).get_attribute('name')
        return wd.execute_script('return document.getElementsByName("%s")[0].value' % attribute)
