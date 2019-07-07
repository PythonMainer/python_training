from model.group import Group
from random import randrange


def test_edit_name_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='group', header='2', footer='2'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name='New group')
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_edit_header__group(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name='group', header='2', footer='2'))
#    app.group.edit_first_group(Group(header='New header'))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)