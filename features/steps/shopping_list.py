from behave import *
from shopomatic.shopping_list import ShoppingList


@given(u'I have a shopping list called "{name}"')
def step_impl(context, name):
    context.list = ShoppingList(name)


@then(u'it should have {count:d} items')
def step_impl(context, count):
    assert len(context.list.items) == int(count)


@then(u'it should have a state of "{state}"')
def step_impl(context, state):
    assert context.list.state == state
