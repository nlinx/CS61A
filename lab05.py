## Rooted Trees, Linked Lists, Dictionaries ##

################
# Rooted Trees #
################

# Tree definition
def rooted(value, branches):
    for branch in branches:
        assert is_rooted(branch), 'branches must be rooted trees'
    return [value] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def leaf(value):
    return rooted(value, [])

def is_rooted_leaf(tree):
    return branches(tree) == []

def is_rooted(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_rooted(branch):
            return False
    return True

t = rooted(1, [leaf(2), rooted(3, [leaf(4), leaf(5)]), rooted(6, [leaf(7)])])


def print_tree(t, indent=0):
    """Return a string representation of this tree in which
    each node is indented by two spaces times its depth from
    the root.

    >>> print_tree(t)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(root(t)))
    for child in branches(t):
        print_tree(child, indent + 1)

# Q1 (optional)
def countdown_tree():
    """Return a tree that has the following structure. 

    >>> print_tree(countdown_tree())
    10
      9
        8
      7
        6
          5
    """
    return rooted(10, [rooted(9, [leaf(8)]), rooted(7, [rooted(6, [leaf(5)])])])

# Q2
def size_of_tree(t):
    """Return the number of entries in the tree.

    >>> print_tree(t)
    1
      2
      3
        4
        5
      6
        7
    >>> size_of_tree(t)
    7
    """
    if not is_rooted(t):
        return 0
    return  1+ sum([size_of_tree(value) for value in branches(t)])


################
# Linked Lists #
################

# Linked List definition
empty = 'empty'

def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1]))

def link(first, rest):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]

def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), 'first only applies to linked lists.'
    assert s != empty, 'empty linked list has no first element.'
    return s[0]

def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), 'rest only applies to linked lists.'
    assert s != empty, 'empty linked list has no rest.'
    return s[1]


# Q3
def sum_linked_list(lst, fn):
    """ Applies a function FN to each number in LST and returns the sum
    of the resulting values

    >>> square = lambda x: x*x
    >>> double = lambda y: 2*y
    >>> lst1 = link(1, link(2, link(3, link(4, empty))))    
    >>> sum_linked_list(lst1, square)
    30
    >>> lst2 = link(3, link(5, link(4, link(10, empty))))
    >>> sum_linked_list(lst2, double)
    44
    """
    
    if lst == empty:
        return 0
    return fn(first(lst)) + sum_linked_list(rest(lst), fn)

################
# Dictionaries #
################

# Q4
def counter(message):
    """ Returns a dictionary of each word in message mapped 
    to the number of times it appears in the input string.
    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    word_list = message.split()
    result_dict = {} # resulting dictionary starts off as an empty dictionary
    for word in word_list:
        if word in result_dict:
            result_dict[word] += 1
        else:
            result_dict[word] = 1
    return result_dict

# Q5
def is_leaf(t):
    return type(t) != list

def height(t):
    """Return the depth of the deepest node in the tree. 

    >>> height(leaf(1))
    0
    >>> height(rooted(1, [leaf(2), leaf(3)]))
    1
    >>> print_tree(t)
    1
      2
      3
        4
        5
      6
        7
    >>> height(t)
    2
    """
    if branches(t) == []:
        return 0
    deepest = 0
    for child in branches(t):
        deepest = max(deepest, height(child))
    return deepest + 1

################
# Linked Lists #
################

def linked_list_to_str(lst):
    s = '< '
    while lst != empty:
        if is_link(first(lst)):
            s = s + linked_list_to_str(first(lst)) + ' '
        else:
            s = s + repr(first(lst)) + ' '
        lst = rest(lst)
    return s + '>'

def print_linked_list(lst):
    """
    >>> print_linked_list(empty)
    < >
    >>> print_linked_list(link(1, empty))
    < 1 >
    >>> print_linked_list(link(2, link(3, link(link(4, empty), empty))))
    < 2 3 < 4 > >
    >>> print_linked_list(link(1, link(link(2, link(3, empty)), \
            link(4, link(link(5, link(6, link(7, empty))), empty)))))
    < 1 < 2 3 > 4 < 5 6 7 > >
    """
    print(linked_list_to_str(lst))

# Q6

def link_to_list(linked_lst):
    """Return a list that contains the values inside of linked_lst

    >>> link_to_list(empty)
    []
    >>> lst1 = link(1, link(2, link(3, empty)))
    >>> link_to_list(lst1)
    [1, 2, 3]
    """
    if linked_lst == empty:
        return []
    return [first(linked_lst)] + link_to_list(rest(linked_lst))


# Q7
def insert_at_end(lst, elem):
    """Return a linked list that is the same as lst with elem added
    at the end.

    >>> lst1 = insert_at_end(empty, 1)
    >>> print_linked_list(lst1)
    < 1 >
    >>> lst2 = insert_at_end(lst1, 2)
    >>> print_linked_list(lst2)
    < 1 2 >
    >>> lst3 = insert_at_end(lst2, 3)
    >>> print_linked_list(lst3)
    < 1 2 3 >
    """
    if lst == empty:
        return link(elem, empty)
    else:
        return link(first(lst), insert_at_end(rest(lst),elem))

################
# Dictionaries #
################

# Q8
def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of
    successors.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev] = []
        table[prev].append(word)
        prev = word
    return table

# Q9
def construct_sent(word, table):
    """Prints a random sentence starting with word, sampling from
    table.
    """
    import random
    result = ' '
    while word not in ['.', '!', '?']:
       result += word + ' '
       word = random.choice(table[word])
    return result + word

# Warning: do NOT try to print the return result of this function
def shakespeare_tokens(path='shakespeare.txt', url='http://goo.gl/SztLfX'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

tokens = shakespeare_tokens()
table = build_successors_table(tokens)

def random_sent():
    import random
    return construct_sent(random.choice(table['.']), table)