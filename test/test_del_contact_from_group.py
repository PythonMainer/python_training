from model.contact import Contact
from model.group import Group
import random
import pytest


def test_del_contact_from_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        contact = (Contact(firstname='Вадим', middlename='Сергеевич', lastname='Трофимов',
                           nickname='Вадик', address='г.Москва ул.Мира д.13', homephone='+7831256899',
                           mobilephone='+7952-548-6933', workphone='+7(800)3585665', email2='2@mail.ru',
                           email3='3@mail.ru', homepage='www.mypage.ru'))
        app.contact.create(contact)
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='group', header='2', footer='2'))
    id_group_list_with_contacts = db.get_group_list_with_contacts()
    if len(id_group_list_with_contacts) == 0:
        id_contact = random.choice(db.get_contact_list()).id
        id_group = random.choice(db.get_group_list()).id
        app.contact.add_contact_to_group(id_group, id_contact)
        id_group_list_with_contacts.append(id_group)
    with pytest.allure.step('Выбираем группу'):
        id_group = random.choice(id_group_list_with_contacts)
    with pytest.allure.step('Выбираем контакт'):
        id_contact = random.choice(orm.get_contacts_in_group(Group(id=id_group))).id
    with pytest.allure.step('Удаляем контакт из группы'):
        app.contact.delete_contact_from_group(id_group, id_contact)
    assert db.get_contact_id(id_contact) not in orm.get_contacts_in_group(Group(id=id_group))

