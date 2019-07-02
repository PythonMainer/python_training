from model.contact import Contact


def test_edit_middlename_contact(app):
    app.contact.edit_first(Contact(middlename='Анатольевич'))


def test_edit_firstname_contact(app):
    app.contact.edit_first(Contact(firstname='Роберт'))