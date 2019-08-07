from model.contact import Contact
import pytest



def test_add_new_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    with pytest.allure.step('Получаем список контактов'):
        old_contacts = db.get_contact_list()
    with pytest.allure.step('Создаем контакт'):
        app.contact.create(contact)
    new_contacts = db.get_contact_list()
    with pytest.allure.step('Сравниваем списки контактов'):
        assert len(old_contact) + 1 == len(new_contact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)