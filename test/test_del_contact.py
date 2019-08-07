from model.contact import Contact
import random
import pytest

def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='Вадим', middlename='Сергеевич', lastname='Трофимов', nickname='Вадик', address='Москва', mobile='+79503585665', email='1@mail.ru'))
    with pytest.allure.step('Сравниваем список контактов'):
        old_contacts = db.get_contact_list()
    with pytest.allure.step('Выбираем случайный контакт'):
        contact = random.choice(old_contacts)
    with pytest.allure.step('Удаляем контакт'):
        app.contact.delete_contact_by_id(contact.id)
    with pytest.allure.step('Проверяем что контакт удален'):
        assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)