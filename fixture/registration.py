import time
from selenium.webdriver.common.by import By


class RegistrationHelper:

    def __init__(self, app):
        self.app = app

    def open_registration_page(self):
        wd = self.app.wd
        wd.get("http://192.168.242.167:8080/lk/#/registration/")
        time.sleep(5)

    def create(self, Registration):
        wd = self.app.wd
        self.open_registration_page()
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").send_keys(Registration.email)
        wd.find_element(By.NAME, "last_name").click()
        wd.find_element(By.NAME, "last_name").send_keys(Registration.surname)
        wd.find_element(By.NAME, "first_name").click()
        wd.find_element(By.NAME, "first_name").send_keys(Registration.name)
        wd.find_element(By.NAME, "patronymic_name").click()
        wd.find_element(By.NAME, "patronymic_name").send_keys(Registration.patronymic)
        wd.find_element(By.NAME, "position").click()
        wd.find_element(By.NAME, "position").send_keys(Registration.position)
        wd.find_element(By.NAME, "phone").click()
        wd.find_element(By.NAME, "phone").send_keys(Registration.phone)
        wd.find_element(By.NAME, "CompanyName").click()
        wd.find_element(By.NAME, "CompanyName").send_keys(Registration.company)
        wd.find_element(By.NAME, "CompanyCity").click()
        wd.find_element(By.NAME, "CompanyCity").send_keys(Registration.city)
        wd.find_element(By.NAME, "CompanySite").click()
        wd.find_element(By.NAME, "CompanySite").send_keys(Registration.site)
        wd.find_element(By.NAME, "CompanySpecialistsCount").click()
        wd.find_element(By.NAME, "CompanySpecialistsCount").send_keys(Registration.technician)
        wd.find_element(By.NAME, "CompanyManagersCount").click()
        wd.find_element(By.NAME, "CompanyManagersCount").send_keys(Registration.manager)
        wd.find_element(By.ID, "submit").click()
        time.sleep(5)
        # проверка создания