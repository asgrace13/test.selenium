# -*- coding: utf-8 -*-
from model.my_contact import MyContact


def test_modify_address_of_first_my_contact(app):
    old_my_contacts = app.my_contacts.get_my_contacts_list()
    app.my_contacts.modify_first_contact(MyContact(address='г Новосибирск, ул Таврическая, д 33'))
    new_my_contacts = app.my_contacts.get_my_contacts_list()
    assert len(old_my_contacts) == new_my_contacts


def test_modify_sales_phone_of_first_my_contact(app):
    old_my_contacts = app.my_contacts.get_my_contacts_list()
    app.my_contacts.modify_first_contact(MyContact(sales_phone="+7 (456) 546-45-65"))
    new_my_contacts = app.my_contacts.get_my_contacts_list()
    assert len(old_my_contacts) == new_my_contacts