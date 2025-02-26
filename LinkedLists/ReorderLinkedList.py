# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Given the head of a singly linked list, reorder the list such that the reversed latter half
#Is interleaved with the first half of the linked list ot make a new linked  list
#We need to do it in place
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        #We can use fast and slow pointers technique to traverse halfway into the linkedlist
        fast=head.next
        slow = head
        dummy = head #Dummy return value
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        slow2 = slow.next #Reverse second half
        slow.next = None #Remove linkage between first half and second half
        prev = None
        while slow2:
            nxt = slow2.next
            slow2.next = prev
            prev = slow2
            slow2 = nxt
        slow2 = prev
        
        #Interleave the reversed second half and firsthalf
        slow = head
        while slow and slow2:
            nxt1=slow.next
            nxt2=slow2.next
            slow.next = slow2
            slow = nxt1
            slow2.next = slow
            slow2 = nxt2
            
            
   



        
