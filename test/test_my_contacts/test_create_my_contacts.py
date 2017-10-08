# -*- coding: utf-8 -*-
from model.my_contact import MyContact


def test_create_my_contact(app, json_my_contacts):
    my_contact = json_my_contacts
    old_my_contacts = app.my_contacts.get_my_contacts_list()
    app.my_contacts.create(my_contact)
    assert len(old_my_contacts) + 1 == app.my_contacts.count()
    new_my_contacts = app.my_contacts.get_my_contacts_list()
    old_my_contacts.append(my_contact)
    assert sorted(old_my_contacts, key=MyContact.id_or_max) == sorted(new_my_contacts, key=MyContact.id_or_max)
