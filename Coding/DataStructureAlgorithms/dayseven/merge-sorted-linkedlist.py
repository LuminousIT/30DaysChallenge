# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        

        list1 = [1,2,4] =>  head = 1; head.next = 2
        list2 = [1,3,4] => head = 1; head.next = 3

        res = ListNode() => dummy node for output. no need to be initialized because in constructor above, it has a default value of 0. and you may even choose to initialize with any random value since you can return (dummy.next) as final answer

        while list1 and list2:
              if list1.val <= list2.val
              res.next = list1
                list1 = list1.next
              else:
              res.next = list2
              list2 = list2.next

        if list1 is not null (i.e still has value):
                append to output
                res.next = list1
        elif: list2 is not null:
                append to output auch
                res.next = list2

                return res.next
        """

        dummy = ListNode()
        tail = dummy

        """
        after creating dummy = ListNode() there is an object in memory (lets call it obj1), which contains int val and ListNode next in itself.
        "dummy" in this case is not an object, but a reference/link to this object in memory ("dummy" -> obj1)
        when we write tail = dummy, we are not creating new object ListNode, but only copying link to obj1, so we get "tail" -> obj1
        after that we do not touch "dummy", so it always pointed at obj1
        to work with obj1 we use "tale" reference
        when we write tale.val - we accessing obj1.val
        when we write tale.next - we accessing obj1.next
        if we write tale.next = ListNode() - now obj1.next contains reference to new object in memory (lets call it obj2)
        after that if we write tale = tale.next - it means that we are changing reference, that our "tale" contains and now it's "tail"->obj2
        dummy object (obj1) was created just for our comfort, so we shouldn't figure out how to create first object in cycle
        after all work done we don't need it anymore, so we do 
        dummy = dummy.next (so now it's "dummy"->obj2)
        return dummy
        """

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next 
            else:
                tail.next = list2 
                list2 = list2.next 

            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2 

        return dummy.next
        
        
        
    def mergeTwoListsArray(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]

        list1 = [1,2,4]
        list2 = [1,3,4]

        loop the list, 
        if val @ list1[i] <= list2[i]
                res.push(i,i)
                if list1[i] > list2[i]
                res.push(list2[i],list1[i])
        """
        res = []
        for i in range(len(list1)):
            if list1[i] <= list2[i]:
                res.append(list1[i])
                res.append(list2[i])
            else:
                res.append(list2[i])
                res.append(list1[i])
        return res

# finalres = Solution().mergeTwoListsArray([1,2,4], [1,3,4])
finalres = Solution().mergeTwoListsArray([1], [0])
print(finalres)

