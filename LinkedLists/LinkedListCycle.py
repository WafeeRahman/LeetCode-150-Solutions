# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#Given the head of a linked list, determine if there is a cycle in the list
#That is, there exists a value in the linked list whos next pointer is a previous pointer within the
#linked list
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #We can do this using the fast and slow pointers technique
        #OR Floyd and Hare
        #Where we have two pointers, a normal linked list traversal and one that moves twice as fast
        #If they meet at some point, that means that there is a cycle
        #But if fast becomes null, that means theres no cycle
        if not head:
            return False
        
        fast = head.next
        slow = head

        while fast and fast.next:
            if slow == fast:
                return True
            fast = fast.next.next
            slow = slow.next
        return False
        
