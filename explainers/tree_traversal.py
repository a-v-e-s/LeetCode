#!/usr/bin/env python

from typing import *


class TreeNode:

 def __init__(self, val=0, left=None, right=None):
     self.val = val
     self.left = left
     self.right = right


class Demo:


    def __init__(self):
        self.q = []
        self.traversal = []


    def preorderTraversal(self, root: Optional[TreeNode], top=False) -> List[int]:

        if top:
            print('Pre-Order Traversal:\n')
        
        if (root is None) or (root.val is None):
            return []
        
        nodes = [root.val]
        print(f'Current node: {nodes}')
        
        if root.left:
            nodes.extend(self.preorderTraversal(root.left))
            print(f'nodes extended to: {nodes}')
        
        if root.right:
            nodes.extend(self.preorderTraversal(root.right))
            print(f'nodes extended to: {nodes}')
        
        print(f'Returning nodes: {nodes}')
        return nodes


    def inorderTraversal(self, root: Optional[TreeNode], top=False) -> List[int]:

        if top:
            print('In-Order Traversal:\n')
        
        nodes = []
        
        if (root is None) or (root.val is None):
            return nodes
        
        if root.left:
            nodes.extend(self.inorderTraversal(root.left))
            print(f'nodes extended to: {nodes}')
        
        nodes.extend([root.val])
        print(f'Current node appended: {nodes}')
        
        if root.right:
            nodes.extend(self.inorderTraversal(root.right))
            print(f'nodes extended to: {nodes}')
        
        print(f'Returning nodes: {nodes}')
        return nodes


    def postorderTraversal(self, root: Optional[TreeNode], top=False) -> List[int]:

        if top:
            print('Post-Order Traversal:\n')
        
        nodes = []
        
        if (root is None) or (root.val is None):
            return nodes
        
        if root.left:
            nodes.extend(self.postorderTraversal(root.left))
            print(f'nodes extended to: {nodes}')
        
        if root.right:
            nodes.extend(self.postorderTraversal(root.right))
            print(f'nodes extended to: {nodes}')
        
        nodes.extend([root.val])
        print(f'Current node appended: {nodes}')
        
        return nodes


    def levelOrder(self, root: Optional[TreeNode], level: int = 0, top=False) -> List[List[int]]:

        if top:
            print('Level-Order (Breadth-First) Traversal:\n')
        
        if (root is None) or (root.val is None):
            return []
        
        if not self.q:
            self.q.append((root.val, level))
            print(f'q started: {self.q}')
        
        if len(self.traversal) <= level:
            self.traversal.append([])
            print(f'traversal appended with []: {self.traversal}')
        
        self.traversal[level] = [val[0] for val in self.q if val[1] == level]
        print(f'self.traversal updated: {self.traversal}')
        
        if root.left:
            self.q.append((root.left.val, level+1))
            print(f'root.left found; self.q appended: {self.q}')
        
        if root.right:
            self.q.append((root.right.val, level+1))
            print(f'root.right found; self.q appended: {self.q}')
        
        if root.left:
            print(f'desceding into root.left, level {level+1}')
            self.levelOrder(root.left, level+1)
        
        if root.right:
            print(f'desceding into root.left, level {level+1}')
            self.levelOrder(root.right, level+1)
        
        if level == 0:
            print(f'Finished, returning self.traversal: {self.traversal}')
            return self.traversal


if __name__ == '__main__':

    tree1_node15 = TreeNode(15, None, None)
    tree1_node14 = TreeNode(14, None, None)
    tree1_node13 = TreeNode(13, None, None)
    tree1_node12 = TreeNode(12, None, None)
    tree1_node11 = TreeNode(11, None, None)
    tree1_node10 = TreeNode(10, None, None)
    tree1_node9 = TreeNode(9, None, None)
    tree1_node8 = TreeNode(8, None, None)
    tree1_node7 = TreeNode(7, tree1_node14, tree1_node15)
    tree1_node6 = TreeNode(6, tree1_node12, tree1_node13)
    tree1_node5 = TreeNode(5, tree1_node10, tree1_node11)
    tree1_node4 = TreeNode(4, tree1_node8, tree1_node9)
    tree1_node3 = TreeNode(3, tree1_node6, tree1_node7)
    tree1_node2 = TreeNode(2, tree1_node4, tree1_node5)
    tree1_node1 = TreeNode(1, tree1_node2, tree1_node3)

    tree2_node15 = TreeNode(15, None, None)
    tree2_node14 = TreeNode(14, None, None)
    tree2_node13 = TreeNode(13, None, None)
    tree2_node12 = TreeNode(12, tree2_node14, tree2_node15)
    tree2_node11 = TreeNode(11, None, None)
    tree2_node10 = TreeNode(10, tree2_node12, tree2_node13)
    tree2_node9 = TreeNode(9, tree2_node10, tree2_node11)
    tree2_node8 = TreeNode(8, None, None)
    tree2_node7 = TreeNode(7, None, None)
    tree2_node6 = TreeNode(6, None, tree2_node9)
    tree2_node5 = TreeNode(5, tree2_node8, None)
    tree2_node4 = TreeNode(4, tree2_node6, tree2_node7)
    tree2_node3 = TreeNode(3, tree2_node4, tree2_node5)
    tree2_node2 = TreeNode(2, tree2_node3, None)
    tree2_node1 = TreeNode(1, None, tree2_node2)

    d = Demo()
    for traversal in [d.preorderTraversal, d.inorderTraversal, d.postorderTraversal, d.levelOrder,]:
        for root_node in [tree1_node1, tree2_node1]:#, tree3_node1, tree4_node1]:
            if d.traversal or d.q:
                d.traversal = []
                d.q = []
            print('\n\n\n')
            traversal(root_node, top=True)
