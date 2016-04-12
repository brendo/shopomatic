from transitions import Machine

from shopomatic.item import Item

"""
Extends the base item class to include quantity and state.
"""


class ListItem(Item):
    states = ['needed', 'partial', 'acquired']

    """
    @:param str name
    @:param int quantity
    """
    def __init__(self, name, quantity=1):
        self.quantity = quantity
        self.machine = Machine(model=self, states=ListItem.states, initial='needed')
        self.machine.add_transition(
            'found',
            ['needed','partial'],
            'acquired',
            conditions=['is_no_longer_required'],
            before='set_quantity'
        )

        self.machine.add_transition(
            'found',
            ['needed','partial'],
            'partial',
            unless=['is_no_longer_required'],
            before='set_quantity'
        )

        super(ListItem, self).__init__(name)

    """
    Given the quantity, update the quantity required for this list item.
    If quantity is not provided, use the item's total quantity

    @:param int quantity
    @:return self
    """
    def set_quantity(self, quantity: int):
        if quantity is None:
            quantity = self.quantity

        self.quantity -= quantity

        return self

    """
    Accessor function, if the quantity required would be reduce the list
    item to 0 with the given quantity, this function will return true.

    @:param int quantity
    @:return bool
    """
    def is_no_longer_required(self, quantity: int) -> bool:
        if quantity is None:
            quantity = self.quantity

        return (self.quantity - quantity) == 0
