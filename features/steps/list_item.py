from behave import *
from shopomatic.list_item import ListItem


@given(u'I add "{name}"')
@given(u'I add "{name}" with a quantity of {quantity:d}')
def step_impl(context, name, quantity=1):
    item = ListItem(name, quantity)
    context.list.add(item)
    pass


@then(u'I should see "{name}" in the shopping list')
def step_impl(context, name):
    assert context.list.get(name) is not None


@then(u'I should not see "{name}" in the shopping list')
def step_impl(context, name):
    assert context.list.get(name) is None


@then(u'"{name}" should have a quantity of {quantity:d}')
def step_impl(context, name, quantity):
    item = context.list.get(name)

    assert item is not None
    assert item.quantity == quantity


@then(u'"{name}" should have a state of "{state}"')
def step_impl(context, name, state):
    item = context.list.get(name)

    assert item is not None
    assert item.state == state


@given(u'I have added the followings items')
def step_impl(context):
    for row in context.table:
        context.list.add(ListItem(row['name'], int(row['quantity'])))


@given(u'I find "{name}"')
@given(u'I find {quantity:d} of "{name}"')
def step_impl(context, name, quantity=1):
    context.list.update(name, quantity)
    pass


@given(u'I remove "{name}"')
def step_impl(context, name):
    context.list.remove(name)
    pass
