from typing import final


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    balance = 0
    stock = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def add_funds(self, funds):
        if self.stock == 0:
            return f'Nothing left to vend. Please restock. Here is your ${funds}.'
        self.balance += funds
        return f'Current balance: ${self.balance}'
    
    def vend(self):
        if self.stock == 0:
            return 'Nothing left to vend. Please restock.'
        elif self.price > self.balance:
            return f'You must add ${self.price-self.balance} more funds.'
        elif self.balance %self.price == 0:
            self.stock -=1
            return f'Here is your {self.name}.'
        else:
            difference = self.balance - self.price
            self.balance = 0
            self.stock -=1
            return f'Here is your {self.name} and ${difference} change.'

    def restock(self, amount):
        self.stock += amount
        return f'Current {self.name} stock: {self.stock}'

class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.present_year.

    >>> mint = Mint()
    >>> mint.year
    2021
    >>> dime = mint.create(Dime)
    >>> dime.year
    2021
    >>> Mint.present_year = 2101  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2021
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2101
    >>> Mint.present_year = 2176     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    present_year = 2021

    def __init__(self):
        self.update()

    def create(self, kind):
        return kind(self.year)

    def update(self):
        self.year = Mint.present_year


class Coin:
    def __init__(self, year):
        self.year = year

    def worth(self):
        if Mint.present_year != self.year:
            return self.cents + ((Mint.present_year - self.year) - 50)
        return self.cents
        


class Nickel(Coin):
    cents = 5


class Dime(Coin):
    cents = 10


def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    >>> # a check for restricted functions
    >>> import inspect, re
    >>> cleaned = re.sub(r"#.*\\n", '', re.sub(r'"{3}[\s\S]*?"{3}', '', inspect.getsource(store_digits)))
    >>> print("Do not use str or reversed!") if any([r in cleaned for r in ["str", "reversed"]]) else None
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    """

    final_link = Link(n%10)
    n = n//10
    while n > 0:
        final_link = Link(n%10, final_link)
        n = n//10
    return final_link
    # final_link = n
    # while n > 0:
    #     if n > 10:
    #         final_link = Link(final_link, n%10)
    #     else:
    #         final_link = Link(final_link, Link(n))
    #     n = n//10
    # return final_link
    # if n < 10:
    #     return Link(n)
    # else:
    #     final_link = Link(n%10, store_digits(n//10))

    
    
    


def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> # Disallow the use of making new Links before calling deep_map_mut
    >>> Link.__init__, hold = lambda *args: print("Do not create any new Links."), Link.__init__
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> Link.__init__ = hold
    >>> print(link1)
    <9 <16> 25 36>
    """
    if link.rest is not Link.empty:
        if isinstance(link.first, Link):
            link.first.first = fn(link.first.first)
        else:
            link.first = fn(link.first)
        deep_map_mut(fn, link.rest)
    else:
        link.first = fn(link.first)

    # while link.rest is not Link.empty:
    #     link.first = fn(link.first)
    #     link.rest = link.rest.first

    # if link.rest is not Link.empty:
    #     deep_map_mut(fn, link.rest)
    #     link.first = fn(link.first)
    # else:
    #     link.first = fn(link.first)


def two_list(vals, amounts):
    """
    Returns a linked list according to the two lists that were passed in. Assume
    vals and amounts are the same size. Elements in vals represent the value, and the
    corresponding element in amounts represents the number of this value desired in the
    final linked list. Assume all elements in amounts are greater than 0. Assume both
    lists have at least one element.

    >>> a = [1, 3, 2]
    >>> b = [1, 1, 1]
    >>> c = two_list(a, b)
    >>> c
    Link(1, Link(3, Link(2)))
    >>> a = [1, 3, 2]
    >>> b = [2, 2, 1]
    >>> c = two_list(a, b)
    >>> c
    Link(1, Link(1, Link(3, Link(3, Link(2)))))
    """

    final_link = Link.empty
    new_vals = [vals[-i-1] for i in range(len(vals))]
    new_amounts = [amounts[-i-1] for i in range(len(amounts))]

    while len(new_amounts) > 0:
        for _ in range(new_amounts[0]):
            final_link = Link(new_vals[0], final_link)
        new_amounts = new_amounts[1:]
        new_vals = new_vals[1:]
    
    
    return final_link
            
    # if len(amounts) == 1:
    #     meme = Link(vals[0])
    #     for _ in range(amounts[0]-1):
    #         meme = Link(meme, vals[0])
    #     return meme
    # else:
    #     for _ in range(amounts[0]-1):
    #         return Link(vals[0], two_list(vals[1:], amounts[1:]))
        

    # final_link = 
    # while amounts.rest is not Link.empty:
    #     for _ in range(amounts.first):
    #         final_link = Link(Link.empty, vals.first)
    #     amounts.first = amounts.rest.first
    #     vals.first = vals.rest.first
    # return final_link
    # final_link = Link(vals.first)
    # while amounts.rest is not Link.empty:
    #     for _ in range(amounts.first):
    #         final_link = Link(final_link, vals.first)
    #     amounts.rest = amounts.rest.first
    #     vals.rest = vals.rest.first
    # return final_link
            
            


class VirFib():
    """A Virahanka Fibonacci number.

    >>> start = VirFib()
    >>> start
    VirFib object, value 0
    >>> start.next()
    VirFib object, value 1
    >>> start.next().next()
    VirFib object, value 1
    >>> start.next().next().next()
    VirFib object, value 2
    >>> start.next().next().next().next()
    VirFib object, value 3
    >>> start.next().next().next().next().next()
    VirFib object, value 5
    >>> start.next().next().next().next().next().next()
    VirFib object, value 8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    VirFib object, value 8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        "*** YOUR CODE HERE ***"

    def __repr__(self):
        return "VirFib object, value " + str(self.value)


def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """
    "*** YOUR CODE HERE ***"


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()