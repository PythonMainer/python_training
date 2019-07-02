from model.contact import Contact


def test_edit_middlename_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Вадим', middlename='Сергеевич', lastname='Трофимов', nickname='Вадик', address='Москва', mobile='+79503585665', email='1@mail.ru'))
    app.contact.edit_first(Contact(middlename='Анатольевич'))


def test_edit_firstname_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Вадим', middlename='Сергеевич', lastname='Трофимов', nickname='Вадик', address='Москва', mobile='+79503585665', email='1@mail.ru'))
    app.contact.edit_first(Contact(firstname='Роберт'))