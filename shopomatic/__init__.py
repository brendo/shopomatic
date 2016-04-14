from __future__ import print_function
from shopomatic.list_item import ListItem
from shopomatic.shopping_list import ShoppingList


def get_items(shopping):
    """
    Retrieve the items and quantity from the user
    """
    while True:
        item = input("What do you want? ")
        quantity = None

        if item == "Q":
            break

        while quantity is None:
            try:
                quantity = int(input("How many? "))

            except ValueError:
                print("Please enter a number")

        shopping.add(ListItem(item, int(quantity)))

    return shopping


def main():
    name = input("What is the name of your list? ")
    shopping = ShoppingList(name)
    get_items(shopping)

    print('My', shopping.name, 'is', shopping.state)
    print('I need:')
    for name, item in shopping.items.items():
        print('-', name, item.quantity, item.state)
        print('I found 1 of them')
        item.found(quantity=1)

        if item.state is not 'acquired':
            print('I now need', item.quantity, 'more', name)
        else:
            print('I got all the', name)

    shopping.done()

    if shopping.is_finished():
        print('Finished shopping, yay!')
    else:
        print('Stuff need things!')
        name = input("What did you get?")

        shopping.update(name, quantity=1)

        print(shopping.is_finished(), shopping.items.items())


if __name__ == '__main__':
    main()
