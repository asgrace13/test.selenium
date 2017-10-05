
class Agreement:

    def __init__(self, type=None, organization=None, inn=None, kpp=None, bik=None, correspondent_account=None,
                 checking_account=None, position=None, surname=None, name=None, patronymic=None, address=None,
                 phone=None, email=None):
        self.type = type
        self.organization = organization
        self.inn = inn
        self.kpp = kpp
        self.bik = bik
        self.correspondent_account = correspondent_account
        self.checking_account = checking_account
        self.position = position
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.address = address
        self.phone = phone
        self.email = email

    def __repr__(self):
        return u"тип: %s; наименование: %s; инн: %s; кпп: %s; бик: %s; корр.счет: %s; ак.счет: %s;" \
               u" должность: %s; фамилия: %s; имя: %s; отчетсво: %s; адрес: %s; телефон: %s; почта: %s]" \
               % (self.type, self.organization, self.inn, self.kpp, self.bik, self.correspondent_account,
                  self.checking_account, self.position, self.surname, self.name, self.patronymic,
                  self.address, self.phone, self.email)