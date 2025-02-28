"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#Given a linked list of length n, where each linked list has an additional linkage to the
#0-nth item in the linked list, at random, the nth value is null, so pointers could be null
#And we need to consider that case

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #Copy Linked Sturcture with a Hashmap to keep track of linkages

        oldToCopy = {None:None} #If theres no head, theres no list to copy
        cur = head
        #One Pass to Copy Each value in the list
        while cur:
            oldToCopy[cur] = ListNode(cur.val)
            cur = cur.next
        cur = head
        #Once we can gurantee that each node is in the array, we can set linkages
        while cur:
            oldToCopy[cur].next = oldToCopy[cur.next] if cur.next else None
            oldToCopy[cur].random = oldToCopy[cur.random] if cur.random else None
            cur = cur.next
        return oldToCopy[head] #Return new list
        
