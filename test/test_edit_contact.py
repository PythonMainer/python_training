from model.contact import Contact


def test_edit_contact(app):
    app.contact.edit(Contact(firstname='Анатолий', middlename='Александрович', lastname='Миронов', nickname='Миронов', address='Мира д.10', mobile='+70003585665', email='3@mail.ru'))