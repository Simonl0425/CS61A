# Trees and Linked Lists

class Link:
    """A linked list.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.first
    1
    >>> s.rest
    Link(2, Link(3))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({})'.format(self.first)
        else:
            return 'Link({}, {})'.format(self.first, repr(self.rest))

def print_link(link):
    """Print elements of a linked list link.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print_link(link)
    <1 2 3>
    >>> link1 = Link(1, Link(Link(2), Link(3)))
    >>> print_link(link1)
    <1 <2> 3>
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print_link(link1)
    <3 <4> 5 6>
    """
    print('<' + helper(link).rstrip() + '>')

def helper(link):
    if link == Link.empty:
        return ''
    elif isinstance(link.first, Link):
        return '<' + helper(link.first).rstrip() + '> ' + helper(link.rest)
    else:
        return str(link.first) +' '+  helper(link.rest)

def every_other(s):
    """Mutates a linked list so that all the odd-indiced elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    if s.rest == Link.empty or s.rest.rest == Link.empty:
        s.rest = Link.empty
    else:
        s.rest = s.rest.rest
        every_other(s.rest)



def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print_link(link1)
    <9 <16> 25 36>
    """
    if link == Link.empty:
        return
    else:
        if isinstance(link.first, Link):
            deep_map_mut(fn, link.first)
        else:
            link.first = fn(link.first)
        deep_map_mut(fn, link.rest)



def two_list(lst1, lst2):
    """
    Returns a linked list according to the two lists that were passed in. Assume
    lst1 and lst2 are the same size. Elements in lst1 represent the value, and the
    corresponding element in lst2 represents the number of this value is desired in the
    final linked list. Assume all elements in lst2 are greater than 0. Assume both
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

    def rec(lst1, lst2, cnt):
        if len(lst1) == 0:
            return Link.empty
        if cnt == 0:
            if  len(lst1) == 1:
                return Link.empty
            lst1.pop(0)
            lst2.pop(0)
            return Link(lst1[0], rec(lst1, lst2, lst2[0]-1))
        else:
            return Link(lst1[0], rec(lst1, lst2, cnt-1))

    return rec(lst1, lst2, lst2[0])

def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    def chk(link, head):
        if link == Link.empty:
            return False
        if link is head:
            return True

        return chk(link.rest, head)

    return chk(link.rest, link)

def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"

class Tree:
    def __init__(self, root, branches=[]):
        for c in branches:
            assert isinstance(c, Tree)
        self.root = root
        self.branches = branches

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.root, branches_str)

    def is_leaf(self):
        return not self.branches

    def __eq__(self, other):
        return type(other) is type(self) and self.root == other.root \
               and self.branches == other.branches

def cumulative_sum(t):
    """Mutates t where each node's root becomes the sum of all entries in the
    corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(t)
    >>> t
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    """
    if t.is_leaf():
        return
    else:
        total = t.root
        for b in t.branches:
            cumulative_sum(b)
            total += b.root
        t.root = total



def prune_min(t):
    """Prune the tree mutatively from the bottom up. Assume the tree and its branches always have either two branches or none. Prune the tree by
    reducing the number of branches from two to one, choosing the branch with the smaller root value. Assume branches have differing root values.
    Do nothing with trees with zero branches.

    >>> t1 = Tree(6)
    >>> prune_min(t1)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_min(t2)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(3, [Tree(1), Tree(2)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_min(t3)
    >>> t3
    Tree(6, [Tree(3, [Tree(1)])])
    """
    for b in t.branches:
        prune_min(b)

    if len(t.branches) == 2:
        if t.branches[0].root < t.branches[1].root:
            t.branches.pop(1)
        else:
            t.branches.pop(0)

def long_paths(tree, n):
    """Return a list all paths in tree with length at least n.

    >>> t = Tree(3, [Tree(4), Tree(4), Tree(5)])
    >>> left = Tree(1, [Tree(2), t])
    >>> mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
    >>> right = Tree(11, [Tree(12)])
    >>> whole = Tree(0, [left, Tree(13), mid, right])
    >>> for path in long_paths(whole, 2):
    ...     print(path)
    ...
    Link(0, Link(1, Link(2)))
    Link(0, Link(1, Link(3, Link(4))))
    Link(0, Link(1, Link(3, Link(4))))
    Link(0, Link(1, Link(3, Link(5))))
    Link(0, Link(6, Link(7, Link(8))))
    Link(0, Link(6, Link(9)))
    Link(0, Link(11, Link(12)))
    >>> for path in long_paths(whole, 3):
    ...     print(path)
    ...
    Link(0, Link(1, Link(3, Link(4))))
    Link(0, Link(1, Link(3, Link(4))))
    Link(0, Link(1, Link(3, Link(5))))
    Link(0, Link(6, Link(7, Link(8))))
    >>> long_paths(whole, 4)
    []
    """
    paths = []
    if n <= 0 and not tree.branches:
        paths.append(Link(tree.root))
    for b in tree.branches:
        for path in long_paths(b, n - 1):
            paths.append(Link(tree.root, path))
    return paths
