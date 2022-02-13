#!/usr/bin/env python3

import random
from string import ascii_lowercase
from typing import *

from leet_objects import ListNode


def pathological_integer_list(lowest=1, highest=1000, length=500, sorted_=False):
    """ Return a list of random integer values, optionally sorted """
    
    ints = [random.randint(lowest, highest) for _ in range(length)]
    
    if sorted_ in {True, 'ascending'}:
        return sorted(ints)
    elif sorted_ == 'descending':
        return sorted(ints, reverse=True)
    else:
        return ints


def pathological_string(length=500, sorted=False, *, chars=ascii_lowercase):
    """ Return a string of random characters, optionally sorted  """
    
    garbled =  ''.join([random.choice([chars] for _ in range(length))])

    if sorted_ in {True, 'ascending'}:
        return sorted(garbled)
    elif sorted_ == 'descending':
        return sorted(garbled, reverse=True)
    else:
        return garbled


def singly_linked_list(vals: List) -> Optional[ListNode]:
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


def circular_linked_list(vals: List) -> Optional[ListNode]:
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


def doubly_linked_list(vals: List) -> Optional[ListNode]:
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


def doubly_circular_list(vals: List) -> Optional[ListNode]:
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


def test_cases():
    pass


def binary_tree():
    pass

