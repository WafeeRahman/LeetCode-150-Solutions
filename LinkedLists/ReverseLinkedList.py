#Given the head of the linked list, reverse the linkages and return the reversed linked list, starting at the new head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        #Reverse Each Linkage, recall that the last element will be the previous head
        #and the next pointer of the last element of each linked list is none, hence we start prev as None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
        
