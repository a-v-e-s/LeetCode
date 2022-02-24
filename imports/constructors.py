from copy import copy
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

    cvals = copy(vals)
    root = TreeNode(cvals.pop(0))
    current = root
    side = 'left'
    next_nodes = []

    while cvals:
        
        val = cvals.pop(0)
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


def bs_tree(vals: List[int]) -> TreeNode:
    """ construct a valid binary search tree and returns the root node"""

    assert len(set(vals)) == len(vals), 'vals must not contain any duplicates!'

    
    def recurse(local_vals, prev, side):
        
        mid = len(local_vals) // 2
        node = TreeNode(local_vals[mid])

        setattr(prev, side, node)
        
        left_vals = local_vals[:mid]
        right_vals = local_vals[mid+1:]
        
        if left_vals:
            recurse(left_vals, node, 'left')
        if right_vals:
            recurse(right_vals, node, 'right')
    

    vals = sorted(vals)
    mid = len(vals) // 2
    root = TreeNode(vals[mid])
    
    left_vals = vals[:mid]
    right_vals = vals[mid+1:]
    
    if left_vals:
        recurse(left_vals, root, 'left')
    if right_vals:
        recurse(right_vals, root, 'right')
    
    return root


def run_testcases(function: Callable, inpt_outpt: List[Tuple], silent=False) -> Union[Dict, bool]:
    """ Performs function on inpt and checks if outpt matches """

    failures = dict()
    for inpt, outpt in inpt_outpt:
        try:
            if function(inpt) == outpt:
                if not silent:
                    print(f'{function.__name__} succeeded with {inpt}, producing: {outpt}')
            else:
                failures[inpt] = outpt
                if not silent:
                    print(f'{function.__name__} failed with {inpt}, producing: {outpt}')
        except Exception as e:
            failures[inpt] = e
            if not silent:
                print(f'{function.__name__} failed with error {e}')

    if failures:
        return failures

    return True