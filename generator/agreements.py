# -*- coding: utf-8 -*-
from generator import random_helper
from model.agreement import Agreement
from generator.json_helper import json_write

test_data = [
        Agreement(type=type, organization=random_helper.rus_string(maxlen=10), inn=random_helper.digits(10),
                  kpp=random_helper.digits(9), bik="048327749", correspondent_account=random_helper.digits(20),
                  checking_account=random_helper.digits(20), position=random_helper.rus_string(maxlen=10),
                  surname=random_helper.rus_string(maxlen=10), name=random_helper.rus_string(maxlen=10),
                  patronymic=random_helper.rus_string(maxlen=10), address=random_helper.rus_string(maxlen=20),
                  phone=random_helper.digits(10), email=random_helper.email(10))
        for type in ["ООО", "ОАО", "ЗАО"]
        ] + [Agreement(type="ИП", organization=random_helper.rus_string(maxlen=10), inn=random_helper.digits(10),
                       kpp=random_helper.digits(9), bik="048327749", correspondent_account=random_helper.digits(20),
                       checking_account=random_helper.digits(20), position=random_helper.rus_string(maxlen=10),
                       surname=random_helper.rus_string(maxlen=10), name=random_helper.rus_string(maxlen=10),
                       patronymic=random_helper.rus_string(maxlen=10), address=random_helper.rus_string(maxlen=20),
                       phone=random_helper.digits(10), email=random_helper.email(10))
        ]

json_write(test_data, "agreements")

