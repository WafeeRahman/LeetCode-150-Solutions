# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        nl = ListNode(0)
        dummy = nl #Dummyy to return

        #create a new linked list with the sum of the two values using traditional addition
        while l1 or l2 or carry:
            #Take the available digits
            digitOne = l1.val if l1 else 0
            digitTwo = l2.val if l2 else 0

            summation = digitOne + digitTwo + carry
            #Take the carry from the summation
            carry = summation // 10
            #Set the digit of the node
            summation = summation % 10
            #Set node
            nl.next = ListNode(summation)
            nl = nl.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
        
    

            
