from model.contact import Contact
import random
import pytest

def test_edit_middlename_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='Вадим', middlename='Сергеевич', lastname='Трофимов', nickname='Вадик', address='Москва', mobile='+79503585665', email='1@mail.ru'))
    with pytest.allure.step('Получение список контактов'):
        old_contacts = db.get_contact_list()
    with pytest.allure.step('Выбираем случайный контакт'):
        id = random.choice(old_contacts).id
    old_contacts_data = db.get_contact_id(id)
    old_contacts.remove(old_contacts_data)
    contact = Contact(firstname='Максим', id=id)
    with pytest.allure.step('Изменяем данные о контакте'):
        app.contact.edit_contact_by_id(id, contact)
    with pytest.allure.step('Получение нового списка контактов'):
        new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    with pytest.allure.step('Проверяем списки'):
        assert len(old_contacts) == app.contact.count()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


#def test_edit_firstname_contact(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname='Вадим', middlename='Сергеевич', lastname='Трофимов', nickname='Вадик', address='Москва', mobile='+79503585665', email='1@mail.ru'))
#    app.contact.edit_first(Contact(firstname='Роберт'))