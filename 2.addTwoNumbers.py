# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = False
        result = ListNode(None)
        ptr = result
        while l1 or l2 or carry:
            value = carry
            value += l1.val if l1 else 0
            value += l2.val if l2 else 0
            carry = False
            
            if value >= 10:
                value -= 10
                carry = True
            newNode = ListNode(value)
            ptr.next = newNode
            ptr = newNode
            
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        
        return result.next