from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='Вадим', middlename='Сергеевич', lastname='Трофимов',
                      nickname='Вадик', address='Москва', homephone='+7831256899', workphone='+78003585665',
                      mobilephone='+79525486933', secondaryphone='+2', email='1@mail.ru')
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)