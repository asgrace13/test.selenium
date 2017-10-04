# -*- coding: utf-8 -*-
from model.my_contact import MyContact


def test_create_my_contact(app):
    app.my_contacts.create(MyContact(address='г Новосибирск, ул Таврическая, д 31', sales_phone="+7 (456) 546-45-65", asc_phone="+7 (456) 546-16-65"))