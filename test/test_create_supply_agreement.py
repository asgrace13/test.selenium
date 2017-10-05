# -*- coding: utf-8 -*-
import pytest
import random
import string
from model.agreement import Agreement


def random_rus_string(prefix='', maxlen=10):
    cyrillic = u'ёйцукенгшщзхъэждлорпавыфячсмитьбюЁЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ'
    symbols = string.digits + cyrillic + ' '*5
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_eng_string(prefix='', maxlen=10):
    symbols = string.digits + string.ascii_letters + ' '*5
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_digits(maxlen=10):
    symbols = string.digits
    return ''.join(random.choice([symbols for i in range(maxlen)]))


def random_email(maxlen=10):
    mail_domains = ["hotmail.com", "gmail.com", "ya.ru", "mail.com", "mail.kz", "yahoo.com"]
    mail_name = random_eng_string(maxlen=maxlen)
    return '%s@%s' % (mail_name, random.choice(mail_domains))


organization_type = ["ООО", "ОАО", "ЗАО", "ИП"]
len_type = len(organization_type)

test_data = [
        Agreement(type=type, organization=organization, inn=inn, kpp=random_digits(9), bik=bik,
            correspondent_account=account, checking_account=account, position=text,
            surname=text, name=text, patronymic=text, address=address, phone=phone, email=email)
        for type in organization_type
        for organization in [random_rus_string(maxlen=10)]*len_type
        for inn in [random_digits(10)]*(len_type-1)+ [random_digits(12)]
        for account in [random_digits(20)]*len_type
        for bik in ["048327749"]*len_type
        for text in [random_rus_string(maxlen=10)]*len_type
        for address in [random_rus_string(maxlen=20)]*len_type
        for phone in [random_digits(10)]*len_type
        for email in [random_email(10)]*len_type
]


@pytest.mark.parametrize('data_agreement', test_data, ids=[repr(x) for x in test_data])
def test_create_supply_agreement(app):
    app.agreement.create(data_agreement)