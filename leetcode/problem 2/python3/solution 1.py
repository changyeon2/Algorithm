# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = None
        carry = 0
        resultHead = None
        
        while l1 != None or l2 != None:
            if l1 != None:
                val1 = l1.val
            elif l1 == None:
                val1 = 0
            
            if l2 != None:
                val2 = l2.val
            elif l2 == None:
                val2 = 0
            
            sumOfVal = val1 + val2 + carry
            resultNode = ListNode(sumOfVal % 10)
            carry = sumOfVal // 10

            if result == None:
                result = resultNode
                resultHead = resultNode
            else:
                result.next = resultNode
                result = result.next

            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

        if carry != 0:
            extraNode = ListNode(carry)
            result.next = extraNode
        
        return resultHead
        
        
