from model.group import Group
import random
import pytest

def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='group', header='2', footer='2'))
    old_groups = db.get_group_list()
    with pytest.allure.step('Выбираем группу'):
        group = random.choice(old_groups)
    with pytest.allure.step('Удаляем выбранную группу'):
        app.group.delete_group_by_id(group.id)
    with pytest.allure.step('Проверяем группа удаленна'):
        assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)