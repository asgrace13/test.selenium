# -*- coding: utf-8 -*-
from model.my_contact import MyContact


def test_create_my_contact(app):
    app.session.login(username="tdreamkas@gmail.com", password="Qwerty12")
    app.my_contacts.create(MyContact(address='г Новосибирск, ул Таврическая, д 31', sales_phone="+7 (456) 546-45-65", asc_phone="+7 (456) 546-16-65"))
    app.session.logout()


def test_modify_address_of_first_my_contact(app):
    app.session.login(username="tdreamkas@gmail.com", password="Qwerty12")
    app.my_contacts.modify_first_contact(MyContact(address='г Новосибирск, ул Таврическая, д 33'))
    app.session.logout()


def test_modify_sales_phone_of_first_my_contact(app):
    app.session.login(username="tdreamkas@gmail.com", password="Qwerty12")
    app.my_contacts.modify_first_contact(MyContact(sales_phone="+7 (456) 546-45-65"))
    app.session.logout()


def test_delete_first_my_contact(app):
    app.session.login(username="tdreamkas@gmail.com", password="Qwerty12")
    app.my_contacts.delete_first_contact()
    app.session.logout()