from model.group import Group


def test_edit__group(app):
    app.session.login(username='admin', password='secret')
    app.group.edit(Group(name='_edit', header='_edit', footer='_edit'))
    app.session.logout()