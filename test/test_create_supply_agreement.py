# -*- coding: utf-8 -*-
from model.agreement import Agreement

def test_create_supply_agreement_with_ooo(app):
    app.session.login(username="tdreamkas@gmail.com", password="Qwerty12")
    app.agreement.create(Agreement(type="ООО", organization="fgdfgdg", inn="4564654649", kpp="456465464", bik="048327749",
                        correspondent_account="45646546444564654644", checking_account="45646546444564654644",
                        position="вапвап", surname="вап", name="вап", patronymic="вап", address="вапвап",
                        phone="+7 (456) 546-45-65", email="tdreamkas@gmail.com"))
    app.agreement.new_supply_should_be_create()
    app.session.logout()