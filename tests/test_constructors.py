#!/usr/bin/env python

import unittest

from os import getcwd
from sys import path
path.append(getcwd())

from imports import *


class Test_Constructors(unittest.TestCase):


    def test_bs_tree(self):
        
        
        def recurse(node, minimum, maximum):
            assert node.val > minimum and node.val < maximum, f'FAILED: {minimum} < {node.val} < {maximum}'
        
            if node.left:
                recurse(node.left, minimum, node.val)
            if node.right:
                recurse(node.right, node.val, maximum)
        
            return True


        vals = list(set(r_ints(-1000, 1000, 500)))
        root = bs_tree(vals)
        
        self.assertTrue(recurse(root, -float('inf'), float('inf')))


if __name__ == '__main__':
    unittest.main()


"""import os, sys
sys.path.append('imports')

from typing import *

from imports import *




def test_bst(root: Optional[TreeNode]) -> bool:
    

    def recurse(node, minimum, maximum):
        assert node.val > minimum and node.val < maximum, f'FAILED: {minimum} < {node.val} < {maximum}'
        
        if node.left:
            recurse(node.left, minimum, node.val)
        if node.right:
            recurse(node.right, node.val, maximum)
        
        return True
    

    if not root:
        root = bs_tree(r_ints())
    
    recurse(root, -float('inf'), float('inf'))

    return True"""