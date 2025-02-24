#Given two sorted linked lists, we need to merge the lists such that they are sorted in ascending order

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Approach: Take The Two Lists and Compare each of their nodes one at a time, 
        #Add the smaller value to a new linked list that merges the two
        l1 = list1
        l2 = list2
        nl = ListNode()
        dummy = nl  #To return the entire list, use a dummy to point at the first value in LL
        while l1 and l2:
            #Choose the next value based on sorting
            if l1.val <= l2.val:
                nl.next = l1
                l1 = l1.next
                nl = nl.next
            elif l2.val <= l1.val:
                nl.next = l2
                l2 = l2.next
                nl = nl.next
        #Whichever of the list is nonnull should be appended after newlist
        if l1:
            nl.next = l1
        if l2:
            nl.next = l2
        return dummy.next

                
        
