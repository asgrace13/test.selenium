# -*- coding: utf-8 -*-
from model.registration import Registration


def test_registration(app):
    app.session.logout()
    app.registration.create(Registration(email='tdreamkas@mail.ru', surname='Попов', name='Аркадий',
                                                patronymic='Вадимович', position='Директор', phone='7654324343',
                                                company='Ромашка', city='Спб', site='нет', technician='3', manager='5'))