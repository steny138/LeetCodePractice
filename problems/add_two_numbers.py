# 2 Add two numbers

import logging

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    @classmethod
    def to_listnode(self, value):
        if value:
            n = self(value[-1])
            n.next = self.to_listnode(value[:-1])
            return n

def link_listnode(ln, l):
    if ln.next is None:
        l.append(str(ln.val))
    else:
        link_listnode(ln.next, l)
        l.append(str(ln.val))
        
    return l

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rl1 = []
        rl1 = link_listnode(l1, rl1)
        i1 = int(''.join([x for x in rl1]))
        
        rl2 = []
        rl2 = link_listnode(l2, rl2)
        i2 = int(''.join([x for x in rl2]))
        
        resultNode = ListNode.to_listnode(str(i1 + i2))
        
        return resultNode