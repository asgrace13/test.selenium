# -*- coding: utf-8 -*-
import os.path
import jsonpickle
from generator import random_data
from model.agreement import Agreement

test_data = [
        Agreement(type=type, organization=random_data.rus_string(maxlen=10), inn=random_data.digits(10),
                  kpp=random_data.digits(9), bik="048327749", correspondent_account=random_data.digits(20),
                  checking_account=random_data.digits(20), position=random_data.rus_string(maxlen=10),
                  surname=random_data.rus_string(maxlen=10), name=random_data.rus_string(maxlen=10),
                  patronymic=random_data.rus_string(maxlen=10), address=random_data.rus_string(maxlen=20),
                  phone=random_data.digits(10), email=random_data.email(10))
        for type in ["ООО", "ОАО", "ЗАО"]
        ] + [Agreement(type="ИП", organization=random_data.rus_string(maxlen=10), inn=random_data.digits(10),
                       kpp=random_data.digits(9), bik="048327749", correspondent_account=random_data.digits(20),
                       checking_account=random_data.digits(20), position=random_data.rus_string(maxlen=10),
                       surname=random_data.rus_string(maxlen=10), name=random_data.rus_string(maxlen=10),
                       patronymic=random_data.rus_string(maxlen=10), address=random_data.rus_string(maxlen=20),
                       phone=random_data.digits(10), email=random_data.email(10))
        ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/agreements.json")

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))
