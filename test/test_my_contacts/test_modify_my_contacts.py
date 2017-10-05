# -*- coding: utf-8 -*-
from random import randrange
import pytest
import random
import string
from model.my_contact import MyContact


def random_digits(maxlen=10):
    symbols = string.digits
    return ''.join(random.choice([symbols for i in range(maxlen)]))


test_data = [
    MyContact(address=address, sales_phone=sales_phone, asc_phone=asc_phone)
    for address in ['г Новосибирск, ул Таврическая, д 33', '', '']
    for sales_phone in ['', random_digits(10), '']
    for asc_phone in ['', '', random_digits(10)]
]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_modify_my_contact(app):
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
