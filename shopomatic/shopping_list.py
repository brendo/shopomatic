from transitions import Machine

"""
A list is known by a name and has many items
"""


class ShoppingList(object):
    states = ['todo', 'progress', 'finished']

    """
    @:param str name
    """
    def __init__(self, name):
        self.name = name
        self.items = {}
        self.machine = Machine(model=self, states=ShoppingList.states, initial='todo')
        self.machine.add_transition('done', ['todo', 'progress'], 'finished', conditions='is_done')
        self.machine.add_transition('shopping', 'todo', 'progress')

    """
    @:param ListItem item
    """
    def add(self, item):
        self.items[item.name] = item

    """
    @:param str name
    @:return ListItem
    """
    def get(self, name):
        return self.items.get(name)

    """
    Look in the items of this shopping list to see if the item was
    found, and if it was, reduce the quantity required by the given
    amount

    @:param str name
    @:param int quantity
    """
    def update(self, name, quantity=1):
        item = self.get(name)

        if item is not None:
            item.found(quantity)

        if self.is_done():
            self.to_finished()

    """
    Determines if the shopping is done by making sure all the list
    items have been fully acquired
    """
    def is_done(self) -> bool:
        items = [item for item in self.items.values() if item.state is not 'acquired']

        return len(items) is 0
