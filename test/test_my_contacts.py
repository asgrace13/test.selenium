# -*- coding: utf-8 -*-
from model.my_contact import MyContact


def test_create_my_contact(app):
    app.my_contacts.create(MyContact(address='г Новосибирск, ул Таврическая, д 31', sales_phone="+7 (456) 546-45-65", asc_phone="+7 (456) 546-16-65"))


def test_modify_address_of_first_my_contact(app):
    app.my_contacts.modify_first_contact(MyContact(address='г Новосибирск, ул Таврическая, д 33'))


def test_modify_sales_phone_of_first_my_contact(app):
    app.my_contacts.modify_first_contact(MyContact(sales_phone="+7 (456) 546-45-65"))


def test_delete_first_my_contact(app):
    if app.my_contacts.count() == 0:
        app.my_contacts.create(MyContact(sales_phone="+7 (456) 546-45-65"))
    app.my_contacts.delete_first_contact()
