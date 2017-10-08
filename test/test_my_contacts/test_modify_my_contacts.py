# -*- coding: utf-8 -*-
from random import randrange
from model.my_contact import MyContact


def test_modify_my_contact(app, json_my_contacts):
    my_contact =json_my_contacts
    if app.my_contacts.count() == 1:
        app.my_contacts.create(MyContact(sales_phone="+7 (456) 546-45-65"))
    old_my_contacts = app.my_contacts.get_my_contacts_list()
    index = randrange(len(old_my_contacts))
    my_contact.id = old_my_contacts[index].id
    app.my_contacts.modify_contact_by_index(index, my_contact)
    assert len(old_my_contacts) == app.my_contacts.count()
    new_my_contacts = app.my_contacts.get_my_contacts_list()
    old_my_contacts[index] = my_contact
    assert sorted(old_my_contacts, key=MyContact.id_or_max) == sorted(new_my_contacts, key=MyContact.id_or_max)
