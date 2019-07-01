from model.group import Group


def test_edit__group(app):
    app.group.edit(Group(name='_edit', header='_edit', footer='_edit'))