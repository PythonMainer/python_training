from model.contact import Contact
import pytest
import random
import string


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


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)