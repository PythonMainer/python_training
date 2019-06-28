# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.open_main_page()
    app.session.login(username='admin', password='secret')
    app.contact.create(Contact(firstname='Вадим', middlename='Сергеевич', lastname='Трофимов', nickname='Вадик', address='Москва', mobile='+79503585665', email='1@mail.ru'))
    app.return_main_page()
    app.session.logout()

