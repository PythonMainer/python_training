from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='Вадим', middlename='Сергеевич', lastname='Трофимов',
                      nickname='Вадик', address='г.Москва ул.Мира', homephone='+7831256899', mobilephone='+7952-548-6933',
                      workphone='+7(800)3585665', secondaryphone='+45', email='1@mail.ru', email2='2@mail.ru',
                      email3='3@mail.ru', homepage='www.mypage.ru')
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)