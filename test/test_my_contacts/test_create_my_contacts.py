# -*- coding: utf-8 -*-
from model.my_contact import MyContact


def test_create_my_contact_with_address_and_sales_phone_and_asc_phone(app):
    old_my_contacts = app.my_contacts.get_my_contacts_list()
    contacts = MyContact(address='г Новосибирск, ул Таврическая, д 31', sales_phone="+7 (456) 546-45-65", asc_phone="+7 (456) 546-16-65")
    app.my_contacts.create(contacts)
    new_my_contacts = app.my_contacts.get_my_contacts_list()
    assert len(old_my_contacts) + 1 == new_my_contacts
    old_my_contacts.append(contacts)
    assert sorted(old_my_contacts, key=MyContact.id_or_max) == sorted(new_my_contacts, key=MyContact.id_or_max)


def test_create_my_contact_with_address(app):
    old_my_contacts = app.my_contacts.get_my_contacts_list()
    contacts = MyContact(address='г Новосибирск, ул Таврическая, д 31')
    app.my_contacts.create(contacts)
    new_my_contacts = app.my_contacts.get_my_contacts_list()
    assert len(old_my_contacts) + 1 == new_my_contacts
    old_my_contacts.append(contacts)
    assert sorted(old_my_contacts, key=MyContact.id_or_max) == sorted(new_my_contacts, key=MyContact.id_or_max)


def test_create_my_contact_with_asc_phone(app):
    old_my_contacts = app.my_contacts.get_my_contacts_list()
    contacts = MyContact(asc_phone="+7 (456) 546-16-65")
    app.my_contacts.create(contacts)
    new_my_contacts = app.my_contacts.get_my_contacts_list()
    assert len(old_my_contacts) + 1 == new_my_contacts
    old_my_contacts.append(contacts)
    assert sorted(old_my_contacts, key=MyContact.id_or_max) == sorted(new_my_contacts, key=MyContact.id_or_max)