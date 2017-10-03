from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By

from fixture.session import SessionHelper
# from fixture.agreement import AgreementHelper
import time


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.session = SessionHelper(self)
        # self.agreement = AgreementHelper(self)

    def new_supply_should_be_create(self):
        wd = self.wd
        time.sleep(5)
        wd.find_element_by_xpath("//div[@class='dk-container--lk']//span[.='Пришлите скан']").click()

    def create_new_supply(self, Agreement):
        wd = self.wd
        self.open_supply_agreement_page()
        wd.find_element(By.CSS_SELECTOR, ".dk-section-title__action .md-button").click()
        # wd.find_element(By.CLASS_NAME, "dk-lpform__legal-form-select").click()
        # select Agreement.type
        wd.find_element(By.NAME, "LegalPerson").click()
        wd.find_element(By.NAME, "LegalPerson").clear()
        wd.find_element(By.NAME, "LegalPerson").send_keys(Agreement.organization)
        wd.find_element(By.NAME, "INN").click()
        wd.find_element(By.NAME, "INN").clear()
        wd.find_element(By.NAME, "INN").send_keys(Agreement.inn)
        wd.find_element(By.NAME, "KPP").click()
        wd.find_element(By.NAME, "KPP").clear()
        wd.find_element(By.NAME, "KPP").send_keys(Agreement.kpp)
        wd.find_element(By.NAME, "BIK").click()
        wd.find_element(By.NAME, "BIK").clear()
        wd.find_element(By.NAME, "BIK").send_keys(Agreement.bik)
        wd.find_element(By.NAME, "CorrespondentAccount").click()
        wd.find_element(By.NAME, "CorrespondentAccount").clear()
        wd.find_element(By.NAME, "CorrespondentAccount").send_keys(Agreement.correspondent_account)
        wd.find_element(By.NAME, "SettlementAccount").click()
        wd.find_element(By.NAME, "SettlementAccount").clear()
        wd.find_element(By.NAME, "SettlementAccount").send_keys(Agreement.checking_account)
        wd.find_element(By.NAME, "HeadPosition").click()
        wd.find_element(By.NAME, "HeadPosition").clear()
        wd.find_element(By.NAME, "HeadPosition").send_keys(Agreement.position)
        wd.find_element(By.NAME, "HeadSecondName").click()
        wd.find_element(By.NAME, "HeadSecondName").clear()
        wd.find_element(By.NAME, "HeadSecondName").send_keys(Agreement.surname)
        wd.find_element(By.NAME, "HeadFirstName").click()
        wd.find_element(By.NAME, "HeadFirstName").clear()
        wd.find_element(By.NAME, "HeadFirstName").send_keys(Agreement.name)
        wd.find_element(By.NAME, "HeadMiddleName").click()
        wd.find_element(By.NAME, "HeadMiddleName").clear()
        wd.find_element(By.NAME, "HeadMiddleName").send_keys(Agreement.patronymic)
        wd.find_element(By.NAME, "LegalAddress").click()
        wd.find_element(By.NAME, "LegalAddress").clear()
        wd.find_element(By.NAME, "LegalAddress").send_keys(Agreement.address)
        wd.find_element(By.NAME, "Phone").click()
        wd.find_element(By.NAME, "Phone").clear()
        wd.find_element(By.NAME, "Phone").send_keys(Agreement.phone)
        wd.find_element(By.NAME, "Email").click()
        wd.find_element(By.NAME, "Email").clear()
        wd.find_element(By.NAME, "Email").send_keys(Agreement.email)
        wd.find_element(By.ID, "submit").click()
        time.sleep(10)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://192.168.242.167:8080/")
        time.sleep(5)

    def open_login_page(self):
        wd = self.wd
        wd.get("http://192.168.242.167:8080/lk/#/login/")
        time.sleep(5)

    def open_supply_agreement_page(self):
        wd = self.wd
        time.sleep(5)
        wd.get("http://192.168.242.167:8080/lk/#/contracts/supplyAgreement")
        time.sleep(5)

    def destroy(self):
        self.wd.quit()


