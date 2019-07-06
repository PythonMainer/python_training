from model.group import Group


def test_edit_name__group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name='group', header='2', footer='2'))
    group = Group(name='New group')
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_edit_header__group(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name='group', header='2', footer='2'))
#    app.group.edit_first_group(Group(header='New header'))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)