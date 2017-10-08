# -*- coding: utf-8 -*-
import os.path
import jsonpickle

from data.generator import data_random
from model.agreement import Agreement

test_data = [
        Agreement(type=type, organization=data_random.rus_string(maxlen=10), inn=data_random.digits(10),
                  kpp=data_random.digits(9), bik="048327749", correspondent_account=data_random.digits(20),
                  checking_account=data_random.digits(20), position=data_random.rus_string(maxlen=10),
                  surname=data_random.rus_string(maxlen=10), name=data_random.rus_string(maxlen=10),
                  patronymic=data_random.rus_string(maxlen=10), address=data_random.rus_string(maxlen=20),
                  phone=data_random.digits(10), email=data_random.email(10))
        for type in ["ООО", "ОАО", "ЗАО"]
        ] + [Agreement(type="ИП", organization=data_random.rus_string(maxlen=10), inn=data_random.digits(10),
                       kpp=data_random.digits(9), bik="048327749", correspondent_account=data_random.digits(20),
                       checking_account=data_random.digits(20), position=data_random.rus_string(maxlen=10),
                       surname=data_random.rus_string(maxlen=10), name=data_random.rus_string(maxlen=10),
                       patronymic=data_random.rus_string(maxlen=10), address=data_random.rus_string(maxlen=20),
                       phone=data_random.digits(10), email=data_random.email(10))
        ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../agreements.json")
#
# with open(file, "w") as f:
#     f.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))