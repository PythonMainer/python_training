from model.group import Group


def test_edit_name__group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='group', header='2', footer='2'))
    app.group.edit_first_group(Group(name='New group'))


def test_edit_header__group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='group', header='2', footer='2'))
    app.group.edit_first_group(Group(header='New header'))