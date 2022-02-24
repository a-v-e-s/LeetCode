#!/usr/bin/env python

import unittest

from os import getcwd
from sys import path
path.append(getcwd())

from imports import *


class Test_Constructors(unittest.TestCase):


    def test_r_ints(self):
        vals = r_ints()
        self.assertTrue(all([(type(val) == int) for val in vals]))


    def test_r_string(self):
        chars = r_string()
        self.assertTrue(all([(type(char) == str) for char in chars]))


    def test_sll(self):
        
        head = sll(r_ints(length=10))
        current = head

        for _ in range(9):
            self.assertIsInstance(current, ListNode)
            self.assertIsInstance(current.val, int)
            self.assertIsNone(current.prev)
            current = current.next
        
        self.assertIsInstance(current, ListNode)
        self.assertIsNone(current.prev)


    def test_cll(self):

        head = cll(r_ints(length=10))
        current = head

        for _ in range(30):
            self.assertIsInstance(current, ListNode)
            self.assertIsInstance(current.val, int)
            self.assertIsInstance(current.next, ListNode)
            self.assertIsNone(current.prev)
            current = current.next

    
    def test_dll(self):

        head = dll(r_ints(length=10))
        current = head

        self.assertIsNone(current.prev)

        for _ in range(9):
            self.assertIsInstance(current, ListNode)
            self.assertIsInstance(current.val, int)
            current = current.next
        
        self.assertIsNone(current.next)

        for _ in range(9):
            self.assertIsInstance(current, ListNode)
            self.assertIsInstance(current.val, int)
            current = current.prev
        
        self.assertIsNone(current.prev)

    
    def test_dcl(self):

        head = dcl(r_ints(length=10))
        current = head

        for _ in range(20):
            self.assertIsInstance(current, ListNode)
            self.assertIsInstance(current.val, int)
            self.assertIsInstance(current.next, ListNode)
            self.assertIsInstance(current.prev, ListNode)
            current = current.next

        for _ in range(20):
            self.assertIsInstance(current, ListNode)
            self.assertIsInstance(current.val, int)
            self.assertIsInstance(current.prev, ListNode)
            self.assertIsInstance(current.next, ListNode)
            current = current.prev
    

    def test_b_tree(self):

        def recurse(node):
            
            nonlocal count

            self.assertIsInstance(node, TreeNode)
            self.assertIsInstance(node.val, int)
            count += 1
            
            if node.left:
                recurse(node.left)
            if node.right:
                recurse(node.right)


        root = b_tree(r_ints(length=100))

        count = 0

        recurse(root)

        self.assertEqual(count, 100)


    def test_bs_tree(self):
        
        def recurse(node, minimum, maximum):
            
            if not (minimum < node.val < maximum):
                return False

            self.assertIsInstance(node, TreeNode)
            self.assertLess(node.val, maximum)
            self.assertGreater(node.val, minimum)

            if node.left:
                if not recurse(node.left, minimum, node.val):
                    return False
            if node.right:
                if not recurse(node.right, node.val, maximum):
                    return False
        
            return True

        vals = list(set(r_ints(-1000, 1000, 500)))
        root = bs_tree(vals)
        
        self.assertTrue(recurse(root, -float('inf'), float('inf')))

    
    def test_run_testcases(self):

        function = lambda a: a*2
        
        good_inputs = r_ints(length=10)
        good_outputs = [val*2 for val in good_inputs]
        inpt_outpt = list(zip(good_inputs, good_outputs))
        
        self.assertTrue(run_testcases(function, inpt_outpt, True))

        bad_outputs = [val/2 for val in good_inputs]
        inpt_outpt = list(zip(good_inputs, bad_outputs))
        
        failures = run_testcases(function, inpt_outpt, True)
        self.assertEqual(len(failures), 10)

if __name__ == '__main__':
    unittest.main()