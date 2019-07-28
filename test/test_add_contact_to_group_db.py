from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group_db(app, db, orm):
    if len(db.get_contact_list()) == 0:
        contact = (Contact(firstname='Вадим', middlename='Сергеевич', lastname='Трофимов',
                           nickname='Вадик', address='г.Москва ул.Мира д.13', homephone='+7831256899',
                           mobilephone='+7952-548-6933', workphone='+7(800)3585665', email2='2@mail.ru',
                           email3='3@mail.ru', homepage='www.mypage.ru'))
        app.contact.create(contact)
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='group', header='2', footer='2'))
    id_contact = random.choice(db.get_contact_list()).id
    id_group = random.choice(db.get_group_list()).id
    app.contact.add_contact_to_group(id_contact, id_group)
    assert db.get_contact_id(id_contact) in orm.get_contacts_in_group(Group(id=id_group))


