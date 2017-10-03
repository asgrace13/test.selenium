# -*- coding: utf-8 -*-
import pytest
from model.agreement import Agreement
from fixture.application import Application

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_create_supply_agreement_with_ooo(app):
    app.session.login(username="tdreamkas@gmail.com", password="Qwerty12")
    app.create_new_supply(Agreement(type="ООО", organization="fgdfgdg", inn="4564654649", kpp="456465464", bik="048327749",
                           correspondent_account="45646546444564654644", checking_account="45646546444564654644",
                           position="вапвап", surname="вап", name="вап", patronymic="вап", address="вапвап",
                           phone="+7 (456) 546-45-65", email="tdreamkas@gmail.com"))
    app.new_supply_should_be_create()
    app.session.logout()

# def test_create_supply_agreement_with_zao(app):
#     app.session.login(username="tdreamkas@gmail.com", password="Qwerty12")
#     app.open_tab_supply()
#     app.create_new_supply(Agreement(type="ЗАО", organization="fgdfgdg", inn="456465464456546", kpp="4564654644", bik="4564654644",
#                            correspondent_account="45646546444564654644", checking_account="45646546444564654644",
#                            position="вапвап", surname="вап", name="вап", patronymic="вап", address="вапвап",
#                            phone="+7 (456) 546-45-65", email="tdreamkas@gmail.com"))
#     app.new_supply_should_be_create()
#     app.session.logout()