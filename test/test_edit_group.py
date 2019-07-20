from model.group import Group
import random


def test_edit_name_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='group', header='2', footer='2'))
    old_groups = db.get_group_list()
    id = random.choice(old_groups).id
    old_group_data = db.get_group_by_id(id)
    old_groups.remove(old_group_data)
    group = Group(name='New group', id=id)
    app.group.edit_group_by_id(id, group)
    old_groups.append(group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_edit_header__group(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name='group', header='2', footer='2'))
#    app.group.edit_first_group(Group(header='New header'))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)