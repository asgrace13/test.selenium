# -*- coding: utf-8 -*-
from random import randrange
from model.my_contact import MyContact


def test_modify_address_of_first_my_contact(app):
    if app.my_contacts.count() == 1:
        app.my_contacts.create(MyContact(sales_phone="+7 (456) 546-45-65"))
    old_my_contacts = app.my_contacts.get_my_contacts_list()
    index = randrange(len(old_my_contacts))
    contacts = MyContact(address='г Новосибирск, ул Таврическая, д 33')
    contacts.id = old_my_contacts[index].id
    app.my_contacts.modify_contact_by_index(index, contacts)
    assert len(old_my_contacts) == app.my_contacts.count()
    new_my_contacts = app.my_contacts.get_my_contacts_list()
    old_my_contacts[index] = contacts
    assert sorted(old_my_contacts, key=MyContact.id_or_max) == sorted(new_my_contacts, key=MyContact.id_or_max)


def test_modify_sales_phone_of_first_my_contact(app):
    old_my_contacts = app.my_contacts.get_my_contacts_list()
    index = randrange(len(old_my_contacts))
    contacts = MyContact(sales_phone="+7 (456) 546-45-65")
    contacts.id = old_my_contacts[index].id
    app.my_contacts.modify_contact_by_index(index, contacts)
    assert len(old_my_contacts) == app.my_contacts.count()
    new_my_contacts = app.my_contacts.get_my_contacts_list()
    old_my_contacts[index] = contacts
    assert sorted(old_my_contacts, key=MyContact.id_or_max) == sorted(new_my_contacts, key=MyContact.id_or_max)