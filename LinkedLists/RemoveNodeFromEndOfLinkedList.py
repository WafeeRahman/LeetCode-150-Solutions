# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Given the head of a linked list and an integer n, removed the nth node from the end of the list
# [1,2,3,4], n = 2
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        right = head
        while n > 0:
            right = right.next
            n-=1
        #We dont have to worry about the case where the size is less than n, as the question garuntees
        # 1 <= n <= sz
        #Start a left point that is n+1 distance away from right, so that when right reaches the end of the list
        #
        left = dummy
        while right:
            print(left.val, right.val)
            right = right.next
            left = left.next
        #Right is at sz, left is at n-1, where we can erase the sz-nth value for garbage collection
        left.next = left.next.next #Erase the nth from end node
        return dummy.next


