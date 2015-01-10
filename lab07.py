## Linked List Class and Generic Functions ##

######################
# Linked Lists Class #
######################

class Link:
    """A linked list.

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> len(s)
    4
    >>> s[2]
    3
    >>> s
    Link(1, Link(2, Link(3, Link(4))))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __str__(self):
        """Returns a human-readable string representation of the Link

        >>> s = Link(1, Link(2, Link(3, Link(4))))
        >>> str(s)
        '<1, 2, 3, 4>'
        >>> str(Link(1))
        '<1>'
        >>> str(Link.empty)  # empty tuple
        '()'
        """
        string = '<'
        while self.rest is not Link.empty:
            string += '{0}, '.format(self.first)
            self = self.rest
        return string + '{0}>'.format(self.first)

    def __add__(self, other):
        """Adds two Links, returning a new Link

        >>> Link(1, Link(2)) + Link(3, Link(4, Link(5)))
        Link(1, Link(2, Link(3, Link(4, Link(5)))))
        """
        result = Link.empty
        while self is not Link.empty:
            result = Link(self.first, result)
            self = self.rest
        while other is not Link.empty:
            result = Link(other.first, result)
            other = other.rest
        return reverse(result)

    def __setitem__(self, index, element):
        """Sets the value at the given index to the element

        >>> s = Link(1, Link(2, Link(3)))
        >>> s[1] = 5
        >>> s
        Link(1, Link(5, Link(3)))
        >>> s[4] = 5
        Traceback (most recent call last):
        ...
        IndexError
        """
        if index == 0:
            self.first = element
        elif self.rest is Link.empty:
            raise IndexError
        else:
            self.rest[index - 1] = element

def insert(link, value, index):
    """Insert a value into a Link at the given index.

    >>> link = Link(1, Link(2, Link(3)))
    >>> insert(link, 9001, 0)
    >>> link
    Link(9001, Link(1, Link(2, Link(3))))
    >>> insert(link, 100, 2)
    >>> link
    Link(9001, Link(1, Link(100, Link(2, Link(3)))))
    >>> insert(link, 4, 5)
    Index out of bounds
    """
    assert len(link) > 0, 'Linked list has no inputs'
    if index == 0:
        link.rest = Link(link.first, link.rest)
        link.first = value
    elif link.rest is Link.empty:
        print('Index out of bounds')
    else:
        insert(link.rest, value, index - 1)

def link_to_list(link):
    """Takes a Link and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    if link is Link.empty:
        return []
    return [link.first] + link_to_list(link.rest)

def reverse(link):
    """Returns a Link that is the reverse of the original.

    >>> Link(1).rest is Link.empty
    True
    >>> link = Link(1, Link(2, Link(3)))
    >>> reverse(link)
    Link(3, Link(2, Link(1)))
    >>> reverse(Link(1))
    Link(1)
    """
    new = Link(link.first)
    while link.rest is not Link.empty:
        link = link.rest
        new = Link(link.first, new)
    return new

def type_tag(x):
    return type_tag.tags[type(x)]

type_tag.tags = {
    list : 'list',
    Link : 'link'
}

def concat(seq1, seq2):
    """Takes the elements of seq1 and seq2 and adds them together.

    >>> link = Link(4, Link(5, Link(6)))
    >>> lst = [1, 2, 3]
    >>> concat(lst, link)
    [1, 2, 3, 4, 5, 6]
    >>> concat(link, [7, 8])
    Link(4, Link(5, Link(6, Link(7, Link(8)))))
    >>> concat(lst, [7, 8, 9])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    if type_tag(seq1) == type_tag(seq2):
        return seq1 + seq2
    else:
        types = (type_tag(seq1), type_tag(seq2))
        if types in concat.adders:
            return concat.adders[types](seq1, seq2)

def add_list_link(lst, link):
    lst += link_to_list(link)
    return lst

def add_link_list(link, lst):
    result = Link.empty
    for x in lst:
        result = Link(x) + result
    return link + reverse(result)

concat.adders = {
    ('list', 'link')  : add_list_link,
    ('link', 'list')  : add_link_list
}