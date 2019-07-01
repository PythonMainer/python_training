# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name='group', header='2', footer='2'))


def test_add_empty_group(app):
    app.group.create(Group(name='group', header='', footer=''))