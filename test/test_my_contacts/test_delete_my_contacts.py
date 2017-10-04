# -*- coding: utf-8 -*-
from random import randrange
from model.my_contact import MyContact


def test_delete_some_my_contact(app):
    if app.my_contacts.count() == 1:
        app.my_contacts.create(MyContact(sales_phone="+7 (456) 546-45-65"))
    old_my_contacts = app.my_contacts.get_my_contacts_list()
    index = randrange(len(old_my_contacts))
    app.my_contacts.delete_contact_by_index(index)
    new_my_contacts = app.my_contacts.get_my_contacts_list()
    assert len(old_my_contacts) - 1 == new_my_contacts
    old_my_contacts[index:index+1] = []
    assert old_my_contacts == new_my_contacts