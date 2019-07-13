from model.contact import Contact
import random
import string


constant = [
    Contact(firstname="firstname", middlename="middlename", lastname="lastname",
            nickname='Вадик', address="address", homephone="+7950258655", email='1@mail.ru',
            email2='2@mail.ru', email3='3@mail.ru', homepage='www.mypage.ru')
]


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + " "*3
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


def random_number(prefix, maxlen):
    symbol = string.digits
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 6), lastname=random_string("lastname", 10),
                    nickname='Вадик', address=random_string("address", 25), homephone=random_number("+", 11), mobilephone=random_number("+", 11),
                    workphone=random_number("+", 11), secondaryphone=random_number("+", 2), email='1@mail.ru', email2='2@mail.ru',
                    email3='3@mail.ru', homepage='www.mypage.ru')
            for i in range(5)
]

