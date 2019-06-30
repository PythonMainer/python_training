from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username='admin', password='secret')
    app.contact.edit(Contact(firstname='', middlename='', lastname='', nickname='', address=' д.10', mobile='+70003585665', email='3@mail.ru'))
    app.session.logout()
