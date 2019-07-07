from model.contact import Contact


def test_edit_middlename_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Вадим', middlename='Сергеевич', lastname='Трофимов', nickname='Вадик', address='Москва', mobile='+79503585665', email='1@mail.ru'))
    contact = Contact(middlename='Анатольевич')
    contact.id = old_contacts[0].id
    app.contact.edit_first(contact)
    new_contacts = app.contact.get_contact_list()
    assert old_contacts == new_contacts
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_edit_firstname_contact(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname='Вадим', middlename='Сергеевич', lastname='Трофимов', nickname='Вадик', address='Москва', mobile='+79503585665', email='1@mail.ru'))
#    app.contact.edit_first(Contact(firstname='Роберт'))