# -*- coding: utf-8 -*-
import random
import string


def rus_string(prefix='', maxlen=10):
    cyrillic = u'ёйцукенгшщзхъэждлорпавыфячсмитьбюЁЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ'
    symbols = string.digits + cyrillic + ' '*3
    test = prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen)+2)])
    return test


def eng_string(prefix='', maxlen=10):
    symbols = string.digits + string.ascii_letters + ' '*3
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen)+2)])


def digits(maxlen=10):
    symbols = string.digits
    return ''.join([random.choice(symbols) for i in range(maxlen)])


def email(maxlen=10):
    mail_domains = ["hotmail.com", "gmail.com", "ya.ru", "mail.com", "mail.kz", "yahoo.com"]
    mail_name = eng_string(maxlen=maxlen).replace(' ', '')
    return '%s@%s' % (mail_name, random.choice(mail_domains))
