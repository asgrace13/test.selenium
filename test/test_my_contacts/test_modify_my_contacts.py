# -*- coding: utf-8 -*-
from model.my_contact import MyContact


def test_modify_address_of_first_my_contact(app):
    old_my_contacts = app.my_contacts.get_my_contacts_list()
    contacts = MyContact(address='г Новосибирск, ул Таврическая, д 33')
    contacts.id = old_my_contacts[0].id
    app.my_contacts.modify_first_contact(contacts)
    new_my_contacts = app.my_contacts.get_my_contacts_list()
    assert len(old_my_contacts) == new_my_contacts
    old_my_contacts[0] = contacts
    assert sorted(old_my_contacts, key=MyContact.id_or_max) == sorted(new_my_contacts, key=MyContact.id_or_max)


def test_modify_sales_phone_of_first_my_contact(app):
    old_my_contacts = app.my_contacts.get_my_contacts_list()
    contacts = MyContact(sales_phone="+7 (456) 546-45-65")
    contacts.id = old_my_contacts[0].id
    app.my_contacts.modify_first_contact(contacts)
    new_my_contacts = app.my_contacts.get_my_contacts_list()
    assert len(old_my_contacts) == new_my_contacts
    old_my_contacts[0] = contacts
    assert sorted(old_my_contacts, key=MyContact.id_or_max) == sorted(new_my_contacts, key=MyContact.id_or_max)