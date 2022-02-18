import random
from string import ascii_lowercase
from typing import *

from .objects import *


def r_ints(lowest=1, highest=1000, length=500, sorted_=False):
    """ Return a list of random integer values, optionally sorted """
    
    ints = [random.randint(lowest, highest) for _ in range(length)]
    
    if sorted_ in {True, 'ascending'}:
        return sorted(ints)
    elif sorted_ == 'descending':
        return sorted(ints, reverse=True)
    else:
        return ints


def r_string(length=500, sorted_=False, *, chars=ascii_lowercase):
    """ Return a string of random characters, optionally sorted  """
    
    garbled =  ''.join([random.choice(chars) for _ in range(length)])

    if sorted_ in {True, 'ascending'}:
        return sorted(garbled)
    elif sorted_ == 'descending':
        return sorted(garbled, reverse=True)
    else:
        return garbled


def sll(vals: List) -> Optional[ListNode]:
    """ Return the head of a singly-linked list """
    
    if not vals:
        return None
    
    head = ListNode(vals[0])
    
    if len(vals) > 1:
        prev = head
        
        for val in vals[1:]:
            node = ListNode(val)
            prev.next = node
            prev = node
    
    return head


def cll(vals: List) -> Optional[ListNode]:
    """ Return the head of a singly-linked circular list """

    if not vals:
        return None
        
    head = ListNode(vals[0])
    
    if len(vals) > 1:
        prev = head
        
        for val in vals[1:]:
            node = ListNode(val)
            prev.next = node
            prev = node
    
    node.next = head
    
    return head


def dll(vals: List) -> Optional[ListNode]:
    """ Return the head of a doubly-linked list """

    if not vals:
        return None
    
    head = ListNode(vals[0])
    
    if len(vals) > 1:
        prev = head

        for val in vals[1:]:
            node = ListNode(val)
            node.prev = prev
            prev.next = node
            prev = node

    return head


def dcl(vals: List) -> Optional[ListNode]:
    """ Return the head of a doubly-linked circular list """

    if not vals:
        return None
    
    head = ListNode(vals[0])

    if len(vals) > 1:
        prev = head

        for val in vals[1:]:
            node = ListNode(val)
            node.prev = prev
            prev.next = node
            prev = node
    
    node.next = head
    head.prev = node

    return head


def b_tree(vals):
    """ Returns the root node of a binary tree constructed from a list of node values """
    
    if not vals:
        return None

    root = TreeNode(vals.pop(0))
    current = root
    side = 'left'
    next_nodes = []

    while vals:
        
        val = vals.pop(0)
        if val:
            next_node = TreeNode(val)
            setattr(current, side, next_node)
            next_nodes.append(next_node)
        
        side = 'right' if side == 'left' else 'left'
        if side == 'left':
            try:
                current = next_nodes.pop(0)
            except IndexError:
                break
    
    return root


def testcases(function: Callable, inpt_outpt: List[Tuple]) -> Union[Dict, bool]:
    """ Performs function on inpt and checks if outpt matches """

    failures = dict()
    for inpt, outpt in inpt_outpt:
        try:
            if function(inpt) == outpt:
                print(f'{function.__name__} succeeded with {inpt}, producing: {outpt}')
            else:
                failures[inpt] = outpt
                print(f'{function.__name__} failed with {inpt}, producing: {outpt}')
        except Exception as e:
            failures[inpt] = e
            print(f'{function.__name__} failed with error {e}')

    if failures:
        return failures

    return True