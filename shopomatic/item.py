
"""
A base item simply is known by it's name
"""


class Item(object):

    """
    @:param str name
    """
    def __init__(self, name):
        self.name = name
