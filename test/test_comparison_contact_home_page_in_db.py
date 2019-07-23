from model.contact import Contact
import re


def test_comparison_contact_home_page_in_db(app, db):
    if len(db.get_contact_list()) == 0:
        contact = (Contact(firstname='Вадим', middlename='Сергеевич', lastname='Трофимов',
                                   nickname='Вадик', address='г.Москва ул.Мира д.13', homephone='+7831256899',
                                   mobilephone='+7952-548-6933',
                                   workphone='+7(800)3585665', email2='2@mail.ru', email3='3@mail.ru',
                                   homepage='www.mypage.ru'))
        app.contact.create(contact)
    contacts_list = app.contact.get_contact_list()
    for contact in contacts_list:
        assert contact.firstname == db.get_contact_id(contact.id).firstname
        assert contact.lastname == db.get_contact_id(contact.id).lastname
        assert contact.address == db.get_contact_id(contact.id).address
        assert contact.all_emails == merge_email_like_on_home_page(db.get_contact_id(contact.id))
        assert contact.all_phones_from_home_page == merge_phones_like_on_home_page(db.get_contact_id(contact.id))


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))

