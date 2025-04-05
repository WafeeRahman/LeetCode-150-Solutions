# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Given a number k and a linked list, reverse every group of k nodes until the end of the linked list
#If The Linked List isnt divisible by K, then the final part indivisible by k can be left by is
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #Get The End of Each Kth Group By Using Dummy Pointers to Point to the 
        #Start of Each K Group
        def getKth(head, k):
            while k > 0 and head:
                head = head.next 
                k-=1
            return head
        #Start with a dummy that points to the start of the list
        groupPrev = ListNode(0, head)
        dummy = groupPrev
        
        while True:
            #Get the end of the kth group if it exists
            kth = getKth(groupPrev, k)
            #If it doesnt there are no nodes to reverse
            if not kth:
                break

            #The Next K Group is the value after k, and the first value in the k group
            #Is reversed to point to the first value of the next k group (until that group is reversed)
            groupNext = kth.next
            prev = groupNext
            curr = head 
            
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            #Our Dummy Points to the new last value of the k group after reversal
            nxt = groupPrev.next
            
            #Make it point to the first, the last reversed value
            groupPrev.next = prev

            #Next Dummy Pointer for the next k group reversal
            groupPrev = nxt
            
            #Start Reversing the Next Group
            head = groupNext
          
        return dummy.next
            




