null = None


class ListNode:
    """ LeetCode's ListNode object """
    
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = None
        self.prev = None


class TreeNode:
    """LeetCode's TreeNode object """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        