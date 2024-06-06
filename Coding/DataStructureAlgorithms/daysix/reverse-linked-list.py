# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head

        while curr:
        #   p  1 -> 2 -> 3 -> 4
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
    
