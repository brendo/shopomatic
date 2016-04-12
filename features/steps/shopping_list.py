from behave import *
from shopomatic.list_item import ListItem
from shopomatic.shopping_list import ShoppingList


@given(u'I have a shopping list called "{name}"')
def step_impl(context, name):
    context.list = ShoppingList(name)


@when(u'I add a new item "{name}"')
def step_impl(context, name):
    item = ListItem(name)
    context.list.add(item)
    pass


@then(u'I should see "{name}" in the shopping list')
def step_impl(context, name):
    assert context.list.get(name) is not None


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