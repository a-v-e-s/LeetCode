null = None


class ListNode:
    """ LeetCode's ListNode object """
    
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = None
        self.prev = None
    

    def __repr__(self):
        if self.prev:
            if self.next:
                return f'ListNode <{hex(id(self))}>\n\tval: {self.val}\n\tprev: {hex(id(self.prev))}\n\tnext: {hex(id(self.next))}'
            else:
                return f'ListNode <{hex(id(self))}>\n\tval: {self.val}\n\tprev: {hex(id(self.prev))}\n\tnext: None'
        elif self.next:
            return f'ListNode <{hex(id(self))}>\n\tval: {self.val}\n\tprev: None\n\tnext: {hex(id(self.next))}'
        else:
            return f'ListNode <{hex(id(self))}>\n\tval: {self.val}\n\tprev: None\n\tnext: None'


class TreeNode:
    """ LeetCode's TreeNode object """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

    def __repr__(self):
        if self.left:
            if self.right:
                return f'TreeNode <{hex(id(self))}>\nt\val: {self.val}\n\tleft: {hex(id(self.left))}\n\tright: {hes(id(self.right))}'
            else:
                return f'TreeNode <{hex(id(self))}>\nt\val: {self.val}\n\tleft: {hex(id(self.left))}\n\tright: None'
        elif self.right:
            return f'TreeNode <{hex(id(self))}>\nt\val: {self.val}\n\tleft: None\n\tright: {hes(id(self.right))}'
        else:
            return f'TreeNode <{hex(id(self))}>\nt\val: {self.val}\n\tleft: None\n\tright: None'
        