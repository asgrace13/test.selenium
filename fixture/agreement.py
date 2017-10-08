from selenium.webdriver.common.by import By
import time


class AgreementHelper:

    def __init__(self, app):
        self.app = app

    def open_supply_agreement_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("lk/#/contracts/supplyAgreement"):
            wd.get(self.app.base_url + "/lk/#/contracts/supplyAgreement")
            self.app.wait_for_page_load()

    def create(self, Agreement):
        wd = self.app.wd
        self.open_supply_agreement_page()
        self.add_new_supply_agreement()
        self.fill_agreement_form(Agreement)
        # проверка создания
        self.app.element_is_hidden((By.NAME, "LegalPerson"), timeout=30)
        

    def fill_agreement_form(self, Agreement):
        # wd.find_element(By.CLASS_NAME, "dk-lpform__legal-form-select").click()
        # select Agreement.type
        organization_locator = (By.NAME, "LegalPerson")
        self.app.change_field_value(locator=organization_locator, text=Agreement.organization)
        inn_locator = (By.NAME, "INN")
        self.app.change_field_value(locator=inn_locator, text=Agreement.inn)
        kpp_locator = (By.NAME, "KPP")
        self.app.change_field_value(locator=kpp_locator, text=Agreement.kpp)
        bik_locator = (By.NAME, "BIK")
        self.app.change_field_value(locator=bik_locator, text=Agreement.bik)
        correspondent_account_locator = (By.NAME, "CorrespondentAccount")
        self.app.change_field_value(locator=correspondent_account_locator, text=Agreement.correspondent_account)
        checking_account_locator = (By.NAME, "SettlementAccount")
        self.app.change_field_value(locator=checking_account_locator, text=Agreement.checking_account)
        position_locator = (By.NAME, "HeadPosition")
        self.app.change_field_value(locator=position_locator, text=Agreement.position)
        surname_locator = (By.NAME, "HeadSecondName")
        self.app.change_field_value(locator=surname_locator, text=Agreement.surname)
        name_locator = (By.NAME, "HeadFirstName")
        self.app.change_field_value(locator=name_locator, text=Agreement.name)
        patronymic_locator = (By.NAME, "HeadMiddleName")
        self.app.change_field_value(locator=patronymic_locator, text=Agreement.patronymic)
        address_locator = (By.NAME, "LegalAddress")
        self.app.change_field_value(locator=address_locator, text=Agreement.address)
        phone_locator = (By.NAME, "Phone")
        self.app.change_field_value(locator=phone_locator, text=Agreement.phone)
        email_locator = (By.NAME, "Email")
        self.app.change_field_value(locator=email_locator, text=Agreement.email)
        self.app.element_is_clickable(By.ID, "submit").click()


    def change_field_value(self, locator, text):
        wd = self.app.wd
        wd.find_element(*locator).click()
        wd.find_element(*locator).send_keys(text)


    def add_new_supply_agreement(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("lk/#/contracts/supplyAgreement") and len(wd.find_elements(By.NAME, "LegalPerson")) < 1):
            wd.find_element(By.CSS_SELECTOR, ".dk-section-title__action .md-button").click()
            time.sleep(2)

    def new_supply_should_be_create(self):
        wd = self.app.wd
        time.sleep(5)
        wd.find_element_by_xpath("//div[@class='dk-container--lk']//span[.='Пришлите скан']").click()

