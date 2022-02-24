import unittest
import re

from os import getcwd
from sys import path
path.append(getcwd())

from imports import *


class Test_Objects(unittest.TestCase):

    listnode_repr = re.compile(
        r'ListNode <0x[0-9a-f]{8,}>\n\tval: (\d){1,}\n\tprev: (None|0x[0-9a-f]{8,})\n\tnext: (None|0x[0-9a-f]{8,})'
    )
    treenode_repr = re.compile(
        r'TreeNode <0x[0-9a-f]{8,}>\n\tval: (\d){1,}\n\tleft: (None|0x[0-9a-f]{8,})\n\tright: (None|0x[0-9a-f]{8,})'
    )


    def test_aliases(self):

        self.assertTrue((pr is print))
        self.assertTrue((null is None))


    """def test_disjoint_set(self):
        pass


    def test_undirected_graph_node(self):
        pass"""


    def test_listnode(self):
        
        head = dcl(r_ints(1, 100, 10))
        current = head
        
        for _ in range(20):
            self.assertRegex(current.__repr__(), self.listnode_repr)
            current = current.next

        for _ in range(20):
            self.assertRegex(current.__repr__(), self.listnode_repr)
            current = current.prev



    def test_treenode(self):

        def recurse(node):
            
            self.assertRegex(node.__repr__(), self.treenode_repr)
            
            if node.left:
                recurse(node.left)
            if node.right:
                recurse(node.right)
        

        root = b_tree(r_ints(1, 100, 20))

        recurse(root)


if __name__ == '__main__':
    unittest.main()