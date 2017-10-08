import time
from selenium.webdriver.common.by import By


class RegistrationHelper:

    def __init__(self, app):
        self.app = app

    def open_registration_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/lk/#/registration/"):
            wd.get(self.app.base_url + "/lk/#/registration/")
            self.app.wait_for_page_load()

    def create(self, Registration):
        wd = self.app.wd
        self.open_registration_page()
        self.fill_registration_form(Registration)
        # проверка создания
        self.app.should_be_open_page(self.app.base_url + "/registration-success/")

    def fill_registration_form(self, Registration):
        email_locator = (By.NAME, "email")
        self.app.change_field_value(locator=email_locator, text=Registration.email)
        surname_locator = (By.NAME, "last_name")
        self.app.change_field_value(locator=surname_locator, text=Registration.surname)
        name_locator = (By.NAME, "first_name")
        self.app.change_field_value(locator=name_locator, text=Registration.name)
        patronymic_locator = (By.NAME, "patronymic_name")
        self.app.change_field_value(locator=patronymic_locator, text=Registration.patronymic)
        position_locator = (By.NAME, "position")
        self.app.change_field_value(locator=position_locator, text=Registration.position)
        phone_locator = (By.NAME, "phone")
        self.app.change_field_value(locator=phone_locator, text=Registration.phone)
        company_locator = (By.NAME, "CompanyName")
        self.app.change_field_value(locator=company_locator, text=Registration.company)
        city_locator = (By.NAME, "CompanyCity")
        self.app.change_field_value(locator=city_locator, text=Registration.city)
        site_locator = (By.NAME, "CompanySite")
        self.app.change_field_value(locator=site_locator, text=Registration.site)
        technician_locator = (By.NAME, "CompanySpecialistsCount")
        self.app.change_field_value(locator=technician_locator, text=Registration.technician)
        manager_locator = (By.NAME, "CompanyManagersCount")
        self.app.change_field_value(locator=manager_locator, text=Registration.manager)
        self.app.element_is_clickable(By.ID, "submit").click()