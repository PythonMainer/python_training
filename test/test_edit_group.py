from model.group import Group


def test_edit_name__group(app):
    app.group.edit_first_group(Group(name='New group'))


def test_edit_header__group(app):
    app.group.edit_first_group(Group(header='New header'))