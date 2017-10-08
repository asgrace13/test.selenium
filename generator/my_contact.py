from generator import random_helper
from generator.json_helper import json_write
from model.my_contact import MyContact


test_data = [
    MyContact(address='г Новосибирск, ул Таврическая, д 33', sales_phone=random_helper.digits(10), asc_phone=random_helper.digits(10)),
    MyContact(address='г Новосибирск, ул Таврическая, д 33'),
    MyContact(sales_phone=random_helper.digits(10)),
    MyContact(asc_phone=random_helper.digits(10))
]

json_write(test_data, "my_contacts")