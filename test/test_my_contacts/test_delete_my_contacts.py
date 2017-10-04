# -*- coding: utf-8 -*-
from model.my_contact import MyContact


def test_delete_first_my_contact(app):
    if app.my_contacts.count() == 0:
        app.my_contacts.create(MyContact(sales_phone="+7 (456) 546-45-65"))
    app.my_contacts.delete_first_contact()
