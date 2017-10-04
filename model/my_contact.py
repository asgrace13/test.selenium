from sys import maxsize


class MyContact:

    def __init__(self, address=None, sales_phone=None, asc_phone=None, id=None):
        self.address = address
        self.sales_phone = sales_phone
        self.asc_phone = asc_phone
        self.id = id

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.address == other.address \
               and self.sales_phone == other.sales_phone and self.asc_phone == other.asc_phone

    def __repr__(self):
        return "%s: [адрес: %s; телефон продаж: %s; телефон асц: %s]" % (self.id, self.address, self.sales_phone, self.asc_phone)

    def id_or_max(contacts):
        if contacts.id:
            return contacts.id
        else:
            return maxsize