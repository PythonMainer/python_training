from model.contact import Contact


def test_add_new_contact(app):
    app.contact.create(Contact(firstname='Вадим', middlename='Сергеевич', lastname='Трофимов', nickname='Вадик', address='Москва', mobile='+79503585665', email='1@mail.ru'))
    app.contact.open_main_page()
