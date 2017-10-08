import time
from selenium.webdriver.common.by import By
from model.my_contact import MyContact


class MyContactsHelper:

    def __init__(self, app):
        self.app = app

    my_contacts_cache = None

    def open_my_contact_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("lk/#/profile/company"):
            wd.get(self.app.base_url + "/lk/#/profile/company")
            self.app.wait_for_page_load()
        # wheel = (By.NAME, "wheel")
        # if len(wd.find_elements(*wheel) > 0):
        #     self.app.element_is_hidden(wheel)

    def create(self, MyContact):
        self.open_my_contact_page()
        self.add_new_contact()
        self.fill_contact_form_by_index(MyContact, self.count() - 1)
        self.save_contacts()
        self.my_contacts_cache = None

    def modify_contact_by_index(self, index, MyContact):
        self.open_my_contact_page()
        self.fill_contact_form_by_index(MyContact, index)
        self.save_contacts()
        self.my_contacts_cache = None

    def modify_first_contact(self, MyContact):
        self.modify_contact_by_index(0, MyContact)

    def save_contacts(self):
        wd = self.app.wd
        wd.find_element(By.ID, "submit").click()
        # проверка сохранения

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_my_contact_page()
        self.app.element_is_clickable(By.CLASS_NAME, "dk-section-new-order__item-remove")[index].click()
        # проверка удаления
        self.my_contacts_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def count(self):
        wd = self.app.wd
        self.open_my_contact_page()
        return len(wd.find_elements(By.CLASS_NAME, "dk-form__group"))

    def add_new_contact(self):
        self.app.element_is_clickable(By.CLASS_NAME, "dk-section-notifications__add-phone").click()
        time.sleep(1)

    def fill_contact_form_by_index(self, MyContact, index=0):
        self.app.change_field_value(locator=(By.CSS_SELECTOR, ".address-input input"), text=MyContact.address, index=index)
        self.app.change_field_value(locator=(By.CLASS_NAME, "sales-phone-input"), text=MyContact.sales_phone, index=index)
        self.app.change_field_value(locator=(By.CLASS_NAME, "repair-phone-input"), text=MyContact.asc_phone, index=index)

    def get_my_contacts_list(self):
        if self.my_contacts_cache is None:
            wd = self.app.wd
            self.open_my_contact_page()
            self.my_contacts_cache = []
            for index, element in enumerate(wd.find_elements(By.CLASS_NAME, "dk-form__group")):
                address = self.app.get_value_of_element(element, (By.CLASS_NAME, "address-input input"))
                sale_phone = self.app.get_value_of_element(element, (By.CLASS_NAME, "sales-phone-input"))
                asc_phone = self.app.get_value_of_element(element, (By.CLASS_NAME, "repair-phone-input"))
                self.my_contacts_cache.append(MyContact(address, sale_phone, asc_phone, index))
        return list(self.my_contacts_cache)

